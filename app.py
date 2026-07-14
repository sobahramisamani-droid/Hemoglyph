import streamlit as st
import os
import json
import pandas as pd
import groq
from clinical_data import FEATURE_REGISTRY, FeatureCategory
from calculators import compute_all_derived
from interpretation import interpret_lab_data
from prediction import predict_2year_risks
from disease_guidelines import DISEASE_GUIDELINES
from AI import BloodLabChatbot
st.markdown("""
<style>
    /* Import Vazir font */
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazir-font@v33.1.0/dist/font-face.css');

    /* ============================
       PROTECT STREAMLIT ICONS
       ============================ */
    [data-testid="stDecoration"],
    [data-testid="stSidebar"],
    .st-emotion-cache-1dp5m8t,
    .st-emotion-cache-1hskb1m,
    .st-emotion-cache-1v02s4x,
    .st-emotion-cache-1n76nqr,
    .st-emotion-cache-1o3jp5z,
    .st-emotion-cache-1p1m4ay,
    .st-emotion-cache-1p8iqe6,
    .st-emotion-cache-1p4g8p1,
    .st-emotion-cache-1p5wlh4,
    .st-emotion-cache-1p6s9q4,
    .st-emotion-cache-10trblm,
    .st-emotion-cache-1q8ddzd,
    .st-emotion-cache-183lzff,
    .st-emotion-cache-1cvow4s,
    .st-emotion-cache-16txtl3,
    .st-emotion-cache-1kyxreq,
    .st-emotion-cache-1v0mbdj,
    .st-emotion-cache-1r6slb0,
    .st-emotion-cache-1xarl3l,
    .st-emotion-cache-1wmy9hl,
    .st-emotion-cache-1avcm0n,
    .st-emotion-cache-1f3w014,
    .st-emotion-cache-1vtueo4,
    .st-emotion-cache-1v7uza4,
    .st-emotion-cache-1l6ema2,
    .st-emotion-cache-1dp5m8t,
    .st-emotion-cache-1hskb1m,
    .st-emotion-cache-1v02s4x,
    .st-emotion-cache-1n76nqr,
    .st-emotion-cache-1o3jp5z,
    .st-emotion-cache-1p1m4ay,
    .st-emotion-cache-1p8iqe6,
    .st-emotion-cache-1p4g8p1,
    .st-emotion-cache-1p5wlh4,
    .st-emotion-cache-1p6s9q4,
    svg,
    .material-icons,
    [class*="material-icons"],
    [class*="icon"] {
        font-family: 'Material Icons', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }

    /* ============================
       GENERAL PAGE FONT (safe)
       ============================ */
    .stApp, body, p, span, div, label, input, textarea, button,
    h1, h2, h3, h4, h5, h6,
    .stMarkdown, .stText, .stAlert, .stButton,
    .stChatMessage, .stSelectbox, .stTextInput, .stNumberInput,
    .stCheckbox, .stExpander, .stDataFrame, .stTabs, .stSidebar,
    .metric-label, .metric-value {
        font-family: 'Inter', 'Vazir', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* ============================
       PERSIAN TEXT ONLY
       ============================ */
    [lang="fa"],
    .persian-text,
    *[lang="fa"] *,
    *:lang("fa") {
        font-family: 'Vazir', 'Inter', sans-serif !important;
    }

    /* ============================
       OPTIONAL RTL SUPPORT
       ============================ */
    [dir="rtl"] {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)
if not hasattr(FeatureCategory, "BONE_MINERAL"):
    FeatureCategory.BONE_MINERAL = "Bone & Mineral Panel"

PROFILE_KEYS = [
    "Age", "Sex", "Weight", "Height", "Waist", "Systolic_BP", "Diastolic_BP",
    "HeartRate", "SleepHours", "Smoking", "PhysicalActivity",
    "FamilyHistory_DM", "FamilyHistory_CAD", "FamilyHistory_HTN", "FamilyHistory_Obesity"
]

QUAL_FEATURES = {
    "UrineNitrite": ["Negative", "Positive"],
    "UrineLeukocyteEsterase": ["Negative", "Positive"],
    "HBsAg": ["Negative", "Positive"],
    "HBeAg": ["Negative", "Positive"],
    "Anti_HCV": ["Negative", "Positive"],
    "HIV_AgAb": ["Negative", "Positive"],
    "RPR": ["Negative", "Positive"],
    "TPPA": ["Negative", "Positive"],
    "DAT": ["Negative", "Positive"],
    "Lupus_Anticoagulant": ["Negative", "Positive"],
    "ANCA": ["Negative", "Positive"],
    "Anti_HBc": ["Negative", "Positive"],
    "Anti_HBe": ["Negative", "Positive"],
    "ENA_Panel": ["Negative", "Positive"],
    "UrineProteinQualitative": ["Negative", "Trace", "1+", "2+", "3+", "4+"],
    "UrineGlucoseQualitative": ["Negative", "Trace", "1+", "2+", "3+", "4+"],
    "UrineKetones": ["Negative", "Trace", "Small", "Moderate", "Large"],
    "UrineBlood": ["Negative", "Trace", "Small", "Moderate", "Large"]
}

st.set_page_config(
    page_title="Clinical Laboratory AI Assistant",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    h1, h2, h3, h4, h5 {
        color: #0f172a !important;
        font-weight: 600 !important;
        letter-spacing: -0.025em;
    }
    .clinical-card {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.02);
        margin-bottom: 20px;
    }
    .diagnosis-badge-present {
        background-color: #fef2f2;
        border: 1px solid #fecaca;
        color: #991b1b;
        padding: 16px 20px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    .diagnosis-badge-absent {
        background-color: #f0fdf4;
        border: 1px solid #bbf7d0;
        color: #166534;
        padding: 16px 20px;
        border-radius: 8px;
        margin-bottom: 12px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 700;
        color: #1e293b;
    }
    .metric-label {
        font-size: 13px;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)
TRANSLATIONS = {
    "en": {
        "title": "🧬 Laboratory AI Assistant",
        "subtitle": "##### Full‑Scope Guideline‑Based Lab Interpretation & 2‑Year Clinical Risk Forecasting",
        "presets_heading": "##### 🚀 Quick Patient Presets",
        "workflow_heading": "📋 Workflow Overview",
        "step_label": "**Step {step} of 4**",
        "step1_title": "### 👤 Step 1: Clinical Profile & Demographics",
        "step1_desc": "Enter basic patient parameters, vitals, lifestyle habits, and hereditary history.",
        "step2_title": "### 🧪 Step 2: Select Lab Panels",
        "step2_desc": "Choose the biomarker groups to evaluate. Only the selected panels will appear in the next step.",
        "step3_title": "### 📋 Step 3: Enter Biomarker Values",
        "step3_desc": "Provide raw laboratory findings for the selected panels. Values are evaluated against dynamic, sex‑specific reference ranges.",
        "step4_title": "### 📊 Step 4: Diagnostics & AI Consultation",
        "step4_desc": "Review the guideline‑driven and AI‑powered evaluation of the patient's comprehensive diagnostic profile.",
        "summary_table_heading": "### 📋 Clinical & Lab Parameters Summary",
        "summary_table_expander": "📊 Expand to View Summary Table",
        "derived_metrics_heading": "#### 🔬 Derived Clinical Metrics",
        "disease_heading": "#### 🩺 Guideline‑Based Disease Interpretation",
        "compatible_count": "🚨 Compatible",
        "no_evidence_count": "🟢 No Evidence",
        "incomplete_count": "⚠️ Incomplete",
        "no_data_count": "⚪ No Input Data",
        "filter_label": "Filter by Status:",
        "sort_label": "Sort by:",
        "show_all": "Show All",
        "compatible_only": "Compatible Only",
        "incomplete_only": "Incomplete Only",
        "no_data_only": "No Input Data",
        "default_sort": "Default (by Panel)",
        "compatible_first_sort": "Compatible First",
        "az_sort": "A‑Z by Disease Name",
        "risk_heading": "#### 🔮 2‑Year Disease Risk Prediction Scores",
        "guideline_heading": "#### 📘 Comprehensive Disease Guideline Browser",
        "expert_heading": "#### 🧠 Expert AI Clinical Consultation",
        "chat_heading": "#### 💬 BloodLab AI Assistant",
        "chat_desc": "Ask questions about your laboratory results, predicted conditions, and clinical findings. Only questions related to your blood analysis will be answered.",
        "chat_placeholder": "Ask about your lab results...",
        "chat_summary_info": "📋 **Your Laboratory Summary**",
        "previous_btn": "⬅️ Previous Step",
        "next_btn1": "Proceed to Panels ➡️",
        "next_btn2": "Proceed to Biomarkers ➡️",
        "next_btn3": "🚀 Run Diagnostic Analysis",
        "sidebar_reset": "##### ⚙️ Reset Panel Data",
        "clear_btn": "🧹 Clear All Inputs",
        "clear_success": "All patient and lab values cleared.",
        "reset_btn": "✨ Reset Selected Panel Values to Midpoint/Normal",
        "reset_success": "All active parameters reset to clinical normal references.",
        "thinking": "Thinking...",
        "spinner_summary": "Preparing your laboratory summary...",
        "spinner_expert": "Analyzing laboratory panels and risk metrics via Groq AI...",
        "generate_expert_btn": "🧠 Generate Expert AI Consultation Report",
        "expert_report_heading": "#### 📋 Expert Medical Consult Report",
        "summary_language": "en",
    },
    "fa": {
        "title": "🧬 دستیار هوشمند آزمایشگاهی",
        "subtitle": "##### تحلیل جامع نتایج آزمایش بر اساس گایدلاین‌های بالینی و پیش‌بینی ریسک ۲ ساله",
        "presets_heading": "##### 🚀 پروفایل‌های آماده بیمار",
        "workflow_heading": "📋 روند کار",
        "step_label": "**مرحله {step} از ۴**",
        "step1_title": "### 👤 مرحله ۱: مشخصات بالینی و جمعیت‌شناختی",
        "step1_desc": "اطلاعات پایه بیمار، علائم حیاتی، عادات زندگی و سابقه خانوادگی را وارد کنید.",
        "step2_title": "### 🧪 مرحله ۲: انتخاب پنل‌های آزمایشگاهی",
        "step2_desc": "گروه‌های بیومارکر مورد نظر خود را برای ارزیابی انتخاب کنید. فقط پنل‌های انتخاب‌شده در مرحله بعد نمایش داده خواهند شد.",
        "step3_title": "### 📋 مرحله ۳: ورود مقادیر آزمایشگاهی",
        "step3_desc": "نتایج خام آزمایشگاهی را برای پنل‌های انتخاب‌شده وارد کنید. مقادیر بر اساس محدوده مرجع وابسته به جنسیت ارزیابی می‌شوند.",
        "step4_title": "### 📊 مرحله ۴: تشخیص و مشاوره هوش مصنوعی",
        "step4_desc": "ارزیابی جامع پروفایل تشخیصی بیمار بر اساس گایدلاین‌ها و هوش مصنوعی را مرور کنید.",
        "summary_table_heading": "### 📋 خلاصه شاخص‌های بالینی و آزمایشگاهی",
        "summary_table_expander": "📊 باز کردن جدول خلاصه",
        "derived_metrics_heading": "#### 🔬 شاخص‌های محاسباتی",
        "disease_heading": "#### 🩺 تفسیر بیماری‌ها بر اساس گایدلاین",
        "compatible_count": "🚨 سازگار",
        "no_evidence_count": "🟢 فاقد شواهد",
        "incomplete_count": "⚠️ ناقص",
        "no_data_count": "⚪ بدون داده ورودی",
        "filter_label": "فیلتر بر اساس وضعیت:",
        "sort_label": "مرتب‌سازی بر اساس:",
        "show_all": "نمایش همه",
        "compatible_only": "فقط موارد سازگار",
        "incomplete_only": "فقط موارد ناقص",
        "no_data_only": "فقط موارد بدون داده",
        "default_sort": "پیش‌فرض (بر اساس پنل)",
        "compatible_first_sort": "ابتدا موارد سازگار",
        "az_sort": "الفبایی (انگلیسی)",
        "risk_heading": "#### 🔮 پیش‌بینی ریسک ۲ ساله",
        "guideline_heading": "#### 📘 مرورگر گایدلاین‌های تشخیصی",
        "expert_heading": "#### 🧠 مشاوره تخصصی هوش مصنوعی",
        "chat_heading": "#### 💬 دستیار هوشمند BloodLab",
        "chat_desc": "سوالات خود را درباره نتایج آزمایش، شرایط پیش‌بینی‌شده و یافته‌های بالینی بپرسید. فقط سوالات مرتبط با تحلیل خون پاسخ داده می‌شود.",
        "chat_placeholder": "سوال خود را درباره نتایج آزمایش بپرسید...",
        "chat_summary_info": "📋 **خلاصه آزمایش شما**",
        "previous_btn": "⬅️ مرحله قبل",
        "next_btn1": "مرحله بعد: پنل‌ها ➡️",
        "next_btn2": "مرحله بعد: بیومارکرها ➡️",
        "next_btn3": "🚀 اجرای تحلیل تشخیصی",
        "sidebar_reset": "##### ⚙️ بازنشانی داده‌ها",
        "clear_btn": "🧹 پاک کردن همه ورودی‌ها",
        "clear_success": "تمام اطلاعات بیمار و مقادیر آزمایشگاهی پاک شد.",
        "reset_btn": "✨ بازنشانی مقادیر پنل به حالت نرمال",
        "reset_success": "تمام پارامترهای فعال به مقادیر نرمال بازنشانی شدند.",
        "thinking": "در حال تفکر...",
        "spinner_summary": "در حال آماده‌سازی خلاصه آزمایش شما...",
        "spinner_expert": "در حال تحلیل پنل‌های آزمایشگاهی و معیارهای ریسک توسط Groq AI...",
        "generate_expert_btn": "🧠 تولید گزارش مشاوره تخصصی",
        "expert_report_heading": "#### 📋 گزارش مشاوره تخصصی",
        "summary_language": "fa",
    }
}
if "lang" not in st.session_state:
    st.session_state.lang = "en"
if "t" not in st.session_state:
    st.session_state.t = TRANSLATIONS[st.session_state.lang]
t = st.session_state.t

if "patient_inputs" not in st.session_state:
    st.session_state.patient_inputs = {k: None for k in FEATURE_REGISTRY.keys()}
    st.session_state.patient_inputs["Age"] = 35.0
    st.session_state.patient_inputs["Sex"] = "Male"
    st.session_state.patient_inputs["Weight"] = 70.0
    st.session_state.patient_inputs["Height"] = 175.0
    st.session_state.patient_inputs["Smoking"] = "No"
    st.session_state.patient_inputs["PhysicalActivity"] = "Light Activity"
    st.session_state.patient_inputs["FamilyHistory_DM"] = "No"
    st.session_state.patient_inputs["FamilyHistory_CAD"] = "No"
    st.session_state.patient_inputs["FamilyHistory_HTN"] = "No"
    st.session_state.patient_inputs["FamilyHistory_Obesity"] = "No"

if "step" not in st.session_state:
    st.session_state.step = 1

if "selected_panels" not in st.session_state:
    st.session_state.selected_panels = [
        "CBC And Differential", "Iron, Vitamin, and Nutrition Panels",
        "Thyroid and Endocrine Panels", "Diabetes and Metabolic Panels",
        "Lipid Panels", "Renal Function and Urine Protein Panels"
    ]

PANELS_TO_CATEGORIES = {
    "CBC And Differential": [FeatureCategory.CBC],
    "Iron, Vitamin, and Nutrition Panels": [FeatureCategory.IRON, FeatureCategory.VITAMIN, FeatureCategory.NUTRITION, FeatureCategory.MICRONUTRIENT],
    "Thyroid and Endocrine Panels": [FeatureCategory.THYROID, FeatureCategory.ENDOCRINE, FeatureCategory.HORMONES, FeatureCategory.REPRODUCTIVE],
    "Diabetes and Metabolic Panels": [FeatureCategory.BLOOD_SUGAR, FeatureCategory.PANCREATIC],
    "Lipid Panels": [FeatureCategory.LIPID],
    "Renal Function and Urine Protein Panels": [FeatureCategory.KIDNEY, FeatureCategory.URINE_PROTEIN],
    "Liver Function and Hepatitis Panels": [FeatureCategory.LIVER, FeatureCategory.HEPATITIS],
    "Electrolyte and Acid–Base Panels": [FeatureCategory.ELECTROLYTE, FeatureCategory.ACID_BASE],
    "Bone and Mineral Panels": [FeatureCategory.BONE_MINERAL],
    "Cardiac Biomarker Panels": [FeatureCategory.CARDIAC, FeatureCategory.MUSCLE],
    "Coagulation Panels": [FeatureCategory.COAGULATION],
    "Inflammatory Panels": [FeatureCategory.INFLAMMATORY, FeatureCategory.HEMOLYSIS],
    "Autoimmune and Rheumatology Panels": [FeatureCategory.AUTOIMMUNE, FeatureCategory.RHEUMATOLOGY],
    "Urinalysis Panels": [FeatureCategory.URINALYSIS],
    "Tumor Marker Panels": [FeatureCategory.TUMOR_MARKER],
    "Additional High-Yield Mapped Diseases": [FeatureCategory.KIDNEY, FeatureCategory.ELECTROLYTE, FeatureCategory.URINALYSIS, FeatureCategory.LIPID, FeatureCategory.CLINICAL]
}

GUIDELINE_CATEGORY_TO_PANEL = {
    "CBC And Differential": "CBC And Differential",
    "Iron, Vitamin, and Nutrition Panels": "Iron, Vitamin, and Nutrition Panels",
    "Thyroid and Endocrine Panels": "Thyroid and Endocrine Panels",
    "Diabetes and Metabolic Panels": "Diabetes and Metabolic Panels",
    "Lipid Panels": "Lipid Panels",
    "Renal Function and Urine Protein Panels": "Renal Function and Urine Protein Panels",
    "Liver Function and Hepatitis Panels": "Liver Function and Hepatitis Panels",
    "Electrolyte and Acid–Base Panels": "Electrolyte and Acid–Base Panels",
    "Bone and Mineral Panels": "Bone and Mineral Panels",
    "Cardiac Biomarker Panels": "Cardiac Biomarker Panels",
    "Coagulation Panels": "Coagulation Panels",
    "Inflammatory Panels": "Inflammatory Panels",
    "Autoimmune and Rheumatology Panels": "Autoimmune and Rheumatology Panels",
    "Pancreatic Panels": "Diabetes and Metabolic Panels",
    "Urinalysis Panels": "Urinalysis Panels",
    "Tumor Marker Panels": "Tumor Marker Panels",
    "Micronutrient Panels": "Iron, Vitamin, and Nutrition Panels",
    "Additional High-Yield Mapped Diseases": "Additional High-Yield Mapped Diseases"
}

PRESETS = {
    "Normal Healthy Adult": {
        "Age": 32.0, "Sex": "Male", "Weight": 74.0, "Height": 178.0, "Smoking": "No", "PhysicalActivity": "Moderate (3-5 days/wk)",
        "FamilyHistory_DM": "No", "FamilyHistory_CAD": "No",
        "Hb": 15.2, "MCV": 88.0, "RBC": 5.1, "WBC": 6.4, "Platelet": 240.0, "NeutrophilsPercent": 58.0,
        "SerumIron": 105.0, "TIBC": 320.0, "Ferritin": 145.0, "FBS": 88.0, "HbA1c": 5.1, "Insulin": 6.2,
        "Total_Cholesterol": 175.0, "HDL": 52.0, "LDL": 95.0, "Triglycerides": 110.0, "Creatinine": 0.9,
        "BUN": 14.0, "Sodium": 141.0, "Potassium": 4.1, "ALT": 22.0, "AST": 24.0, "CRP": 1.2
    },
    "Iron Deficiency Anemia": {
        "Age": 28.0, "Sex": "Female", "Weight": 58.0, "Height": 162.0, "Smoking": "No", "PhysicalActivity": "Sedentary",
        "FamilyHistory_DM": "No", "FamilyHistory_CAD": "No",
        "Hb": 10.2, "MCV": 71.0, "RBC": 3.8, "WBC": 5.8, "Platelet": 390.0, "NeutrophilsPercent": 61.0,
        "SerumIron": 24.0, "TIBC": 410.0, "Ferritin": 8.0, "FBS": 85.0, "HbA1c": 5.0, "Insulin": 5.0,
        "Total_Cholesterol": 180.0, "HDL": 48.0, "LDL": 102.0, "Triglycerides": 120.0, "Creatinine": 0.7,
        "BUN": 11.0, "Sodium": 139.0, "Potassium": 3.9, "ALT": 15.0, "AST": 18.0, "CRP": 2.1
    },
    "Metabolic Syndrome & Diabetic Nephropathy": {
        "Age": 56.0, "Sex": "Male", "Weight": 98.0, "Height": 175.0, "Smoking": "Yes", "PhysicalActivity": "Sedentary",
        "FamilyHistory_DM": "Yes", "FamilyHistory_CAD": "Yes", "Waist": 114.0, "Systolic_BP": 145.0, "Diastolic_BP": 92.0,
        "Hb": 13.8, "MCV": 92.0, "RBC": 4.6, "WBC": 7.8, "Platelet": 210.0, "NeutrophilsPercent": 63.0,
        "SerumIron": 85.0, "TIBC": 280.0, "Ferritin": 180.0, "FBS": 154.0, "HbA1c": 7.8, "Insulin": 22.4,
        "Total_Cholesterol": 245.0, "HDL": 34.0, "LDL": 152.0, "Triglycerides": 295.0, "Creatinine": 1.6,
        "BUN": 28.0, "Sodium": 138.0, "Potassium": 4.6, "ALT": 48.0, "AST": 42.0, "CRP": 6.8,
        "UrineAlbumin": 120.0, "UrineCreatinine": 100.0
    },
    "Hypothyroidism & High TSH": {
        "Age": 42.0, "Sex": "Female", "Weight": 82.0, "Height": 165.0, "Smoking": "No", "PhysicalActivity": "Light Activity",
        "FamilyHistory_DM": "No", "FamilyHistory_CAD": "No",
        "Hb": 12.1, "MCV": 89.0, "RBC": 4.1, "WBC": 6.2, "Platelet": 230.0, "TSH": 18.5, "FreeT4": 0.6, "Anti_TPO": 245.0,
        "FBS": 94.0, "HbA1c": 5.4, "Total_Cholesterol": 220.0, "HDL": 44.0, "LDL": 138.0, "Triglycerides": 140.0,
        "Creatinine": 0.8, "BUN": 13.0, "Sodium": 140.0, "Potassium": 4.0, "ALT": 21.0, "AST": 19.0, "CRP": 1.5
    }
}

st.title(t["title"])
st.markdown(t["subtitle"])
st.markdown("---")

# Quick presets
st.markdown(t["presets_heading"])
cols = st.columns(len(PRESETS))
for i, (name, preset_vals) in enumerate(PRESETS.items()):
    with cols[i]:
        if st.button(name, key=f"preset_{i}", use_container_width=True):
            for k in st.session_state.patient_inputs.keys():
                st.session_state.patient_inputs[k] = preset_vals.get(k, None)
            active_panels = []
            for p_name, categories in PANELS_TO_CATEGORIES.items():
                filtered = [
                    k for k, item in FEATURE_REGISTRY.items()
                    if item.get("category") in categories and not item.get("derived")
                ]
                if any(preset_vals.get(f_key) is not None for f_key in filtered):
                    active_panels.append(p_name)
            st.session_state.selected_panels = active_panels if active_panels else list(PANELS_TO_CATEGORIES.keys())
            st.session_state.step = 4
            st.success(f"Loaded '{name}' profile – {len(st.session_state.selected_panels)} panels auto‑selected.")
            st.rerun()

st.markdown("---")
with st.sidebar:
    # Language selector
    lang = st.selectbox("🌐 Language / زبان", ["en", "fa"], index=0 if st.session_state.lang == "en" else 1, key="lang_select")
    if lang != st.session_state.lang:
        st.session_state.lang = lang
        st.session_state.t = TRANSLATIONS[lang]
        t = st.session_state.t
        st.rerun()

    st.header(t["workflow_heading"])
    st.markdown(t["step_label"].format(step=st.session_state.step))
    steps_list = [
        "1. Clinical Profile & Demographics",
        "2. Select Active Lab Panels",
        "3. Enter Lab Biomarkers",
        "4. Diagnostics & AI Consultation"
    ]
    for s_idx, s_lbl in enumerate(steps_list):
        if st.session_state.step == s_idx + 1:
            st.markdown(f"🎯 **{s_lbl}**")
        elif st.session_state.step > s_idx + 1:
            st.markdown(f"✅ *{s_lbl}*")
        else:
            st.markdown(f"⚪ {s_lbl}")
    st.markdown("---")
    st.markdown(t["sidebar_reset"])
    if st.button(t["clear_btn"], use_container_width=True):
        st.session_state.patient_inputs = {k: None for k in FEATURE_REGISTRY.keys()}
        st.session_state.step = 1
        st.success(t["clear_success"])
        st.rerun()
step = st.session_state.step

def get_step_style(step_num):
    if step == step_num:
        return "background-color: #3b82f6; color: white; border-color: #3b82f6; font-weight: bold; box-shadow: 0 0 10px rgba(59,130,246,0.3);"
    elif step > step_num:
        return "background-color: #10b981; color: white; border-color: #10b981; font-weight: bold;"
    else:
        return "background-color: white; color: #94a3b8; border-color: #cbd5e1;"

st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px; background-color: white; padding: 16px 24px; border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
    <div style="display: flex; align-items: center; flex: 1; justify-content: center;">
        <span style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; border: 2px solid; margin-right: 10px; font-size: 13px; {get_step_style(1)}">1</span>
        <span style="font-size: 14px; font-weight: 500;">Clinical Profile</span>
    </div>
    <div style="width: 50px; height: 2px; background-color: #e2e8f0;"></div>
    <div style="display: flex; align-items: center; flex: 1; justify-content: center;">
        <span style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; border: 2px solid; margin-right: 10px; font-size: 13px; {get_step_style(2)}">2</span>
        <span style="font-size: 14px; font-weight: 500;">Select Panels</span>
    </div>
    <div style="width: 50px; height: 2px; background-color: #e2e8f0;"></div>
    <div style="display: flex; align-items: center; flex: 1; justify-content: center;">
        <span style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; border: 2px solid; margin-right: 10px; font-size: 13px; {get_step_style(3)}">3</span>
        <span style="font-size: 14px; font-weight: 500;">Biomarker Data</span>
    </div>
    <div style="width: 50px; height: 2px; background-color: #e2e8f0;"></div>
    <div style="display: flex; align-items: center; flex: 1; justify-content: center;">
        <span style="display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; border: 2px solid; margin-right: 10px; font-size: 13px; {get_step_style(4)}">4</span>
        <span style="font-size: 14px; font-weight: 500;">Analysis & Consult</span>
    </div>
</div>
""", unsafe_allow_html=True)
if step == 1:
    st.markdown(t["step1_title"])
    st.markdown(t["step1_desc"])
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("##### 👤 Demographics & Body Metrics")
            age = st.number_input("Age (Years)", min_value=1.0, max_value=120.0, value=float(st.session_state.patient_inputs.get("Age") or 35.0), step=1.0)
            st.session_state.patient_inputs["Age"] = age
            sex_sel = st.selectbox("Biological Sex", ["Male", "Female"], index=0 if st.session_state.patient_inputs.get("Sex") == "Male" else 1)
            st.session_state.patient_inputs["Sex"] = sex_sel
            weight = st.number_input("Weight (kg)", min_value=10.0, max_value=250.0, value=float(st.session_state.patient_inputs.get("Weight") or 70.0), step=0.5)
            st.session_state.patient_inputs["Weight"] = weight
            height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0, value=float(st.session_state.patient_inputs.get("Height") or 175.0), step=1.0)
            st.session_state.patient_inputs["Height"] = height
            waist = st.number_input("Waist Circumference (cm) – Optional", min_value=0.0, max_value=200.0, value=float(st.session_state.patient_inputs.get("Waist") or 0.0), step=1.0)
            st.session_state.patient_inputs["Waist"] = waist if waist > 0 else None
        with col2:
            st.markdown("##### 🩺 Vital Signs")
            sbp = st.number_input("Systolic BP (mmHg) – Optional", min_value=0.0, max_value=250.0, value=float(st.session_state.patient_inputs.get("Systolic_BP") or 0.0), step=1.0)
            st.session_state.patient_inputs["Systolic_BP"] = sbp if sbp > 0 else None
            dbp = st.number_input("Diastolic BP (mmHg) – Optional", min_value=0.0, max_value=150.0, value=float(st.session_state.patient_inputs.get("Diastolic_BP") or 0.0), step=1.0)
            st.session_state.patient_inputs["Diastolic_BP"] = dbp if dbp > 0 else None
            hr = st.number_input("Heart Rate (bpm) – Optional", min_value=0.0, max_value=220.0, value=float(st.session_state.patient_inputs.get("HeartRate") or 0.0), step=1.0)
            st.session_state.patient_inputs["HeartRate"] = hr if hr > 0 else None
            sleep = st.number_input("Sleep Duration (hours/day) – Optional", min_value=0.0, max_value=24.0, value=float(st.session_state.patient_inputs.get("SleepHours") or 0.0), step=0.5)
            st.session_state.patient_inputs["SleepHours"] = sleep if sleep > 0 else None
        with col3:
            st.markdown("##### 🧬 Family History & Lifestyle")
            smoking_checked = st.checkbox("Smoking Status (active smoker)", value=(st.session_state.patient_inputs.get("Smoking") == "Yes"), key="input_smoking")
            st.session_state.patient_inputs["Smoking"] = "Yes" if smoking_checked else "No"
            act_levels = ["Sedentary", "Light Activity", "Moderate (3-5 days/wk)", "Vigorous (6+ days/wk)"]
            curr_act = st.session_state.patient_inputs.get("PhysicalActivity", "Light Activity")
            act_idx = act_levels.index(curr_act) if curr_act in act_levels else 1
            act_sel = st.selectbox("Physical Activity Level", act_levels, index=act_idx)
            st.session_state.patient_inputs["PhysicalActivity"] = act_sel
            fh_dm_checked = st.checkbox("Family History of Diabetes", value=(st.session_state.patient_inputs.get("FamilyHistory_DM") == "Yes"), key="input_fh_dm")
            st.session_state.patient_inputs["FamilyHistory_DM"] = "Yes" if fh_dm_checked else "No"
            fh_cad_checked = st.checkbox("Family History of Heart Disease (CAD)", value=(st.session_state.patient_inputs.get("FamilyHistory_CAD") == "Yes"), key="input_fh_cad")
            st.session_state.patient_inputs["FamilyHistory_CAD"] = "Yes" if fh_cad_checked else "No"
            fh_htn_checked = st.checkbox("Family History of Hypertension", value=(st.session_state.patient_inputs.get("FamilyHistory_HTN") == "Yes"), key="input_fh_htn")
            st.session_state.patient_inputs["FamilyHistory_HTN"] = "Yes" if fh_htn_checked else "No"
            fh_ob_checked = st.checkbox("Family History of Obesity", value=(st.session_state.patient_inputs.get("FamilyHistory_Obesity") == "Yes"), key="input_fh_ob")
            st.session_state.patient_inputs["FamilyHistory_Obesity"] = "Yes" if fh_ob_checked else "No"
