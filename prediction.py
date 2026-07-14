# prediction.py

import math

def predict_2year_risks(inputs: dict, derived: dict, patient: dict, diagnoses: list) -> list:
    dataset = {**inputs, **derived}
    gender = "male" if patient.get("Sex") == 1 or patient.get("Sex") == "Male" else "female"
    results = []

    # Helper to check if a disease is already diagnosed as Present
    def has_diagnosis(key: str) -> bool:
        # key can be "Diabetes_Mellitus", "Prediabetes", "Cardiovascular_Risk", etc.
        # We map these keys to the actual diagnosed disease names or keys from interpretation.py:
        key_mappings = {
            "Diabetes_Mellitus": ["Type_2_diabetes_mellitus", "Type_1_diabetes_mellitus", "Gestational_diabetes"],
            "Prediabetes": ["Prediabetes"],
            "Cardiovascular_Risk": ["Acute_myocardial_infarction", "Non_ST_elevation_myocardial_infarction", "Heart_failure", "Acute_decompensated_heart_failure", "Myocardial_injury", "Myocarditis", "Coronary_artery_disease", "Coronary_Artery_Disease", "CAD"],
            "Chronic_Kidney_Disease": ["Chronic_kidney_disease", "Diabetic_kidney_disease", "Hypertensive_nephropathy", "Glomerulonephritis", "Nephrotic_syndrome", "Nephritic_syndrome", "IgA_nephropathy", "Lupus_nephritis", "Minimal_change_disease", "Focal_segmental_glomerulosclerosis", "Membranous_nephropathy", "Acute_tubular_necrosis", "Interstitial_nephritis", "Polycystic_kidney_disease", "Albuminuria", "Proteinuria", "Nephrotic_range_proteinuria", "Uremia", "End_stage_kidney_disease"],
            "Acute_Kidney_Injury": ["Acute_kidney_injury", "Acute_tubular_necrosis"],
            "NAFLD": ["Nonalcoholic_fatty_liver_disease", "Metabolic_dysfunction_associated_steatotic_liver_disease", "Nonalcoholic_steatohepatitis", "Cirrhosis"],
            "NASH": ["Nonalcoholic_steatohepatitis", "NASH", "Cirrhosis"],
            "Metabolic_Syndrome": ["Metabolic_syndrome", "Obesity"],
            "Iron_Deficiency_Anemia": ["Iron_deficiency_anemia"],
            "Primary_Hypothyroidism": ["Primary_hypothyroidism", "Subclinical_hypothyroidism", "Secondary_hypothyroidism", "Hashimoto_thyroiditis"],
            "Gout": ["Gout", "Hyperuricemia"]
        }
        
        target_keys = key_mappings.get(key, [key])
        
        for d in diagnoses:
            d_key = d.get("diseaseKey", "")
            d_name = d.get("nameEn", "")
            if d.get("status") == "Present":
                if d_key in target_keys or any(tk.lower() in d_key.lower() for tk in target_keys) or any(tk.replace("_", " ").lower() in d_name.lower() for tk in target_keys):
                    return True
        return False

    # Define strict required features for each prediction model
    PREDICTION_REQUIREMENTS = {
        "Diabetes_Mellitus": ["FBS", "BMI", "FamilyHistory_DM"],
        "Prediabetes": ["FBS", "BMI", "PhysicalActivity"],
        "Cardiovascular_Risk": ["Systolic_BP", "Smoking", "LDL", "FamilyHistory_CAD"],
        "Chronic_Kidney_Disease": ["eGFR", "ACR", "FBS", "Systolic_BP"],
        "Acute_Kidney_Injury": ["Creatinine", "BUN", "Systolic_BP"],
        "NAFLD": ["ALT", "AST", "BMI", "Triglycerides"],
        "NASH": ["ALT", "AST", "CRP", "BMI"],
        "Metabolic_Syndrome": ["Waist", "BMI", "Triglycerides", "FBS"],
        "Iron_Deficiency_Anemia": ["Ferritin", "Hb", "SerumIron"],
        "Primary_Hypothyroidism": ["TSH", "Anti_TPO"],
        "Gout": ["Uric_Acid", "Creatinine"]
    }

    # 1. Diabetes Risk Model
    reqs = PREDICTION_REQUIREMENTS["Diabetes_Mellitus"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)
    
    if has_diagnosis("Diabetes_Mellitus"):
        results.append({
            "diseaseKey": "Diabetes_Mellitus",
            "nameEn": "Type 2 Diabetes Mellitus",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Diabetes_Mellitus",
            "nameEn": "Type 2 Diabetes Mellitus",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        fbs = dataset["FBS"]
        bmi = dataset["BMI"]
        age = patient.get("Age", 35)
        fh = 1.5 if patient.get("FamilyHistory_DM") == 1 else 0.0

        score = (fbs - 70.0) * 0.15 + (bmi - 20.0) * 0.2 + (age - 30.0) * 0.05 + fh
        prob = min(max(1.0 / (1.0 + math.exp(-(-2.5 + score * 0.45))), 0.01), 0.99)
        
        risk = "Low"
        if prob > 0.6: risk = "Very High"
        elif prob > 0.3: risk = "High"
        elif prob > 0.15: risk = "Moderate"

        results.append({
            "diseaseKey": "Diabetes_Mellitus",
            "nameEn": "Type 2 Diabetes Mellitus",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 2. Prediabetes Risk Model
    reqs = PREDICTION_REQUIREMENTS["Prediabetes"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Diabetes_Mellitus") or has_diagnosis("Prediabetes"):
        results.append({
            "diseaseKey": "Prediabetes",
            "nameEn": "Prediabetes Progression",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Prediabetes",
            "nameEn": "Prediabetes Progression",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        fbs = dataset["FBS"]
        bmi = dataset["BMI"]
        act = patient.get("PhysicalActivity", 1)  # 0 to 3

        score = (fbs - 70.0) * 0.25 + (bmi - 20.0) * 0.15 + (3.0 - act) * 0.5
        prob = min(max(1.0 / (1.0 + math.exp(-(-2.0 + score * 0.45))), 0.01), 0.99)
        
        risk = "Low"
        if prob > 0.5: risk = "Very High"
        elif prob > 0.25: risk = "High"
        elif prob > 0.12: risk = "Moderate"

        results.append({
            "diseaseKey": "Prediabetes",
            "nameEn": "Prediabetes Progression",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 3. Cardiovascular Risk Model
    reqs = PREDICTION_REQUIREMENTS["Cardiovascular_Risk"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Cardiovascular_Risk"):
        results.append({
            "diseaseKey": "Cardiovascular_Risk",
            "nameEn": "Coronary Artery Disease & Cardiac Events",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Cardiovascular_Risk",
            "nameEn": "Coronary Artery Disease & Cardiac Events",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        sbp = dataset["Systolic_BP"]
        smk = 1.5 if patient.get("Smoking") == 1 else 0.0
        ldl = dataset["LDL"]
        age = patient.get("Age", 35)
        fh_cad = 1.2 if patient.get("FamilyHistory_CAD") == 1 else 0.0

        score = (sbp - 110.0) * 0.05 + smk + (ldl - 90.0) * 0.03 + (age - 35.0) * 0.08 + fh_cad
        prob = min(max(1.0 / (1.0 + math.exp(-(-3.5 + score * 0.5))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.3: risk = "Very High"
        elif prob > 0.15: risk = "High"
        elif prob > 0.07: risk = "Moderate"

        results.append({
            "diseaseKey": "Cardiovascular_Risk",
            "nameEn": "Coronary Artery Disease & Cardiac Events",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 4. Chronic Kidney Disease Risk Model
    reqs = PREDICTION_REQUIREMENTS["Chronic_Kidney_Disease"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Chronic_Kidney_Disease"):
        results.append({
            "diseaseKey": "Chronic_Kidney_Disease",
            "nameEn": "CKD Progression Risk",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Chronic_Kidney_Disease",
            "nameEn": "CKD Progression Risk",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        egfr = dataset["eGFR"]
        acr = dataset["ACR"]
        dm = 1.0 if dataset.get("FBS", 85) > 110 else 0.0
        htn = 1.0 if dataset.get("Systolic_BP", 120) > 130 else 0.0

        score = (90.0 - egfr) * 0.1 + (1.5 if acr > 30.0 else 0.0) + dm * 0.8 + htn * 0.6
        prob = min(max(1.0 / (1.0 + math.exp(-(-3.0 + score * 0.6))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.35: risk = "Very High"
        elif prob > 0.18: risk = "High"
        elif prob > 0.08: risk = "Moderate"

        results.append({
            "diseaseKey": "Chronic_Kidney_Disease",
            "nameEn": "CKD Progression Risk",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 5. Acute Kidney Injury Risk Model
    reqs = PREDICTION_REQUIREMENTS["Acute_Kidney_Injury"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Acute_Kidney_Injury"):
        results.append({
            "diseaseKey": "Acute_Kidney_Injury",
            "nameEn": "Acute Kidney Injury Risk",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Acute_Kidney_Injury",
            "nameEn": "Acute Kidney Injury Risk",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        cr = dataset["Creatinine"]
        bun = dataset["BUN"]
        sbp = dataset["Systolic_BP"]

        score = (cr - 0.7) * 0.8 + (bun - 10.0) * 0.05 + (1.2 if sbp < 90.0 else 0.0) + (0.6 if sbp > 160.0 else 0.0)
        prob = min(max(1.0 / (1.0 + math.exp(-(-4.0 + score * 0.75))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.25: risk = "Very High"
        elif prob > 0.12: risk = "High"
        elif prob > 0.05: risk = "Moderate"

        results.append({
            "diseaseKey": "Acute_Kidney_Injury",
            "nameEn": "Acute Kidney Injury Risk",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 6. NAFLD Fatty Liver Risk Model
    reqs = PREDICTION_REQUIREMENTS["NAFLD"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("NAFLD"):
        results.append({
            "diseaseKey": "NAFLD",
            "nameEn": "NAFLD Development Risk",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "NAFLD",
            "nameEn": "NAFLD Development Risk",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        alt = dataset["ALT"]
        ast = dataset["AST"]
        bmi = dataset["BMI"]
        tg = dataset["Triglycerides"]

        score = (alt - 15.0) * 0.05 + (ast - 15.0) * 0.03 + (bmi - 22.0) * 0.15 + (tg - 100.0) * 0.005
        prob = min(max(1.0 / (1.0 + math.exp(-(-2.8 + score * 0.5))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.45: risk = "Very High"
        elif prob > 0.22: risk = "High"
        elif prob > 0.1: risk = "Moderate"

        results.append({
            "diseaseKey": "NAFLD",
            "nameEn": "NAFLD Development Risk",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 7. NASH Progress Risk Model
    reqs = PREDICTION_REQUIREMENTS["NASH"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("NASH"):
        results.append({
            "diseaseKey": "NASH",
            "nameEn": "NASH Progression Risk",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "NASH",
            "nameEn": "NASH Progression Risk",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        alt = dataset["ALT"]
        ast = dataset["AST"]
        crp = dataset["CRP"]
        bmi = dataset["BMI"]

        score = (alt - 30.0) * 0.04 + (ast - 30.0) * 0.05 + (crp - 2.0) * 0.15 + (bmi - 25.0) * 0.1
        prob = min(max(1.0 / (1.0 + math.exp(-(-3.5 + score * 0.55))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.35: risk = "Very High"
        elif prob > 0.18: risk = "High"
        elif prob > 0.08: risk = "Moderate"

        results.append({
            "diseaseKey": "NASH",
            "nameEn": "NASH Progression Risk",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 8. Metabolic Syndrome & Obesity Risk Model
    reqs = PREDICTION_REQUIREMENTS["Metabolic_Syndrome"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Metabolic_Syndrome"):
        results.append({
            "diseaseKey": "Metabolic_Syndrome",
            "nameEn": "Metabolic Syndrome & Obesity Risk",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Metabolic_Syndrome",
            "nameEn": "Metabolic Syndrome & Obesity Risk",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        waist = dataset["Waist"]
        bmi = dataset["BMI"]
        tg = dataset["Triglycerides"]
        fbs = dataset["FBS"]

        score = (waist - 80.0) * 0.08 + (bmi - 20.0) * 0.15 + (tg - 110.0) * 0.006 + (fbs - 80.0) * 0.04
        prob = min(max(1.0 / (1.0 + math.exp(-(-2.6 + score * 0.5))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.48: risk = "Very High"
        elif prob > 0.25: risk = "High"
        elif prob > 0.11: risk = "Moderate"

        results.append({
            "diseaseKey": "Metabolic_Syndrome",
            "nameEn": "Metabolic Syndrome & Obesity Risk",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 9. Iron Deficiency Anemia Risk Model
    reqs = PREDICTION_REQUIREMENTS["Iron_Deficiency_Anemia"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Iron_Deficiency_Anemia"):
        results.append({
            "diseaseKey": "Iron_Deficiency_Anemia",
            "nameEn": "Iron Deficiency Anemia Recurrence",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Iron_Deficiency_Anemia",
            "nameEn": "Iron Deficiency Anemia Recurrence",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        ferritin = dataset["Ferritin"]
        hb = dataset["Hb"]
        iron = dataset["SerumIron"]

        score = (40.0 - ferritin) * 0.08 + (13.0 - hb) * 0.6 + (75.0 - iron) * 0.02
        prob = min(max(1.0 / (1.0 + math.exp(-(-2.2 + score * 0.6))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.4: risk = "Very High"
        elif prob > 0.2: risk = "High"
        elif prob > 0.09: risk = "Moderate"

        results.append({
            "diseaseKey": "Iron_Deficiency_Anemia",
            "nameEn": "Iron Deficiency Anemia Recurrence",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 10. Hypothyroidism Risk Model
    reqs = PREDICTION_REQUIREMENTS["Primary_Hypothyroidism"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Primary_Hypothyroidism"):
        results.append({
            "diseaseKey": "Primary_Hypothyroidism",
            "nameEn": "Hypothyroidism Progression",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Primary_Hypothyroidism",
            "nameEn": "Hypothyroidism Progression",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        tsh = dataset["TSH"]
        tpo = dataset["Anti_TPO"]

        score = (tsh - 1.5) * 0.6 + (1.8 if tpo > 34.0 else 0.0)
        prob = min(max(1.0 / (1.0 + math.exp(-(-3.0 + score * 0.75))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.3: risk = "Very High"
        elif prob > 0.15: risk = "High"
        elif prob > 0.06: risk = "Moderate"

        results.append({
            "diseaseKey": "Primary_Hypothyroidism",
            "nameEn": "Hypothyroidism Progression",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    # 11. Gout Flare Risk Model
    reqs = PREDICTION_REQUIREMENTS["Gout"]
    has_reqs = all(dataset.get(r) is not None for r in reqs)

    if has_diagnosis("Gout"):
        results.append({
            "diseaseKey": "Gout",
            "nameEn": "Gout Flare & Joint Attack",
            "probability": 1.0,
            "riskLevel": "Existing",
            "status": "AlreadyDiagnosed",
            "exclusionReason": "شما در حال حاضر به این بیماری مبتلا هستید (You currently have this disease).",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })
    elif not has_reqs:
        missing = [r for r in reqs if dataset.get(r) is None]
        results.append({
            "diseaseKey": "Gout",
            "nameEn": "Gout Flare & Joint Attack",
            "status": "Insufficient Data",
            "requiredFeatures": reqs,
            "missingFeatures": missing
        })
    else:
        uric = dataset["Uric_Acid"]
        cr = dataset["Creatinine"]

        score = (uric - 5.5) * 1.1 + (cr - 0.8) * 0.8
        prob = min(max(1.0 / (1.0 + math.exp(-(-3.2 + score * 0.8))), 0.01), 0.99)

        risk = "Low"
        if prob > 0.3: risk = "Very High"
        elif prob > 0.15: risk = "High"
        elif prob > 0.06: risk = "Moderate"

        results.append({
            "diseaseKey": "Gout",
            "nameEn": "Gout Flare & Joint Attack",
            "probability": prob,
            "riskLevel": risk,
            "status": "Evaluated",
            "requiredFeatures": reqs,
            "missingFeatures": []
        })

    return results
