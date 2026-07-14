
import os
import logging
from dotenv import load_dotenv
import groq
import streamlit as st

load_dotenv()
logger = logging.getLogger(__name__)


class BloodLabChatbot:
    """BloodLab AI Assistant – Groq version"""

    SYSTEM_INSTRUCTION = """You are **BloodLab AI Assistant**, a specialized medical AI that ONLY answers questions about the patient's laboratory results.

**Your response format for questions about diseases or findings:**
1. State the finding clearly with the patient's actual lab values
2. Reference the specific guideline criteria that support or rule out the finding
3. If asked about specialists, recommend the appropriate specialist type
4. Keep answers concise but evidence-based

**Rules:**
- Only answer about the patient's lab results, medical conditions, or risk predictions
- If asked about unrelated topics, reply: "I can only answer questions related to your laboratory analysis."
- Never invent lab values — use only data from the provided context
- Never diagnose or prescribe medication
- Always recommend consulting a physician"""

    MAX_QUESTIONS = 15
    KEEP_LAST_MESSAGES = 8
    MAX_NORMAL_VALUES = 3

    def __init__(self, api_key: str | None = None, model: str = "llama-3.3-70b-versatile"):
        if api_key is None:
            try:
                api_key = st.secrets["GROQ_API_KEY"]
            except (FileNotFoundError, KeyError, ImportError):
                api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is missing. Set it in .streamlit/secrets.toml or .env file."
            )

        self.client = groq.Client(api_key=api_key)
        self.model = model
        self.patient_context: str | None = None
        self.history: list[dict] = []
        self.question_count: int = 0

    def build_and_set_context(self, patient_prof, clean_inputs, derived,
                              active_diagnoses, risk_predictions,
                              feature_registry, profile_keys):
        gender = "Male" if patient_prof.get("Sex") == 1 else "Female"
        age = patient_prof.get("Age", "N/A")
        bmi = derived.get("BMI", "N/A")
        smoker = "Yes" if patient_prof.get("Smoking") == 1 else "No"

        lines = [
            "## Patient Profile",
            f"- Age: {age}",
            f"- Sex: {gender}",
            f"- BMI: {bmi} kg/m²",
            f"- Smoking: {smoker}",
            "",
            "## Laboratory Values (only abnormal + key normal values)"
        ]

        gender_lower = "male" if gender == "Male" else "female"
        high_vals, low_vals, normal_vals = [], [], []

        for key, val in clean_inputs.items():
            if key in profile_keys:
                continue
            fdata = feature_registry.get(key, {})
            disp = fdata.get("displayEn", key)
            unit = fdata.get("unit", "")
            refs = fdata.get("referenceRanges", [])
            ref = next((r for r in refs if r.get("gender") == gender_lower), refs[0] if refs else None)

            line = f"- {disp}: {val} {unit}"
            if ref and "range" in ref:
                low, high = ref["range"]
                try:
                    v = float(val)
                    if v < low:
                        line += f" ⬇️ LOW (normal {low}-{high})"
                        low_vals.append(line)
                    elif v > high:
                        line += f" ⬆️ HIGH (normal {low}-{high})"
                        high_vals.append(line)
                    else:
                        line += f" (normal {low}-{high})"
                        normal_vals.append(line)
                except:
                    normal_vals.append(line)
            else:
                normal_vals.append(line)

        if high_vals:
            lines.append("### HIGH")
            lines.extend(high_vals)
        if low_vals:
            lines.append("### LOW")
            lines.extend(low_vals)
        if normal_vals:
            lines.append(f"### KEY NORMAL VALUES (showing first {self.MAX_NORMAL_VALUES})")
            lines.extend(normal_vals[:self.MAX_NORMAL_VALUES])

        important_derived = {"eGFR", "HOMA_IR", "ACR", "BMI", "Transferrin_Sat", "Non_HDL", "VLDL"}
        lines.append("\n## Derived Metrics")
        for dk, dv in derived.items():
            if dk in important_derived:
                fdata = feature_registry.get(dk, {})
                unit = fdata.get("unit", "")
                lines.append(f"- {dk}: {dv} {unit}")

        compat = [d for d in active_diagnoses if d.get("status") == "Present" or "Compatible" in str(d.get("evidence"))]
        if compat:
            lines.append("\n## Guideline-Based Findings")
            for d in compat:
                ev = "; ".join(d.get("evidence", [])[:2])
                lines.append(f"- {d['nameEn']} (ICD-10 {d['icd10']}) — {ev}")

        risks = [r for r in risk_predictions if r.get("status") == "Evaluated"]
        if risks:
            risks.sort(key=lambda r: r.get("probability", 0), reverse=True)
            lines.append("\n## 2-Year Risk Predictions")
            for r in risks:
                prob = round(r.get("probability", 0) * 100, 1)
                lines.append(f"- {r['nameEn']}: {prob}% ({r.get('riskLevel', '')})")

        self.patient_context = "\n".join(lines)

    def generate_initial_summary(self) -> str:
        if not self.patient_context:
            raise ValueError("Patient context has not been set.")

        lang = st.session_state.get("lang", "en")

        if lang == "fa":
            strict_lang_order = (
                "**CRITICAL: YOU MUST ANSWER ONLY IN PERSIAN (FARSI). "
                "DO NOT USE ENGLISH. EVEN IF THE DATA IS IN ENGLISH, YOUR RESPONSE MUST BE IN PERSIAN.**"
            )
            user_prompt = (
                "لطفاً یک خلاصهٔ مختصر و مفید از نتایج آزمایش من به زبان فارسی ارائه دهید. "
                "مهم‌ترین یافته‌های غیرطبیعی، بیماری‌های سازگار با گایدلاین‌ها "
                "و پیش‌بینی‌های ریسک ۲ ساله را ذکر کنید. "
                "پاسخ باید ساده و قابل فهم برای یک فرد غیرپزشکی باشد."
            )
            system_content = f"{strict_lang_order}\n\n{self.SYSTEM_INSTRUCTION}\n\n{self.patient_context}"
        else:
            user_prompt = (
                "Please provide a brief, friendly summary of my laboratory results, "
                "highlighting the most important abnormal findings, compatible guideline-based "
                "conditions, and any significant 2-year risk predictions. "
                "Keep it understandable for a non-medical person."
            )
            system_content = f"{self.SYSTEM_INSTRUCTION}\n\n{self.patient_context}"

        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_prompt}
        ]
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.0,         
                max_tokens=400
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.warning(f"generate_initial_summary failed: {e}")
            return "I'm sorry, I couldn't generate the summary." if lang == "en" else "متأسفانه نتوانستم خلاصه را تولید کنم."
    def chat(self, user_message: str) -> str:
        if self.question_count >= self.MAX_QUESTIONS:
            return "You have reached the maximum number of questions for this session. Please consult your physician for further information."

        self.question_count += 1

        messages = [{"role": "system", "content": self.SYSTEM_INSTRUCTION}]

        lang = st.session_state.get("lang", "en")
        if lang == "fa":
            messages.append({"role": "system", "content": "از این پس تمام پاسخ‌های خود را فقط به فارسی بنویس."})
        else:
            messages.append({"role": "system", "content": "From now on, answer only in English."})

        if self.patient_context:
            messages.append({
                "role": "system",
                "content": "Patient laboratory context:\n" + self.patient_context
            })

        recent = self.history[-self.KEEP_LAST_MESSAGES:] if self.history else []
        for msg in recent:
            messages.append({"role": msg["role"], "content": msg["content"]})

        messages.append({"role": "user", "content": user_message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.1,
                max_tokens=300
            )
            reply = response.choices[0].message.content
        except Exception as e:
            logger.warning(f"chat failed: {e}")
            reply = "I'm having trouble connecting to the AI service." if lang == "en" else "متأسفانه در اتصال به سرویس هوش مصنوعی مشکلی پیش آمد."

        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def reset(self):
        self.history.clear()
        self.question_count = 0
        self.patient_context = None
