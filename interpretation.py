# interpretation.py

from disease_guidelines import DISEASE_GUIDELINES
from clinical_data import FEATURE_REGISTRY


def interpret_lab_data(inputs: dict, derived: dict, patient: dict) -> list:
    dataset = {**inputs, **derived}
    gender = "male" if patient.get("Sex") in [1, "1", "Male", "male"] else "female"
    age = patient.get("Age", 35)
    results = []
    # Diseases that have explicit rules (the large if/elif chain)
    EXPLICIT_RULE_DISEASES = {
        # 1. CBC AND DIFFERENTIAL
        "Iron deficiency anemia", "Anemia of chronic disease", "Thalassemia trait",
        "Sideroblastic anemia", "Hemolytic anemia", "Aplastic anemia",
        "Acute blood loss anemia", "Megaloblastic anemia", "Vitamin B12 deficiency anemia",
        "Folate deficiency anemia", "Autoimmune hemolytic anemia", "Hereditary spherocytosis",
        "G6PD deficiency", "Sickle cell disease", "Myelodysplastic syndrome",
        "Leukopenia", "Neutropenia", "Lymphocytosis", "Eosinophilia", "Basophilia",
        "Monocytosis", "Thrombocytopenia", "Immune thrombocytopenia", "Thrombocytosis",
        "Polycythemia vera",
        # 2. IRON, VITAMIN, AND NUTRITION
        "Iron deficiency without anemia", "Functional iron deficiency", "Iron overload",
        "Hereditary hemochromatosis", "Vitamin B12 deficiency", "Folate deficiency",
        "Copper deficiency", "Zinc deficiency", "Vitamin D deficiency", "Vitamin K deficiency",
        "Protein-energy malnutrition", "Sarcopenia", "Cachexia", "Refeeding syndrome",
        "Chronic malnutrition",
        # 3. THYROID AND ENDOCRINE
        "Primary hypothyroidism", "Subclinical hypothyroidism", "Secondary hypothyroidism",
        "Hyperthyroidism", "Subclinical hyperthyroidism", "Graves disease",
        "Hashimoto thyroiditis", "Thyroiditis", "Central adrenal insufficiency",
        "Primary adrenal insufficiency", "Cushing syndrome", "Hyperprolactinemia",
        "Acromegaly", "Growth hormone deficiency", "Hypogonadism",
        "Polycystic ovary syndrome", "Menopause-related endocrine dysfunction",
        "Congenital adrenal hyperplasia",
        # 4. DIABETES AND METABOLIC
        "Prediabetes", "Type 2 diabetes mellitus", "Type 1 diabetes mellitus",
        "Gestational diabetes", "Diabetic ketoacidosis", "Hyperosmolar hyperglycemic state",
        "Insulin resistance syndrome", "Metabolic syndrome", "Reactive hypoglycemia",
        "Fasting hypoglycemia", "Dyslipidemia of diabetes",
        # 5. LIPID PANELS
        "Hypercholesterolemia", "Hypertriglyceridemia", "Mixed dyslipidemia",
        "Familial hypercholesterolemia", "Familial combined hyperlipidemia",
        "Familial chylomicronemia syndrome", "Remnant cholesterol excess",
        "Atherogenic dyslipidemia", "Severe hypertriglyceridemia", "Low HDL syndrome",
        # 6. RENAL FUNCTION AND URINE PROTEIN
        "Chronic kidney disease", "Diabetic kidney disease", "Hypertensive nephropathy",
        "Acute kidney injury", "Glomerulonephritis", "Nephrotic syndrome",
        "Nephritic syndrome", "IgA nephropathy", "Lupus nephritis",
        "Minimal change disease", "Focal segmental glomerulosclerosis",
        "Membranous nephropathy", "Acute tubular necrosis", "Interstitial nephritis",
        "Polycystic kidney disease", "Albuminuria", "Proteinuria",
        "Nephrotic-range proteinuria", "Uremia", "End-stage kidney disease",
        # 7. LIVER FUNCTION AND HEPATITIS
        "Acute viral hepatitis", "Chronic hepatitis B", "Chronic hepatitis C",
        "Hepatitis C infection",  # because of 'or' condition
        "Nonalcoholic fatty liver disease",
        "MASLD (Metabolic dysfunction-associated steatotic liver disease)",
        "Nonalcoholic steatohepatitis", "Alcohol-associated liver disease",
        "Drug-induced liver injury", "Cholestatic liver disease", "Autoimmune hepatitis",
        "Primary biliary cholangitis", "Cirrhosis", "Acute liver failure",
        "Hepatic synthetic dysfunction", "Obstructive jaundice",
        # 8. ELECTROLYTE AND ACID–BASE
        "Hyponatremia", "Hypernatremia", "Hypokalemia", "Hyperkalemia",
        "Hypocalcemia", "Hypercalcemia", "Hypomagnesemia", "Hypermagnesemia",
        "Hypophosphatemia", "Hyperphosphatemia", "Metabolic acidosis",
        "Metabolic alkalosis", "Respiratory acidosis", "Respiratory alkalosis",
        "High anion gap acidosis", "SIADH",
        "Syndrome of inappropriate antidiuretic hormone secretion",
        # 9. BONE AND MINERAL
        "Primary hyperparathyroidism", "Secondary hyperparathyroidism",
        "Hypoparathyroidism", "Osteomalacia", "Rickets", "Paget disease of bone",
        # 10. CARDIAC BIOMARKERS
        "Acute myocardial infarction", "Heart failure", "Acute decompensated heart failure",
        "Myocardial injury", "Myocarditis", "Cardiorenal syndrome", "Stress cardiomyopathy",
        # 11. COAGULATION
        "Disseminated intravascular coagulation", "Venous thromboembolism",
        "Deep vein thrombosis", "Pulmonary embolism", "Liver-related coagulopathy",
        "Vitamin K deficiency coagulopathy", "Consumptive coagulopathy", "Hypercoagulable state",
        # 12. INFLAMMATORY
        "Acute bacterial infection", "Viral infection", "Sepsis",
        # 13. AUTOIMMUNE AND RHEUMATOLOGY
        "Systemic lupus erythematosus", "Rheumatoid arthritis", "Sjögren syndrome",
        "Systemic sclerosis", "Mixed connective tissue disease", "Antiphospholipid syndrome",
        "ANCA-associated vasculitis", "Dermatomyositis", "Polymyositis",
        "Undifferentiated connective tissue disease", "Autoimmune thyroid disease",
        "Autoimmune liver disease",
        # 14. PANCREATIC
        "Acute pancreatitis", "Chronic pancreatitis", "Pancreatic exocrine dysfunction",
        "Pancreaticobiliary inflammation",
        # 15. URINALYSIS
        "Urinary tract infection", "Hematuria syndrome", "Pyuria", "Crystalluria",
        "Glucosuria", "Ketonuria", "Tubular injury pattern", "Cast-associated renal disease",
        # 16. ADDITIONAL HIGH-YIELD
        "Gout", "Hyperuricemia", "Pseudohyperkalemia", "Pseudohyponatremia",
        "Factitious hypoglycemia", "Rhabdomyolysis", "Tumor lysis syndrome"
    }
    # Safe conversion helpers
    def get_num(key, default=None):
        val = dataset.get(key)
        if val is None:
            return default
        try:
            return float(val)
        except (ValueError, TypeError):
            return default

    def get_str(key, default=""):
        val = dataset.get(key)
        if val is None:
            return default
        return str(val).strip()

    def is_positive(s):
        return s.lower() in ["positive", "reactive", "yes", "true", "1", "small", "moderate", "large"]

    # Define diagnostic rule checks for ALL mapped diseases
    for disease in DISEASE_GUIDELINES:
        name = disease["name"]
        required = disease["required_features"]

        # Check if ALL required features are entered
        has_required = all(dataset.get(feat) is not None for feat in required)
        if not has_required:
            continue

        is_present = False
        evidence = []

        # ---------------------------------------------------------------
        # 1. CBC AND DIFFERENTIAL
        # ---------------------------------------------------------------
        if name == "Iron deficiency anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            ferritin = get_num("Ferritin")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv < 80 and ferritin < 30:
                is_present = True
                evidence.append(f"Low Hemoglobin: {hb} g/dL (Threshold: < {hb_limit})")
                evidence.append(f"Microcytosis: MCV {mcv} fL (Threshold: < 80)")
                evidence.append(f"Depleted Ferritin stores: {ferritin} ng/mL (Threshold: < 30)")

        elif name == "Anemia of chronic disease":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            ferritin = get_num("Ferritin")
            crp = get_num("CRP")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and 80 <= mcv <= 100 and ferritin >= 100 and crp > 5.0:
                is_present = True
                evidence.append(f"Low Hemoglobin: {hb} g/dL (Threshold: < {hb_limit})")
                evidence.append(f"Normocytic MCV: {mcv} fL (Range: 80-100)")
                evidence.append(f"Preserved/High Ferritin: {ferritin} ng/mL (>= 100)")
                evidence.append(f"Systemic inflammation: CRP {crp} mg/L (> 5.0)")

        elif name == "Thalassemia trait":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            rbc = get_num("RBC")
            mch = get_num("MCH")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv < 75 and rbc >= 5.0 and mch < 25:
                is_present = True
                evidence.append(f"Mild anemia: Hb {hb} g/dL (< {hb_limit})")
                evidence.append(f"Severe microcytosis: MCV {mcv} fL (< 75)")
                evidence.append(f"High RBC count: {rbc} x10^12/L (>= 5.0)")
                evidence.append(f"Low MCH: {mch} pg (< 25)")

        elif name == "Sideroblastic anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            iron = get_num("SerumIron")
            ferritin = get_num("Ferritin")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv < 80 and iron > 150 and ferritin > 200:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL (< {hb_limit})")
                evidence.append(f"Microcytosis: MCV {mcv} fL (< 80)")
                evidence.append(f"High Serum Iron: {iron} µg/dL (> 150)")
                evidence.append(f"Elevated Ferritin: {ferritin} ng/mL (> 200)")

        elif name == "Hemolytic anemia":
            hb = get_num("Hb")
            t_bil = get_num("Total_Bilirubin")
            i_bil = get_num("Indirect_Bilirubin")
            ldh = get_num("LDH")
            hapto = get_num("Haptoglobin")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and t_bil > 1.2 and i_bil > 0.8 and ldh > 250 and hapto < 25:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL (< {hb_limit})")
                evidence.append(f"Elevated Total Bilirubin: {t_bil} mg/dL (> 1.2)")
                evidence.append(f"Indirect Hyperbilirubinemia: {i_bil} mg/dL (> 0.8)")
                evidence.append(f"Elevated LDH: {ldh} U/L (> 250)")
                evidence.append(f"Low Haptoglobin: {hapto} mg/dL (< 25)")

        elif name == "Aplastic anemia":
            hb = get_num("Hb")
            wbc = get_num("WBC")
            plt = get_num("Platelet")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and wbc < 3.5 and plt < 100:
                is_present = True
                evidence.append("Pancytopenia detected (all 3 lineages)")
                evidence.append(f"Low Hb: {hb} g/dL, WBC: {wbc} x10^9/L, Plt: {plt} x10^9/L")

        elif name == "Acute blood loss anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            hb_limit = 12.0 if gender == "male" else 10.5
            if hb < hb_limit and 80 <= mcv <= 100:
                is_present = True
                evidence.append(f"Significant Hb drop: {hb} g/dL (< {hb_limit})")
                evidence.append(f"Normocytic RBC volume: MCV {mcv} fL")

        elif name == "Megaloblastic anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            b12 = get_num("VitaminB12")
            folate = get_num("Folate")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv > 100 and (b12 < 200 or folate < 2.0):
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Macrocytosis: MCV {mcv} fL (> 100)")
                if b12 < 200:
                    evidence.append(f"Vitamin B12 deficiency: {b12} pg/mL (< 200)")
                if folate < 2.0:
                    evidence.append(f"Folate deficiency: {folate} ng/mL (< 2.0)")

        elif name == "Vitamin B12 deficiency anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            b12 = get_num("VitaminB12")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv > 100 and b12 < 200:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Macrocytic MCV: {mcv} fL (> 100)")
                evidence.append(f"Vitamin B12 deficiency: {b12} pg/mL (< 200)")

        elif name == "Folate deficiency anemia":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            folate = get_num("Folate")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mcv > 100 and folate < 2.0:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Macrocytic MCV: {mcv} fL (> 100)")
                evidence.append(f"Folate deficiency: {folate} ng/mL (< 2.0)")

        elif name == "Autoimmune hemolytic anemia":
            hb = get_num("Hb")
            i_bil = get_num("Indirect_Bilirubin")
            dat = get_str("DAT")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and i_bil > 0.8 and is_positive(dat):
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Indirect Hyperbilirubinemia: {i_bil} mg/dL (> 0.8)")
                evidence.append(f"Positive Direct Antiglobulin Test (DAT): {dat}")

        elif name == "Hereditary spherocytosis":
            hb = get_num("Hb")
            mchc = get_num("MCHC")
            i_bil = get_num("Indirect_Bilirubin")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and mchc > 36.0 and i_bil > 0.8:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Elevated MCHC: {mchc} g/dL (> 36.0)")
                evidence.append(f"Indirect Hyperbilirubinemia: {i_bil} mg/dL (> 0.8)")

        elif name == "G6PD deficiency":
            hb = get_num("Hb")
            i_bil = get_num("Indirect_Bilirubin")
            g6pd = get_num("G6PD_Activity")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb < hb_limit and i_bil > 0.8 and g6pd < 10:
                is_present = True
                evidence.append(f"Low Hb: {hb} g/dL")
                evidence.append(f"Indirect Hyperbilirubinemia: {i_bil} mg/dL (> 0.8)")
                evidence.append(f"Severely reduced G6PD activity: {g6pd}% (< 10% of normal)")

        elif name == "Sickle cell disease":
            hb = get_num("Hb")
            mcv = get_num("MCV")
            rbc = get_num("RBC")
            if hb < 9.0 and rbc < 3.5 and mcv < 100:
                is_present = True
                evidence.append(f"Severe Anemia: Hb {hb} g/dL (< 9.0)")
                evidence.append(f"Low RBC count: {rbc} x10^12/L (< 3.5)")
                evidence.append(f"MCV {mcv} fL (normo‑/microcytic)")

        elif name == "Myelodysplastic syndrome":
            hb = get_num("Hb")
            wbc = get_num("WBC")
            plt = get_num("Platelet")
            mcv = get_num("MCV")
            hb_limit = 13.5 if gender == "male" else 12.0
            cytopenias = sum([hb < hb_limit, wbc < 3.5, plt < 150])
            if cytopenias >= 2 and mcv > 100:
                is_present = True
                evidence.append(f"Cytopenias in {cytopenias} lineages (≥2)")
                evidence.append(f"Macrocytosis: MCV {mcv} fL (> 100)")

        elif name == "Leukopenia":
            wbc = get_num("WBC")
            if wbc < 4.0:
                is_present = True
                evidence.append(f"WBC {wbc} x10^9/L (< 4.0)")

        elif name == "Neutropenia":
            anc = get_num("ANC")
            if anc < 1.5:
                is_present = True
                evidence.append(f"ANC {anc} x10^9/L (< 1.5)")

        elif name == "Lymphocytosis":
            alc = get_num("ALC")
            if alc > 4.0:
                is_present = True
                evidence.append(f"ALC {alc} x10^9/L (> 4.0)")

        elif name == "Eosinophilia":
            eos = get_num("EosinophilsPercent")
            if eos > 6.0:
                is_present = True
                evidence.append(f"Eosinophils {eos}% (> 6%)")

        elif name == "Basophilia":
            bas = get_num("BasophilsPercent")
            if bas > 1.5:
                is_present = True
                evidence.append(f"Basophils {bas}% (> 1.5%)")

        elif name == "Monocytosis":
            mono = get_num("MonocytesPercent")
            if mono > 10.0:
                is_present = True
                evidence.append(f"Monocytes {mono}% (> 10%)")

        elif name == "Thrombocytopenia":
            plt = get_num("Platelet")
            if plt < 150:
                is_present = True
                evidence.append(f"Platelets {plt} x10^9/L (< 150)")

        elif name == "Immune thrombocytopenia":
            plt = get_num("Platelet")
            hb = get_num("Hb")
            wbc = get_num("WBC")
            hb_limit = 13.5 if gender == "male" else 12.0
            if plt < 100 and hb >= hb_limit and wbc >= 4.0:
                is_present = True
                evidence.append(f"Isolated thrombocytopenia: Plt {plt} x10^9/L (< 100)")
                evidence.append(f"Normal Hb ({hb} g/dL) and WBC ({wbc} x10^9/L)")

        elif name == "Thrombocytosis":
            plt = get_num("Platelet")
            if plt > 450:
                is_present = True
                evidence.append(f"Platelets {plt} x10^9/L (> 450)")

        elif name == "Polycythemia vera":
            hb = get_num("Hb")
            hct = get_num("Hct")
            rbc = get_num("RBC")
            hb_th = 18.5 if gender == "male" else 16.5
            hct_th = 52.0 if gender == "male" else 48.0
            if hb > hb_th and hct > hct_th and rbc > 5.5:
                is_present = True
                evidence.append(f"Erythrocytosis: Hb {hb} g/dL (> {hb_th}), Hct {hct}%, RBC {rbc}")

        # ---------------------------------------------------------------
        # 2. IRON, VITAMIN, AND NUTRITION
        # ---------------------------------------------------------------
        elif name == "Iron deficiency without anemia":
            ferritin = get_num("Ferritin")
            hb = get_num("Hb")
            hb_limit = 13.5 if gender == "male" else 12.0
            if ferritin < 30 and hb >= hb_limit:
                is_present = True
                evidence.append(f"Ferritin {ferritin} ng/mL (< 30), Hb normal ({hb} g/dL)")

        elif name == "Functional iron deficiency":
            ferritin = get_num("Ferritin")
            tsat = get_num("Transferrin_Sat")
            crp = get_num("CRP")
            if ferritin >= 100 and tsat < 20 and crp > 5.0:
                is_present = True
                evidence.append(f"Ferritin {ferritin} ng/mL (≥100), TSAT {tsat}% (<20%), CRP {crp} mg/L (>5.0)")

        elif name == "Iron overload":
            ferritin = get_num("Ferritin")
            tsat = get_num("Transferrin_Sat")
            ferr_limit = 300 if gender == "male" else 200
            if ferritin > ferr_limit and tsat > 45:
                is_present = True
                evidence.append(f"Ferritin {ferritin} ng/mL (> {ferr_limit}), TSAT {tsat}% (>45%)")

        elif name == "Hereditary hemochromatosis":
            ferritin = get_num("Ferritin")
            tsat = get_num("Transferrin_Sat")
            if ferritin > 400 and tsat > 55:
                is_present = True
                evidence.append(f"Ferritin {ferritin} ng/mL (>400), TSAT {tsat}% (>55%)")

        elif name == "Vitamin B12 deficiency":
            b12 = get_num("VitaminB12")
            if b12 < 200:
                is_present = True
                evidence.append(f"Vitamin B12 {b12} pg/mL (<200)")

        elif name == "Folate deficiency":
            folate = get_num("Folate")
            if folate < 2.0:
                is_present = True
                evidence.append(f"Folate {folate} ng/mL (<2.0)")

        elif name == "Copper deficiency":
            hb = get_num("Hb")
            anc = get_num("ANC")
            hb_limit = 13.5 if gender == "male" else 12.0
            if hb is not None and anc is not None:          # ← safety check added
                if hb < hb_limit and anc < 1.5:
                    is_present = True
                    evidence.append(f"Anemia (Hb {hb} g/dL) and neutropenia (ANC {anc} x10^9/L)")

        elif name == "Zinc deficiency":
            zinc = get_num("Zinc")
            if zinc < 60:
                is_present = True
                evidence.append(f"Zinc {zinc} µg/dL (<60)")

        elif name == "Vitamin D deficiency":
            vit_d = get_num("Vitamin_D")
            if vit_d < 20:
                is_present = True
                evidence.append(f"25‑OH Vitamin D {vit_d} ng/mL (<20)")

        elif name == "Vitamin K deficiency":
            inr = get_num("INR")
            pt = get_num("PT")
            if inr > 1.2 and pt > 14.0:
                is_present = True
                evidence.append(f"INR {inr} (>1.2), PT {pt} sec (>14.0)")

        elif name == "Protein-energy malnutrition":
            alb = get_num("Albumin")
            prealb = get_num("Prealbumin")
            tp = get_num("Total_Protein")
            if alb < 3.4 and prealb < 15 and tp < 6.0:
                is_present = True
                evidence.append(f"Alb {alb} g/dL, Prealb {prealb} mg/dL, TP {tp} g/dL")

        elif name == "Sarcopenia":
            weight = get_num("Weight")
            height = get_num("Height")
            if age > 65 and weight and height:
                bmi = weight / ((height / 100) ** 2)
                if bmi < 18.5:
                    is_present = True
                    evidence.append(f"Age {age}y, BMI {round(bmi,1)} kg/m² (<18.5)")

        elif name == "Cachexia":
            crp = get_num("CRP")
            alb = get_num("Albumin")
            if crp > 5.0 and alb < 3.5:
                is_present = True
                evidence.append(f"CRP {crp} mg/L (>5.0), Alb {alb} g/dL (<3.5)")

        elif name == "Refeeding syndrome":
            phos = get_num("Phosphate")
            k = get_num("Potassium")
            mg = get_num("Magnesium")
            if phos < 2.5 and k < 3.5 and mg < 1.5:
                is_present = True
                evidence.append(f"Phos {phos} mg/dL, K {k} mmol/L, Mg {mg} mg/dL")

        elif name == "Chronic malnutrition":
            alb = get_num("Albumin")
            prealb = get_num("Prealbumin")
            if alb < 3.5 and prealb < 10:
                is_present = True
                evidence.append(f"Alb {alb} g/dL, Prealb {prealb} mg/dL")

        # ---------------------------------------------------------------
        # 3. THYROID AND ENDOCRINE
        # ---------------------------------------------------------------
        elif name == "Primary hypothyroidism":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            if tsh > 4.5 and ft4 < 0.8:
                is_present = True
                evidence.append(f"TSH {tsh} mIU/L (>4.5), FreeT4 {ft4} ng/dL (<0.8)")

        elif name == "Subclinical hypothyroidism":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            if tsh > 4.5 and 0.8 <= ft4 <= 1.8:
                is_present = True
                evidence.append(f"TSH {tsh} mIU/L, FreeT4 normal ({ft4} ng/dL)")

        elif name == "Secondary hypothyroidism":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            if tsh < 4.5 and ft4 < 0.8:
                is_present = True
                evidence.append(f"TSH {tsh} mIU/L (inappropriately normal/low), FreeT4 {ft4} ng/dL (<0.8)")

        elif name == "Hyperthyroidism":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            if tsh < 0.1 and ft4 > 1.8:
                is_present = True
                evidence.append(f"Suppressed TSH {tsh} mIU/L, elevated FreeT4 {ft4} ng/dL")

        elif name == "Subclinical hyperthyroidism":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            if tsh < 0.4 and 0.8 <= ft4 <= 1.8:
                is_present = True
                evidence.append(f"TSH suppressed {tsh} mIU/L, FreeT4 normal ({ft4} ng/dL)")

        elif name == "Graves disease":
            tsh = get_num("TSH")
            ft4 = get_num("FreeT4")
            trab = get_num("TRAb")
            if tsh < 0.4 and ft4 > 1.8 and trab > 1.75:
                is_present = True
                evidence.append(f"TSH {tsh}, FreeT4 {ft4}, TRAb {trab} IU/L (>1.75)")

        elif name == "Hashimoto thyroiditis":
            tsh = get_num("TSH")
            anti_tpo = get_num("Anti_TPO")
            if anti_tpo > 34 and tsh > 4.0:
                is_present = True
                evidence.append(f"Anti-TPO {anti_tpo} IU/mL (>34), TSH {tsh} mIU/L")

        elif name == "Thyroiditis":
            tsh = get_num("TSH")
            crp = get_num("CRP")
            if crp > 10.0 and (tsh < 0.4 or tsh > 4.5):
                is_present = True
                evidence.append(f"CRP {crp} mg/L, TSH {tsh} mIU/L (dysfunction)")

        elif name == "Central adrenal insufficiency":
            cort = get_num("Cortisol")
            acth = get_num("ACTH")
            if cort < 5.0 and acth < 10:
                is_present = True
                evidence.append(f"Cortisol {cort} µg/dL (<5.0), ACTH {acth} pg/mL (<10)")

        elif name == "Primary adrenal insufficiency":
            cort = get_num("Cortisol")
            acth = get_num("ACTH")
            na = get_num("Sodium")
            k = get_num("Potassium")
            if cort < 5.0 and acth > 60 and na < 135 and k > 5.0:
                is_present = True
                evidence.append(f"Cortisol {cort}, ACTH {acth}, Na {na}, K {k}")

        elif name == "Cushing syndrome":
            cort = get_num("Cortisol")
            acth = get_num("ACTH")
            if cort > 25 and acth > 60:
                is_present = True
                evidence.append(f"Cortisol {cort} µg/dL (>25), ACTH {acth} pg/mL (>60)")

        elif name == "Hyperprolactinemia":
            prol = get_num("Prolactin")
            limit = 18.0 if gender == "male" else 29.0
            if prol > limit:
                is_present = True
                evidence.append(f"Prolactin {prol} ng/mL (> {limit})")

        elif name == "Acromegaly":
            igf1 = get_num("IGF1")
            if igf1 > 250:
                is_present = True
                evidence.append(f"IGF-1 {igf1} ng/mL (>250)")

        elif name == "Growth hormone deficiency":
            igf1 = get_num("IGF1")
            if igf1 < 50:
                is_present = True
                evidence.append(f"IGF-1 {igf1} ng/mL (<50)")

        elif name == "Hypogonadism":
            testo = get_num("Testosterone")
            lh = get_num("LH")
            fsh = get_num("FSH")
            if testo < 300:
                is_present = True
                evidence.append(f"Testosterone {testo} ng/dL (<300)")
                if lh is not None:
                    if lh > 10:
                        evidence.append(f"High LH ({lh} IU/L) → primary hypogonadism")
                    elif lh < 1.5:
                        evidence.append(f"Low LH ({lh} IU/L) → secondary hypogonadism")

        elif name == "Polycystic ovary syndrome":
            lh = get_num("LH")
            fsh = get_num("FSH")
            testo = get_num("Testosterone")
            if fsh > 0 and (lh / fsh) > 2.0 and testo > 50:
                is_present = True
                evidence.append(f"LH/FSH ratio {round(lh/fsh,1)} (>2:1), Testosterone {testo} ng/dL (>50)")

        elif name == "Menopause-related endocrine dysfunction":
            fsh = get_num("FSH")
            est = get_num("Estradiol")
            if fsh > 30 and est < 30:
                is_present = True
                evidence.append(f"FSH {fsh} IU/L (>30), Estradiol {est} pg/mL (<30)")

        elif name == "Congenital adrenal hyperplasia":
            cort = get_num("Cortisol")
            if cort < 5.0:
                is_present = True
                evidence.append(f"Cortisol {cort} µg/dL (<5.0)")

        # ---------------------------------------------------------------
        # 4. DIABETES AND METABOLIC
        # ---------------------------------------------------------------
        elif name == "Prediabetes":
            fbs = get_num("FBS")
            hba1c = get_num("HbA1c")
            if (100 <= fbs <= 125) or (5.7 <= hba1c <= 6.4):
                is_present = True
                evidence.append(f"FBS {fbs} mg/dL, HbA1c {hba1c}%")

        elif name == "Type 2 diabetes mellitus":
            fbs = get_num("FBS")
            hba1c = get_num("HbA1c")
            if fbs >= 126 or hba1c >= 6.5:
                is_present = True
                evidence.append(f"FBS {fbs} mg/dL, HbA1c {hba1c}%")

        elif name == "Type 1 diabetes mellitus":
            fbs = get_num("FBS")
            insulin = get_num("Insulin")
            if fbs >= 126 and insulin < 3.0:
                is_present = True
                evidence.append(f"Hyperglycemia {fbs} mg/dL, very low Insulin {insulin} µIU/mL")

        elif name == "Gestational diabetes":
            fbs = get_num("FBS")
            ogtt = get_num("OGTT_2h")
            if fbs >= 92 or ogtt >= 153:
                is_present = True
                evidence.append(f"FBS {fbs} mg/dL, 2h OGTT {ogtt} mg/dL")

        elif name == "Diabetic ketoacidosis":
            fbs = get_num("FBS")
            ket = get_str("UrineKetones")
            hco3 = get_num("HCO3")
            if fbs > 250 and is_positive(ket) and hco3 < 18:
                is_present = True
                evidence.append(f"Glucose {fbs} mg/dL, Ketones {ket}, HCO3 {hco3} mmol/L")

        elif name == "Hyperosmolar hyperglycemic state":
            fbs = get_num("FBS")
            if fbs > 600:
                is_present = True
                evidence.append(f"Extreme hyperglycemia: {fbs} mg/dL (>600)")

        elif name == "Insulin resistance syndrome":
            insulin = get_num("Insulin")
            homa = get_num("HOMA_IR")
            if insulin > 15 and homa > 2.5:
                is_present = True
                evidence.append(f"Insulin {insulin} µIU/mL, HOMA‑IR {homa}")

        elif name == "Metabolic syndrome":
            waist = get_num("Waist", 0)
            tg = get_num("Triglycerides", 0)
            hdl = get_num("HDL", 100)
            fbs = get_num("FBS", 0)
            sbp = get_num("Systolic_BP", 0)
            dbp = get_num("Diastolic_BP", 0)
            met = 0
            if waist >= (102 if gender == "male" else 88): met += 1
            if tg >= 150: met += 1
            if hdl < (40 if gender == "male" else 50): met += 1
            if fbs >= 100: met += 1
            if sbp >= 130 or dbp >= 85: met += 1
            if met >= 3:
                is_present = True
                evidence.append(f"Metabolic syndrome criteria met: {met}/5")

        elif name == "Reactive hypoglycemia":
            fbs = get_num("FBS")
            if fbs < 55:
                is_present = True
                evidence.append(f"Postprandial glucose {fbs} mg/dL (<55)")

        elif name == "Fasting hypoglycemia":
            fbs = get_num("FBS")
            insulin = get_num("Insulin")
            if fbs < 55 and insulin > 3.0:
                is_present = True
                evidence.append(f"Glucose {fbs} mg/dL, Insulin {insulin} µIU/mL (inappropriate)")

        elif name == "Dyslipidemia of diabetes":
            hba1c = get_num("HbA1c")
            tg = get_num("Triglycerides")
            hdl = get_num("HDL")
            hdl_th = 40 if gender == "male" else 50
            if hba1c >= 6.5 and tg > 150 and hdl < hdl_th:
                is_present = True
                evidence.append(f"HbA1c {hba1c}%, TG {tg} mg/dL, HDL {hdl} mg/dL")

        # ---------------------------------------------------------------
        # 5. LIPID PANELS
        # ---------------------------------------------------------------
        elif name == "Hypercholesterolemia":
            tc = get_num("Total_Cholesterol")
            if tc >= 200:
                is_present = True
                evidence.append(f"Total Cholesterol {tc} mg/dL (≥200)")

        elif name == "Hypertriglyceridemia":
            tg = get_num("Triglycerides")
            if tg > 150:
                is_present = True
                evidence.append(f"Triglycerides {tg} mg/dL (>150)")

        elif name == "Mixed dyslipidemia":
            tc = get_num("Total_Cholesterol")
            tg = get_num("Triglycerides")
            if tc >= 200 and tg > 150:
                is_present = True
                evidence.append(f"TC {tc} mg/dL, TG {tg} mg/dL")

        elif name == "Familial hypercholesterolemia":
            ldl = get_num("LDL")
            if ldl >= 190:
                is_present = True
                evidence.append(f"LDL {ldl} mg/dL (≥190)")

        elif name == "Familial combined hyperlipidemia":
            ldl = get_num("LDL")
            tg = get_num("Triglycerides")
            if ldl > 160 and tg > 200:
                is_present = True
                evidence.append(f"LDL {ldl} mg/dL, TG {tg} mg/dL")

        elif name == "Familial chylomicronemia syndrome":
            tg = get_num("Triglycerides")
            if tg >= 1000:
                is_present = True
                evidence.append(f"Severe HyperTG: {tg} mg/dL (≥1000)")

        elif name == "Remnant cholesterol excess":
            tc = get_num("Total_Cholesterol")
            hdl = get_num("HDL")
            ldl = get_num("LDL")
            if tc and hdl and ldl:
                rem = tc - hdl - ldl
                if rem >= 30:
                    is_present = True
                    evidence.append(f"Remnant Chol {rem:.1f} mg/dL (≥30)")

        elif name == "Atherogenic dyslipidemia":
            tg = get_num("Triglycerides")
            hdl = get_num("HDL")
            ldl = get_num("LDL")
            hdl_th = 40 if gender == "male" else 50
            if tg > 150 and hdl < hdl_th and ldl > 130:
                is_present = True
                evidence.append(f"TG {tg}, HDL {hdl}, LDL {ldl}")

        elif name == "Severe hypertriglyceridemia":
            tg = get_num("Triglycerides")
            if tg >= 500:
                is_present = True
                evidence.append(f"Triglycerides {tg} mg/dL (≥500)")

        elif name == "Low HDL syndrome":
            hdl = get_num("HDL")
            hdl_th = 40 if gender == "male" else 50
            if hdl < hdl_th:
                is_present = True
                evidence.append(f"HDL {hdl} mg/dL (< {hdl_th})")

        # ---------------------------------------------------------------
        # 6. RENAL FUNCTION AND URINE PROTEIN
        # ---------------------------------------------------------------
        elif name == "Chronic kidney disease":
            egfr = get_num("eGFR")
            if egfr < 60:
                is_present = True
                evidence.append(f"eGFR {egfr} mL/min/1.73m² (<60)")

        elif name == "Diabetic kidney disease":
            hba1c = get_num("HbA1c")
            egfr = get_num("eGFR")
            acr = get_num("ACR")
            if hba1c >= 6.5 and acr >= 30:
                is_present = True
                evidence.append(f"HbA1c {hba1c}%, ACR {acr} mg/g, eGFR {egfr}")

        elif name == "Hypertensive nephropathy":
            sbp = get_num("Systolic_BP")
            egfr = get_num("eGFR")
            acr = get_num("ACR")
            if sbp >= 130 and egfr < 90 and acr < 300:
                is_present = True
                evidence.append(f"SBP {sbp} mmHg, eGFR {egfr}, ACR {acr}")

        elif name == "Acute kidney injury":
            cr = get_num("Creatinine")
            bun = get_num("BUN")
            cr_limit = 1.3 if gender == "male" else 1.1
            if cr > cr_limit and bun > 24:
                is_present = True
                evidence.append(f"Creatinine {cr} mg/dL (> {cr_limit}), BUN {bun} mg/dL")

        elif name == "Glomerulonephritis":
            ublood = get_str("UrineBlood")
            uwbc = get_num("UrineWBC")
            urbc = get_num("UrineRBC")
            if is_positive(ublood) and uwbc > 5 and urbc > 5:
                is_present = True
                evidence.append(f"Active urine sediment: Blood {ublood}, WBC {uwbc}, RBC {urbc}")

        elif name == "Nephrotic syndrome":
            u24 = get_num("UrineProtein24h")
            alb = get_num("Albumin")
            if u24 > 3.5 and alb < 3.0:
                is_present = True
                evidence.append(f"Proteinuria {u24} g/24h, Alb {alb} g/dL")

        elif name == "Nephritic syndrome":
            ublood = get_str("UrineBlood")
            sbp = get_num("Systolic_BP")
            if is_positive(ublood) and sbp >= 140:
                is_present = True
                evidence.append(f"Hematuria + Hypertension (SBP {sbp})")

        elif name == "IgA nephropathy":
            ublood = get_str("UrineBlood")
            urbc = get_num("UrineRBC")
            if is_positive(ublood) and urbc > 5:
                is_present = True
                evidence.append(f"Microscopic hematuria: RBC {urbc}/hpf")

        elif name == "Lupus nephritis":
            ana = get_num("ANA")
            acr = get_num("ACR")
            if ana > 1.0 and acr > 500:
                is_present = True
                evidence.append(f"ANA {ana} (>1.0), ACR {acr} mg/g (>500)")

        elif name == "Minimal change disease":
            u24 = get_num("UrineProtein24h")
            alb = get_num("Albumin")
            if u24 > 3.5 and alb < 3.0:
                is_present = True
                evidence.append(f"Nephrotic: protein {u24} g/24h, Alb {alb} g/dL")

        elif name == "Focal segmental glomerulosclerosis":
            u24 = get_num("UrineProtein24h")
            alb = get_num("Albumin")
            egfr = get_num("eGFR")
            if u24 > 3.5 and alb < 3.0 and egfr < 90:
                is_present = True
                evidence.append(f"Protein {u24} g/24h, Alb {alb}, eGFR {egfr}")

        elif name == "Membranous nephropathy":
            u24 = get_num("UrineProtein24h")
            alb = get_num("Albumin")
            if u24 > 3.5 and alb < 3.0:
                is_present = True
                evidence.append(f"Heavy proteinuria {u24} g/24h, Alb {alb}")

        elif name == "Acute tubular necrosis":
            cr = get_num("Creatinine")
            bun = get_num("BUN")
            if cr > 2.0 and bun > 40:
                is_present = True
                evidence.append(f"Creatinine {cr} mg/dL, BUN {bun} mg/dL")

        elif name == "Interstitial nephritis":
            cr = get_num("Creatinine")
            uwbc = get_num("UrineWBC")
            if cr > 1.5 and uwbc > 10:
                is_present = True
                evidence.append(f"Creatinine {cr} mg/dL, Urine WBC {uwbc}/hpf")

        elif name == "Polycystic kidney disease":
            egfr = get_num("eGFR")
            sbp = get_num("Systolic_BP")
            if egfr < 90 and sbp >= 140:
                is_present = True
                evidence.append(f"eGFR {egfr}, Hypertension SBP {sbp}")

        elif name == "Albuminuria":
            acr = get_num("ACR")
            if acr >= 30:
                is_present = True
                evidence.append(f"ACR {acr} mg/g (≥30)")

        elif name == "Proteinuria":
            pcr = get_num("PCR")
            if pcr >= 150:
                is_present = True
                evidence.append(f"PCR {pcr} mg/g (≥150)")

        elif name == "Nephrotic-range proteinuria":
            u24 = get_num("UrineProtein24h")
            if u24 >= 3500:
                is_present = True
                evidence.append(f"Protein {u24} mg/24h (≥3500)")

        elif name == "Uremia":
            bun = get_num("BUN")
            cr = get_num("Creatinine")
            if bun > 80 and cr > 3.0:
                is_present = True
                evidence.append(f"BUN {bun} mg/dL, Creatinine {cr} mg/dL")

        elif name == "End-stage kidney disease":
            egfr = get_num("eGFR")
            if egfr < 15:
                is_present = True
                evidence.append(f"eGFR {egfr} mL/min/1.73m² (<15)")

        # ---------------------------------------------------------------
        # 7. LIVER FUNCTION AND HEPATITIS
        # ---------------------------------------------------------------
        elif name == "Acute viral hepatitis":
            alt = get_num("ALT")
            ast = get_num("AST")
            if alt > 500 and ast > 500:
                is_present = True
                evidence.append(f"ALT {alt} U/L, AST {ast} U/L (>500)")

        elif name == "Chronic hepatitis B":
            hbsag = get_str("HBsAg")
            if is_positive(hbsag):
                is_present = True
                evidence.append("HBsAg positive")

        elif name == "Chronic hepatitis C" or name == "Hepatitis C infection":
            anti_hcv = get_str("Anti_HCV")
            if is_positive(anti_hcv):
                is_present = True
                evidence.append("Anti-HCV positive")

        elif name == "Nonalcoholic fatty liver disease":
            alt = get_num("ALT")
            ast = get_num("AST")
            if alt > 40 and ast > 35 and (ast / alt) < 1:
                is_present = True
                evidence.append(f"ALT {alt} U/L, AST/ALT ratio {ast/alt:.2f} (<1)")

        elif name == "MASLD (Metabolic dysfunction-associated steatotic liver disease)":
            alt = get_num("ALT")
            fbs = get_num("FBS")
            hdl = get_num("HDL")
            if alt > 40 and (fbs >= 100 or hdl < (40 if gender == "male" else 50)):
                is_present = True
                evidence.append(f"ALT {alt} U/L + metabolic risk factor")

        elif name == "Nonalcoholic steatohepatitis":
            alt = get_num("ALT")
            ast = get_num("AST")
            crp = get_num("CRP")
            if alt > 50 and ast > 50 and crp > 5.0:
                is_present = True
                evidence.append(f"ALT {alt}, AST {ast}, CRP {crp}")

        elif name == "Alcohol-associated liver disease":
            alt = get_num("ALT")
            ast = get_num("AST")
            ggt = get_num("GGT")
            if ast / alt >= 2.0 and ggt > 100:
                is_present = True
                evidence.append(f"AST/ALT ≥2, GGT {ggt} U/L")

        elif name == "Drug-induced liver injury":
            alt = get_num("ALT")
            ast = get_num("AST")
            alp = get_num("ALP")
            if (alt and alt > 120) or (ast and ast > 120) or (alp and alp > 300):
                is_present = True
                evidence.append(f"ALT {alt}, AST {ast}, ALP {alp}")

        elif name == "Cholestatic liver disease":
            alp = get_num("ALP")
            ggt = get_num("GGT")
            t_bil = get_num("Total_Bilirubin")
            if alp > 150 and ggt > 50 and t_bil > 1.2:
                is_present = True
                evidence.append(f"ALP {alp}, GGT {ggt}, TBil {t_bil}")

        elif name == "Autoimmune hepatitis":
            alt = get_num("ALT")
            ana = get_num("ANA")
            if alt > 80 and ana > 1.0:
                is_present = True
                evidence.append(f"ALT {alt}, ANA {ana}")

        elif name == "Primary biliary cholangitis":
            alp = get_num("ALP")
            ggt = get_num("GGT")
            if alp > 150 and ggt > 50:
                is_present = True
                evidence.append(f"ALP {alp}, GGT {ggt}")

        elif name == "Cirrhosis":
            ast = get_num("AST")
            alt = get_num("ALT")
            plt = get_num("Platelet")
            inr = get_num("INR")
            alb = get_num("Albumin")
            if plt < 150 and inr > 1.2 and alb < 3.5 and (ast / alt) > 1:
                is_present = True
                evidence.append(f"Plt {plt}, INR {inr}, Alb {alb}, AST/ALT ratio >1")

        elif name == "Acute liver failure":
            alt = get_num("ALT")
            ast = get_num("AST")
            inr = get_num("INR")
            if alt > 500 and inr >= 1.5:
                is_present = True
                evidence.append(f"ALT {alt}, INR {inr}")

        elif name == "Hepatic synthetic dysfunction":
            alb = get_num("Albumin")
            inr = get_num("INR")
            if alb < 3.2 and inr > 1.3:
                is_present = True
                evidence.append(f"Alb {alb} g/dL, INR {inr}")

        elif name == "Obstructive jaundice":
            t_bil = get_num("Total_Bilirubin")
            d_bil = get_num("Direct_Bilirubin")
            alp = get_num("ALP")
            if t_bil > 2.0 and d_bil / t_bil > 0.5 and alp > 150:
                is_present = True
                evidence.append(f"TBil {t_bil}, DBil {d_bil}, ALP {alp}")

        # ---------------------------------------------------------------
        # 8. ELECTROLYTE AND ACID–BASE PANELS
        # ---------------------------------------------------------------
        elif name == "Hyponatremia":
            na = get_num("Sodium")
            if na < 135:
                is_present = True
                evidence.append(f"Sodium {na} mmol/L (<135)")

        elif name == "Hypernatremia":
            na = get_num("Sodium")
            if na > 145:
                is_present = True
                evidence.append(f"Sodium {na} mmol/L (>145)")

        elif name == "Hypokalemia":
            k = get_num("Potassium")
            if k < 3.5:
                is_present = True
                evidence.append(f"Potassium {k} mmol/L (<3.5)")

        elif name == "Hyperkalemia":
            k = get_num("Potassium")
            if k > 5.0:
                is_present = True
                evidence.append(f"Potassium {k} mmol/L (>5.0)")

        elif name == "Hypocalcemia":
            ca = get_num("Calcium")
            if ca < 8.5:
                is_present = True
                evidence.append(f"Calcium {ca} mg/dL (<8.5)")

        elif name == "Hypercalcemia":
            ca = get_num("Calcium")
            if ca > 10.2:
                is_present = True
                evidence.append(f"Calcium {ca} mg/dL (>10.2)")

        elif name == "Hypomagnesemia":
            mg = get_num("Magnesium")
            if mg < 1.5:
                is_present = True
                evidence.append(f"Magnesium {mg} mg/dL (<1.5)")

        elif name == "Hypermagnesemia":
            mg = get_num("Magnesium")
            if mg > 2.5:
                is_present = True
                evidence.append(f"Magnesium {mg} mg/dL (>2.5)")

        elif name == "Hypophosphatemia":
            phos = get_num("Phosphate")
            if phos < 2.5:
                is_present = True
                evidence.append(f"Phosphate {phos} mg/dL (<2.5)")

        elif name == "Hyperphosphatemia":
            phos = get_num("Phosphate")
            if phos > 4.5:
                is_present = True
                evidence.append(f"Phosphate {phos} mg/dL (>4.5)")

        elif name == "Metabolic acidosis":
            ph = get_num("pH")
            hco3 = get_num("HCO3")
            if ph < 7.35 and hco3 < 22:
                is_present = True
                evidence.append(f"pH {ph}, HCO3 {hco3} mmol/L")

        elif name == "Metabolic alkalosis":
            ph = get_num("pH")
            hco3 = get_num("HCO3")
            if ph > 7.45 and hco3 > 26:
                is_present = True
                evidence.append(f"pH {ph}, HCO3 {hco3} mmol/L")

        elif name == "Respiratory acidosis":
            paco2 = get_num("PaCO2")
            ph = get_num("pH")
            if paco2 > 45 and ph < 7.35:
                is_present = True
                evidence.append(f"PaCO2 {paco2} mmHg, pH {ph}")

        elif name == "Respiratory alkalosis":
            paco2 = get_num("PaCO2")
            ph = get_num("pH")
            if paco2 < 35 and ph > 7.45:
                is_present = True
                evidence.append(f"PaCO2 {paco2} mmHg, pH {ph}")

        elif name == "High anion gap acidosis":
            ag = get_num("Anion_Gap")
            if ag > 16:
                is_present = True
                evidence.append(f"Anion Gap {ag} mmol/L (>16)")

        elif name == "SIADH" or name == "Syndrome of inappropriate antidiuretic hormone secretion":
            na = get_num("Sodium")
            usg = get_num("UrineSpecificGravity")
            if na < 135 and usg > 1.015:
                is_present = True
                evidence.append(f"Hyponatremia {na} mmol/L, high USG {usg}")

        # ---------------------------------------------------------------
        # 9. BONE AND MINERAL
        # ---------------------------------------------------------------
        elif name == "Primary hyperparathyroidism":
            ca = get_num("Calcium")
            pth = get_num("PTH")
            if ca > 10.2 and pth > 65:
                is_present = True
                evidence.append(f"Ca {ca} mg/dL, PTH {pth} pg/mL")

        elif name == "Secondary hyperparathyroidism":
            ca = get_num("Calcium")
            pth = get_num("PTH")
            if ca <= 9.0 and pth > 65:
                is_present = True
                evidence.append(f"Low‑normal Ca {ca}, elevated PTH {pth}")

        elif name == "Hypoparathyroidism":
            ca = get_num("Calcium")
            pth = get_num("PTH")
            if ca < 8.5 and pth < 15:
                is_present = True
                evidence.append(f"Hypocalcemia {ca} mg/dL, low PTH {pth}")

        elif name == "Osteomalacia":
            vitd = get_num("Vitamin_D")
            ca = get_num("Calcium")
            if vitd < 15 and ca < 8.5:
                is_present = True
                evidence.append(f"Vitamin D {vitd} ng/mL, Ca {ca} mg/dL")

        elif name == "Rickets":
            vitd = get_num("Vitamin_D")
            alp = get_num("ALP")
            if vitd < 15 and alp > 300:
                is_present = True
                evidence.append(f"Vitamin D {vitd}, ALP {alp}")

        elif name == "Paget disease of bone":
            alp = get_num("ALP")
            ca = get_num("Calcium")
            if alp > 200 and ca <= 10.2:
                is_present = True
                evidence.append(f"ALP {alp} U/L, normal Ca {ca}")

        # ---------------------------------------------------------------
        # 10. CARDIAC BIOMARKERS
        # ---------------------------------------------------------------
        elif name == "Acute myocardial infarction":
            trop = get_num("Troponin")
            ck_mb = get_num("CK_MB")
            if trop > 0.04 and ck_mb > 5.0:
                is_present = True
                evidence.append(f"Troponin {trop} ng/mL, CK‑MB {ck_mb} ng/mL")

        elif name == "Heart failure":
            bnp = get_num("BNP")
            if bnp > 100:
                is_present = True
                evidence.append(f"BNP {bnp} pg/mL (>100)")

        elif name == "Acute decompensated heart failure":
            bnp = get_num("BNP")
            na = get_num("Sodium")
            if bnp > 400 and na < 135:
                is_present = True
                evidence.append(f"BNP {bnp} pg/mL, Na {na} mmol/L")

        elif name == "Myocardial injury":
            trop = get_num("Troponin")
            if trop > 0.04:
                is_present = True
                evidence.append(f"Troponin {trop} ng/mL (>0.04)")

        elif name == "Myocarditis":
            trop = get_num("Troponin")
            crp = get_num("CRP")
            esr = get_num("ESR")
            if trop > 0.04 and crp > 10.0 and esr > 20:
                is_present = True
                evidence.append(f"Trop {trop}, CRP {crp}, ESR {esr}")

        elif name == "Cardiorenal syndrome":
            bnp = get_num("BNP")
            cr = get_num("Creatinine")
            bun = get_num("BUN")
            if bnp > 100 and cr > 1.3 and bun > 20:
                is_present = True
                evidence.append(f"BNP {bnp}, Cr {cr}, BUN {bun}")

        elif name == "Stress cardiomyopathy":
            trop = get_num("Troponin")
            bnp = get_num("BNP")
            if trop > 0.04 and bnp > 200:
                is_present = True
                evidence.append(f"Mild Trop {trop}, high BNP {bnp}")

        # ---------------------------------------------------------------
        # 11. COAGULATION
        # ---------------------------------------------------------------
        elif name == "Disseminated intravascular coagulation":
            plt = get_num("Platelet")
            inr = get_num("INR")
            fib = get_num("Fibrinogen")
            dd = get_num("D_Dimer")
            if plt < 100 and inr > 1.5 and fib < 150 and dd > 2.0:
                is_present = True
                evidence.append(f"Plt {plt}, INR {inr}, Fib {fib}, D‑dimer {dd}")

        elif name == "Venous thromboembolism" or name == "Deep vein thrombosis":
            dd = get_num("D_Dimer")
            if dd > 0.5:
                is_present = True
                evidence.append(f"D‑dimer {dd} µg/mL (>0.5)")

        elif name == "Pulmonary embolism":
            dd = get_num("D_Dimer")
            trop = get_num("Troponin")
            if dd > 0.5 and trop > 0.04:
                is_present = True
                evidence.append(f"D‑dimer {dd}, Troponin {trop}")

        elif name == "Liver-related coagulopathy":
            inr = get_num("INR")
            plt = get_num("Platelet")
            alt = get_num("ALT")
            if inr > 1.5 and plt < 150 and alt > 50:
                is_present = True
                evidence.append(f"INR {inr}, Plt {plt}, ALT {alt}")

        elif name == "Vitamin K deficiency coagulopathy":
            inr = get_num("INR")
            pt = get_num("PT")
            if inr > 1.5 and pt > 17:
                is_present = True
                evidence.append(f"INR {inr}, PT {pt} sec")

        elif name == "Consumptive coagulopathy":
            plt = get_num("Platelet")
            fib = get_num("Fibrinogen")
            dd = get_num("D_Dimer")
            if plt < 150 and fib < 150 and dd > 2.0:
                is_present = True
                evidence.append(f"Plt {plt}, Fib {fib}, D‑dimer {dd}")

        elif name == "Hypercoagulable state":
            plt = get_num("Platelet")
            dd = get_num("D_Dimer")
            if plt > 450 and dd > 0.5:
                is_present = True
                evidence.append(f"Plt {plt}, D‑dimer {dd}")

        # ---------------------------------------------------------------
        # 12. INFLAMMATORY
        # ---------------------------------------------------------------
        elif name == "Acute bacterial infection":
            wbc = get_num("WBC")
            neut = get_num("NeutrophilsPercent")
            crp = get_num("CRP")
            if wbc > 11.0 and neut > 75 and crp > 10.0:
                is_present = True
                evidence.append(f"WBC {wbc}, Neut {neut}%, CRP {crp}")

        elif name == "Viral infection":
            wbc = get_num("WBC")
            lymph = get_num("LymphocytesPercent")
            if wbc <= 11.0 and lymph > 45:
                is_present = True
                evidence.append(f"WBC {wbc}, Lymph {lymph}%")

        elif name == "Sepsis":
            wbc = get_num("WBC")
            crp = get_num("CRP")
            lactate = get_num("Lactate")
            plt = get_num("Platelet")
            if lactate > 2.0 and crp > 10 and (wbc > 11 or wbc < 4) and plt < 100:
                is_present = True
                evidence.append(f"Lactate {lactate}, CRP {crp}, WBC {wbc}, Plt {plt}")

        # ---------------------------------------------------------------
        # 13. AUTOIMMUNE AND RHEUMATOLOGY
        # ---------------------------------------------------------------
        elif name == "Systemic lupus erythematosus":
            ana = get_num("ANA")
            dsdna = get_num("Anti_dsDNA")
            if ana > 1.0 and dsdna > 30:
                is_present = True
                evidence.append(f"ANA {ana}, anti‑dsDNA {dsdna} IU/mL")

        elif name == "Rheumatoid arthritis":
            rf = get_num("RF") or get_num("Anti_CCP", 0)
            crp = get_num("CRP")
            if rf > 15 and crp > 5.0:
                is_present = True
                evidence.append(f"RF/anti‑CCP positive, CRP {crp}")

        elif name == "Sjögren syndrome":
            ana = get_num("ANA")
            ena = get_str("ENA_Panel")
            if ana > 1.0 and is_positive(ena):
                is_present = True
                evidence.append(f"ANA {ana}, ENA positive")

        elif name == "Systemic sclerosis":
            ana = get_num("ANA")
            ena = get_str("ENA_Panel")
            if ana > 1.0 and is_positive(ena):
                is_present = True
                evidence.append(f"ANA {ana}, ENA positive (scleroderma pattern)")

        elif name == "Mixed connective tissue disease":
            ana = get_num("ANA")
            ena = get_str("ENA_Panel")
            if ana > 1.0 and is_positive(ena):
                is_present = True
                evidence.append(f"ANA {ana}, ENA positive (U1‑RNP)")

        elif name == "Antiphospholipid syndrome":
            la = get_str("Lupus_Anticoagulant")
            acl = get_num("Anti_Cardiolipin")
            ab2 = get_num("Anti_Beta2GP1")
            if (is_positive(la) or acl > 40 or ab2 > 20):
                is_present = True
                evidence.append("Positive antiphospholipid antibodies")

        elif name == "ANCA-associated vasculitis":
            anca = get_str("ANCA")
            crp = get_num("CRP")
            urbc = get_num("UrineRBC")
            if is_positive(anca) and crp > 15 and urbc > 3:
                is_present = True
                evidence.append(f"ANCA positive, CRP {crp}, RBC {urbc}/hpf")

        elif name == "Dermatomyositis":
            ck = get_num("CK")
            ast = get_num("AST")
            alt = get_num("ALT")
            ana = get_num("ANA")
            crp = get_num("CRP")
            if ck > 1000 and ana > 1.0 and crp > 5.0:
                is_present = True
                evidence.append(f"CK {ck}, AST {ast}, ALT {alt}, ANA {ana}, CRP {crp}")

        elif name == "Polymyositis":
            ck = get_num("CK")
            ast = get_num("AST")
            alt = get_num("ALT")
            crp = get_num("CRP")
            if ck > 500 and crp > 5.0:
                is_present = True
                evidence.append(f"CK {ck}, AST {ast}, ALT {alt}, CRP {crp}")

        elif name == "Undifferentiated connective tissue disease":
            ana = get_num("ANA")
            crp = get_num("CRP")
            if ana > 1.0 and crp > 5.0:
                is_present = True
                evidence.append(f"ANA {ana}, CRP {crp}")

        elif name == "Autoimmune thyroid disease":
            anti_tpo = get_num("Anti_TPO")
            tsh = get_num("TSH")
            if anti_tpo > 34 and (tsh > 4.0 or tsh < 0.4):
                is_present = True
                evidence.append(f"Anti‑TPO {anti_tpo}, TSH {tsh}")

        elif name == "Autoimmune liver disease":
            ana = get_num("ANA")
            alt = get_num("ALT")
            if ana > 1.0 and alt > 50:
                is_present = True
                evidence.append(f"ANA {ana}, ALT {alt}")

        # ---------------------------------------------------------------
        # 14. PANCREATIC
        # ---------------------------------------------------------------
        elif name == "Acute pancreatitis":
            lip = get_num("Lipase") or get_num("Amylase", 0)
            if lip > 180:
                is_present = True
                evidence.append(f"Lipase/Amylase {lip} U/L (>>3× ULN)")

        elif name == "Chronic pancreatitis":
            lip = get_num("Lipase")
            amy = get_num("Amylase")
            if lip and lip < 10:
                is_present = True
                evidence.append(f"Low lipase {lip} U/L, possible exocrine insufficiency")

        elif name == "Pancreatic exocrine dysfunction":
            lip = get_num("Lipase")
            if lip and lip < 10:
                is_present = True
                evidence.append(f"Serum lipase {lip} U/L (low) – fecal elastase recommended")

        elif name == "Pancreaticobiliary inflammation":
            amy = get_num("Amylase")
            alt = get_num("ALT")
            alp = get_num("ALP")
            if amy > 100 and alt > 50 and alp > 150:
                is_present = True
                evidence.append(f"Amylase {amy}, ALT {alt}, ALP {alp}")

        # ---------------------------------------------------------------
        # 15. URINALYSIS
        # ---------------------------------------------------------------
        elif name == "Urinary tract infection":
            nit = get_str("UrineNitrite")
            le = get_str("UrineLeukocyteEsterase")
            uwbc = get_num("UrineWBC")
            if (is_positive(nit) or is_positive(le)) and uwbc > 5:
                is_present = True
                evidence.append(f"Nitrite {nit}, LE {le}, WBC {uwbc}/hpf")

        elif name == "Hematuria syndrome":
            ublood = get_str("UrineBlood")
            urbc = get_num("UrineRBC")
            if is_positive(ublood) and urbc > 3:
                is_present = True
                evidence.append(f"Blood {ublood}, RBC {urbc}/hpf")

        elif name == "Pyuria":
            uwbc = get_num("UrineWBC")
            if uwbc > 5:
                is_present = True
                evidence.append(f"Urine WBC {uwbc}/hpf (>5)")

        elif name == "Crystalluria":
            uph = get_num("UrinepH")
            if uph and (uph < 5.5 or uph > 7.5):
                is_present = True
                evidence.append(f"Urine pH {uph} (crystal‑prone)")

        elif name == "Glucosuria":
            uglu = get_str("UrineGlucoseQualitative")
            fbs = get_num("FBS")
            if is_positive(uglu) and fbs > 180:
                is_present = True
                evidence.append(f"Glucose in urine, FBS {fbs} mg/dL")

        elif name == "Ketonuria":
            ket = get_str("UrineKetones")
            if is_positive(ket):
                is_present = True
                evidence.append(f"Urine ketones {ket}")

        elif name == "Tubular injury pattern":
            usg = get_num("UrineSpecificGravity")
            cr = get_num("Creatinine")
            if usg and 1.008 <= usg <= 1.012 and cr > 1.3:
                is_present = True
                evidence.append(f"Fixed USG {usg}, Creatinine {cr}")

        elif name == "Cast-associated renal disease":
            upro = get_str("UrineProteinQualitative")
            cr = get_num("Creatinine")
            if is_positive(upro) and cr > 1.3:
                is_present = True
                evidence.append(f"Protein casts, Creatinine {cr}")

        # ---------------------------------------------------------------
        # 16. ADDITIONAL HIGH-YIELD DISEASES
        # ---------------------------------------------------------------
        elif name == "Gout":
            uric = get_num("Uric_Acid")
            limit = 7.2 if gender == "male" else 6.0
            if uric > limit:
                is_present = True
                evidence.append(f"Uric acid {uric} mg/dL (> {limit})")

        elif name == "Hyperuricemia":
            uric = get_num("Uric_Acid")
            limit = 7.2 if gender == "male" else 6.0
            if uric > limit:
                is_present = True
                evidence.append(f"Uric acid {uric} mg/dL")

        elif name == "Pseudohyperkalemia":
            k = get_num("Potassium")
            plt = get_num("Platelet")
            if k > 5.0 and plt > 500:
                is_present = True
                evidence.append(f"K {k} mmol/L with extreme thrombocytosis ({plt})")

        elif name == "Pseudohyponatremia":
            na = get_num("Sodium")
            tg = get_num("Triglycerides")
            if na < 135 and tg > 1000:
                is_present = True
                evidence.append(f"Na {na} mmol/L, TG {tg} mg/dL")

        elif name == "Factitious hypoglycemia":
            fbs = get_num("FBS")
            insulin = get_num("Insulin")
            if fbs < 55 and insulin > 10:
                is_present = True
                evidence.append(f"Glucose {fbs} mg/dL, very high Insulin {insulin} µIU/mL")

        elif name == "Rhabdomyolysis":
            ck = get_num("CK")
            cr = get_num("Creatinine")
            if ck > 1000 and cr > 1.3:
                is_present = True
                evidence.append(f"CK {ck} U/L, Creatinine {cr} mg/dL")

        elif name == "Tumor lysis syndrome":
            uric = get_num("Uric_Acid")
            phos = get_num("Phosphate")
            k = get_num("Potassium")
            ca = get_num("Calcium")
            if uric > 8.0 and phos > 4.5 and k > 6.0 and ca < 7.0:
                is_present = True
                evidence.append(f"UA {uric}, Phos {phos}, K {k}, Ca {ca}")

        # ---------------------------------------------------------------
        # HEURISTIC FALLBACK
        # ---------------------------------------------------------------
        if not is_present and name not in EXPLICIT_RULE_DISEASES: 
            entered_count = 0
            abnormal_count = 0
            temp_evidence = []

            for feat in required:
                val_num = get_num(feat)
                val_str = get_str(feat)
                if val_num is None and not val_str:
                    continue

                entered_count += 1
                f_data = FEATURE_REGISTRY.get(feat, {})
                ref_list = f_data.get("referenceRanges", [])
                matched_ref = next((r for r in ref_list if r.get("gender") == gender), ref_list[0] if ref_list else None)

                is_abnormal = False
                if matched_ref and "range" in matched_ref and val_num is not None:
                    low, high = matched_ref["range"]
                    if val_num < low or val_num > high:
                        is_abnormal = True
                        direction = "Low" if val_num < low else "High"
                        temp_evidence.append(f"{direction} {f_data.get('displayEn', feat)}: {val_num} {f_data.get('unit', '')} (Ref: {low}‑{high})")
                else:
                    if val_str and is_positive(val_str):
                        is_abnormal = True
                        temp_evidence.append(f"Positive {f_data.get('displayEn', feat)}: '{val_str}'")

                if is_abnormal:
                    abnormal_count += 1

            if entered_count > 0 and abnormal_count >= entered_count * 0.8:
                is_present = True
                evidence.extend(temp_evidence)

        if is_present:
            results.append({
                "diseaseKey": name.replace(" ", "_").replace("-", "_").replace("(", "").replace(")", ""),
                "nameEn": name,
                "icd10": disease["icd10"],
                "status": "Present",
                "evidence": evidence,
                "guideline": disease["guideline"],
                "noteEn": disease["criteria"],
                "confirmRequired": False
            })

    return results