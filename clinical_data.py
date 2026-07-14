class FeatureCategory:
    CLINICAL = "Clinical"
    CBC = "CBC"
    IRON = "Iron Studies"
    VITAMIN = "Vitamin Panel"
    THYROID = "Thyroid Panel"
    BLOOD_SUGAR = "Diabetes Panel"
    LIPID = "Lipid Panel"
    KIDNEY = "Renal Panel"
    LIVER = "Liver Panel"
    ELECTROLYTE = "Electrolyte Panel"
    CARDIAC = "Cardiac Biomarkers"
    COAGULATION = "Coagulation Panel"
    INFLAMMATORY = "Inflammatory Panel"
    AUTOIMMUNE = "Autoimmune Panel"
    RHEUMATOLOGY = "Rheumatology Panel"
    HEPATITIS = "Hepatitis Panel"
    ENDOCRINE = "Endocrine Panel"
    REPRODUCTIVE = "Reproductive Panel"
    TUMOR_MARKER = "Tumor Marker Panel"
    PANCREATIC = "Pancreatic Panel"
    ACID_BASE = "Acid Base Panel"
    URINALYSIS = "Urinalysis"
    URINE_PROTEIN = "Urine Protein"
    NUTRITION = "Nutrition"
    MICRONUTRIENT = "Micronutrient"
    HORMONES = "Hormones"
    MUSCLE = "Muscle Enzymes"
    HEMOLYSIS = "Hemolysis Markers"
    INFECTIOUS = "Infectious Serology"

