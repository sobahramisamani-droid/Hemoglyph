# AI.py

import os
import logging
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st

load_dotenv()
logger = logging.getLogger(__name__)


class BloodLabChatbot:
    """دستیار هوشمند آزمایش خون – نسخهٔ نهایی و بدون باگ"""

    # ----------------------------------------------------------------
    SYSTEM_INSTRUCTION = """You are **BloodLab AI Assistant**, a specialized medical AI that ONLY answers questions related to blood tests, laboratory values, disease predictions, clinical findings, medical terminology, and recommendations based on the patient's laboratory report.

**Rules you must follow strictly:**
- Only answer if the question is about the patient's lab results, medical conditions, risk predictions, or general explanation of blood test markers.
- If the user asks about anything else (politics, programming, entertainment, mathematics, etc.), reply: "I am a blood laboratory assistant. I can only answer questions related to your laboratory analysis and prediction results."
- Always answer ONLY from the provided laboratory context. If information is missing, say: "The available laboratory information is insufficient to answer that question."
- Never invent laboratory values. Use only the data provided in the context.
- Never diagnose a disease or prescribe medication. Always recommend consulting a physician.
- Never mention probabilities or diseases that are not present in the provided context.
- Do not infer new medical conditions beyond the supplied laboratory findings.
- Keep answers concise, informative, and patient-friendly.
- You may explain why a certain risk or finding is present by referencing the lab values and patient profile from the context.
- Never provide emergency medical advice. Never tell the patient to ignore symptoms. If symptoms suggest an emergency, recommend immediate medical evaluation."""

    MAX_QUESTIONS = 15
    KEEP_LAST_MESSAGES = 8          # ۴ تبادل آخر
    MAX_NORMAL_VALUES = 3           # حداکثر مقادیر طبیعی در Context

    # ----------------------------------------------------------------
    def __init__(self, api_key: str | None = None, model: str = "gemini-2.0-flash"):
        if api_key is None:
            try:
                # اولویت اول: Streamlit Secrets
                api_key = st.secrets["GEMINI_API_KEY"]
            except (FileNotFoundError, KeyError, ImportError):
                # اگر Streamlit نبود یا secrets تعریف نشده بود، از .env بخوان
                from dotenv import load_dotenv
                load_dotenv()
                api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing. Set it in .streamlit/secrets.toml or .env file."
            )

        self.client = genai.Client(api_key=api_key)
        self.model = model
        self.patient_context: str | None = None
        self.history: list[dict] = []        # فقط گفتگوی واقعی (بدون Context و Summary)
        self.question_count: int = 0

    # ----------------------------------------------------------------
    def build_and_set_context(self, patient_prof, clean_inputs, derived,
                              active_diagnoses, risk_predictions,
                              feature_registry, profile_keys):
        """ساخت Context سبک: فقط غیرطبیعی‌ها + ۳ نرمال کلیدی"""
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

        # Derived metrics مهم
        important_derived = {"eGFR", "HOMA_IR", "ACR", "BMI", "Transferrin_Sat", "Non_HDL", "VLDL"}
        lines.append("\n## Derived Metrics")
        for dk, dv in derived.items():
            if dk in important_derived:
                fdata = feature_registry.get(dk, {})
                unit = fdata.get("unit", "")
                lines.append(f"- {dk}: {dv} {unit}")

        # Guideline-based findings
        compat = [d for d in active_diagnoses if d.get("status") == "Present" or "Compatible" in str(d.get("evidence"))]
        if compat:
            lines.append("\n## Guideline-Based Findings")
            for d in compat:
                ev = "; ".join(d.get("evidence", [])[:2])
                lines.append(f"- {d['nameEn']} (ICD-10 {d['icd10']}) — {ev}")

        # Risk predictions (مرتب نزولی)
        risks = [r for r in risk_predictions if r.get("status") == "Evaluated"]
        if risks:
            risks.sort(key=lambda r: r.get("probability", 0), reverse=True)
            lines.append("\n## 2-Year Risk Predictions")
            for r in risks:
                prob = round(r.get("probability", 0) * 100, 1)
                lines.append(f"- {r['nameEn']}: {prob}% ({r.get('riskLevel', '')})")

        self.patient_context = "\n".join(lines)

    # ----------------------------------------------------------------
    def generate_initial_summary(self) -> str:
        """خلاصهٔ اولیه (بدون ذخیره در history)"""
        if not self.patient_context:
            raise ValueError("Patient context has not been set. Call build_and_set_context() first.")

        prompt = (
            "Please provide a brief, friendly summary of my laboratory results, "
            "highlighting the most important abnormal findings, compatible guideline-based "
            "conditions, and any significant 2-year risk predictions. "
            "Keep it understandable for a non-medical person."
        )
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=self.SYSTEM_INSTRUCTION + "\n\n" + self.patient_context,
                    temperature=0.1,
                    max_output_tokens=600
                )
            )
            return response.text
        except Exception as e:
            logger.warning(f"generate_initial_summary failed: {e}")
            return "I'm sorry, I couldn't generate the summary. Please check your API key and try again."

    # ----------------------------------------------------------------
    def chat(self, user_message: str) -> str:
        """پاسخ به سوال کاربر – Context همیشه به‌عنوان اولین Content ارسال می‌شود"""
        if self.question_count >= self.MAX_QUESTIONS:
            return (
                "You have reached the maximum number of questions for this session. "
                "Please consult your physician for further information."
            )

        self.question_count += 1

        # ساخت لیست Content‌ها با ترتیب: Context → History → Current Question
        contents = []

        # ۱. Context بیمار (همیشه اول)
        if self.patient_context:
            contents.append(types.Content(
                role="user",
                parts=[types.Part(text=self.patient_context)]
            ))

        # ۲. تاریخچه واقعی (آخرین ۸ پیام)
        recent = self.history[-self.KEEP_LAST_MESSAGES:] if self.history else []
        for msg in recent:
            role = "user" if msg["role"] == "user" else "model"
            contents.append(types.Content(role=role, parts=[types.Part(text=msg["content"])]))

        # ۳. سوال جاری
        contents.append(types.Content(role="user", parts=[types.Part(text=user_message)]))

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=types.GenerateContentConfig(
                    system_instruction=self.SYSTEM_INSTRUCTION,   # فقط قوانین، بدون Context
                    temperature=0.1,
                    max_output_tokens=600
                )
            )
            reply = response.text
        except Exception as e:
            logger.warning(f"chat failed: {e}")
            reply = "I'm having trouble connecting to the AI service. Please try again later."

        # به‌روزرسانی تاریخچه (بدون Context و Summary)
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})

        return reply

    # ----------------------------------------------------------------
    def reset(self):
        """بازنشانی کامل"""
        self.history.clear()
        self.question_count = 0
        self.patient_context = None