elif step == 2:
    st.markdown(t["step2_title"])
    st.markdown(t["step2_desc"])
    with st.container(border=True):
        st.markdown("##### 📁 Available Panels")
        selected = []
        cols = st.columns(3)
        for idx, panel_name in enumerate(PANELS_TO_CATEGORIES.keys()):
            col = cols[idx % 3]
            with col:
                is_checked = panel_name in st.session_state.selected_panels
                if st.checkbox(f"🧪 {panel_name}", value=is_checked, key=f"panel_check_{panel_name}"):
                    selected.append(panel_name)
        st.session_state.selected_panels = selected
    if not st.session_state.selected_panels:
        st.warning("⚠️ Please select at least one laboratory panel to proceed.")
elif step == 3:
    st.markdown(t["step3_title"])
    st.markdown(t["step3_desc"])
    gender_lower = st.session_state.patient_inputs["Sex"].lower()
    for panel_name in st.session_state.selected_panels:
        categories = PANELS_TO_CATEGORIES[panel_name]
        filtered = [k for k, item in FEATURE_REGISTRY.items()
                    if item.get("category") in categories and not item.get("derived") and k not in PROFILE_KEYS]
        for f_key in filtered:
            if st.session_state.patient_inputs.get(f_key) is None:
                f_data = FEATURE_REGISTRY[f_key]
                ref_list = f_data.get("referenceRanges", [])
                matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
                if f_key in QUAL_FEATURES:
                    st.session_state.patient_inputs[f_key] = QUAL_FEATURES[f_key][0]
                elif matched_ref and "range" in matched_ref:
                    st.session_state.patient_inputs[f_key] = float(sum(matched_ref["range"]) / 2.0)
                else:
                    st.session_state.patient_inputs[f_key] = 0.0

    st.markdown("##### 💡 Efficiency Helpers")
    if st.button(t["reset_btn"], use_container_width=True):
        for panel_name in st.session_state.selected_panels:
            categories = PANELS_TO_CATEGORIES[panel_name]
            filtered = [k for k, item in FEATURE_REGISTRY.items()
                        if item.get("category") in categories and not item.get("derived") and k not in PROFILE_KEYS]
            for f_key in filtered:
                f_data = FEATURE_REGISTRY[f_key]
                ref_list = f_data.get("referenceRanges", [])
                matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
                if f_key in QUAL_FEATURES:
                    st.session_state.patient_inputs[f_key] = QUAL_FEATURES[f_key][0]
                elif matched_ref and "range" in matched_ref:
                    st.session_state.patient_inputs[f_key] = float(sum(matched_ref["range"]) / 2.0)
                else:
                    st.session_state.patient_inputs[f_key] = 0.0
        st.success(t["reset_success"])
        st.rerun()

    st.markdown("---")
    if not st.session_state.selected_panels:
        st.warning("⚠️ No lab panels selected. Please go back to Step 2 and select at least one lab panel.")
    else:
        rendered_features = set()
        for panel_name in st.session_state.selected_panels:
            categories = PANELS_TO_CATEGORIES[panel_name]
            filtered_features = [(k, item) for k, item in FEATURE_REGISTRY.items()
                                 if item.get("category") in categories and not item.get("derived") and k not in PROFILE_KEYS]
            if not filtered_features:
                continue
            st.markdown(f"#### 📋 {panel_name}")
            with st.container(border=True):
                feat_cols = st.columns(2)
                col_idx = 0
                for f_key, f_data in filtered_features:
                    if f_key in rendered_features:
                        continue
                    rendered_features.add(f_key)
                    col = feat_cols[col_idx % 2]
                    col_idx += 1
                    with col:
                        ref_list = f_data.get("referenceRanges", [])
                        matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
                        ref_desc = "N/A"
                        if matched_ref and "range" in matched_ref:
                            ref_desc = f"{matched_ref['range'][0]} – {matched_ref['range'][1]}"
                        unit = f_data.get("unit", "")
                        label = f"**{f_data.get('displayEn')}** ({unit})" if unit else f"**{f_data.get('displayEn')}**"
                        if f_key in QUAL_FEATURES:
                            choices = QUAL_FEATURES[f_key]
                            if len(choices) == 2:
                                val = st.session_state.patient_inputs.get(f_key, "Negative")
                                is_checked = (val == "Positive")
                                checked = st.checkbox(
                                    f"{f_data.get('displayEn')} (Positive)",
                                    value=is_checked,
                                    key=f"input_check_{f_key}",
                                    help="Normal: Negative"
                                )
                                st.session_state.patient_inputs[f_key] = "Positive" if checked else "Negative"
                            else:
                                val = st.session_state.patient_inputs.get(f_key, choices[0])
                                curr_idx = choices.index(val) if val in choices else 0
                                sel_val = st.selectbox(
                                    label,
                                    choices,
                                    index=curr_idx,
                                    key=f"input_sel_{f_key}",
                                    help=f"Normal: {ref_desc}"
                                )
                                st.session_state.patient_inputs[f_key] = sel_val
                        else:
                            step_val = 0.1
                            min_val = 0.0
                            if f_key in ["Platelet", "SerumIron", "TIBC", "Ferritin", "FBS", "Total_Cholesterol", "HDL", "LDL", "Triglycerides", "BUN", "Sodium", "Zinc", "Magnesium", "Selenium", "Iodine", "VitaminA", "VitaminE", "VitaminC"]:
                                step_val = 1.0
                            elif f_key in ["TSH", "FreeT4", "Anti_TPO", "Creatinine", "Potassium", "ALT", "AST", "CRP"]:
                                step_val = 0.01 if f_key == "Creatinine" else 0.1
                            val = st.session_state.patient_inputs.get(f_key)
                            if val is None:
                                val = float(matched_ref["range"][0] if matched_ref and "range" in matched_ref else 0.0)
                            val_input = st.number_input(
                                label,
                                value=float(val),
                                step=step_val,
                                min_value=min_val,
                                key=f"input_num_{f_key}",
                                help=f"Normal: {ref_desc}"
                            )
                            st.session_state.patient_inputs[f_key] = val_input
                st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)