FEATURE_REGISTRY = {
    "Age": {
        "canonical": "Age",
        "displayEn": "Age",
        "unit": "years",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["age"],
        "referenceRanges": [{"range": [0, 120]}]
    },
    "Sex": {
        "canonical": "Sex",
        "displayEn": "Sex",
        "unit": "Male/Female",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["sex", "gender"]
    },
    "Height": {
        "canonical": "Height",
        "displayEn": "Height",
        "unit": "cm",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["height"]
    },
    "Weight": {
        "canonical": "Weight",
        "displayEn": "Weight",
        "unit": "kg",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["weight"]
    },
    "BMI": {
        "canonical": "BMI",
        "displayEn": "BMI",
        "unit": "kg/m²",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["bmi"],
        "derived": True,
        "referenceRanges": [{"range": [18.5, 24.9]}]
    },
    "Waist": {
        "canonical": "Waist",
        "displayEn": "Waist Circumference",
        "unit": "cm",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["waist"],
        "referenceRanges": [
            {"gender": "male", "range": [0, 102]},
            {"gender": "female", "range": [0, 88]}
        ]
    },
    "Systolic_BP": {
        "canonical": "Systolic_BP",
        "displayEn": "Systolic Blood Pressure",
        "unit": "mmHg",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["sbp"],
        "referenceRanges": [{"range": [90, 120]}]
    },
    "Diastolic_BP": {
        "canonical": "Diastolic_BP",
        "displayEn": "Diastolic Blood Pressure",
        "unit": "mmHg",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["dbp"],
        "referenceRanges": [{"range": [60, 80]}]
    },
    "HeartRate": {
        "canonical": "HeartRate",
        "displayEn": "Heart Rate",
        "unit": "bpm",
        "category": FeatureCategory.CLINICAL,
        "aliases": ["hr", "pulse"],
        "referenceRanges": [{"range": [60, 100]}]
    },

    "WBC": {
        "canonical": "WBC",
        "displayEn": "WBC (White Blood Cells)",
        "unit": "10^9/L",
        "category": FeatureCategory.CBC,
        "aliases": ["wbc", "leukocyte"],
        "referenceRanges": [{"range": [4.0, 11.0]}]
    },
    "RBC": {
        "canonical": "RBC",
        "displayEn": "RBC (Red Blood Cells)",
        "unit": "10^12/L",
        "category": FeatureCategory.CBC,
        "aliases": ["rbc", "erythrocyte"],
        "referenceRanges": [
            {"gender": "male", "range": [4.5, 5.9]},
            {"gender": "female", "range": [4.0, 5.2]}
        ]
    },
    "Hb": {
        "canonical": "Hb",
        "displayEn": "Hemoglobin",
        "unit": "g/dL",
        "category": FeatureCategory.CBC,
        "aliases": ["hgb", "hb", "haemoglobin"],
        "referenceRanges": [
            {"gender": "male", "range": [13.5, 17.5]},
            {"gender": "female", "range": [12.0, 16.0]}
        ]
    },
    "Hct": {
        "canonical": "Hct",
        "displayEn": "Hematocrit",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["hct", "hematocrit"],
        "referenceRanges": [
            {"gender": "male", "range": [41.0, 50.0]},
            {"gender": "female", "range": [36.0, 46.0]}
        ]
    },
    "MCV": {
        "canonical": "MCV",
        "displayEn": "MCV (Mean Corpuscular Volume)",
        "unit": "fL",
        "category": FeatureCategory.CBC,
        "aliases": ["mcv"],
        "referenceRanges": [{"range": [80.0, 100.0]}]
    },
    "MCH": {
        "canonical": "MCH",
        "displayEn": "MCH",
        "unit": "pg",
        "category": FeatureCategory.CBC,
        "aliases": ["mch"],
        "referenceRanges": [{"range": [27.0, 33.0]}]
    },
    "MCHC": {
        "canonical": "MCHC",
        "displayEn": "MCHC",
        "unit": "g/dL",
        "category": FeatureCategory.CBC,
        "aliases": ["mchc"],
        "referenceRanges": [{"range": [32.0, 36.0]}]
    },
    "RDW": {
        "canonical": "RDW",
        "displayEn": "RDW (Red Cell Distribution Width)",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["rdw"],
        "referenceRanges": [{"range": [11.5, 14.5]}]
    },
    "Platelet": {
        "canonical": "Platelet",
        "displayEn": "Platelet Count",
        "unit": "10^9/L",
        "category": FeatureCategory.CBC,
        "aliases": ["plt", "platelets"],
        "referenceRanges": [{"range": [150, 450]}]
    },
    "NeutrophilsPercent": {
        "canonical": "NeutrophilsPercent",
        "displayEn": "Neutrophils %",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["neut_pct", "neutrophils_pct"],
        "referenceRanges": [{"range": [40, 75]}]
    },
    "LymphocytesPercent": {
        "canonical": "LymphocytesPercent",
        "displayEn": "Lymphocytes %",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["lymph_pct", "lymphocytes_pct"],
        "referenceRanges": [{"range": [20, 45]}]
    },
    "MonocytesPercent": {
        "canonical": "MonocytesPercent",
        "displayEn": "Monocytes %",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["mono_pct", "monocytes_pct"],
        "referenceRanges": [{"range": [2, 10]}]
    },
    "EosinophilsPercent": {
        "canonical": "EosinophilsPercent",
        "displayEn": "Eosinophils %",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["eos_pct", "eosinophils_pct"],
        "referenceRanges": [{"range": [1, 6]}]
    },
    "BasophilsPercent": {
        "canonical": "BasophilsPercent",
        "displayEn": "Basophils %",
        "unit": "%",
        "category": FeatureCategory.CBC,
        "aliases": ["baso_pct", "basophils_pct"],
        "referenceRanges": [{"range": [0.5, 1.5]}]
    },
    "ANC": {
        "canonical": "ANC",
        "displayEn": "Absolute Neutrophil Count",
        "unit": "10^9/L",
        "category": FeatureCategory.CBC,
        "aliases": ["anc", "absolute_neutrophils"],
        "referenceRanges": [{"range": [1.8, 7.7]}]
    },
    "ALC": {
        "canonical": "ALC",
        "displayEn": "Absolute Lymphocyte Count",
        "unit": "10^9/L",
        "category": FeatureCategory.CBC,
        "aliases": ["alc", "absolute_lymphocytes"],
        "referenceRanges": [{"range": [1.0, 4.8]}]
    },

    "Ferritin": {
        "canonical": "Ferritin",
        "displayEn": "Ferritin",
        "unit": "ng/mL",
        "category": FeatureCategory.IRON,
        "aliases": ["ferritin"],
        "referenceRanges": [
            {"gender": "male", "range": [30, 300]},  # adjusted lower bound to match deficiency threshold
            {"gender": "female", "range": [15, 200]}  # lower bound includes iron deficiency cutoff
        ]
    },
    "SerumIron": {
        "canonical": "SerumIron",
        "displayEn": "Serum Iron",
        "unit": "µg/dL",
        "category": FeatureCategory.IRON,
        "aliases": ["iron", "serum_iron"],
        "referenceRanges": [{"range": [60, 170]}]
    },
    "TIBC": {
        "canonical": "TIBC",
        "displayEn": "TIBC",
        "unit": "µg/dL",
        "category": FeatureCategory.IRON,
        "aliases": ["tibc"],
        "referenceRanges": [{"range": [240, 450]}]
    },
    "Transferrin": {
        "canonical": "Transferrin",
        "displayEn": "Transferrin",
        "unit": "mg/dL",
        "category": FeatureCategory.IRON,
        "aliases": ["transferrin"],
        "referenceRanges": [{"range": [200, 360]}]
    },
    "Transferrin_Sat": {
        "canonical": "Transferrin_Sat",
        "displayEn": "Transferrin Saturation",
        "unit": "%",
        "category": FeatureCategory.IRON,
        "aliases": ["tsat", "transferrin_sat"],
        "derived": True,
        "referenceRanges": [{"range": [20, 50]}]
    },

    "VitaminB12": {
        "canonical": "VitaminB12",
        "displayEn": "Vitamin B12",
        "unit": "pg/mL",
        "category": FeatureCategory.VITAMIN,
        "aliases": ["b12", "vitamin_b12"],
        "referenceRanges": [{"range": [200, 900]}]
    },
    "Folate": {
        "canonical": "Folate",
        "displayEn": "Folate",
        "unit": "ng/mL",
        "category": FeatureCategory.VITAMIN,
        "aliases": ["folic_acid", "folate"],
        "referenceRanges": [{"range": [2.0, 20.0]}]  # corrected to match deficiency threshold <2.0
    },
    "Vitamin_D": {
        "canonical": "Vitamin_D",
        "displayEn": "25-OH Vitamin D",
        "unit": "ng/mL",
        "category": FeatureCategory.VITAMIN,
        "aliases": ["vit_d", "vitamin_d", "25_oh_vitamin_d"],
        "referenceRanges": [{"range": [20, 100]}]  # deficiency <20, so normal starts at 20
    },
    "TSH": {
        "canonical": "TSH",
        "displayEn": "TSH",
        "unit": "mIU/L",
        "category": FeatureCategory.THYROID,
        "aliases": ["tsh"],
        "referenceRanges": [{"range": [0.4, 4.0]}]
    },
    "FreeT4": {
        "canonical": "FreeT4",
        "displayEn": "Free T4",
        "unit": "ng/dL",
        "category": FeatureCategory.THYROID,
        "aliases": ["ft4", "free_t4"],
        "referenceRanges": [{"range": [0.8, 1.8]}]
    },
    "FreeT3": {
        "canonical": "FreeT3",
        "displayEn": "Free T3",
        "unit": "pg/mL",
        "category": FeatureCategory.THYROID,
        "aliases": ["ft3", "free_t3"],
        "referenceRanges": [{"range": [2.0, 4.4]}]
    },
    "Anti_TPO": {
        "canonical": "Anti_TPO",
        "displayEn": "Anti-TPO Antibodies",
        "unit": "IU/mL",
        "category": FeatureCategory.THYROID,
        "aliases": ["anti_tpo"],
        "referenceRanges": [{"range": [0, 34]}]
    },
    "Anti_TG": {
        "canonical": "Anti_TG",
        "displayEn": "Anti-Thyroglobulin",
        "unit": "IU/mL",
        "category": FeatureCategory.THYROID,
        "aliases": ["anti_tg", "anti_thyroglobulin"],
        "referenceRanges": [{"range": [0, 115]}]
    },
    "TRAb": {
        "canonical": "TRAb",
        "displayEn": "TRAb (TSH Receptor Ab)",
        "unit": "IU/L",
        "category": FeatureCategory.THYROID,
        "aliases": ["trab"],
        "referenceRanges": [{"range": [0, 1.75]}]
    },

    # --- DIABETES PANEL ---
    "FBS": {
        "canonical": "FBS",
        "displayEn": "Fasting Plasma Glucose (FBS)",
        "unit": "mg/dL",
        "category": FeatureCategory.BLOOD_SUGAR,
        "aliases": ["fbs", "fasting_glucose", "fpg"],
        "referenceRanges": [{"range": [70, 99]}]
    },
    "HbA1c": {
        "canonical": "HbA1c",
        "displayEn": "HbA1c",
        "unit": "%",
        "category": FeatureCategory.BLOOD_SUGAR,
        "aliases": ["hba1c", "a1c"],
        "referenceRanges": [{"range": [4.0, 5.6]}]
    },
    "OGTT_2h": {
        "canonical": "OGTT_2h",
        "displayEn": "2-hour OGTT Glucose",
        "unit": "mg/dL",
        "category": FeatureCategory.BLOOD_SUGAR,
        "aliases": ["ogtt", "ogtt_2h"],
        "referenceRanges": [{"range": [70, 139]}]
    },
    "Insulin": {
        "canonical": "Insulin",
        "displayEn": "Fasting Insulin",
        "unit": "µIU/mL",
        "category": FeatureCategory.BLOOD_SUGAR,
        "aliases": ["insulin"],
        "referenceRanges": [{"range": [2.6, 24.9]}]
    },
    "HOMA_IR": {
        "canonical": "HOMA_IR",
        "displayEn": "HOMA-IR",
        "unit": "Index",
        "category": FeatureCategory.BLOOD_SUGAR,
        "aliases": ["homa_ir"],
        "derived": True,
        "referenceRanges": [{"range": [0, 2.5]}]
    },

    "Total_Cholesterol": {
        "canonical": "Total_Cholesterol",
        "displayEn": "Total Cholesterol",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["tc", "total_cholesterol"],
        "referenceRanges": [{"range": [125, 200]}]
    },
    "LDL": {
        "canonical": "LDL",
        "displayEn": "LDL-C",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["ldl", "ldl_c"],
        "referenceRanges": [{"range": [0, 100]}]
    },
    "HDL": {
        "canonical": "HDL",
        "displayEn": "HDL-C",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["hdl", "hdl_c"],
        "referenceRanges": [
            {"gender": "male", "range": [40, 60]},
            {"gender": "female", "range": [50, 70]}
        ]
    },
    "Triglycerides": {
        "canonical": "Triglycerides",
        "displayEn": "Triglycerides",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["tg", "triglycerides"],
        "referenceRanges": [{"range": [0, 150]}]
    },
    "Non_HDL": {
        "canonical": "Non_HDL",
        "displayEn": "Non-HDL Cholesterol",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["non_hdl"],
        "derived": True,
        "referenceRanges": [{"range": [0, 130]}]
    },
    "VLDL": {
        "canonical": "VLDL",
        "displayEn": "VLDL Cholesterol",
        "unit": "mg/dL",
        "category": FeatureCategory.LIPID,
        "aliases": ["vldl"],
        "derived": True,
        "referenceRanges": [{"range": [5, 40]}]
    },
    "Creatinine": {
        "canonical": "Creatinine",
        "displayEn": "Serum Creatinine",
        "unit": "mg/dL",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["creatinine", "cr"],
        "referenceRanges": [
            {"gender": "male", "range": [0.7, 1.3]},
            {"gender": "female", "range": [0.6, 1.1]}
        ]
    },
    "eGFR": {
        "canonical": "eGFR",
        "displayEn": "eGFR",
        "unit": "mL/min/1.73m²",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["egfr", "gfr"],
        "derived": True,
        "referenceRanges": [{"range": [90, 150]}]
    },
    "BUN": {
        "canonical": "BUN",
        "displayEn": "BUN (Urea Nitrogen)",
        "unit": "mg/dL",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["bun"],
        "referenceRanges": [{"range": [7, 20]}]
    },
    "CystatinC": {
        "canonical": "CystatinC",
        "displayEn": "Cystatin C",
        "unit": "mg/L",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["cystatin_c"],
        "referenceRanges": [{"range": [0.6, 1.0]}]
    },
    "Uric_Acid": {
        "canonical": "Uric_Acid",
        "displayEn": "Uric Acid",
        "unit": "mg/dL",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["uric_acid"],
        "referenceRanges": [
            {"gender": "male", "range": [3.5, 7.2]},
            {"gender": "female", "range": [2.6, 6.0]}
        ]
    },
    "ALT": {
        "canonical": "ALT",
        "displayEn": "ALT (SGPT)",
        "unit": "U/L",
        "category": FeatureCategory.LIVER,
        "aliases": ["alt", "sgpt"],
        "referenceRanges": [
            {"gender": "male", "range": [10, 40]},
            {"gender": "female", "range": [7, 35]}
        ]
    },
    "AST": {
        "canonical": "AST",
        "displayEn": "AST (SGOT)",
        "unit": "U/L",
        "category": FeatureCategory.LIVER,
        "aliases": ["ast", "sgot"],
        "referenceRanges": [{"range": [10, 40]}]
    },
    "ALP": {
        "canonical": "ALP",
        "displayEn": "ALP (Alkaline Phosphatase)",
        "unit": "U/L",
        "category": FeatureCategory.LIVER,
        "aliases": ["alp"],
        "referenceRanges": [{"range": [44, 147]}]
    },
    "GGT": {
        "canonical": "GGT",
        "displayEn": "GGT",
        "unit": "U/L",
        "category": FeatureCategory.LIVER,
        "aliases": ["ggt"],
        "referenceRanges": [
            {"gender": "male", "range": [9, 48]},
            {"gender": "female", "range": [9, 36]}
        ]
    },
    "Total_Bilirubin": {
        "canonical": "Total_Bilirubin",
        "displayEn": "Total Bilirubin",
        "unit": "mg/dL",
        "category": FeatureCategory.LIVER,
        "aliases": ["t_bil", "total_bilirubin"],
        "referenceRanges": [{"range": [0.1, 1.2]}]
    },
    "Direct_Bilirubin": {
        "canonical": "Direct_Bilirubin",
        "displayEn": "Direct Bilirubin",
        "unit": "mg/dL",
        "category": FeatureCategory.LIVER,
        "aliases": ["d_bil", "direct_bilirubin"],
        "referenceRanges": [{"range": [0.0, 0.3]}]
    },
    "Indirect_Bilirubin": {
        "canonical": "Indirect_Bilirubin",
        "displayEn": "Indirect Bilirubin",
        "unit": "mg/dL",
        "category": FeatureCategory.LIVER,
        "aliases": ["i_bil", "indirect_bilirubin"],
        "derived": True,
        "referenceRanges": [{"range": [0.1, 0.8]}]
    },
    "Albumin": {
        "canonical": "Albumin",
        "displayEn": "Albumin",
        "unit": "g/dL",
        "category": FeatureCategory.LIVER,
        "aliases": ["albumin"],
        "referenceRanges": [{"range": [3.5, 5.0]}]
    },
    "Total_Protein": {
        "canonical": "Total_Protein",
        "displayEn": "Total Protein",
        "unit": "g/dL",
        "category": FeatureCategory.LIVER,
        "aliases": ["total_protein"],
        "referenceRanges": [{"range": [6.0, 8.3]}]
    },
    "AST_ALT_Ratio": {
        "canonical": "AST_ALT_Ratio",
        "displayEn": "AST/ALT Ratio",
        "unit": "Ratio",
        "category": FeatureCategory.LIVER,
        "aliases": ["ast_alt_ratio"],
        "derived": True
    },
    "Sodium": {
        "canonical": "Sodium",
        "displayEn": "Sodium",
        "unit": "mmol/L",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["na", "sodium"],
        "referenceRanges": [{"range": [135, 145]}]
    },
    "Potassium": {
        "canonical": "Potassium",
        "displayEn": "Potassium",
        "unit": "mmol/L",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["k", "potassium"],
        "referenceRanges": [{"range": [3.5, 5.0]}]
    },
    "Chloride": {
        "canonical": "Chloride",
        "displayEn": "Chloride",
        "unit": "mmol/L",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["cl"],
        "referenceRanges": [{"range": [98, 107]}]
    },
    "Bicarbonate": {
        "canonical": "Bicarbonate",
        "displayEn": "Bicarbonate",
        "unit": "mmol/L",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["hco3", "bicarbonate"],
        "referenceRanges": [{"range": [22, 29]}]
    },
    "Anion_Gap": {
        "canonical": "Anion_Gap",
        "displayEn": "Anion Gap",
        "unit": "mmol/L",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["anion_gap"],
        "derived": True,
        "referenceRanges": [{"range": [8, 16]}]
    },
    "Calcium": {
        "canonical": "Calcium",
        "displayEn": "Total Calcium",
        "unit": "mg/dL",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["ca", "calcium"],
        "referenceRanges": [{"range": [8.5, 10.5]}]
    },
    "IonizedCalcium": {
        "canonical": "IonizedCalcium",
        "displayEn": "Ionized Calcium",
        "unit": "mg/dL",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["ionized_ca"],
        "referenceRanges": [{"range": [4.5, 5.6]}]
    },
    "Phosphate": {
        "canonical": "Phosphate",
        "displayEn": "Inorganic Phosphate",
        "unit": "mg/dL",
        "category": FeatureCategory.KIDNEY,
        "aliases": ["phosphate", "phos", "phosphorus"],
        "referenceRanges": [{"range": [2.5, 4.5]}]
    },
    "Magnesium": {
        "canonical": "Magnesium",
        "displayEn": "Magnesium",
        "unit": "mg/dL",
        "category": FeatureCategory.ELECTROLYTE,
        "aliases": ["mg", "magnesium"],
        "referenceRanges": [{"range": [1.7, 2.2]}]
    },
    "PTH": {
        "canonical": "PTH",
        "displayEn": "Parathyroid Hormone (PTH)",
        "unit": "pg/mL",
        "category": FeatureCategory.HORMONES,
        "aliases": ["pth"],
        "referenceRanges": [{"range": [15, 65]}]
    },
    "Troponin": {
        "canonical": "Troponin",
        "displayEn": "Cardiac Troponin I",
        "unit": "ng/mL",
        "category": FeatureCategory.CARDIAC,
        "aliases": ["troponin", "c_tn", "troponin_i"],
        "referenceRanges": [{"range": [0.0, 0.04]}]
    },
    "CK_MB": {
        "canonical": "CK_MB",
        "displayEn": "CK-MB",
        "unit": "ng/mL",
        "category": FeatureCategory.CARDIAC,
        "aliases": ["ckmb", "ck_mb"],
        "referenceRanges": [{"range": [0, 5.0]}]
    },
    "BNP": {
        "canonical": "BNP",
        "displayEn": "BNP",
        "unit": "pg/mL",
        "category": FeatureCategory.CARDIAC,
        "aliases": ["bnp"],
        "referenceRanges": [{"range": [0, 100]}]
    },
    "NT_proBNP": {
        "canonical": "NT_proBNP",
        "displayEn": "NT-proBNP",
        "unit": "pg/mL",
        "category": FeatureCategory.CARDIAC,
        "aliases": ["nt_pro_bnp"],
        "referenceRanges": [{"range": [0, 125]}]
    },
    "CK": {                              # NEW
        "canonical": "CK",
        "displayEn": "Creatine Kinase (Total CK)",
        "unit": "U/L",
        "category": FeatureCategory.MUSCLE,
        "aliases": ["ck", "creatine_kinase"],
        "referenceRanges": [
            {"gender": "male", "range": [38, 174]},
            {"gender": "female", "range": [26, 140]}
        ]
    },
    "PT": {
        "canonical": "PT",
        "displayEn": "Prothrombin Time (PT)",
        "unit": "seconds",
        "category": FeatureCategory.COAGULATION,
        "aliases": ["pt"],
        "referenceRanges": [{"range": [11.0, 13.5]}]
    },
    "INR": {
        "canonical": "INR",
        "displayEn": "INR",
        "unit": "Ratio",
        "category": FeatureCategory.COAGULATION,
        "aliases": ["inr"],
        "referenceRanges": [{"range": [0.8, 1.2]}]
    },
    "aPTT": {
        "canonical": "aPTT",
        "displayEn": "aPTT",
        "unit": "seconds",
        "category": FeatureCategory.COAGULATION,
        "aliases": ["aptt"],
        "referenceRanges": [{"range": [25, 35]}]
    },
    "Fibrinogen": {
        "canonical": "Fibrinogen",
        "displayEn": "Fibrinogen",
        "unit": "mg/dL",
        "category": FeatureCategory.COAGULATION,
        "aliases": ["fibrinogen"],
        "referenceRanges": [{"range": [200, 400]}]
    },
    "D_Dimer": {
        "canonical": "D_Dimer",
        "displayEn": "D-Dimer",
        "unit": "µg/mL",
        "category": FeatureCategory.COAGULATION,
        "aliases": ["d_dimer"],
        "referenceRanges": [{"range": [0.0, 0.5]}]
    },

    # --- INFLAMMATORY PANEL ---
    "CRP": {
        "canonical": "CRP",
        "displayEn": "C-Reactive Protein (CRP)",
        "unit": "mg/L",
        "category": FeatureCategory.INFLAMMATORY,
        "aliases": ["crp", "hs_crp"],
        "referenceRanges": [{"range": [0, 5.0]}]
    },
    "ESR": {
        "canonical": "ESR",
        "displayEn": "ESR (Sed Rate)",
        "unit": "mm/hr",
        "category": FeatureCategory.INFLAMMATORY,
        "aliases": ["esr"],
        "referenceRanges": [
            {"gender": "male", "range": [0, 15]},
            {"gender": "female", "range": [0, 20]}
        ]
    },
    "Procalcitonin": {
        "canonical": "Procalcitonin",
        "displayEn": "Procalcitonin",
        "unit": "ng/mL",
        "category": FeatureCategory.INFLAMMATORY,
        "aliases": ["procalcitonin", "pct"],
        "referenceRanges": [{"range": [0, 0.05]}]
    },
    "LDH": {
        "canonical": "LDH",
        "displayEn": "Lactate Dehydrogenase",
        "unit": "U/L",
        "category": FeatureCategory.HEMOLYSIS,
        "aliases": ["ldh"],
        "referenceRanges": [{"range": [140, 280]}]
    },
    "Haptoglobin": {
        "canonical": "Haptoglobin",
        "displayEn": "Haptoglobin",
        "unit": "mg/dL",
        "category": FeatureCategory.HEMOLYSIS,
        "aliases": ["haptoglobin"],
        "referenceRanges": [{"range": [30, 200]}]
    },
    "ANA": {
        "canonical": "ANA",
        "displayEn": "ANA (Antinuclear Antibodies)",
        "unit": "Titer / Index",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["ana"],
        "referenceRanges": [{"range": [0, 1]}]
    },
    "Anti_dsDNA": {
        "canonical": "Anti_dsDNA",
        "displayEn": "Anti-dsDNA",
        "unit": "IU/mL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["ds_dna", "anti_dsdna"],
        "referenceRanges": [{"range": [0, 30]}]
    },
    "C3": {
        "canonical": "C3",
        "displayEn": "C3 Complement",
        "unit": "mg/dL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["c3"],
        "referenceRanges": [{"range": [80, 160]}]
    },
    "C4": {
        "canonical": "C4",
        "displayEn": "C4 Complement",
        "unit": "mg/dL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["c4"],
        "referenceRanges": [{"range": [16, 47]}]
    },
    "ENA_Panel": {
        "canonical": "ENA_Panel",
        "displayEn": "ENA Panel",
        "unit": "Qualitative",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["ena"]
    },
    "DAT": {                              # NEW
        "canonical": "DAT",
        "displayEn": "Direct Antiglobulin Test (Coombs)",
        "unit": "Qualitative",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["dat", "coombs", "direct_coombs"],
        "referenceRanges": []  # Qualitative: Positive/Negative
    },
    "Lupus_Anticoagulant": {             # NEW
        "canonical": "Lupus_Anticoagulant",
        "displayEn": "Lupus Anticoagulant",
        "unit": "Qualitative",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["lac", "lupus_anticoagulant"]
    },
    "Anti_Cardiolipin": {                # NEW
        "canonical": "Anti_Cardiolipin",
        "displayEn": "Anti-Cardiolipin Antibody",
        "unit": "GPL/MPL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["aca", "anti_cardiolipin"],
        "referenceRanges": [{"range": [0, 20]}]  # cut-off varies, set low normal
    },
    "Anti_Beta2GP1": {                   # NEW
        "canonical": "Anti_Beta2GP1",
        "displayEn": "Anti-β2-Glycoprotein I",
        "unit": "U/mL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["b2gp1", "anti_b2gp1"],
        "referenceRanges": [{"range": [0, 20]}]
    },
    "ANCA": {                             # NEW
        "canonical": "ANCA",
        "displayEn": "ANCA (Antineutrophil Cytoplasmic Ab)",
        "unit": "Qualitative/Pattern",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["anca"]
    },
    "PR3": {                              # NEW
        "canonical": "PR3",
        "displayEn": "Anti-PR3 Antibody",
        "unit": "U/mL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["pr3"],
        "referenceRanges": [{"range": [0, 3.5]}]
    },
    "MPO": {                              # NEW
        "canonical": "MPO",
        "displayEn": "Anti-MPO Antibody",
        "unit": "U/mL",
        "category": FeatureCategory.AUTOIMMUNE,
        "aliases": ["mpo"],
        "referenceRanges": [{"range": [0, 3.5]}]
    },
    "RF": {
        "canonical": "RF",
        "displayEn": "Rheumatoid Factor (RF)",
        "unit": "IU/mL",
        "category": FeatureCategory.RHEUMATOLOGY,
        "aliases": ["rf"],
        "referenceRanges": [{"range": [0, 15]}]
    },
    "Anti_CCP": {
        "canonical": "Anti_CCP",
        "displayEn": "Anti-CCP Antibodies",
        "unit": "U/mL",
        "category": FeatureCategory.RHEUMATOLOGY,
        "aliases": ["anti_ccp", "ccp"],
        "referenceRanges": [{"range": [0, 20]}]
    },

    # --- HEPATITIS PANEL ---
    "HBsAg": {
        "canonical": "HBsAg",
        "displayEn": "HBsAg",
        "unit": "Index / Qual",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["hbsag"]
    },
    "Anti_HBs": {
        "canonical": "Anti_HBs",
        "displayEn": "Anti-HBs",
        "unit": "mIU/mL",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["anti_hbs"],
        "referenceRanges": [{"range": [10, 1000]}]
    },
    "Anti_HBc": {
        "canonical": "Anti_HBc",
        "displayEn": "Anti-HBc",
        "unit": "Qualitative",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["anti_hbc"]
    },
    "HBeAg": {
        "canonical": "HBeAg",
        "displayEn": "HBeAg",
        "unit": "Qualitative",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["hbeag"]
    },
    "Anti_HBe": {
        "canonical": "Anti_HBe",
        "displayEn": "Anti-HBe",
        "unit": "Qualitative",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["anti_hbe"]
    },
    "Anti_HCV": {
        "canonical": "Anti_HCV",
        "displayEn": "Anti-HCV",
        "unit": "Qualitative",
        "category": FeatureCategory.HEPATITIS,
        "aliases": ["anti_hcv"]
    },
    "HIV_AgAb": {                        # NEW
        "canonical": "HIV_AgAb",
        "displayEn": "HIV-1/2 Antigen/Antibody Test",
        "unit": "Qualitative",
        "category": FeatureCategory.INFECTIOUS,
        "aliases": ["hiv", "hiv_test"]
    },
    "RPR": {                              # NEW
        "canonical": "RPR",
        "displayEn": "RPR (Rapid Plasma Reagin)",
        "unit": "Qualitative/Titer",
        "category": FeatureCategory.INFECTIOUS,
        "aliases": ["rpr"]
    },
    "TPPA": {                             # NEW
        "canonical": "TPPA",
        "displayEn": "TPPA (Treponema Pallidum Particle Agglutination)",
        "unit": "Qualitative",
        "category": FeatureCategory.INFECTIOUS,
        "aliases": ["tppa"]
    },
    "G6PD_Activity": {                   # NEW
        "canonical": "G6PD_Activity",
        "displayEn": "G6PD Enzyme Activity",
        "unit": "% of normal",
        "category": FeatureCategory.CBC,   # or separate enzyme panel
        "aliases": ["g6pd"],
        "referenceRanges": [{"range": [60, 150]}]  # normal >60%
    },
    "Cortisol": {
        "canonical": "Cortisol",
        "displayEn": "Serum Cortisol (Morning)",
        "unit": "µg/dL",
        "category": FeatureCategory.ENDOCRINE,
        "aliases": ["cortisol"],
        "referenceRanges": [{"range": [5, 25]}]
    },
    "ACTH": {
        "canonical": "ACTH",
        "displayEn": "ACTH",
        "unit": "pg/mL",
        "category": FeatureCategory.ENDOCRINE,
        "aliases": ["acth"],
        "referenceRanges": [{"range": [10, 60]}]
    },
    "Prolactin": {
        "canonical": "Prolactin",
        "displayEn": "Prolactin",
        "unit": "ng/mL",
        "category": FeatureCategory.ENDOCRINE,
        "aliases": ["prolactin"],
        "referenceRanges": [
            {"gender": "male", "range": [2, 18]},
            {"gender": "female", "range": [2, 29]}
        ]
    },
    "IGF1": {
        "canonical": "IGF1",
        "displayEn": "IGF-1",
        "unit": "ng/mL",
        "category": FeatureCategory.ENDOCRINE,
        "aliases": ["igf_1", "igf1"],
        "referenceRanges": [{"range": [100, 400]}]
    },
    "LH": {
        "canonical": "LH",
        "displayEn": "Luteinizing Hormone (LH)",
        "unit": "IU/L",
        "category": FeatureCategory.REPRODUCTIVE,
        "aliases": ["lh"],
        "referenceRanges": [{"range": [1.5, 12.6]}]
    },
    "FSH": {
        "canonical": "FSH",
        "displayEn": "Follicle-Stimulating Hormone",
        "unit": "IU/L",
        "category": FeatureCategory.REPRODUCTIVE,
        "aliases": ["fsh"],
        "referenceRanges": [{"range": [1.5, 12.5]}]
    },
    "Estradiol": {
        "canonical": "Estradiol",
        "displayEn": "Estradiol",
        "unit": "pg/mL",
        "category": FeatureCategory.REPRODUCTIVE,
        "aliases": ["estradiol", "e2"],
        "referenceRanges": [
            {"gender": "female", "range": [30, 400]},
            {"gender": "male", "range": [10, 50]}
        ]
    },
    "Progesterone": {
        "canonical": "Progesterone",
        "displayEn": "Progesterone",
        "unit": "ng/mL",
        "category": FeatureCategory.REPRODUCTIVE,
        "aliases": ["progesterone"],
        "referenceRanges": [{"gender": "female", "range": [0.1, 20.0]}]
    },
    "Testosterone": {
        "canonical": "Testosterone",
        "displayEn": "Total Testosterone",
        "unit": "ng/dL",
        "category": FeatureCategory.REPRODUCTIVE,
        "aliases": ["testosterone", "testo"],
        "referenceRanges": [
            {"gender": "male", "range": [300, 1000]},
            {"gender": "female", "range": [15, 70]}
        ]
    },
    "AFP": {
        "canonical": "AFP",
        "displayEn": "Alpha-Fetoprotein (AFP)",
        "unit": "ng/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["afp"],
        "referenceRanges": [{"range": [0, 8.5]}]
    },
    "CEA": {
        "canonical": "CEA",
        "displayEn": "Carcinoembryonic Antigen (CEA)",
        "unit": "ng/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["cea"],
        "referenceRanges": [{"range": [0, 5.0]}]
    },
    "CA19_9": {
        "canonical": "CA19_9",
        "displayEn": "CA 19-9",
        "unit": "U/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["ca_19_9", "ca199"],
        "referenceRanges": [{"range": [0, 37]}]
    },
    "CA125": {
        "canonical": "CA125",
        "displayEn": "CA-125",
        "unit": "U/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["ca_125", "ca125"],
        "referenceRanges": [{"range": [0, 35]}]
    },
    "PSA": {
        "canonical": "PSA",
        "displayEn": "PSA (Prostate-Specific Ag)",
        "unit": "ng/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["psa"],
        "referenceRanges": [{"gender": "male", "range": [0, 4.0]}]
    },
    "Beta_hCG": {
        "canonical": "Beta_hCG",
        "displayEn": "Beta-hCG",
        "unit": "mIU/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["bhcg", "beta_hcg", "hcg"],
        "referenceRanges": [{"range": [0, 5.0]}]
    },
    "Chromogranin_A": {                  # NEW
        "canonical": "Chromogranin_A",
        "displayEn": "Chromogranin A",
        "unit": "ng/mL",
        "category": FeatureCategory.TUMOR_MARKER,
        "aliases": ["cga", "chromogranin"],
        "referenceRanges": [{"range": [0, 100]}]
    },
    "Lipase": {
        "canonical": "Lipase",
        "displayEn": "Lipase",
        "unit": "U/L",
        "category": FeatureCategory.PANCREATIC,
        "aliases": ["lipase"],
        "referenceRanges": [{"range": [10, 140]}]
    },
    "Amylase": {
        "canonical": "Amylase",
        "displayEn": "Amylase",
        "unit": "U/L",
        "category": FeatureCategory.PANCREATIC,
        "aliases": ["amylase"],
        "referenceRanges": [{"range": [30, 110]}]
    },

    # --- ACID-BASE PANEL ---
    "pH": {
        "canonical": "pH",
        "displayEn": "Blood pH",
        "unit": "Index",
        "category": FeatureCategory.ACID_BASE,
        "aliases": ["ph"],
        "referenceRanges": [{"range": [7.35, 7.45]}]
    },
    "PaCO2": {
        "canonical": "PaCO2",
        "displayEn": "PaCO2",
        "unit": "mmHg",
        "category": FeatureCategory.ACID_BASE,
        "aliases": ["paco2"],
        "referenceRanges": [{"range": [35, 45]}]
    },
    "HCO3": {
        "canonical": "HCO3",
        "displayEn": "HCO3- (Bicarbonate)",
        "unit": "mmol/L",
        "category": FeatureCategory.ACID_BASE,
        "aliases": ["hco3_art"],
        "referenceRanges": [{"range": [22, 26]}]
    },
    "PaO2": {
        "canonical": "PaO2",
        "displayEn": "PaO2",
        "unit": "mmHg",
        "category": FeatureCategory.ACID_BASE,
        "aliases": ["pao2"],
        "referenceRanges": [{"range": [80, 100]}]
    },
    "Lactate": {
        "canonical": "Lactate",
        "displayEn": "Lactate",
        "unit": "mmol/L",
        "category": FeatureCategory.ACID_BASE,
        "aliases": ["lactate"],
        "referenceRanges": [{"range": [0.5, 2.2]}]
    },
    "UrineSpecificGravity": {
        "canonical": "UrineSpecificGravity",
        "displayEn": "Specific Gravity",
        "unit": "Index",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["sg", "urine_sg"],
        "referenceRanges": [{"range": [1.005, 1.030]}]
    },
    "UrinepH": {
        "canonical": "UrinepH",
        "displayEn": "Urine pH",
        "unit": "Index",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["urine_ph"],
        "referenceRanges": [{"range": [5.0, 8.0]}]
    },
    "UrineProteinQualitative": {
        "canonical": "UrineProteinQualitative",
        "displayEn": "Urine Protein (Qualitative)",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_prot", "urine_protein"]
    },
    "UrineGlucoseQualitative": {
        "canonical": "UrineGlucoseQualitative",
        "displayEn": "Urine Glucose (Qualitative)",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_gluc", "urine_glucose"]
    },
    "UrineKetones": {
        "canonical": "UrineKetones",
        "displayEn": "Urine Ketones",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_ket", "urine_ketones"]
    },
    "UrineBlood": {
        "canonical": "UrineBlood",
        "displayEn": "Urine Blood / Hemoglobin",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_bld", "urine_blood"]
    },
    "UrineNitrite": {
        "canonical": "UrineNitrite",
        "displayEn": "Urine Nitrite",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_nit", "urine_nitrite"]
    },
    "UrineLeukocyteEsterase": {
        "canonical": "UrineLeukocyteEsterase",
        "displayEn": "Leukocyte Esterase",
        "unit": "Qualitative",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_le", "urine_le"]
    },
    "UrineWBC": {
        "canonical": "UrineWBC",
        "displayEn": "Urine WBC / hpf",
        "unit": "/hpf",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_wbc"],
        "referenceRanges": [{"range": [0, 5]}]
    },
    "UrineRBC": {
        "canonical": "UrineRBC",
        "displayEn": "Urine RBC / hpf",
        "unit": "/hpf",
        "category": FeatureCategory.URINALYSIS,
        "aliases": ["u_rbc"],
        "referenceRanges": [{"range": [0, 3]}]
    },
    "UrineAlbumin": {
        "canonical": "UrineAlbumin",
        "displayEn": "Urine Albumin (Microalbumin)",
        "unit": "mg/L",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["u_alb"],
        "referenceRanges": [{"range": [0, 20]}]
    },
    "UrineCreatinine": {
        "canonical": "UrineCreatinine",
        "displayEn": "Urine Creatinine",
        "unit": "mg/dL",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["u_cr"]
    },
    "ACR": {
        "canonical": "ACR",
        "displayEn": "ACR (Albumin-to-Creatinine Ratio)",
        "unit": "mg/g",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["acr", "uacr"],
        "derived": True,
        "referenceRanges": [{"range": [0, 30]}]
    },
    "PCR": {
        "canonical": "PCR",
        "displayEn": "PCR (Protein-to-Creatinine Ratio)",
        "unit": "mg/g",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["pcr"],
        "derived": True,
        "referenceRanges": [{"range": [0, 150]}]
    },
    "UrineProtein24h": {
        "canonical": "UrineProtein24h",
        "displayEn": "24-Hour Urine Protein",
        "unit": "mg/24h",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["protein_24h"],
        "referenceRanges": [{"range": [0, 150]}]
    },
    "UrineProteinQuantitative": {        # NEW (optional for calculators)
        "canonical": "UrineProteinQuantitative",
        "displayEn": "Urine Protein (Quantitative)",
        "unit": "mg/L",
        "category": FeatureCategory.URINE_PROTEIN,
        "aliases": ["u_prot_quant", "urine_protein_quant"]
    },
    "Prealbumin": {
        "canonical": "Prealbumin",
        "displayEn": "Prealbumin",
        "unit": "mg/dL",
        "category": FeatureCategory.NUTRITION,
        "aliases": ["prealbumin"],
        "referenceRanges": [{"range": [15, 36]}]
    },
    "Zinc": {
        "canonical": "Zinc",
        "displayEn": "Zinc Level",
        "unit": "µg/dL",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["zinc"],
        "referenceRanges": [{"range": [60, 120]}]
    },
    "Selenium": {
        "canonical": "Selenium",
        "displayEn": "Selenium",
        "unit": "µg/L",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["selenium"],
        "referenceRanges": [{"range": [70, 150]}]
    },
    "Iodine": {
        "canonical": "Iodine",
        "displayEn": "Iodine Level",
        "unit": "µg/L",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["iodine"],
        "referenceRanges": [{"range": [40, 92]}]
    },
    "VitaminA": {
        "canonical": "VitaminA",
        "displayEn": "Vitamin A (Retinol)",
        "unit": "µg/dL",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["vit_a"],
        "referenceRanges": [{"range": [30, 80]}]
    },
    "VitaminE": {
        "canonical": "VitaminE",
        "displayEn": "Vitamin E (Tocopherol)",
        "unit": "mg/dL",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["vit_e"],
        "referenceRanges": [{"range": [0.5, 1.8]}]
    },
    "VitaminC": {
        "canonical": "VitaminC",
        "displayEn": "Vitamin C",
        "unit": "mg/dL",
        "category": FeatureCategory.MICRONUTRIENT,
        "aliases": ["vit_c"],
        "referenceRanges": [{"range": [0.4, 1.5]}]
    }
}

PANEL_FEATURES_MAP = {
    "CBC": ["WBC", "RBC", "Hb", "Hct", "MCV", "MCH", "MCHC", "RDW", "Platelet", "NeutrophilsPercent", "LymphocytesPercent", "MonocytesPercent", "EosinophilsPercent", "BasophilsPercent", "ANC", "ALC"],
    "Iron_Studies": ["Ferritin", "SerumIron", "TIBC", "Transferrin", "Transferrin_Sat"],
    "Vitamin_Panel": ["VitaminB12", "Folate", "Vitamin_D"],
    "Thyroid_Panel": ["TSH", "FreeT4", "FreeT3", "Anti_TPO", "Anti_TG", "TRAb"],
    "Diabetes_Panel": ["FBS", "HbA1c", "OGTT_2h", "Insulin", "HOMA_IR"],
    "Lipid_Panel": ["Total_Cholesterol", "LDL", "HDL", "Triglycerides", "Non_HDL", "VLDL"],
    "Renal_Function_Panel": ["Creatinine", "eGFR", "BUN", "CystatinC", "Uric_Acid"],
    "Liver_Function_Panel": ["ALT", "AST", "ALP", "GGT", "Total_Bilirubin", "Direct_Bilirubin", "Indirect_Bilirubin", "Albumin", "Total_Protein", "AST_ALT_Ratio"],
    "Electrolyte_Panel": ["Sodium", "Potassium", "Chloride", "Bicarbonate", "Anion_Gap"],
    "Bone & Mineral Panel": ["Calcium", "IonizedCalcium", "Phosphate", "Magnesium", "PTH"],
    "Cardiac_Biomarkers": ["Troponin", "CK_MB", "BNP", "NT_proBNP", "CK"],
    "Coagulation_Panel": ["PT", "INR", "aPTT", "Fibrinogen", "D_Dimer"],
    "Inflammatory_Panel": ["CRP", "ESR", "Procalcitonin", "Ferritin"],
    "Autoimmune_Panel": ["ANA", "Anti_dsDNA", "C3", "C4", "ENA_Panel", "DAT", "Lupus_Anticoagulant", "Anti_Cardiolipin", "Anti_Beta2GP1", "ANCA", "PR3", "MPO"],
    "Rheumatology_Panel": ["RF", "Anti_CCP", "ANA", "ESR", "CRP", "Uric_Acid"],
    "Hepatitis_Panel": ["HBsAg", "Anti_HBs", "Anti_HBc", "HBeAg", "Anti_HBe", "Anti_HCV"],
    "Endocrine_Panel": ["Cortisol", "ACTH", "Prolactin", "IGF1", "LH", "FSH"],
    "Reproductive_Hormone_Panel": ["LH", "FSH", "Estradiol", "Progesterone", "Testosterone", "Prolactin"],
    "Tumor_Marker_Panel": ["AFP", "CEA", "CA19_9", "CA125", "PSA", "Beta_hCG", "Chromogranin_A"],
    "Pancreatic_Panel": ["Lipase", "Amylase", "FBS", "Triglycerides"],
    "Acid_Base_Panel": ["pH", "PaCO2", "HCO3", "PaO2", "Lactate"],
    "Urinalysis_Panel": ["UrineSpecificGravity", "UrinepH", "UrineProteinQualitative", "UrineGlucoseQualitative", "UrineKetones", "UrineBlood", "UrineNitrite", "UrineLeukocyteEsterase", "UrineWBC", "UrineRBC"],
    "Urine_Protein_Panel": ["UrineAlbumin", "UrineCreatinine", "ACR", "PCR", "UrineProtein24h", "UrineProteinQuantitative"],
    "Nutrition_Malnutrition_Panel": ["Albumin", "Prealbumin", "Total_Protein", "Ferritin", "VitaminB12", "Folate", "Vitamin_D", "Zinc", "Magnesium"],
    "Hemolysis_Panel": ["LDH", "Haptoglobin", "Indirect_Bilirubin"],
    "Infectious_Serology": ["HIV_AgAb", "RPR", "TPPA"],
    "Muscle_Panel": ["CK"]
}