elif step == 4:
    st.markdown(t["step4_title"])
    st.markdown(t["step4_desc"])
    clean_inputs = {k: v for k, v in st.session_state.patient_inputs.items() if v is not None}
    patient_prof = {
        "Age": clean_inputs.get("Age", 35.0),
        "Sex": 1 if st.session_state.patient_inputs["Sex"] == "Male" else 2,
        "Weight": clean_inputs.get("Weight", 70.0),
        "Height": clean_inputs.get("Height", 175.0),
        "Smoking": 1 if st.session_state.patient_inputs["Smoking"] == "Yes" else 0,
        "PhysicalActivity": ["Sedentary", "Light Activity", "Moderate (3-5 days/wk)", "Vigorous (6+ days/wk)"].index(st.session_state.patient_inputs["PhysicalActivity"]),
        "FamilyHistory_DM": 1 if st.session_state.patient_inputs["FamilyHistory_DM"] == "Yes" else 0,
        "FamilyHistory_CAD": 1 if st.session_state.patient_inputs["FamilyHistory_CAD"] == "Yes" else 0
    }
    derived_markers = compute_all_derived(clean_inputs, patient_prof["Age"], "male" if patient_prof["Sex"] == 1 else "female")
    combined_data = {**clean_inputs, **derived_markers}
    active_diagnoses = interpret_lab_data(clean_inputs, derived_markers, patient_prof)
    risk_predictions = predict_2year_risks(clean_inputs, derived_markers, patient_prof, active_diagnoses)

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = BloodLabChatbot()
    chatbot = st.session_state.chatbot

    chatbot.build_and_set_context(
        patient_prof, clean_inputs, derived_markers,
        active_diagnoses, risk_predictions,
        FEATURE_REGISTRY, PROFILE_KEYS
    )

    if "initial_summary" not in st.session_state:
        with st.spinner(t["spinner_summary"]):
            st.session_state.initial_summary = chatbot.generate_initial_summary()

    st.markdown(t["summary_table_heading"])
    with st.expander(t["summary_table_expander"], expanded=True):
        summary_rows = []
        gender_lower = st.session_state.patient_inputs["Sex"].lower()
        profile_labels = {
            "Age": "Age", "Sex": "Sex", "Weight": "Weight", "Height": "Height",
            "Waist": "Waist Circumference", "Systolic_BP": "Systolic BP", "Diastolic_BP": "Diastolic BP",
            "HeartRate": "Heart Rate", "SleepHours": "Sleep Duration",
            "Smoking": "Smoking Status", "PhysicalActivity": "Physical Activity",
            "FamilyHistory_DM": "Family History of Diabetes", "FamilyHistory_CAD": "Family History of CAD",
            "FamilyHistory_HTN": "Family History of Hypertension", "FamilyHistory_Obesity": "Family History of Obesity"
        }
        for p_key, p_label in profile_labels.items():
            p_val = st.session_state.patient_inputs.get(p_key)
            if p_val is not None:
                f_data = FEATURE_REGISTRY.get(p_key, {})
                unit = f_data.get("unit", "")
                ref_desc = "N/A"
                ref_list = f_data.get("referenceRanges", [])
                matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
                if matched_ref and "range" in matched_ref:
                    ref_desc = f"{matched_ref['range'][0]} – {matched_ref['range'][1]}"
                status_str = "Normal ✅"
                if matched_ref and "range" in matched_ref:
                    try:
                        vn = float(p_val)
                        if vn < matched_ref["range"][0]:
                            status_str = "Low 🔽"
                        elif vn > matched_ref["range"][1]:
                            status_str = "High 🔼"
                    except:
                        pass
                summary_rows.append({
                    "Category": "Clinical Profile",
                    "Biomarker": p_label,
                    "Value": str(p_val),
                    "Unit": unit,
                    "Reference Range": ref_desc,
                    "Status": status_str
                })
        for panel_name in st.session_state.selected_panels:
            categories = PANELS_TO_CATEGORIES[panel_name]
            filtered = [(k, item) for k, item in FEATURE_REGISTRY.items()
                        if item.get("category") in categories and not item.get("derived") and k not in PROFILE_KEYS]
            for f_key, f_data in filtered:
                val = st.session_state.patient_inputs.get(f_key)
                if val is not None:
                    unit = f_data.get("unit", "")
                    ref_desc = "N/A"
                    ref_list = f_data.get("referenceRanges", [])
                    matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
                    if matched_ref and "range" in matched_ref:
                        ref_desc = f"{matched_ref['range'][0]} – {matched_ref['range'][1]}"
                    status_str = "Normal ✅"
                    if f_key in QUAL_FEATURES:
                        if val in ["Positive", "Trace", "1+", "2+", "3+", "4+", "Small", "Moderate", "Large"]:
                            status_str = "Abnormal ⚠️"
                    elif matched_ref and "range" in matched_ref:
                        try:
                            vn = float(val)
                            if vn < matched_ref["range"][0]:
                                status_str = "Low 🔽"
                            elif vn > matched_ref["range"][1]:
                                status_str = "High 🔼"
                        except:
                            pass
                    summary_rows.append({
                        "Category": panel_name,
                        "Biomarker": f_data.get("displayEn", f_key),
                        "Value": str(val),
                        "Unit": unit,
                        "Reference Range": ref_desc,
                        "Status": status_str
                    })
        for d_key, d_val in derived_markers.items():
            f_data = FEATURE_REGISTRY.get(d_key, {})
            unit = f_data.get("unit", "")
            ref_desc = "N/A"
            ref_list = f_data.get("referenceRanges", [])
            matched_ref = next((r for r in ref_list if r.get("gender") == gender_lower), ref_list[0] if ref_list else None)
            if matched_ref and "range" in matched_ref:
                ref_desc = f"{matched_ref['range'][0]} – {matched_ref['range'][1]}"
            status_str = "Normal ✅"
            if matched_ref and "range" in matched_ref:
                try:
                    vn = float(d_val)
                    if vn < matched_ref["range"][0]:
                        status_str = "Low 🔽"
                    elif vn > matched_ref["range"][1]:
                        status_str = "High 🔼"
                except:
                    pass
            summary_rows.append({
                "Category": "Derived Metrics",
                "Biomarker": f_data.get("displayEn", d_key),
                "Value": str(d_val),
                "Unit": unit,
                "Reference Range": ref_desc,
                "Status": status_str
            })
        if summary_rows:
            st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)
        else:
            st.info("No clinical or lab data entered.")

    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔬 Clinical Interpretations",
        "🔮 2‑Year Risk Forecasting",
        "📘 Guideline Registry Search",
        "🧠 Expert AI Consulting",
        "💬 BloodLab AI Assistant"
    ])

    with tab1:
        st.markdown(t["derived_metrics_heading"])
        if derived_markers:
            d_cols = st.columns(min(len(derived_markers), 4))
            for idx, (dk, dv) in enumerate(derived_markers.items()):
                with d_cols[idx % len(d_cols)]:
                    unit = FEATURE_REGISTRY.get(dk, {}).get("unit", "")
                    st.markdown(f"""
                    <div class="clinical-card" style="padding: 12px; text-align: center; margin-bottom: 10px; border-top: 3px solid #3b82f6;">
                        <div class="metric-label">{dk}</div>
                        <div class="metric-value" style="font-size: 20px;">{dv} <span style="font-size: 11px; font-weight: normal; color: #64748b;">{unit}</span></div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("No derived metrics calculated yet.")

        st.markdown(t["disease_heading"])
        active_panel_diseases = []
        for panel_name in st.session_state.selected_panels:
            active_panel_diseases.extend([d for d in DISEASE_GUIDELINES if GUIDELINE_CATEGORY_TO_PANEL.get(d["category"]) == panel_name])
        unique = []
        seen = set()
        for d in active_panel_diseases:
            if d["name"] not in seen:
                seen.add(d["name"])
                unique.append(d)

        compat = not_compat = incomp = no_dat = 0
        for d in unique:
            matched = next((diag for diag in active_diagnoses if diag["nameEn"] == d["name"]), None)
            entered_count = sum(1 for feat in d["required_features"] if combined_data.get(feat) is not None)
            if matched:
                compat += 1
            elif entered_count == 0:
                no_dat += 1
            elif entered_count < len(d["required_features"]):
                incomp += 1
            else:
                not_compat += 1

        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        with m_col1:
            st.markdown(f"""<div style="background-color:#fef2f2;border:1px solid #fecaca;padding:12px;border-radius:8px;text-align:center;margin-bottom:15px;border-top:4px solid #ef4444;">
                <div style="font-size:11px;font-weight:bold;color:#991b1b;">{t["compatible_count"]}</div><div style="font-size:24px;font-weight:bold;color:#ef4444;">{compat}</div></div>""", unsafe_allow_html=True)
        with m_col2:
            st.markdown(f"""<div style="background-color:#f0fdf4;border:1px solid #bbf7d0;padding:12px;border-radius:8px;text-align:center;margin-bottom:15px;border-top:4px solid #10b981;">
                <div style="font-size:11px;font-weight:bold;color:#166534;">{t["no_evidence_count"]}</div><div style="font-size:24px;font-weight:bold;color:#10b981;">{not_compat}</div></div>""", unsafe_allow_html=True)
        with m_col3:
            st.markdown(f"""<div style="background-color:#fffbeb;border:1px solid #fde68a;padding:12px;border-radius:8px;text-align:center;margin-bottom:15px;border-top:4px solid #f59e0b;">
                <div style="font-size:10px;font-weight:bold;color:#92400e;">{t["incomplete_count"]}</div><div style="font-size:24px;font-weight:bold;color:#f59e0b;">{incomp}</div></div>""", unsafe_allow_html=True)
        with m_col4:
            st.markdown(f"""<div style="background-color:#f8fafc;border:1px solid #e2e8f0;padding:12px;border-radius:8px;text-align:center;margin-bottom:15px;border-top:4px solid #64748b;">
                <div style="font-size:11px;font-weight:bold;color:#475569;">{t["no_data_count"]}</div><div style="font-size:24px;font-weight:bold;color:#64748b;">{no_dat}</div></div>""", unsafe_allow_html=True)

        st.markdown("---")
        col_sort, col_filter = st.columns(2)
        with col_filter:
            filter_opt = st.selectbox(t["filter_label"], [t["show_all"], t["compatible_only"], t["incomplete_only"], t["no_data_only"]], key="filter_opt")
        with col_sort:
            sort_opt = st.selectbox(t["sort_label"], [t["default_sort"], t["compatible_first_sort"], t["az_sort"]], key="sort_opt")

        evaluated = []
        for d in unique:
            matched = next((diag for diag in active_diagnoses if diag["nameEn"] == d["name"]), None)
            entered_count = sum(1 for feat in d["required_features"] if combined_data.get(feat) is not None)
            if matched:
                status_label = "Compatible"
                status_text = "🚨 Compatible with Evidence"
                order = 0
                badge = "background-color:#fef2f2;border:1px solid #fecaca;color:#991b1b;padding:14px;border-radius:8px;margin-bottom:12px;border-left:5px solid #ef4444;"
                evidence_list = matched["evidence"]
            elif entered_count == 0:
                status_label = "No Data"
                status_text = "⚪ No Input Data"
                order = 3
                badge = "background-color:#f8fafc;border:1px solid #e2e8f0;color:#64748b;padding:10px;border-radius:8px;margin-bottom:8px;"
                evidence_list = []
            elif entered_count < len(d["required_features"]):
                status_label = "Incomplete"
                status_text = "⚠️ Incomplete Data"
                order = 2
                badge = "background-color:#fffbeb;border:1px solid #fde68a;color:#92400e;padding:12px;border-radius:8px;margin-bottom:12px;border-left:5px solid #f59e0b;"
                evidence_list = []
            else:
                status_label = "No Evidence"
                status_text = "🟢 Not Compatible"
                order = 1
                badge = "background-color:#f0fdf4;border:1px solid #bbf7d0;color:#166534;padding:12px;border-radius:8px;margin-bottom:12px;border-left:5px solid #10b981;"
                evidence_list = []
            evaluated.append({
                "disease": d,
                "status_label": status_label,
                "status_text": status_text,
                "order": order,
                "badge": badge,
                "evidence": evidence_list
            })

        if filter_opt == t["compatible_only"]:
            evaluated = [x for x in evaluated if x["status_label"] == "Compatible"]
        elif filter_opt == t["incomplete_only"]:
            evaluated = [x for x in evaluated if x["status_label"] == "Incomplete"]
        elif filter_opt == t["no_data_only"]:
            evaluated = [x for x in evaluated if x["status_label"] == "No Data"]

        if sort_opt == t["compatible_first_sort"]:
            evaluated.sort(key=lambda x: x["order"])
        elif sort_opt == t["az_sort"]:
            evaluated.sort(key=lambda x: x["disease"]["name"].lower())

        if sort_opt == t["default_sort"]:
            for panel_name in st.session_state.selected_panels:
                panel_items = [x for x in evaluated if GUIDELINE_CATEGORY_TO_PANEL.get(x["disease"]["category"]) == panel_name]
                if panel_items:
                    with st.container(border=True):
                        st.markdown(f"##### 📁 {panel_name}")
                        for item in panel_items:
                            d = item["disease"]
                            icd = d["icd10"]
                            criteria_desc = d["criteria"]
                            guideline_ref = d["guideline"]
                            if item["status_label"] == "Compatible":
                                ev_html = "".join([f"<li>{ev}</li>" for ev in item["evidence"]])
                                st.markdown(f"""<div style="{item['badge']}">
                                    <div style="display:flex;justify-content:space-between;align-items:center;font-weight:bold;font-size:15px;">
                                        <span>📘 {d['name']} (ICD‑10: {icd})</span>
                                        <span style="font-size:11px;background-color:#ef4444;color:white;padding:3px 8px;border-radius:4px;">{item['status_text']}</span>
                                    </div>
                                    <div style="font-size:13px;margin-top:10px;line-height:1.5;color:#1e293b;">
                                        <strong style="color:#991b1b;">📋 Evidence:</strong>
                                        <ul style="margin:6px 0 10px 0;padding-left:20px;color:#451a03;">{ev_html}</ul>
                                        <strong>🧬 Criteria:</strong> {criteria_desc}<br>
                                        <span style="font-size:11px;color:#64748b;">Reference: {guideline_ref}</span>
                                    </div>
                                </div>""", unsafe_allow_html=True)
                            else:
                                st.markdown(f"""<div style="{item['badge']}">
                                    <div style="display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:13px;">
                                        <span>📘 {d['name']} (ICD‑10: {icd})</span>
                                        <span style="font-size:10px;background-color:#10b981;color:white;padding:2px 6px;border-radius:4px;">{item['status_text']}</span>
                                    </div>
                                    <div style="font-size:12px;margin-top:6px;line-height:1.4;color:#1e3a1e;">
                                        Criteria: {criteria_desc}
                                    </div>
                                </div>""", unsafe_allow_html=True)
        else:
            if evaluated:
                for item in evaluated:
                    d = item["disease"]
                    icd = d["icd10"]
                    criteria_desc = d["criteria"]
                    guideline_ref = d["guideline"]
                    if item["status_label"] == "Compatible":
                        ev_html = "".join([f"<li>{ev}</li>" for ev in item["evidence"]])
                        st.markdown(f"""<div style="{item['badge']}">
                            <div style="display:flex;justify-content:space-between;align-items:center;font-weight:bold;font-size:15px;">
                                <span>📘 {d['name']} (ICD‑10: {icd})</span>
                                <span style="font-size:11px;background-color:#ef4444;color:white;padding:3px 8px;border-radius:4px;">{item['status_text']}</span>
                            </div>
                            <div style="font-size:13px;margin-top:10px;line-height:1.5;color:#1e293b;">
                                <strong style="color:#991b1b;">📋 Evidence:</strong>
                                <ul style="margin:6px 0 10px 0;padding-left:20px;color:#451a03;">{ev_html}</ul>
                                <strong>🧬 Criteria:</strong> {criteria_desc}<br>
                                <span style="font-size:11px;color:#64748b;">Reference: {guideline_ref}</span>
                            </div>
                        </div>""", unsafe_allow_html=True)
                    else:
                        st.markdown(f"""<div style="{item['badge']}">
                            <div style="display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:13px;">
                                <span>📘 {d['name']} (ICD‑10: {icd})</span>
                                <span style="font-size:10px;background-color:#10b981;color:white;padding:2px 6px;border-radius:4px;">{item['status_text']}</span>
                            </div>
                            <div style="font-size:12px;margin-top:6px;line-height:1.4;color:#1e3a1e;">
                                Criteria: {criteria_desc}
                            </div>
                        </div>""", unsafe_allow_html=True)
            else:
                st.info("No diseases match the selected filter.")

    with tab2:
        st.markdown(t["risk_heading"])
        already = [r for r in risk_predictions if r.get("status") == "AlreadyDiagnosed"]
        evaluated_risks = [r for r in risk_predictions if r.get("status") == "Evaluated"]
        insufficient = [r for r in risk_predictions if r.get("status") == "Insufficient Data"]
        excluded = [r for r in risk_predictions if r.get("status") == "Excluded"]
        if already:
            st.markdown("##### 🚨 Active Clinical Diagnoses (No Risk Prediction Needed)")
            for pred in already:
                st.markdown(f"""<div class="clinical-card" style="padding:16px;margin-bottom:12px;border-left:5px solid #ef4444;background-color:#fef2f2;border:1px solid #fecaca;border-radius:8px;">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span style="font-size:14px;font-weight:bold;color:#991b1b;">📊 {pred['nameEn']}</span>
                        <span style="background-color:#fecaca;color:#ef4444;font-size:11px;font-weight:bold;padding:3px 8px;border-radius:4px;">Active Diagnosis</span>
                    </div>
                    <div style="font-size:13px;margin-top:8px;color:#7f1d1d;">This condition is already present; risk prediction is not applicable.</div>
                </div>""", unsafe_allow_html=True)
            st.markdown("---")
        if evaluated_risks:
            for pred in evaluated_risks:
                prob = pred.get("probability", 0.0)
                risk_lvl = pred.get("riskLevel", "Low")
                risk_colors = {"Very High": ("#ef4444","#fee2e2"), "High": ("#f97316","#ffedd5"), "Moderate": ("#eab308","#fef9c3"), "Low": ("#10b981","#d1fae5")}
                pc, bg = risk_colors.get(risk_lvl, ("#10b981","#d1fae5"))
                st.markdown(f"""<div class="clinical-card" style="padding:16px;margin-bottom:8px;border-left:5px solid {pc};">
                    <div style="display:flex;justify-content:space-between;align-items:center;">
                        <span style="font-size:14px;font-weight:600;color:#0f172a;">{pred['nameEn']}</span>
                        <span style="background-color:{bg};color:{pc};font-size:11px;font-weight:bold;padding:2px 8px;border-radius:4px;">{risk_lvl} RISK ({round(prob*100,1)}%)</span>
                    </div>
                    <div style="width:100%;background-color:#e2e8f0;height:8px;border-radius:4px;margin-top:8px;overflow:hidden;">
                        <div style="width:{prob*100}%;background-color:{pc};height:100%;"></div>
                    </div>
                </div>""", unsafe_allow_html=True)
        elif not already:
            st.info("No risk prediction models have sufficient data. Fill required parameters in Step 3.")
        if insufficient or excluded:
            st.markdown("##### 🔍 Pending & Excluded Models")
            for pred in insufficient:
                missing = ", ".join([FEATURE_REGISTRY.get(m,{}).get("displayEn", m) for m in pred["missingFeatures"]])
                st.markdown(f"""<div style="padding:10px 14px;background-color:#f1f5f9;border:1px solid #cbd5e1;border-radius:8px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;">
                    <span style="font-size:13px;color:#475569;font-weight:500;">📊 {pred['nameEn']}</span>
                    <span style="font-size:11px;color:#64748b;font-style:italic;">Missing: {missing}</span>
                </div>""", unsafe_allow_html=True)
            for pred in excluded:
                st.markdown(f"""<div style="padding:10px 14px;background-color:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;margin-bottom:8px;display:flex;justify-content:space-between;align-items:center;">
                    <span style="font-size:13px;color:#64748b;font-weight:500;text-decoration:line-through;">📊 {pred['nameEn']}</span>
                    <span style="font-size:11px;color:#94a3b8;font-style:italic;">Excluded: {pred['exclusionReason']}</span>
                </div>""", unsafe_allow_html=True)

    with tab3:
        st.markdown(t["guideline_heading"])
        st.markdown("Search and filter the complete clinical database of 100+ diagnostic guidelines.")
        col1, col2 = st.columns([1,1])
        with col1:
            search_query = st.text_input("🔍 Search by disease name or ICD‑10 code", key="search_guideline")
        with col2:
            categories_list = ["All Categories"] + sorted(set(d["category"] for d in DISEASE_GUIDELINES))
            selected_cat = st.selectbox("Filter by Lab Panel Type", categories_list, key="cat_select")
        matched = []
        for d in DISEASE_GUIDELINES:
            if selected_cat != "All Categories" and d["category"] != selected_cat:
                continue
            if search_query and search_query.lower() not in d["name"].lower() and search_query.lower() not in d["icd10"].lower():
                continue
            matched.append(d)
        if matched:
            st.markdown(f"Showing **{len(matched)}** matching guidelines:")
            for d in matched:
                with st.expander(f"📘 {d['name']} (ICD‑10: {d['icd10']}) — {d['category']}"):
                    st.markdown(f"""
                    - **Guideline:** `{d['guideline']}`
                    - **Required Markers:** {", ".join([FEATURE_REGISTRY.get(m,{}).get("displayEn", m) for m in d['required_features']])}
                    - **Criteria:** {d['criteria']}
                    """)
        else:
            st.info("No matching guidelines found.")

    with tab4:
        st.markdown(t["expert_heading"])
        def generate_ai_interpretation(patient_info, inputs, derived, diagnoses, risks):
            api_key = os.environ.get("GROQ_API_KEY")
            if not api_key:
                try:
                    api_key = st.secrets["GROQ_API_KEY"]
                except (FileNotFoundError, KeyError):
                    return "Groq API key not configured."

            try:
                client = groq.Client(api_key=api_key)

                lang = st.session_state.get("lang", "en")

                abnormal_labs = []
                gender_lower = "male" if patient_info.get("Sex") == 1 else "female"
                for key, val in inputs.items():
                    if key in PROFILE_KEYS:
                        continue
                    fdata = FEATURE_REGISTRY.get(key, {})
                    refs = fdata.get("referenceRanges", [])
                    ref = next((r for r in refs if r.get("gender") == gender_lower), refs[0] if refs else None)
                    if ref and "range" in ref:
                        low, high = ref["range"]
                        try:
                            v = float(val)
                            if v < low:
                                abnormal_labs.append(f"{fdata.get('displayEn', key)}: {v} {fdata.get('unit','')} ⬇️ LOW (normal {low}-{high})")
                            elif v > high:
                                abnormal_labs.append(f"{fdata.get('displayEn', key)}: {v} {fdata.get('unit','')} ⬆️ HIGH (normal {low}-{high})")
                        except:
                            pass
                        
                compat_names = []
                noncompat_names = []
                incomplete_names = []
                for d in diagnoses:
                    status = d.get("status", "")
                    evidence = d.get("evidence", [])
                    name = d.get("nameEn", "")
                    if status == "Present" or "Compatible" in str(evidence):
                        compat_names.append(name)
                    elif status == "Insufficient Data":
                        incomplete_names.append(name)
                    else:
                        noncompat_names.append(name)

                risk_text = ", ".join(
                    [f"{r.get('nameEn','')} ({round(r.get('probability',0)*100,1)}% - {r.get('riskLevel','')})"
                     for r in risks if r.get("status") in ("Evaluated", "AlreadyDiagnosed")]
                ) if risks else "None"

                if lang == "fa":
                    prompt = f"""
        شما یک پزشک مشاور بالینی هستید. بر اساس اطلاعات زیر یک **گزارش روایی و یکپارچه** (نه لیست) به فارسی بنویسید.
        یافته‌های مهم را با پیشنهادات عملی ترکیب کنید و به تفاسیر بالینی ارجاع دهید.

        ### مشخصات بیمار
        سن {patient_info.get('Age')}، {"مرد" if patient_info.get('Sex')==1 else "زن"}، BMI {derived.get('BMI','N/A')}، سیگار {"بله" if patient_info.get('Smoking')==1 else "خیر"}

        ### آزمایش‌های غیرطبیعی
        {json.dumps(abnormal_labs, indent=2) if abnormal_labs else "همه موارد در محدوده طبیعی"}

        ### شاخص‌های محاسباتی
        eGFR: {derived.get('eGFR','N/A')} | ACR: {derived.get('ACR','N/A')} | HOMA-IR: {derived.get('HOMA_IR','N/A')}

        ### بیماری‌های سازگار با گایدلاین (تأیید شده با شواهد)
        {', '.join(compat_names) if compat_names else 'موردی یافت نشد'}

        ### بیماری‌های رد شده
        {', '.join(noncompat_names) if noncompat_names else 'موردی نیست'}

        ### بیماری‌های نیازمند آزمایش بیشتر
        {', '.join(incomplete_names) if incomplete_names else 'موردی نیست'}

        ### ریسک‌های ۲ ساله
        {risk_text}

        **دستور تهیه گزارش:**
        - یک متن روان و منسجم بنویس، نه لیست گلوله‌ای.
        - ابتدا مهم‌ترین یافته‌های غیرطبیعی را مرور کن و ارتباط آن‌ها را با بیماری‌های سازگار توضیح بده.
        - سپس به بیماری‌های رد شده و علت رد آن‌ها اشاره کن (بدون اینکه دوباره فهرست کنی).
        - بر اساس یافته‌ها، یک سری **پیشنهادات عملی** (مانند آزمایش‌های تکمیلی، اصلاح سبک زندگی، مراجعه به متخصص) ارائه کن.
        - در انتها یک ارزیابی کلی ۴-۵ جمله‌ای بنویس که وضعیت بیمار را جمع‌بندی کند.
        - **ارجاعات به تفاسیر بالینی** را با ذکر نام بیماری‌ها در دل متن بیاور (مثلاً «با توجه به معیارهای ADA، بیمار شرایط دیابت نوع ۲ را دارد»).
        - از مقادیر واقعی استفاده کن و چیزی اختراع نکن. تشخیص قطعی نده.
        """
                else:
                    prompt = f"""
        You are a clinical consultant. Based on the data below, write a **cohesive narrative report** (not a bullet list) in English.
        Weave the important findings together with practical suggestions and clinical interpretation references.

        ### Patient
        Age {patient_info.get('Age')}, {"Male" if patient_info.get('Sex')==1 else "Female"}, BMI {derived.get('BMI','N/A')}, Smoking {"Yes" if patient_info.get('Smoking')==1 else "No"}

        ### Abnormal Labs
        {json.dumps(abnormal_labs, indent=2) if abnormal_labs else "All within normal limits"}

        ### Derived Metrics
        eGFR: {derived.get('eGFR','N/A')} | ACR: {derived.get('ACR','N/A')} | HOMA-IR: {derived.get('HOMA_IR','N/A')}

        ### Guideline-Compatible Conditions (confirmed)
        {', '.join(compat_names) if compat_names else 'None'}

        ### Ruled Out Conditions
        {', '.join(noncompat_names) if noncompat_names else 'None'}

        ### Conditions Requiring Further Data
        {', '.join(incomplete_names) if incomplete_names else 'None'}

        ### 2-Year Risk Predictions
        {risk_text}

        **Report Instructions:**
        - Write a smooth, flowing narrative, not bullet points.
        - Start by reviewing the most significant abnormal findings and explain their relationship to the compatible conditions.
        - Mention ruled-out conditions and briefly why they don't apply (without listing).
        - Based on the findings, provide **practical suggestions** (e.g., additional tests, lifestyle modifications, specialist referrals).
        - End with a 4-5 sentence overall assessment.
        - **Reference the clinical interpretations** by mentioning disease names within the narrative (e.g., "According to ADA criteria, the patient meets the threshold for type 2 diabetes").
        - Use real values; do not invent. Do not give a definitive diagnosis.
        """

                messages = [
                    {"role": "system", "content": "You are a clinical consultant. Write a cohesive, evidence-based report that integrates findings, references, and recommendations."},
                    {"role": "user", "content": prompt}
                ]
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=messages,
                    temperature=0.3,
                    max_tokens=800
                )
                return response.choices[0].message.content

            except Exception as e:
                return f"Failed to generate AI interpretation: {str(e)}"
        if st.button(t["generate_expert_btn"], type="primary", use_container_width=True):
            with st.spinner(t["spinner_expert"]):
                ai_report = generate_ai_interpretation(patient_prof, clean_inputs, derived_markers, active_diagnoses, risk_predictions)
                st.markdown(t["expert_report_heading"])
                if st.session_state.lang == "fa":
                    st.markdown(
                        f'<div style="direction: rtl; text-align: justify; font-family: Vazir, sans-serif;">{ai_report}</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(ai_report)

    with tab5:
        st.markdown(t["chat_heading"])
        st.markdown(t["chat_desc"])
        if "initial_summary" in st.session_state:
#            st.info(t["chat_summary_info"])
            summary_text = st.session_state.initial_summary
            if st.session_state.lang == "fa":
                st.markdown(
                    f'<div style="direction: rtl; text-align: justify; font-family: Vazir, sans-serif;">{summary_text}</div>',
                    unsafe_allow_html=True
                )
            else:
                st.markdown(summary_text)
        for msg in chatbot.history:
            with st.chat_message(msg["role"]):
                content = msg["content"]
                if msg["role"] == "assistant" and st.session_state.lang == "fa":
                    st.markdown(
                        f'<div style="direction: rtl; text-align: justify; font-family: Vazir, sans-serif;">{content}</div>',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(content)
        if user_query := st.chat_input(t["chat_placeholder"]):
            with st.chat_message("user"):
                st.markdown(user_query)
            with st.chat_message("assistant"):
                with st.spinner(t["thinking"]):
                    reply = chatbot.chat(user_query)
                st.markdown(reply)
            st.rerun()
            
st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
col_prev, _, col_next = st.columns([1.5, 4, 1.5])
with col_prev:
    if step > 1:
        if st.button(t["previous_btn"], use_container_width=True):
            st.session_state.step -= 1
            st.rerun()
with col_next:
    if step < 4:
        lbl = t["next_btn1"] if step == 1 else (t["next_btn2"] if step == 2 else t["next_btn3"])
        if st.button(lbl, use_container_width=True, type="primary"):
            st.session_state.step += 1
            st.rerun()
