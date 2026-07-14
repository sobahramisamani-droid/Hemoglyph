# disease_guidelines.py

DISEASE_GUIDELINES = [
    # --- CBC AND DIFFERENTIAL ---
    {
        "category": "CBC And Differential",
        "name": "Iron deficiency anemia",
        "icd10": "D50.9",
        "required_features": ["Hb", "MCV", "Ferritin"],
        "guideline": "WHO 2020 Guidelines",
        "criteria": "Hemoglobin < 13.5 g/dL (males) or < 12.0 g/dL (females), MCV < 80 fL, and Serum Ferritin < 30 ng/mL."
    },
    {
        "category": "CBC And Differential",
        "name": "Anemia of chronic disease",
        "icd10": "D63.8",
        "required_features": ["Hb", "MCV", "Ferritin", "CRP"],
        "guideline": "WHO / ASH Guidelines",
        "criteria": "Hemoglobin below normal reference range, normal or elevated MCV (80-100 fL), normal or elevated Serum Ferritin (>= 100 ng/mL), and elevated inflammatory markers (CRP > 5.0 mg/L)."
    },
    {
        "category": "CBC And Differential",
        "name": "Thalassemia trait",
        "icd10": "D56.3",
        "required_features": ["Hb", "MCV", "RBC", "MCH"],
        "guideline": "ACOG Guidelines",
        "criteria": "Mild microcytic anemia (MCV < 75 fL) with relatively high or borderline-high RBC count (RBC >= 5.0 x10^12/L) and low MCH (< 25 pg). Mentzer index (MCV/RBC) < 13."
    },
    {
        "category": "CBC And Differential",
        "name": "Sideroblastic anemia",
        "icd10": "D64.3",
        "required_features": ["Hb", "MCV", "SerumIron", "Ferritin"],
        "guideline": "ASH Guidelines",
        "criteria": "Microcytic or normocytic anemia with high Serum Iron (> 150 µg/dL) and elevated Ferritin (> 200 ng/mL), indicating impaired iron utilization into hemoglobin synthesis."
    },
    {
        "category": "CBC And Differential",
        "name": "Hemolytic anemia",
        "icd10": "D58.9",
        "required_features": ["Hb", "Total_Bilirubin", "Indirect_Bilirubin", "LDH", "Haptoglobin"],
        "guideline": "ASH Guidelines",
        "criteria": "Anemia with elevated indirect bilirubin (> 0.8 mg/dL), LDH > 1.5× ULN, and low haptoglobin (< 25 mg/dL). Reticulocytosis confirms marrow compensation."
    },
    {
        "category": "CBC And Differential",
        "name": "Aplastic anemia",
        "icd10": "D61.9",
        "required_features": ["Hb", "WBC", "Platelet"],
        "guideline": "WHO Guidelines",
        "criteria": "Pancytopenia resulting from bone marrow failure: low Hemoglobin, leukopenia (WBC < 3.5 x10^9/L), and thrombocytopenia (Platelets < 100 x10^9/L)."
    },
    {
        "category": "CBC And Differential",
        "name": "Acute blood loss anemia",
        "icd10": "D62",
        "required_features": ["Hb", "MCV", "RBC"],
        "guideline": "WHO Guidelines",
        "criteria": "Compatible with acute blood loss pattern. Clinical history of bleeding required."
    },
    {
        "category": "CBC And Differential",
        "name": "Megaloblastic anemia",
        "icd10": "D51.9",
        "required_features": ["Hb", "MCV", "VitaminB12", "Folate"],
        "guideline": "WHO / ASH Guidelines",
        "criteria": "Macrocytic anemia (MCV > 100 fL) caused by severe Vitamin B12 (< 200 pg/mL) or Folate (< 2.0 ng/mL) deficiencies, showing hypersegmented neutrophils."
    },
    {
        "category": "CBC And Differential",
        "name": "Vitamin B12 deficiency anemia",
        "icd10": "D51.9",
        "required_features": ["Hb", "MCV", "VitaminB12"],
        "guideline": "ASH Guidelines",
        "criteria": "Anemia with macrocytosis (MCV > 100 fL) directly attributable to Serum Vitamin B12 levels below 200 pg/mL."
    },
    {
        "category": "CBC And Differential",
        "name": "Folate deficiency anemia",
        "icd10": "D52.9",
        "required_features": ["Hb", "MCV", "Folate"],
        "guideline": "ASH Guidelines",
        "criteria": "Anemia with macrocytosis (MCV > 100 fL) with Serum Folate < 2.0 ng/mL (or RBC Folate < 140 ng/mL), confirming tissue folate deficiency."
    },
    {
        "category": "CBC And Differential",
        "name": "Autoimmune hemolytic anemia",
        "icd10": "D59.1",
        "required_features": ["Hb", "Indirect_Bilirubin", "DAT"],
        "guideline": "AABB / ASH Guidelines",
        "criteria": "Hemolytic anemia (low Hb, elevated indirect bilirubin) with positive Direct Antiglobulin Test (Coombs) confirming antibody-mediated red cell destruction."
    },
    {
        "category": "CBC And Differential",
        "name": "Hereditary spherocytosis",
        "icd10": "D58.0",
        "required_features": ["Hb", "MCV", "MCHC", "Indirect_Bilirubin"],
        "guideline": "British J. Haematology",
        "criteria": "Anemia with typical micro- or normocytic MCV, elevated MCHC (> 36 g/dL, which is highly specific for spherocytosis) and indirect hyperbilirubinemia (> 0.8 mg/dL)."
    },
    {
        "category": "CBC And Differential",
        "name": "G6PD deficiency",
        "icd10": "D55.0",
        "required_features": ["Hb", "Indirect_Bilirubin", "G6PD_Activity"],
        "guideline": "WHO Guidelines",
        "criteria": "Acute hemolysis (low Hb, elevated indirect bilirubin) with markedly reduced G6PD enzyme activity (< 10% of normal) during steady state. During crisis, reticulocytes may show normal activity; repeat testing may be needed."
    },
    {
        "category": "CBC And Differential",
        "name": "Sickle cell disease",
        "icd10": "D57.1",
        "required_features": ["Hb", "MCV", "RBC"],
        "guideline": "NHLBI Guidelines",
        "criteria": "Laboratory findings compatible with sickle cell disease; confirmation requires hemoglobin electrophoresis."
    },
    {
        "category": "CBC And Differential",
        "name": "Myelodysplastic syndrome",
        "icd10": "D46.9",
        "required_features": ["Hb", "WBC", "Platelet", "MCV"],
        "guideline": "NCCN Guidelines",
        "criteria": "Bicytopenia or pancytopenia (e.g., low Hb, Platelets, or WBC) accompanied by macrocytosis (MCV > 100 fL) in an older adult."
    },
    {
        "category": "CBC And Differential",
        "name": "Leukopenia",
        "icd10": "D72.81",
        "required_features": ["WBC"],
        "guideline": "Hematology Consensus",
        "criteria": "Decreased white blood cell count (WBC < 4.0 x10^9/L), predisposing to infections."
    },
    {
        "category": "CBC And Differential",
        "name": "Neutropenia",
        "icd10": "D70.9",
        "required_features": ["ANC"],
        "guideline": "IDSA Guidelines",
        "criteria": "Absolute Neutrophil Count (ANC) below 1.5 x10^9/L, representing high risk of bacterial infections."
    },
    {
        "category": "CBC And Differential",
        "name": "Lymphocytosis",
        "icd10": "D72.8",
        "required_features": ["ALC"],
        "guideline": "Hematology Consensus",
        "criteria": "Absolute Lymphocyte Count (ALC) greater than 4.0 x10^9/L, frequently a reactive response to viral infection."
    },
    {
        "category": "CBC And Differential",
        "name": "Eosinophilia",
        "icd10": "D72.1",
        "required_features": ["EosinophilsPercent"],
        "guideline": "Hematology Consensus",
        "criteria": "Eosinophils greater than 6% of total WBC, indicating possible allergic, parasitic, or autoimmune etiology."
    },
    {
        "category": "CBC And Differential",
        "name": "Basophilia",
        "icd10": "D72.824",
        "required_features": ["BasophilsPercent"],
        "guideline": "Hematology Consensus",
        "criteria": "Basophils exceeding 1.5% of total WBC, often associated with myeloproliferative disorders."
    },
    {
        "category": "CBC And Differential",
        "name": "Monocytosis",
        "icd10": "D72.8",
        "required_features": ["MonocytesPercent"],
        "guideline": "Hematology Consensus",
        "criteria": "Monocytes exceeding 10% of total WBC, observed in chronic infections or inflammatory states."
    },
    {
        "category": "CBC And Differential",
        "name": "Thrombocytopenia",
        "icd10": "D69.6",
        "required_features": ["Platelet"],
        "guideline": "ASH Guidelines",
        "criteria": "Platelet count below 150 x10^9/L, escalating bleeding or bruising risks."
    },
    {
        "category": "CBC And Differential",
        "name": "Immune thrombocytopenia",
        "icd10": "D69.3",
        "required_features": ["Platelet", "Hb", "WBC"],
        "guideline": "ASH 2019 Guidelines",
        "criteria": "Isolated thrombocytopenia (Platelets < 100 x10^9/L) without anemia or leukopenia, and no other clear secondary causes."
    },
    {
        "category": "CBC And Differential",
        "name": "Thrombocytosis",
        "icd10": "D75.8",
        "required_features": ["Platelet"],
        "guideline": "ASH Guidelines",
        "criteria": "Platelet count above 450 x10^9/L, suggesting reactive thrombocytosis or primary thrombocythemia."
    },
    {
        "category": "CBC And Differential",
        "name": "Polycythemia vera",
        "icd10": "D45",
        "required_features": ["Hb", "Hct", "RBC"],
        "guideline": "WHO 2016 Guidelines",
        "criteria": "Sustained high Hemoglobin (> 18.5 g/dL in males, > 16.5 in females) and Hct with RBC elevation. Highly suggestive of primary polycythemia; requires JAK2 mutation screening."
    },

    # --- IRON, VITAMIN, AND NUTRITION ---
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Iron deficiency without anemia",
        "icd10": "E61.1",
        "required_features": ["Ferritin", "Hb"],
        "guideline": "WHO 2020 Guidelines",
        "criteria": "Depleted iron stores (Ferritin < 30 ng/mL) prior to the development of microcytic anemia (Hb remains within normal reference range)."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Functional iron deficiency",
        "icd10": "E61.1",
        "required_features": ["Ferritin", "Transferrin_Sat", "CRP"],
        "guideline": "ASH Guidelines",
        "criteria": "Normal or elevated Ferritin acting as an acute-phase reactant, coupled with low Transferrin Saturation (< 20%) and high CRP (> 5.0 mg/L) in inflammatory chronic diseases."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Iron overload",
        "icd10": "E83.11",
        "required_features": ["Ferritin", "Transferrin_Sat"],
        "guideline": "EASL Guidelines",
        "criteria": "Markedly elevated Ferritin (> 300 ng/mL in males, > 200 in females) along with Transferrin Saturation > 45%."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Hereditary hemochromatosis",
        "icd10": "E83.110",
        "required_features": ["Ferritin", "Transferrin_Sat"],
        "guideline": "AASLD Guidelines",
        "criteria": "Persistent Transferrin Saturation > 55% with marked Ferritin overload. Suspected genetic hemochromatosis; HFE gene analysis is recommended."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Vitamin B12 deficiency",
        "icd10": "E53.8",
        "required_features": ["VitaminB12"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Vitamin B12 levels below 200 pg/mL, indicating critical cellular deficiency with or without hematologic signs."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Folate deficiency",
        "icd10": "E53.8",
        "required_features": ["Folate"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Folate < 2.0 ng/mL, indicating true cellular folate depletion. RBC Folate (< 140 ng/mL) provides a longer-term assessment."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Copper deficiency",
        "icd10": "E61.0",
        "required_features": ["Hb", "ANC"],      # ← now includes ANC
        "guideline": "Hematology Consensus",
        "criteria": "Presents as microcytic/normocytic anemia and neutropenia mimicking myelodysplasia, secondary to low copper cofactor stores."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Zinc deficiency",
        "icd10": "E60",
        "required_features": ["Zinc"],
        "guideline": "WHO Guidelines",
        "criteria": "Serum Zinc level below 60 µg/dL, resulting in dermatologic lesions, immunological delay, and slow healing."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Vitamin D deficiency",
        "icd10": "E55.9",
        "required_features": ["Vitamin_D"],
        "guideline": "Endocrine Society 2011",
        "criteria": "Serum 25-OH Vitamin D level below 20 ng/mL, requiring supplementation."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Vitamin K deficiency",
        "icd10": "E56.1",
        "required_features": ["INR", "PT"],
        "guideline": "Coagulation Consensus",
        "criteria": "Prolonged PT and elevated INR (> 1.2) in the absence of warfarin therapy, correcting rapidly upon administration of Vitamin K."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Protein-energy malnutrition",
        "icd10": "E46",
        "required_features": ["Albumin", "Prealbumin", "Total_Protein"],
        "guideline": "ASPEN / ESPEN Guidelines",
        "criteria": "Co-existent low Albumin (< 3.5 g/dL), low Prealbumin (< 15 mg/dL), and low Total Protein (< 6.0 g/dL) representing systemic protein malnutrition."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Sarcopenia",
        "icd10": "M62.84",
        "required_features": ["Age", "Weight", "Height"],
        "guideline": "EWGSOP2 2019",
        "criteria": "Loss of skeletal muscle mass and strength, clinically supported by low BMI and clinical assessment."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Cachexia",
        "icd10": "R64",
        "required_features": ["Weight", "CRP", "Albumin"],
        "guideline": "International Cachexia Consensus",
        "criteria": "Unintentional weight loss > 5% over 6 months alongside systemic inflammatory response (CRP > 5.0) and hypoalbuminemia."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Refeeding syndrome",
        "icd10": "Y40.9",
        "required_features": ["Phosphate", "Potassium", "Magnesium"],
        "guideline": "ASPEN Refeeding Guidelines",
        "criteria": "Severe, abrupt hypophosphatemia, hypokalemia, and hypomagnesemia triggered by reinstitution of nutrition in chronically malnourished patients."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Chronic malnutrition",
        "icd10": "E44.0",
        "required_features": ["Albumin", "Prealbumin"],
        "guideline": "ASPEN / ESPEN Guidelines",
        "criteria": "Sustained hypoproteinemia and weight loss, characterized by low Prealbumin (< 10 mg/dL) reflecting long-term negative nitrogen balance."
    },

    # --- THYROID AND ENDOCRINE ---
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Primary hypothyroidism",
        "icd10": "E03.9",
        "required_features": ["TSH", "FreeT4"],
        "guideline": "ATA 2014 Guidelines",
        "criteria": "Elevated TSH (> 4.5 mIU/L) with concurrently low Free T4 (< 0.8 ng/dL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Subclinical hypothyroidism",
        "icd10": "E02",
        "required_features": ["TSH", "FreeT4"],
        "guideline": "ATA 2014 Guidelines",
        "criteria": "Elevated TSH (> 4.5 mIU/L) with entirely normal Free T4 levels (0.8 - 1.8 ng/dL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Secondary hypothyroidism",
        "icd10": "E23.0",
        "required_features": ["TSH", "FreeT4"],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Low or inappropriately normal TSH in the presence of low Free T4 (< 0.8 ng/dL), suggesting pituitary/hypothalamic dysfunction."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Hyperthyroidism",
        "icd10": "E05.9",
        "required_features": ["TSH", "FreeT4"],
        "guideline": "ATA 2016 Guidelines",
        "criteria": "Suppressed TSH (< 0.1 mIU/L) accompanied by elevated Free T4 (> 1.8 ng/dL) or Free T3."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Subclinical hyperthyroidism",
        "icd10": "E05.8",
        "required_features": ["TSH", "FreeT4"],
        "guideline": "ATA 2016 Guidelines",
        "criteria": "Suppressed TSH (< 0.4 mIU/L) in the presence of completely normal Free T4 levels (0.8 - 1.8 ng/dL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Graves disease",
        "icd10": "E05.0",
        "required_features": ["TSH", "FreeT4", "TRAb"],
        "guideline": "ATA 2016 Guidelines",
        "criteria": "Suppressed TSH and high Free T4 combined with elevated TSH Receptor Antibody (TRAb > 1.75 IU/L)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Hashimoto thyroiditis",
        "icd10": "E06.3",
        "required_features": ["TSH", "Anti_TPO"],
        "guideline": "ATA 2014 Guidelines",
        "criteria": "Primary or subclinical hypothyroidism associated with positive Anti-TPO Antibodies (> 34 IU/mL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Thyroiditis",
        "icd10": "E06.9",
        "required_features": ["TSH", "FreeT4", "CRP"],
        "guideline": "ATA Guidelines",
        "criteria": "Transient thyrotoxic phase followed by hypothyroid phase, accompanied by localized pain and highly elevated inflammatory markers (CRP)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Central adrenal insufficiency",
        "icd10": "E23.0",
        "required_features": ["Cortisol", "ACTH"],
        "guideline": "Endocrine Society 2016",
        "criteria": "Low morning Cortisol (< 5.0 µg/dL) with low or inappropriately normal ACTH levels (< 10 pg/mL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Primary adrenal insufficiency",
        "icd10": "E27.1",
        "required_features": ["Cortisol", "ACTH", "Sodium", "Potassium"],
        "guideline": "Endocrine Society 2016",
        "criteria": "Extremely low morning Cortisol (< 5.0 µg/dL) along with significantly elevated ACTH (> 60 pg/mL), frequently accompanied by hyponatremia and hyperkalemia."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Cushing syndrome",
        "icd10": "E24.9",
        "required_features": ["Cortisol", "ACTH"],
        "guideline": "Endocrine Society 2008",
        "criteria": "Significantly elevated morning Cortisol (> 25 µg/dL) with autonomous secretion patterns. Requires confirmation with 24-hour urine free cortisol or dexamethasone suppression test."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Hyperprolactinemia",
        "icd10": "E22.1",
        "required_features": ["Prolactin"],
        "guideline": "Endocrine Society 2011",
        "criteria": "Elevated Prolactin levels above normal thresholds (> 29 ng/mL in females, > 18 in males)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Acromegaly",
        "icd10": "E22.0",
        "required_features": ["IGF1"],
        "guideline": "AACE / Endocrine Society",
        "criteria": "Significantly elevated insulin-like growth factor-1 (IGF-1) above age-specific normal reference limits, confirmed with oral glucose tolerance test."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Growth hormone deficiency",
        "icd10": "E23.0",
        "required_features": ["IGF1"],
        "guideline": "AACE Guidelines",
        "criteria": "Markedly low IGF-1 levels coupled with pituitary structural lesions or failing stimulus assays."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Hypogonadism",
        "icd10": "E29.1",
        "required_features": ["Testosterone", "LH", "FSH"],
        "guideline": "Endocrine Society 2018",
        "criteria": "Total morning Testosterone < 300 ng/dL in males alongside symptoms, with high LH/FSH (primary) or low/normal LH/FSH (secondary/hypogonadotropic)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Polycystic ovary syndrome",
        "icd10": "E28.2",
        "required_features": ["LH", "FSH", "Testosterone"],
        "guideline": "Rotterdam 2003 Criteria",
        "criteria": "Characterized by LH/FSH ratio > 2:1, mild to moderate total testosterone elevation, oligomenorrhea, and clinical hyperandrogenism."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Menopause-related endocrine dysfunction",
        "icd10": "N95.1",
        "required_features": ["FSH", "Estradiol"],
        "guideline": "NAMS Guidelines",
        "criteria": "Sustained elevation of Serum FSH > 30 IU/L alongside low Estradiol (< 30 pg/mL) in females with appropriate clinical context."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Congenital adrenal hyperplasia",
        "icd10": "E25.0",
        "required_features": ["Cortisol"],
        "guideline": "Endocrine Society 2018",
        "criteria": "Enzymatic blockade leading to hypocortisolemia, elevated 17-OHP, and androgen excess."
    },

    # --- DIABETES AND METABOLIC ---
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Prediabetes",
        "icd10": "R73.03",
        "required_features": ["FBS", "HbA1c"],
        "guideline": "ADA 2024 Guidelines",
        "criteria": "Fasting blood sugar (FBS) between 100 and 125 mg/dL, or HbA1c between 5.7% and 6.4%."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Type 2 diabetes mellitus",
        "icd10": "E11.9",
        "required_features": ["FBS", "HbA1c"],
        "guideline": "ADA 2024 Guidelines",
        "criteria": "Fasting blood sugar (FBS) >= 126 mg/dL, or HbA1c >= 6.5%, or random glucose >= 200 mg/dL with symptoms."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Type 1 diabetes mellitus",
        "icd10": "E10.9",
        "required_features": ["FBS", "HbA1c", "Insulin"],
        "guideline": "ADA 2024 Guidelines",
        "criteria": "Severe hyperglycemia with extremely low or undetectable fasting Insulin and C-peptide levels, often accompanied by positive autoantibodies."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Gestational diabetes",
        "icd10": "O24.4",
        "required_features": ["FBS", "OGTT_2h"],
        "guideline": "ADA 2024 Guidelines",
        "criteria": "Diagnosed during pregnancy using a 75g oral glucose tolerance test showing fasting >= 92 mg/dL or 2h post-load >= 153 mg/dL."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Diabetic ketoacidosis",
        "icd10": "E11.10",
        "required_features": ["FBS", "HCO3", "pH", "UrineKetones"],
        "guideline": "ADA Guidelines",
        "criteria": "Blood glucose > 250 mg/dL, arterial pH < 7.30, serum bicarbonate < 18 mmol/L, and moderate to strong positive urine/serum ketones."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Hyperosmolar hyperglycemic state",
        "icd10": "E11.00",
        "required_features": ["FBS", "pH", "HCO3"],
        "guideline": "ADA Guidelines",
        "criteria": "Severe hyperglycemia (Glucose > 600 mg/dL), high serum osmolality (> 320 mOsm/kg), minimal ketosis, and normal pH (> 7.30) / HCO3 (> 15 mmol/L)."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Insulin resistance syndrome",
        "icd10": "E88.81",
        "required_features": ["FBS", "Insulin", "HOMA_IR"],
        "guideline": "AACE Guidelines",
        "criteria": "Fasting Insulin > 15 µIU/mL and HOMA-IR ratio > 2.5 in the presence of normal or borderline fasting glucose, demonstrating cellular resistance."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Metabolic syndrome",
        "icd10": "E88.81",
        "required_features": ["Waist", "Triglycerides", "HDL", "FBS", "Systolic_BP"],
        "guideline": "AHA / NHLBI 2009 Consensus",
        "criteria": "Diagnosed when >= 3 of: Waist circumference >= 102cm (males) or >= 88cm (females), Triglycerides >= 150 mg/dL, HDL < 40 mg/dL (males) or < 50 mg/dL (females), BP >= 130/85 mmHg, Fasting Glucose >= 100 mg/dL."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Reactive hypoglycemia",
        "icd10": "E16.2",
        "required_features": ["FBS"],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Whipple triad: symptomatic blood glucose drops < 55 mg/dL occurring 2-5 hours post-prandially, resolving rapidly upon carbohydrate intake."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Fasting hypoglycemia",
        "icd10": "E16.2",
        "required_features": ["FBS", "Insulin"],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Symptomatic fasting blood glucose < 55 mg/dL with inappropriately elevated serum insulin (> 3.0 µIU/mL) suggesting hyperinsulinemic hypoglycemia or insulinoma."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Dyslipidemia of diabetes",
        "icd10": "E11.8",
        "required_features": ["HbA1c", "Triglycerides", "HDL"],
        "guideline": "ADA / ACC Guidelines",
        "criteria": "Diabetic patients with characteristically high Triglycerides (> 150 mg/dL), low HDL-C (< 40 mg/dL in males, < 50 mg/dL in females), and dense LDL particles."
    },

    # --- LIPID PANELS ---
    {
        "category": "Lipid Panels",
        "name": "Hypercholesterolemia",
        "icd10": "E78.0",
        "required_features": ["Total_Cholesterol"],
        "guideline": "NCEP ATP III Guidelines",
        "criteria": "Total Serum Cholesterol >= 200 mg/dL, denoting elevated hyperlipidemic cardiovascular risk."
    },
    {
        "category": "Lipid Panels",
        "name": "Hypertriglyceridemia",
        "icd10": "E78.1",
        "required_features": ["Triglycerides"],
        "guideline": "NCEP ATP III Guidelines",
        "criteria": "Fasting Serum Triglycerides exceeding 150 mg/dL, predisposing to metabolic syndrome."
    },
    {
        "category": "Lipid Panels",
        "name": "Mixed dyslipidemia",
        "icd10": "E78.2",
        "required_features": ["Total_Cholesterol", "Triglycerides"],
        "guideline": "NCEP ATP III Guidelines",
        "criteria": "Simultaneous elevation of both Total Cholesterol (>= 200 mg/dL) and Triglycerides (> 150 mg/dL)."
    },
    {
        "category": "Lipid Panels",
        "name": "Familial hypercholesterolemia",
        "icd10": "E78.01",
        "required_features": ["LDL"],
        "guideline": "Dutch Lipid Clinic Network",
        "criteria": "Primary severe LDL cholesterol elevation >= 190 mg/dL in adults, along with family history of premature CAD or tendon xanthomas."
    },
    {
        "category": "Lipid Panels",
        "name": "Familial combined hyperlipidemia",
        "icd10": "E78.2",
        "required_features": ["Total_Cholesterol", "Triglycerides", "LDL"],
        "guideline": "AHA Guidelines",
        "criteria": "Mixed hyperlipidemia showing elevated LDL and TG with variable phenotype expression in multiple first-degree relatives."
    },
    {
        "category": "Lipid Panels",
        "name": "Familial chylomicronemia syndrome",
        "icd10": "E78.3",
        "required_features": ["Triglycerides"],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Severe hypertriglyceridemia (often > 1000 mg/dL) starting in childhood, caused by LPL deficiency, presenting high risk for recurrent pancreatitis."
    },
    {
        "category": "Lipid Panels",
        "name": "Remnant cholesterol excess",
        "icd10": "E78.5",
        "required_features": ["Total_Cholesterol", "HDL", "LDL"],
        "guideline": "ACC / AHA Guidelines",
        "criteria": "Calculated Remnant Cholesterol (TC - HDL - LDL) >= 30 mg/dL, reflecting highly atherogenic remnant lipoprotein particles."
    },
    {
        "category": "Lipid Panels",
        "name": "Atherogenic dyslipidemia",
        "icd10": "E78.5",
        "required_features": ["Triglycerides", "HDL", "LDL"],
        "guideline": "ESC / EAS Guidelines",
        "criteria": "Highly atherogenic triad consisting of fasting Triglycerides > 150 mg/dL, low HDL (< 40 mg/dL in males, < 50 mg/dL in females), and elevated LDL particles."
    },
    {
        "category": "Lipid Panels",
        "name": "Severe hypertriglyceridemia",
        "icd10": "E78.1",
        "required_features": ["Triglycerides"],
        "guideline": "AHA 2021 Scientific Statement",
        "criteria": "Fasting Triglycerides >= 500 mg/dL, creating an acute and significant risk for pancreatic necroinflammation."
    },
    {
        "category": "Lipid Panels",
        "name": "Low HDL syndrome",
        "icd10": "E78.6",
        "required_features": ["HDL"],
        "guideline": "NCEP ATP III Guidelines",
        "criteria": "Isolated low HDL-C (< 40 mg/dL in males, < 50 mg/dL in females) despite normal total cholesterol and triglycerides, indicating lack of reverse cholesterol transport."
    },

    # --- RENAL FUNCTION AND URINE PROTEIN ---
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Chronic kidney disease",
        "icd10": "N18.9",
        "required_features": ["eGFR"],
        "guideline": "KDIGO 2024 Guidelines",
        "criteria": "Glomerular Filtration Rate (eGFR) below 60 mL/min/1.73m² persisting for 3 or more months, classified into stages G1-G5."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Diabetic kidney disease",
        "icd10": "E11.21",
        "required_features": ["FBS", "eGFR", "ACR"],
        "guideline": "ADA / KDIGO 2024 Consensus",
        "criteria": "Persistent micro- or macroalbuminuria (Urine ACR >= 30 mg/g) in patients with diabetes, accompanied by progressive decline in eGFR."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Hypertensive nephropathy",
        "icd10": "I12.9",
        "required_features": ["Systolic_BP", "eGFR", "ACR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Mild to moderate proteinuria (ACR < 300 mg/g) and slowly declining eGFR in a patient with a long-standing history of arterial hypertension."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Acute kidney injury",
        "icd10": "N17.9",
        "required_features": ["Creatinine", "BUN"],
        "guideline": "KDIGO 2012 Guidelines",
        "criteria": "Abrupt decline in renal clearance: rise in Serum Creatinine by >= 0.3 mg/dL within 48h, or >= 1.5 times baseline within 7 days, or oliguria."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Glomerulonephritis",
        "icd10": "N05.9",
        "required_features": ["UrineBlood", "UrineWBC", "UrineRBC"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Hematuria (dysmorphic RBCs and RBC casts), pyuria, mild proteinuria, hypertension, and rapid loss of renal filtration function."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Nephrotic syndrome",
        "icd10": "N04.9",
        "required_features": ["UrineProtein24h", "Albumin"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Classic triad of: heavy proteinuria (Urine Protein > 3.5 g/24h or PCR > 3000 mg/g), profound hypoalbuminemia (< 3.0 g/dL), generalized edema, and hyperlipidemia."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Nephritic syndrome",
        "icd10": "N00.9",
        "required_features": ["UrineBlood", "eGFR", "Systolic_BP"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Glomerular inflammation presenting with gross hematuria, oliguria, hypertension, mild to moderate edema, and mild proteinuria."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "IgA nephropathy",
        "icd10": "N02.8",
        "required_features": ["UrineBlood", "UrineRBC"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Recurrent macroscopic hematuria concurrent with upper respiratory tract infections (synpharyngitic), or persistent asymptomatic microscopic hematuria."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Lupus nephritis",
        "icd10": "M32.14",
        "required_features": ["ANA", "Anti_dsDNA", "UrineProteinQualitative", "ACR"],
        "guideline": "ACR Guidelines",
        "criteria": "Glomerular damage in systemic lupus erythematosus, diagnosed by persistent proteinuria > 0.5 g/day (ACR > 500 mg/g) or cellular casts."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Minimal change disease",
        "icd10": "N04.0",
        "required_features": ["UrineProtein24h", "Albumin"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Abrupt onset of full nephrotic syndrome in children or adults, showing normal glomerular architecture on light microscopy but podocyte effacement on electron microscopy."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Focal segmental glomerulosclerosis",
        "icd10": "N04.1",
        "required_features": ["UrineProtein24h", "Albumin", "eGFR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Severe nephrotic range proteinuria with high prevalence of hypertension, microhematuria, and progressive renal insufficiency."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Membranous nephropathy",
        "icd10": "N04.2",
        "required_features": ["UrineProtein24h", "Albumin"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Common cause of primary nephrotic syndrome in older adults, often positive for anti-PLA2R antibodies, showing subepithelial immune deposits."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Acute tubular necrosis",
        "icd10": "N17.0",
        "required_features": ["Creatinine", "BUN"],
        "guideline": "KDIGO Guidelines",
        "criteria": "AKI secondary to ischemia or nephrotoxins, characterized by muddy brown granular casts, high fractional excretion of sodium (FE_Na > 2%), and low urine specific gravity."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Interstitial nephritis",
        "icd10": "N10",
        "required_features": ["Creatinine", "UrineWBC"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Drug-induced hypersensitivity showing acute rise in creatinine, sterile pyuria with eosinophiluria, rash, and fever. Clinical correlation required."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Polycystic kidney disease",
        "icd10": "Q61.3",
        "required_features": ["eGFR", "Creatinine"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Renal dysfunction suspicious for ADPKD. Imaging confirmation required."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Albuminuria",
        "icd10": "R80.9",
        "required_features": ["ACR"],
        "guideline": "KDIGO 2024 Guidelines",
        "criteria": "Urine Albumin-to-Creatinine Ratio (ACR) >= 30 mg/g, representing glomerular barrier leakage and early cardiorenal marker."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Proteinuria",
        "icd10": "R80.9",
        "required_features": ["PCR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Urine Protein-to-Creatinine Ratio (PCR) >= 150 mg/g, indicating urinary protein excretion pathway loss."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Nephrotic-range proteinuria",
        "icd10": "N04.9",
        "required_features": ["UrineProtein24h"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Urinary total protein excretion exceeding 3500 mg per 24 hours, characteristic of severe glomerular disease."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "Uremia",
        "icd10": "N18.9",
        "required_features": ["BUN", "Creatinine"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Severe azotemia compatible with uremia; clinical symptoms should be assessed."
    },
    {
        "category": "Renal Function and Urine Protein Panels",
        "name": "End-stage kidney disease",
        "icd10": "N18.5",
        "required_features": ["eGFR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Glomerular filtration rate eGFR < 15 mL/min/1.73m² (CKD Stage G5), requiring renal replacement therapy (dialysis or transplantation)."
    },

    # --- LIVER FUNCTION AND HEPATITIS ---
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Acute viral hepatitis",
        "icd10": "B19.9",
        "required_features": ["ALT", "AST", "Total_Bilirubin"],
        "guideline": "AASLD Guidelines",
        "criteria": "Pattern compatible with acute hepatitis. Etiology requires viral serology."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Chronic hepatitis B",
        "icd10": "B18.1",
        "required_features": ["HBsAg"],
        "guideline": "AASLD 2018 Guidelines",
        "criteria": "Persistence of Hepatitis B Surface Antigen (HBsAg) in the serum for longer than 6 months."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Chronic hepatitis C",
        "icd10": "B18.2",
        "required_features": ["Anti_HCV"],
        "guideline": "AASLD / IDSA Guidelines",
        "criteria": "Anti-HCV positive; active infection requires HCV RNA confirmation."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Nonalcoholic fatty liver disease",
        "icd10": "K76.0",
        "required_features": ["ALT", "AST"],
        "guideline": "AASLD 2018 Guidelines",
        "criteria": "Mild transaminitis (ALT > AST) in a patient without substantial alcohol intake, representing hepatic steatosis."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "MASLD (Metabolic dysfunction-associated steatotic liver disease)",
        "icd10": "K76.0",
        "required_features": ["ALT", "AST", "FBS", "HDL"],
        "guideline": "AASLD / EASL 2023 Guidelines",
        "criteria": "Hepatic steatosis accompanied by at least one metabolic cardiometabolic risk factor (hyperglycemia, low HDL, hypertension)."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Nonalcoholic steatohepatitis",
        "icd10": "K75.81",
        "required_features": ["ALT", "AST", "CRP"],
        "guideline": "AASLD Guidelines",
        "criteria": "Hepatic steatosis accompanied by active necroinflammation, suspected when ALT/AST are high alongside elevated inflammatory markers (CRP > 5.0 mg/L)."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Alcohol-associated liver disease",
        "icd10": "K70.9",
        "required_features": ["AST", "ALT", "GGT"],
        "guideline": "ACG Guidelines",
        "criteria": "AST/ALT ratio >= 2:1 alongside significantly elevated GGT and a positive history of chronic heavy alcohol use."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Drug-induced liver injury",
        "icd10": "K72.0",
        "required_features": ["ALT", "AST", "ALP"],
        "guideline": "ACG 2023 Guidelines",
        "criteria": "An acute rise in transaminases or ALP temporally linked to starting a prescription, herbal, or OTC drug, in the absence of other etiologies."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Cholestatic liver disease",
        "icd10": "K71.0",
        "required_features": ["ALP", "GGT", "Total_Bilirubin"],
        "guideline": "EASL Guidelines",
        "criteria": "Marked elevation of ALP and GGT with high Total/Direct Bilirubin, suggesting impaired bile secretion or biliary obstruction."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Autoimmune hepatitis",
        "icd10": "K75.4",
        "required_features": ["ALT", "AST", "ANA"],
        "guideline": "AASLD Guidelines",
        "criteria": "Chronic transaminitis, highly elevated serum IgG, and positive autoantibodies (ANA, ASMA) in a patient without viral hepatitis."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Primary biliary cholangitis",
        "icd10": "K74.3",
        "required_features": ["ALP", "GGT"],
        "guideline": "EASL / AASLD Guidelines",
        "criteria": "Chronic cholestasis (high ALP and GGT) with positive Antimitochondrial Antibodies (AMA), representing immune destruction of small bile ducts."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Primary sclerosing cholangitis",
        "icd10": "K74.5",
        "required_features": ["ALP", "GGT"],
        "guideline": "EASL / AASLD Guidelines",
        "criteria": "Chronic cholestatic pattern often associated with inflammatory bowel disease (IBD), showing characteristic beaded bile ducts on MRCP."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Cirrhosis",
        "icd10": "K74.6",
        "required_features": ["AST", "ALT", "Platelet", "INR", "Albumin"],
        "guideline": "EASL Guidelines",
        "criteria": "Advanced hepatic fibrosis: thrombocytopenia (Platelets < 150 x10^9/L), prolonged INR (> 1.2), low Albumin (< 3.5 g/dL), and AST/ALT ratio > 1."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Acute liver failure",
        "icd10": "K72.0",
        "required_features": ["ALT", "AST", "INR"],
        "guideline": "AASLD Guidelines",
        "criteria": "Severe acute parenchymal injury (transaminitis) with prolonged coagulation (INR >= 1.5) and encephalopathy within 26 weeks in a patient without cirrhosis."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Hepatic synthetic dysfunction",
        "icd10": "K72.9",
        "required_features": ["Albumin", "INR"],
        "guideline": "ACG Guidelines",
        "criteria": "Impaired hepatocellular protein synthesis reflected by low Albumin (< 3.2 g/dL) and elevated INR (> 1.3) not responding to vitamin K."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Obstructive jaundice",
        "icd10": "K83.1",
        "required_features": ["Total_Bilirubin", "Direct_Bilirubin", "ALP"],
        "guideline": "EASL Guidelines",
        "criteria": "Biliary flow mechanical blockage: hyperbilirubinemia with high direct/conjugated fraction and elevated ALP/GGT."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Hepatocellular injury pattern",
        "icd10": "K72.9",
        "required_features": ["ALT", "AST", "ALP"],
        "guideline": "ACG 2017 Guidelines",
        "criteria": "Calculated R-value (ALT_observed/ALT_ULN)/(ALP_observed/ALP_ULN) >= 5, indicating direct liver cell injury."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Cholestatic injury pattern",
        "icd10": "K71.0",
        "required_features": ["ALT", "AST", "ALP"],
        "guideline": "ACG 2017 Guidelines",
        "criteria": "Calculated R-value (ALT_observed/ALT_ULN)/(ALP_observed/ALP_ULN) <= 2, indicating bile duct injury predominance."
    },

    # --- ELECTROLYTE AND ACID-BASE ---
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hyponatremia",
        "icd10": "E87.1",
        "required_features": ["Sodium"],
        "guideline": "Clinical Consensus Guidelines",
        "criteria": "Serum Sodium level below 135 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypernatremia",
        "icd10": "E87.0",
        "required_features": ["Sodium"],
        "guideline": "Clinical Consensus Guidelines",
        "criteria": "Serum Sodium level exceeding 145 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypokalemia",
        "icd10": "E87.6",
        "required_features": ["Potassium"],
        "guideline": "Clinical Consensus Guidelines",
        "criteria": "Serum Potassium level below 3.5 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hyperkalemia",
        "icd10": "E87.5",
        "required_features": ["Potassium"],
        "guideline": "Clinical Consensus Guidelines",
        "criteria": "Serum Potassium level exceeding 5.0 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypocalcemia",
        "icd10": "E83.51",
        "required_features": ["Calcium"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Calcium level below 8.5 mg/dL (corrected for albumin if needed) or Ionized Calcium < 1.15 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypercalcemia",
        "icd10": "E83.52",
        "required_features": ["Calcium"],
        "guideline": "Endocrine Society",
        "criteria": "Serum Total Calcium level exceeding 10.2 mg/dL or Ionized Calcium > 1.30 mmol/L."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypomagnesemia",
        "icd10": "E83.42",
        "required_features": ["Magnesium"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Magnesium level below 1.7 mg/dL (or < 0.70 mmol/L)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypermagnesemia",
        "icd10": "E83.41",
        "required_features": ["Magnesium"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Magnesium level exceeding 2.6 mg/dL (or > 1.05 mmol/L)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hypophosphatemia",
        "icd10": "E83.39",
        "required_features": ["Phosphate"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Inorganic Phosphate level below 2.5 mg/dL."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Hyperphosphatemia",
        "icd10": "E83.39",
        "required_features": ["Phosphate"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Inorganic Phosphate level exceeding 4.5 mg/dL."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Metabolic acidosis",
        "icd10": "E87.2",
        "required_features": ["pH", "HCO3"],
        "guideline": "Clinical Consensus",
        "criteria": "Arterial blood pH < 7.35 with primary reduction in HCO3- (< 22 mmol/L)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Metabolic alkalosis",
        "icd10": "E87.2",
        "required_features": ["pH", "HCO3"],
        "guideline": "Clinical Consensus",
        "criteria": "Arterial blood pH > 7.45 with primary elevation in HCO3- (> 26 mmol/L)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Respiratory acidosis",
        "icd10": "E87.2",
        "required_features": ["pH", "PaCO2"],
        "guideline": "Clinical Consensus",
        "criteria": "Arterial blood pH < 7.35 with primary retention of carbon dioxide (PaCO2 > 45 mmHg)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Respiratory alkalosis",
        "icd10": "E87.2",
        "required_features": ["pH", "PaCO2"],
        "guideline": "Clinical Consensus",
        "criteria": "Arterial blood pH > 7.45 with primary hyperventilatory loss of carbon dioxide (PaCO2 < 35 mmHg)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "High anion gap acidosis",
        "icd10": "E87.2",
        "required_features": ["pH", "HCO3", "Anion_Gap"],
        "guideline": "Clinical Consensus",
        "criteria": "Metabolic acidosis showing high calculated Anion Gap (Na - [Cl + HCO3]) > 12 mmol/L, indicating accumulation of unmeasured organic acids (MUDPILES)."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Non-anion gap acidosis",
        "icd10": "E87.2",
        "required_features": ["pH", "HCO3", "Anion_Gap"],
        "guideline": "Clinical Consensus",
        "criteria": "Metabolic acidosis showing normal Anion Gap (8-12 mmol/L), often secondary to renal bicarbonate loss or severe diarrhea."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Lactic acidosis",
        "icd10": "E87.2",
        "required_features": ["Lactate", "pH"],
        "guideline": "Surviving Sepsis Campaign",
        "criteria": "Metabolic acidosis presenting with Serum Lactate level exceeding 2.0 mmol/L, reflecting systemic tissue hypoperfusion."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Ketoacidosis",
        "icd10": "E11.10",
        "required_features": ["FBS", "UrineKetones", "HCO3"],
        "guideline": "ADA Guidelines",
        "criteria": "Metabolic acidosis with strong ketonuria and hyperketonemia, secondary to severe insulin lack or starvation."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Renal tubular acidosis",
        "icd10": "N25.8",
        "required_features": ["Potassium", "UrinepH", "Bicarbonate"],
        "guideline": "Clinical Consensus",
        "criteria": "Normal anion gap metabolic acidosis caused by defective renal acidification in the presence of normal glomerular clearance."
    },

    # --- BONE AND MINERAL ---
    {
        "category": "Bone and Mineral Panels",
        "name": "Primary hyperparathyroidism",
        "icd10": "E21.0",
        "required_features": ["Calcium", "PTH"],
        "guideline": "AACE Guidelines",
        "criteria": "Hypercalcemia (Calcium > 10.2 mg/dL) coupled with elevated or inappropriately normal PTH levels (> 65 pg/mL)."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Secondary hyperparathyroidism",
        "icd10": "E21.1",
        "required_features": ["Calcium", "PTH", "Vitamin_D"],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Low or normal Serum Calcium with elevated PTH, driven by chronic hypocalcemia, vitamin D deficiency, or chronic kidney disease."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Tertiary hyperparathyroidism",
        "icd10": "E21.2",
        "required_features": ["Calcium", "PTH", "eGFR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Hypercalcemia and severely elevated PTH in long-standing secondary hyperparathyroidism (usually ESKD), driven by autonomous parathyroid hyperplasia."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Hypoparathyroidism",
        "icd10": "E20.9",
        "required_features": ["Calcium", "PTH"],
        "guideline": "Endocrine Society 2016",
        "criteria": "Hypocalcemia (Calcium < 8.5 mg/dL) coupled with low or undetectable PTH levels (< 15 pg/mL)."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Osteomalacia",
        "icd10": "M83.9",
        "required_features": ["Vitamin_D", "Calcium", "Phosphate"],
        "guideline": "Clinical Consensus",
        "criteria": "Impaired bone mineralization in adults secondary to profound chronic hypovitaminosis D, presenting with low calcium and phosphate."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Rickets",
        "icd10": "E55.0",
        "required_features": ["Vitamin_D", "Calcium", "ALP"],
        "guideline": "Pediatric Endocrine Consensus",
        "criteria": "Defective bone mineralization in growing children showing elevated ALP, low calcium/phosphate, and typical skeletal deformities."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Osteoporosis",
        "icd10": "M81.0",
        "required_features": ["Age"],
        "guideline": "NOF / AACE Guidelines",
        "criteria": "Fragility fractures or bone mineral density T-score <= -2.5 on DEXA scan in older adults."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Paget disease of bone",
        "icd10": "M88.9",
        "required_features": ["ALP", "Calcium"],
        "guideline": "Endocrine Society 2014",
        "criteria": "Highly elevated serum ALP with completely normal serum calcium and phosphorus, indicating localized bone remodeling acceleration."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Renal osteodystrophy",
        "icd10": "N25.0",
        "required_features": ["PTH", "Phosphate", "eGFR"],
        "guideline": "KDIGO Guidelines",
        "criteria": "Bone pathology in advanced CKD, driven by systemic phosphate retention and abnormal osteoid mineralization."
    },

    # --- CARDIAC BIOMARKER ---
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Acute myocardial infarction",
        "icd10": "I21.9",
        "required_features": ["Troponin", "CK_MB"],
        "guideline": "ESC / ACC 2018 Guidelines",
        "criteria": "Ischemic presentation alongside rise/fall of highly sensitive Cardiac Troponin I (> 0.04 ng/mL) and elevated CK-MB."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Heart failure",
        "icd10": "I50.9",
        "required_features": ["BNP"],
        "guideline": "ESC 2021 Guidelines",
        "criteria": "Ventricular stretch pathology supported by elevated Serum BNP (> 100 pg/mL) or NT-proBNP (> 125 pg/mL)."
    },

    # --- COAGULATION ---
    {
        "category": "Coagulation Panels",
        "name": "Disseminated intravascular coagulation",
        "icd10": "D65",
        "required_features": ["Platelet", "INR", "Fibrinogen", "D_Dimer"],
        "guideline": "ISTH DIC Score",
        "criteria": "Systemic coagulation activation presenting as severe thrombocytopenia, prolonged INR, low Fibrinogen (< 150 mg/dL), and critical D-Dimer elevation."
    },

    # --- INFLAMMATORY ---
    {
        "category": "Inflammatory Panels",
        "name": "Acute bacterial infection",
        "icd10": "A49.9",
        "required_features": ["WBC", "NeutrophilsPercent", "CRP"],
        "guideline": "CDC Guidelines",
        "criteria": "Marked leukocytosis (WBC > 11.0 x10^9/L) with neutrophil predominance (> 75%) and highly elevated CRP (> 10.0 mg/L)."
    },
    {
        "category": "Inflammatory Panels",
        "name": "Viral infection",
        "icd10": "B34.9",
        "required_features": ["WBC", "LymphocytesPercent"],
        "guideline": "Clinical Consensus",
        "criteria": "Normal or low total WBC count alongside lymphocytosis (> 45%)."
    },

    # --- AUTOIMMUNE AND RHEUMATOLOGY ---
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Systemic lupus erythematosus",
        "icd10": "M32.9",
        "required_features": ["ANA", "Anti_dsDNA"],
        "guideline": "ACR / EULAR 2019 Criteria",
        "criteria": "Highly positive ANA titer coupled with elevated anti-dsDNA autoantibodies (> 30 IU/mL) and systemic clinical manifestations."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Rheumatoid arthritis",
        "icd10": "M06.9",
        "required_features": ["RF", "Anti_CCP", "CRP"],
        "guideline": "ACR / EULAR 2010 Criteria",
        "criteria": "Positive Rheumatoid Factor (RF > 15 IU/mL) and positive Anti-CCP (> 20 U/mL), representing autoimmune synovitis."
    },

    # --- PANCREATIC ---
    {
        "category": "Pancreatic Panels",
        "name": "Acute pancreatitis",
        "icd10": "K85.9",
        "required_features": ["Lipase", "Amylase"],
        "guideline": "Atlanta 2012 Classification",
        "criteria": "Severe epigastric pain radiating to the back with serum Lipase or Amylase levels elevated to >= 3 times the upper limit of normal."
    },

    # --- URINALYSIS ---
    {
        "category": "Urinalysis Panels",
        "name": "Urinary tract infection",
        "icd10": "N39.0",
        "required_features": ["UrineNitrite", "UrineLeukocyteEsterase", "UrineWBC"],
        "guideline": "IDSA Guidelines",
        "criteria": "Positive nitrite, positive leukocyte esterase in raw urine, and pyuria (Urine WBC > 5 /hpf) with dysuria."
    },

    # --- TUMOR MARKER ---
    {
        "category": "Tumor Marker Panels",
        "name": "Prostate cancer (Suspected)",
        "icd10": "C61",
        "required_features": ["PSA"],
        "guideline": "NCCN Guidelines",
        "criteria": "Total Serum PSA exceeding age-specific reference limits (generally > 4.0 ng/mL), requiring digital rectal exam and core biopsy."
    },

    # --- MICRONUTRIENT ---
    {
        "category": "Micronutrient Panels",
        "name": "Selenium deficiency",
        "icd10": "E61.4",
        "required_features": ["Selenium"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum Selenium level below 70 µg/L, predisposing to Keshan disease or skeletal muscle myopathies."
    },
    {
        "category": "Micronutrient Panels",
        "name": "Iodine deficiency",
        "icd10": "E61.2",
        "required_features": ["Iodine"],
        "guideline": "WHO Guidelines",
        "criteria": "Median urinary iodine concentration < 100 µg/L (or individual spot urine < 50 µg/L). Serum iodine is not a reliable indicator; however, if serum iodine is used, values < 40 µg/L suggest deficiency."
    },
    {
        "category": "Micronutrient Panels",
        "name": "Vitamin A deficiency",
        "icd10": "E50.9",
        "required_features": ["VitaminA"],
        "guideline": "WHO Guidelines",
        "criteria": "Serum Retinol level below 30 µg/dL, resulting in xerophthalmia, night blindness, and severe mucosal susceptibility."
    },
    {
        "category": "Micronutrient Panels",
        "name": "Vitamin E deficiency",
        "icd10": "E56.0",
        "required_features": ["VitaminE"],
        "guideline": "Clinical Consensus",
        "criteria": "Serum alpha-tocopherol level below 0.5 mg/dL, causing peripheral neuropathy, spinocerebellar ataxia, and hemolysis."
    },
    {
        "category": "Micronutrient Panels",
        "name": "Vitamin C deficiency",
        "icd10": "E54",
        "required_features": ["VitaminC"],
        "guideline": "WHO Guidelines",
        "criteria": "Serum Vitamin C level below 0.4 mg/dL, causing scurvy (corkscrew hairs, perifollicular hemorrhages, gum disease)."
    },

    # --- ADDITIONAL HIGH-YIELD MAPPED DISEASES ---
    {
        "category": "Additional High-Yield Mapped Diseases",
        "name": "Gout",
        "icd10": "M10.9",
        "required_features": ["Uric_Acid"],
        "guideline": "ACR 2020 Guidelines",
        "criteria": "Uric Acid levels exceeding gender thresholds (7.2 mg/dL in males, 6.0 mg/dL in females), representing precipitation risk of monosodium urate crystals."
    },
    {
        "category": "Additional High-Yield Mapped Diseases",
        "name": "SIADH",
        "icd10": "E22.2",
        "required_features": ["Sodium", "UrineSpecificGravity"],
        "guideline": "Clinical Consensus",
        "criteria": "Euvolemic hyponatremia (Sodium < 135 mmol/L) with high urine specific gravity (> 1.015) representing inappropriate urinary concentration."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Metabolic dysfunction-associated steatotic liver disease",
        "icd10": "K76.0",
        "required_features": ['ALT', 'AST', 'Triglycerides', 'BMI'],
        "guideline": "AASLD 2023 Guidelines",
        "criteria": "Evidence of hepatic steatosis (mildly elevated ALT/AST, Triglycerides > 150 mg/dL, and BMI > 25) with no other secondary causes of hepatic fat accumulation."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "CKD-mineral and bone disorder",
        "icd10": "N25.0",
        "required_features": ['Calcium', 'Phosphate', 'PTH', 'eGFR'],
        "guideline": "KDIGO 2017 Guidelines",
        "criteria": "Presence of abnormalities in serum Calcium (< 8.4 or > 10.2 mg/dL), Phosphate (> 4.5 mg/dL), or PTH (> 65 pg/mL) in patients with eGFR < 60 mL/min/1.73m²."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Vitamin D deficiency bone disease",
        "icd10": "M83.9",
        "required_features": ['Vitamin_D', 'Calcium', 'ALP'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Serum 25-hydroxyvitamin D < 20 ng/mL, coupled with low/normal serum Calcium and elevated ALP (> 120 U/L) indicating bone mineralization defect (osteomalacia/rickets)."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Hypercalciuria",
        "icd10": "E83.52",
        "required_features": ['Calcium'],
        "guideline": "AUA Guidelines",
        "criteria": "Elevated 24-hour urine calcium excretion (> 250 mg/day in women, > 300 mg/day in men) or high urine calcium/creatinine ratio. Serum calcium may be normal."
    },
    {
        "category": "Bone and Mineral Panels",
        "name": "Osteitis fibrosa cystica",
        "icd10": "M85.0",
        "required_features": ['PTH', 'Calcium', 'ALP'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Severe hyperparathyroidism (PTH > 300 pg/mL) with hypercalcemia (> 10.5 mg/dL) and elevated ALP (> 150 U/L), reflecting advanced parathyroid-induced bone resorption."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Non-ST elevation myocardial infarction",
        "icd10": "I21.4",
        "required_features": ['Troponin', 'CK_MB'],
        "guideline": "ESC 2020 Guidelines",
        "criteria": "Acute ischemic symptoms with elevated Cardiac Troponin (> 0.04 ng/mL) or dynamic rising pattern, and elevated CK-MB (> 5.0 ng/mL) in the absence of ST-elevation."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Acute decompensated heart failure",
        "icd10": "I50.9",
        "required_features": ['BNP', 'Sodium'],
        "guideline": "ACC/AHA 2022 Guidelines",
        "criteria": "Acute onset dyspnea with significantly elevated BNP (> 400 pg/mL) or NT-proBNP, often accompanied by dilutional hyponatremia (Sodium < 135 mmol/L)."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Myocardial injury",
        "icd10": "I51.89",
        "required_features": ['Troponin'],
        "guideline": "Fourth Universal Definition of MI",
        "criteria": "Detection of elevated Cardiac Troponin (> 0.04 ng/mL) above the 99th percentile upper reference limit, with or without clinical evidence of ischemia."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Myocarditis",
        "icd10": "I40.9",
        "required_features": ['Troponin', 'CRP', 'ESR'],
        "guideline": "ESC Guidelines",
        "criteria": "Acute chest pain, dyspnea, or palpitation with elevated Troponin (> 0.04 ng/mL) and marked inflammatory marker elevations (CRP > 10.0 mg/L, ESR > 20 mm/hr) in the absence of CAD."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Cardiorenal syndrome",
        "icd10": "I50.9",
        "required_features": ['BNP', 'Creatinine', 'BUN'],
        "guideline": "AHA Scientific Statement",
        "criteria": "Concomitant cardiac and renal dysfunction: elevated BNP (> 100 pg/mL) or NT-proBNP combined with renal impairment (Creatinine > 1.3 mg/dL and BUN > 20 mg/dL)."
    },
    {
        "category": "Cardiac Biomarker Panels",
        "name": "Stress cardiomyopathy",
        "icd10": "I42.8",
        "required_features": ['Troponin', 'BNP'],
        "guideline": "ESC Guidelines",
        "criteria": "Transient LV dysfunction (Takotsubo) triggered by severe emotional/physical stress, with mild Troponin elevation (> 0.04 ng/mL) and disproportionally high BNP (> 200 pg/mL)."
    },
    {
        "category": "Coagulation Panels",
        "name": "Venous thromboembolism",
        "icd10": "I82.91",
        "required_features": ['D_Dimer'],
        "guideline": "ASH 2020 Guidelines",
        "criteria": "Clinical suspicion of deep venous clot or pulmonary clot accompanied by elevated D-Dimer (> 0.5 µg/mL FEU)."
    },
    {
        "category": "Coagulation Panels",
        "name": "Deep vein thrombosis",
        "icd10": "I82.40",
        "required_features": ['D_Dimer'],
        "guideline": "ASH 2020 Guidelines",
        "criteria": "Suspected acute deep venous thrombosis in lower or upper extremity, supported by elevated D-Dimer (> 0.5 µg/mL FEU)."
    },
    {
        "category": "Coagulation Panels",
        "name": "Pulmonary embolism",
        "icd10": "I26.99",
        "required_features": ['D_Dimer', 'Troponin'],
        "guideline": "ESC 2019 Guidelines",
        "criteria": "Suspected acute occlusion of pulmonary arterial bed, with elevated D-Dimer (> 0.5 µg/mL FEU). Troponin may be elevated (> 0.04 ng/mL) due to right ventricular overload."
    },
    {
        "category": "Coagulation Panels",
        "name": "Liver-related coagulopathy",
        "icd10": "D68.4",
        "required_features": ['INR', 'Platelet', 'ALT'],
        "guideline": "EASL Guidelines",
        "criteria": "Coagulation defect due to liver failure: elevated INR (> 1.5) and thrombocytopenia (Platelets < 150 x10^9/L) in a setting of hepatocellular injury (elevated ALT/AST)."
    },
    {
        "category": "Coagulation Panels",
        "name": "Vitamin K deficiency coagulopathy",
        "icd10": "D68.4",
        "required_features": ['INR', 'PT'],
        "guideline": "Clinical Consensus",
        "criteria": "Prolongation of prothrombin time (PT) and elevated INR (> 1.5) in the presence of Vitamin K depletion or malnutrition, rapidly reversed by Vitamin K."
    },
    {
        "category": "Coagulation Panels",
        "name": "Consumptive coagulopathy",
        "icd10": "D65",
        "required_features": ['Platelet', 'Fibrinogen', 'D_Dimer'],
        "guideline": "ISTH Guidelines",
        "criteria": "Consumption of clotting factors: progressive thrombocytopenia (Platelets < 150 x10^9/L), low Fibrinogen (< 150 mg/dL), and highly elevated D-Dimer (> 2.0 µg/mL FEU)."
    },
    {
        "category": "Coagulation Panels",
        "name": "Hypercoagulable state",
        "icd10": "D68.9",
        "required_features": ['Platelet', 'D_Dimer'],
        "guideline": "ASH Guidelines",
        "criteria": "Predisposition to thrombotic events suggested by thrombocytosis (Platelets > 450 x10^9/L) or persistently elevated D-Dimer (> 0.5 µg/mL)."
    },
    {
        "category": "Inflammatory Panels",
        "name": "Sepsis",
        "icd10": "A41.9",
        "required_features": ['WBC', 'CRP', 'Lactate', 'Platelet'],
        "guideline": "Surviving Sepsis 2021",
        "criteria": "Systemic organ dysfunction from infection: elevated Lactate (> 2.0 mmol/L), severe inflammation (CRP > 10 mg/L or WBC > 11.0 or < 4.0), and acute thrombocytopenia (< 100 x10^9/L)."
    },
    {
        "category": "Inflammatory Panels",
        "name": "Chronic inflammatory disease",
        "icd10": "M35.9",
        "required_features": ['CRP', 'ESR', 'Albumin'],
        "guideline": "Clinical Consensus",
        "criteria": "Persistent systemic inflammation with elevated CRP (> 5.0 mg/L) and ESR (> 20 mm/hr), often accompanied by mild hypoalbuminemia (< 3.5 g/dL) as a negative acute-phase reactant."
    },
    {
        "category": "Inflammatory Panels",
        "name": "Inflammatory flare state",
        "icd10": "M35.9",
        "required_features": ['CRP', 'ESR'],
        "guideline": "Clinical Consensus",
        "criteria": "Acute exacerbation of chronic rheumatologic or autoinflammatory conditions, evidenced by rapid rise in CRP (> 15.0 mg/L) and ESR (> 30 mm/hr)."
    },
    {
        "category": "Inflammatory Panels",
        "name": "Systemic inflammatory response syndrome",
        "icd10": "R65.10",
        "required_features": ['WBC', 'HeartRate'],
        "guideline": "Sepsis-2 Guidelines",
        "criteria": "SIRS is recognized by tachycardia (Heart Rate > 90 bpm) combined with leukocyte abnormalities (WBC > 12.0 or < 4.0 x10^9/L)."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Sjögren syndrome",
        "icd10": "M35.00",
        "required_features": ['ANA', 'ENA_Panel'],
        "guideline": "ACR/EULAR 2016 Criteria",
        "criteria": "Positive Antinuclear Antibodies (ANA > 1.0) and positive ENA Panel (specifically Anti-SSA/Ro or Anti-SSB/La autoantibodies)."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Systemic sclerosis",
        "icd10": "M34.9",
        "required_features": ['ANA', 'ENA_Panel'],
        "guideline": "ACR/EULAR 2013 Criteria",
        "criteria": "Positive Antinuclear Antibodies (ANA > 1.0) with scleroderma-specific autoantibodies (such as anti-Scl70, anti-centromere, or anti-RNA polymerase III)."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Mixed connective tissue disease",
        "icd10": "M35.1",
        "required_features": ['ANA', 'ENA_Panel'],
        "guideline": "Alarcon-Segovia Criteria",
        "criteria": "High-titer speckled ANA (> 1.0) with highly elevated Anti-U1 RNP autoantibodies on ENA Panel."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Antiphospholipid syndrome",
        "icd10": "D68.61",
        "required_features": ['Lupus_Anticoagulant', 'Anti_Cardiolipin', 'Anti_Beta2GP1'],
        "guideline": "Sydney Criteria 2006",
        "criteria": "Vascular thrombosis or pregnancy morbidity with persistently positive antiphospholipid antibodies (Lupus anticoagulant, anti-cardiolipin IgG/IgM > 40 GPL/MPL, or anti-β2-glycoprotein I > 99th percentile) on 2 occasions 12 weeks apart."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "ANCA-associated vasculitis",
        "icd10": "M31.3",
        "required_features": ['ANCA', 'PR3', 'MPO', 'CRP', 'UrineRBC'],
        "guideline": "ACR/EULAR 2022 Criteria",
        "criteria": "Positive ANCA (cytoplasmic or perinuclear pattern) with high anti-PR3 or anti-MPO titers, systemic inflammation (elevated CRP/ESR), and active glomerulonephritis (hematuria with dysmorphic RBCs)."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Dermatomyositis",
        "icd10": "M33.9",
        "required_features": ['CK', 'AST', 'ALT', 'ANA', 'CRP'],
        "guideline": "EULAR/ACR 2017 Criteria",
        "criteria": "Proximal muscle weakness and characteristic skin rashes with elevated CK (> 10× ULN), transaminases (AST/ALT), positive ANA, and elevated inflammatory markers. Anti-Jo-1 or other myositis antibodies often present."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Polymyositis",
        "icd10": "M33.2",
        "required_features": ['CK', 'AST', 'ALT', 'CRP'],
        "guideline": "EULAR/ACR 2017 Criteria",
        "criteria": "Proximal muscle weakness without rash, elevated CK (> 5× ULN) and transaminases (AST/ALT), and elevated CRP. Muscle biopsy shows endomysial CD8+ T-cell infiltrates."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Undifferentiated connective tissue disease",
        "icd10": "M35.9",
        "required_features": ['ANA', 'CRP'],
        "guideline": "Clinical Consensus",
        "criteria": "Signs of autoimmune disease with positive ANA (> 1.0) and elevated CRP, but failing to meet specific classification criteria for SLE, Sjögren's, or Scleroderma."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Autoimmune thyroid disease",
        "icd10": "E06.3",
        "required_features": ['Anti_TPO', 'TSH'],
        "guideline": "ATA Guidelines",
        "criteria": "Presence of autoantibodies to thyroid peroxidase (Anti-TPO > 34 IU/mL) indicating autoimmune thyroiditis (Hashimoto's or Graves' disease) with altered TSH."
    },
    {
        "category": "Autoimmune and Rheumatology Panels",
        "name": "Autoimmune liver disease",
        "icd10": "K75.4",
        "required_features": ['ANA', 'ALT', 'AST'],
        "guideline": "AASLD Guidelines",
        "criteria": "Chronic hepatitis with positive autoantibodies: elevated ALT/AST and positive ANA (> 1.0), in the absence of viral hepatitis."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Chronic pancreatitis",
        "icd10": "K86.1",
        "required_features": ['Amylase', 'Lipase'],
        "guideline": "AGA Guidelines",
        "criteria": "Persistent abdominal pain with pancreatic exocrine insufficiency, where Amylase or Lipase may be mildly elevated or abnormally low in late-stage disease."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Pancreatic exocrine dysfunction",
        "icd10": "K86.81",
        "required_features": ['Amylase', 'Lipase'],
        "guideline": "AGA Guidelines",
        "criteria": "Malabsorption and chronic diarrhea due to pancreatic enzyme deficiency; fecal elastase-1 < 200 µg/g confirms. Serum Lipase (< 10 U/L) or Amylase may be low."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Pancreaticobiliary inflammation",
        "icd10": "K83.0",
        "required_features": ['Amylase', 'ALT', 'ALP'],
        "guideline": "Clinical Consensus",
        "criteria": "Concomitant elevation of pancreatic enzymes (Amylase > 100 U/L) and biliary obstruction markers (ALT > 50 U/L and ALP > 150 U/L)."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Hematuria syndrome",
        "icd10": "R31.9",
        "required_features": ['UrineBlood', 'UrineRBC'],
        "guideline": "AUA 2020 Guidelines",
        "criteria": "Presence of abnormal blood in qualitative urinalysis (Positive/Trace) confirmed by microscopic hematuria (Urine RBC > 3 /hpf)."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Pyuria",
        "icd10": "N39.0",
        "required_features": ['UrineWBC'],
        "guideline": "Clinical Consensus",
        "criteria": "Presence of pus cells in urine: Urine WBC > 5 per high-power field, indicating active urinary tract inflammation or infection."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Crystalluria",
        "icd10": "R82.9",
        "required_features": ['UrinepH'],
        "guideline": "Clinical Consensus",
        "criteria": "Detection of microscopic crystals in urine, influenced by acidic pH (< 5.5, uric acid/cystine) or alkaline pH (> 7.5, struvite/calcium phosphate)."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Glucosuria",
        "icd10": "R81",
        "required_features": ['UrineGlucoseQualitative', 'FBS'],
        "guideline": "ADA Guidelines",
        "criteria": "Excretion of glucose in urine (qualitative Urine Glucose is Trace/Positive) occurring when serum glucose (FBS > 180 mg/dL) exceeds the renal threshold."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Ketonuria",
        "icd10": "R82.4",
        "required_features": ['UrineKetones'],
        "guideline": "ADA Guidelines",
        "criteria": "Excretion of ketone bodies in urine (qualitative Urine Ketones is Trace/Small/Moderate/Large), reflecting accelerated fatty acid metabolism (diabetic ketoacidosis or starvation)."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Tubular injury pattern",
        "icd10": "N17.0",
        "required_features": ['UrineSpecificGravity', 'Creatinine'],
        "guideline": "KDIGO Guidelines",
        "criteria": "Acute tubular necrosis or injury: elevated serum Creatinine (> 1.3 mg/dL) with low, fixed urine specific gravity (1.010), representing impaired concentration capacity."
    },
    {
        "category": "Urinalysis Panels",
        "name": "Cast-associated renal disease",
        "icd10": "N18.9",
        "required_features": ['UrineProteinQualitative', 'Creatinine'],
        "guideline": "Clinical Consensus",
        "criteria": "Presence of protein casts in urine sediment accompanied by elevated serum Creatinine (> 1.3 mg/dL), indicating glomerular or tubular pathology."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Male hypogonadism",
        "icd10": "E29.1",
        "required_features": ['Testosterone', 'LH'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Total Serum Testosterone < 300 ng/dL in adult males, accompanied by low or normal LH (secondary hypogonadism) or high LH (primary hypogonadism)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Female hypogonadism",
        "icd10": "E28.3",
        "required_features": ['Estradiol', 'FSH', 'LH'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Abnormally low Estradiol (< 30 pg/mL) combined with elevated gonadotropins (FSH > 40 IU/L, primary ovarian failure) or low gonadotropins (hypogonadotropic hypogonadism)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Ovarian insufficiency",
        "icd10": "E28.319",
        "required_features": ['FSH', 'Estradiol'],
        "guideline": "ESHRE Guidelines",
        "criteria": "Primary ovarian insufficiency (POI) in females < 40 years: elevated FSH > 25 IU/L on two occasions, and low Estradiol (< 30 pg/mL)."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Menopausal transition",
        "icd10": "N95.1",
        "required_features": ['FSH', 'Estradiol'],
        "guideline": "STRAW+10 Stages",
        "criteria": "Elevated FSH (> 30 IU/L) with decreasing Estradiol, irregular menstrual cycles, and vasomotor symptoms in women typically aged 45-55."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Hyperandrogenism",
        "icd10": "E28.1",
        "required_features": ['Testosterone'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Elevated total or free Testosterone (> 80 ng/dL in females) leading to hirsutism, acne, or androgenic alopecia."
    },
    {
        "category": "Thyroid and Endocrine Panels",
        "name": "Infertility-associated endocrine disorder",
        "icd10": "E28.3",
        "required_features": ['FSH', 'LH', 'Prolactin'],
        "guideline": "ASRM Guidelines",
        "criteria": "Hormonal dysregulation predisposing to subfertility: high FSH (> 10 IU/L), abnormal LH, or hyperprolactinemia (> 25 ng/mL)."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Hepatocellular carcinoma",
        "icd10": "C22.0",
        "required_features": ['AFP', 'ALT'],
        "guideline": "AASLD Guidelines",
        "criteria": "Markedly elevated Alpha-Fetoprotein (AFP > 200 ng/mL) in patients with cirrhosis or chronic hepatitis B/C, highly suggestive of HCC."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Prostate cancer",
        "icd10": "C61",
        "required_features": ['PSA'],
        "guideline": "NCCN Guidelines",
        "criteria": "Total Serum PSA exceeding age-specific reference limits (generally > 4.0 ng/mL), requiring digital rectal exam and core biopsy."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Ovarian epithelial cancer",
        "icd10": "C56.9",
        "required_features": ['CA125'],
        "guideline": "NCCN Guidelines",
        "criteria": "Significantly elevated Cancer Antigen 125 (CA-125 > 35 U/mL) in postmenopausal females with pelvic masses."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Colorectal cancer",
        "icd10": "C18.9",
        "required_features": ['CEA'],
        "guideline": "NCCN Guidelines",
        "criteria": "Elevated Carcinoembryonic Antigen (CEA > 5.0 ng/mL), used primarily for monitoring recurrence or prognosis of colorectal adenocarcinoma."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Pancreatic adenocarcinoma",
        "icd10": "C25.9",
        "required_features": ['CA19_9'],
        "guideline": "NCCN Guidelines",
        "criteria": "Markedly elevated Cancer Antigen 19-9 (CA19-9 > 37 U/mL) in a patient with obstructive jaundice or pancreatic mass."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Germ cell tumor",
        "icd10": "C62.90",
        "required_features": ['AFP', 'Beta_hCG'],
        "guideline": "NCCN Guidelines",
        "criteria": "Co-elevation of Alpha-Fetoprotein (AFP > 10 ng/mL) and Beta-hCG in young males, highly suggestive of testicular germ cell tumors."
    },
    {
        "category": "Tumor Marker Panels",
        "name": "Neuroendocrine tumor",
        "icd10": "C7A.00",
        "required_features": ['Chromogranin_A'],
        "guideline": "ENETS Guidelines",
        "criteria": "Elevated Chromogranin A (CgA) > 3× ULN, or specific hormones (e.g., gastrin, serotonin) depending on tumor type. Confirm with somatostatin-receptor imaging."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Hepatitis B infection",
        "icd10": "B18.1",
        "required_features": ['HBsAg', 'Anti_HBc'],
        "guideline": "AASLD Guidelines",
        "criteria": "Presence of Hepatitis B surface antigen (HBsAg Positive) and total Anti-HBc, indicating acute or chronic HBV infection."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Hepatitis C infection",
        "icd10": "B18.2",
        "required_features": ['Anti_HCV'],
        "guideline": "AASLD/IDSA Guidelines",
        "criteria": "Anti-HCV positive; active infection requires HCV RNA confirmation."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "HIV infection",
        "icd10": "B20",
        "required_features": ['HIV_AgAb'],
        "guideline": "CDC Guidelines",
        "criteria": "Positive 4th-generation HIV-1/2 antigen/antibody combination test, confirmed by HIV-1 RNA PCR or differentiation immunoassay."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Epstein–Barr virus infection",
        "icd10": "B27.0",
        "required_features": ['WBC', 'LymphocytesPercent', 'ALT'],
        "guideline": "CDC Guidelines",
        "criteria": "Acute mononucleosis: leukocytosis with absolute lymphocytosis (> 50% lymphocytes) and atypical lymphocytes, often with transient reactive hepatitis (elevated ALT/AST)."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Cytomegalovirus infection",
        "icd10": "B25.9",
        "required_features": ['WBC', 'LymphocytesPercent', 'ALT'],
        "guideline": "CDC Guidelines",
        "criteria": "CMV mononucleosis syndrome: lymphocytosis, normal or elevated WBC, and elevated transaminases, presenting similarly to EBV but negative for heterophile antibodies."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Syphilis",
        "icd10": "A53.9",
        "required_features": ['RPR', 'TPPA'],
        "guideline": "CDC 2021 Guidelines",
        "criteria": "Positive non-treponemal test (RPR or VDRL) followed by positive treponemal-specific test (TPPA or FTA-ABS) confirming syphilis infection."
    },
    {
        "category": "Liver Function and Hepatitis Panels",
        "name": "Toxoplasmosis",
        "icd10": "B58.9",
        "required_features": ['WBC'],
        "guideline": "CDC Guidelines",
        "criteria": "Diagnosed by serology showing high anti-Toxoplasma IgG and IgM titers in setting of lymphadenopathy or immune deficiency."
    },
    {
        "category": "CBC And Differential",
        "name": "Hypoxemic respiratory failure",
        "icd10": "J96.01",
        "required_features": ['PaO2'],
        "guideline": "ATS Guidelines",
        "criteria": "Severe impairment in gas exchange with arterial blood oxygen levels falling below 60 mmHg (PaO2 < 60 mmHg) on room air."
    },
    {
        "category": "CBC And Differential",
        "name": "Hypercapnic respiratory failure",
        "icd10": "J96.02",
        "required_features": ['PaCO2', 'pH'],
        "guideline": "ATS Guidelines",
        "criteria": "Alveolar hypoventilation leading to elevated arterial carbon dioxide (PaCO2 > 45 mmHg) accompanied by respiratory acidosis (pH < 7.35)."
    },
    {
        "category": "CBC And Differential",
        "name": "COPD exacerbation",
        "icd10": "J44.1",
        "required_features": ['PaCO2', 'pH', 'PaO2'],
        "guideline": "GOLD 2023 Guidelines",
        "criteria": "Acute worsening of respiratory symptoms requiring therapy, marked by acute hypoxemia (PaO2 < 60) or hypercapnia with acidosis."
    },
    {
        "category": "CBC And Differential",
        "name": "Severe asthma exacerbation",
        "icd10": "J45.901",
        "required_features": ['PaCO2', 'pH', 'PaO2'],
        "guideline": "GINA Guidelines",
        "criteria": "Acute severe bronchospasm leading to hypoxemia. Normal or elevated PaCO2 (> 40 mmHg) is a warning sign of impending respiratory fatigue."
    },
    {
        "category": "CBC And Differential",
        "name": "Acute respiratory distress syndrome",
        "icd10": "J80",
        "required_features": ['PaO2'],
        "guideline": "Berlin Definition 2012",
        "criteria": "Acute onset bilateral lung infiltrates within 1 week of clinical insult, with severe hypoxemia (PaO2/FiO2 ratio < 300 mmHg) not fully explained by heart failure."
    },
    {
        "category": "Iron, Vitamin, and Nutrition Panels",
        "name": "Multiple micronutrient deficiency",
        "icd10": "E61.7",
        "required_features": ['Zinc', 'Selenium', 'VitaminA'],
        "guideline": "WHO Guidelines",
        "criteria": "Concomitant deficient states of more than one essential trace element or vitamin (e.g., low Zinc < 70, low Selenium < 70, or low Vitamin A < 30)."
    },
    {
        "category": "CBC And Differential",
        "name": "Acute myeloid leukemia",
        "icd10": "C92.00",
        "required_features": ['WBC', 'Platelet', 'Hb'],
        "guideline": "WHO 2022 Classification",
        "criteria": "Rapidly progressive bone marrow failure: marked leukocytosis or leukopenia with severe thrombocytopenia (Platelets < 50) and anemia. Requires bone marrow flow cytometry (>= 20% myeloblasts)."
    },
    {
        "category": "CBC And Differential",
        "name": "Acute lymphoblastic leukemia",
        "icd10": "C91.00",
        "required_features": ['WBC', 'Platelet', 'Hb'],
        "guideline": "WHO 2022 Classification",
        "criteria": "Malignant clonal expansion of lymphoid progenitors, presenting with pancytopenia or extreme leukocytosis with blast cells. Requires bone marrow aspirate."
    },
    {
        "category": "CBC And Differential",
        "name": "Chronic lymphocytic leukemia",
        "icd10": "C91.10",
        "required_features": ['WBC', 'ALC'],
        "guideline": "iwCLL Guidelines",
        "criteria": "Sustained absolute monoclonal lymphocytosis in peripheral blood (ALC >= 5.0 x10^9/L) for at least 3 months, with characteristic flow cytometry."
    },
    {
        "category": "CBC And Differential",
        "name": "Chronic myeloid leukemia",
        "icd10": "C92.10",
        "required_features": ['WBC', 'Platelet'],
        "guideline": "ELN 2020 Guidelines",
        "criteria": "Marked neutrophilic leukocytosis (WBC often > 50.0 x10^9/L) with entire spectrum of myeloid precursors, frequently with basophilia (> 2%) and thrombocytosis."
    },
    {
        "category": "CBC And Differential",
        "name": "Multiple myeloma",
        "icd10": "C90.00",
        "required_features": ['Total_Protein', 'Albumin', 'Calcium', 'Creatinine'],
        "guideline": "IMWG 2014 Criteria",
        "criteria": "Clonal plasma cell proliferative disorder marked by the CRAB criteria: Hypercalcemia (Calcium > 11.0 mg/dL), Renal insufficiency (Creatinine > 2.0 mg/dL), Anemia, or Bone lesions, with a high globulin gap (Total Protein - Albumin > 4.0 g/dL)."
    },
    {
        "category": "CBC And Differential",
        "name": "Monoclonal gammopathy",
        "icd10": "D47.2",
        "required_features": ['Total_Protein', 'Albumin'],
        "guideline": "IMWG Criteria",
        "criteria": "Presence of a monoclonal protein in serum (high globulin gap > 3.5 g/dL) but without end-organ CRAB damage (normal calcium, normal creatinine, no anemia)."
    },
    {
        "category": "CBC And Differential",
        "name": "Myeloproliferative neoplasm",
        "icd10": "D47.1",
        "required_features": ['Platelet', 'WBC', 'Hb'],
        "guideline": "WHO 2016 Guidelines",
        "criteria": "Clonal myeloid proliferation presenting as Essential Thrombocythemia (Platelets > 450), Polycythemia Vera (high Hb), or Primary Myelofibrosis."
    },
    {
        "category": "CBC And Differential",
        "name": "Plasma cell dyscrasia",
        "icd10": "D47.Z9",
        "required_features": ['Total_Protein', 'Albumin'],
        "guideline": "Clinical Consensus",
        "criteria": "Group of disorders characterized by clonal expansion of plasma cells, leading to monoclonal immunoglobulins, indicated by an elevated total globulin gap."
    },
    {
        "category": "CBC And Differential",
        "name": "Wilson disease",
        "icd10": "E83.01",
        "required_features": ['ALT', 'AST'],
        "guideline": "AASLD Guidelines",
        "criteria": "Impaired copper metabolism: acute or chronic hepatitis (high ALT/AST), Coombs-negative hemolytic anemia, and neurologic signs. Confirmed by low ceruloplasmin and high 24h urine copper."
    },
    {
        "category": "CBC And Differential",
        "name": "Hemophagocytic lymphohistiocytosis",
        "icd10": "D76.1",
        "required_features": ['Ferritin', 'WBC', 'Platelet', 'Hb'],
        "guideline": "HLH-2004 Protocol",
        "criteria": "Severe hyperinflammatory syndrome: extreme hyperferritinemia (Ferritin > 500 ng/mL, often > 10,000) and cytopenias in >= 2 lineages (anemia, neutropenia, or thrombocytopenia)."
    },
    {
        "category": "CBC And Differential",
        "name": "Amyloidosis",
        "icd10": "E85.9",
        "required_features": ['UrineProteinQualitative', 'Creatinine'],
        "guideline": "Clinical Consensus",
        "criteria": "Extracellular deposition of insoluble fibrils: presenting with nephrotic syndrome (heavy proteinuria with elevated creatinine) or restrictive cardiomyopathy."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Nephrogenic syndrome of inappropriate antidiuresis",
        "icd10": "E22.2",
        "required_features": ['Sodium', 'UrineSpecificGravity'],
        "guideline": "Clinical Consensus",
        "criteria": "Euvolemic hyponatremia (Sodium < 135 mmol/L) with concentrated urine, presenting identically to SIADH but caused by gain-of-function V2 receptor mutations."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Syndrome of inappropriate antidiuretic hormone secretion",
        "icd10": "E22.2",
        "required_features": ['Sodium', 'UrineSpecificGravity'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Hypotonic hyponatremia (Sodium < 135 mmol/L) with high urine specific gravity (> 1.015) in a clinically euvolemic patient."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Diabetes insipidus",
        "icd10": "E23.2",
        "required_features": ['Sodium', 'UrineSpecificGravity'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Polyuria with hypernatremia (Sodium > 145 mmol/L) and low, dilute urine specific gravity (< 1.005) representing impaired ADH secretion or action."
    },
    {
        "category": "CBC And Differential",
        "name": "Rhabdomyolysis",
        "icd10": "M62.82",
        "required_features": ['CK', 'Creatinine'],
        "guideline": "Clinical Consensus",
        "criteria": "Marked elevation of total Creatine Kinase (CK > 5× upper limit of normal) with myoglobinuria and acute kidney injury risk (elevated Creatinine). AST/ALT can rise but are not diagnostic."
    },
    {
        "category": "CBC And Differential",
        "name": "Tumor lysis syndrome",
        "icd10": "Y43.3",
        "required_features": ['Uric_Acid', 'Phosphate', 'Potassium', 'Calcium'],
        "guideline": "Cairo-Bishop Criteria",
        "criteria": "Massive tumor cell necrosis: hyperuricemia (> 8.0 mg/dL), hyperphosphatemia (> 4.5 mg/dL), hyperkalemia (> 6.0 mmol/L), and hypocalcemia (< 7.0 mg/dL) within 7 days of chemotherapy."
    },
    {
        "category": "Additional High-Yield Mapped Diseases",
        "name": "Hyperuricemia",
        "icd10": "E79.0",
        "required_features": ['Uric_Acid'],
        "guideline": "ACR Guidelines",
        "criteria": "Elevated uric acid levels (> 7.2 mg/dL in males, > 6.0 in females) without active gouty arthritis or tophi."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Pseudohyperkalemia",
        "icd10": "E87.5",
        "required_features": ['Potassium', 'Platelet'],
        "guideline": "Clinical Consensus",
        "criteria": "Factitiously elevated serum potassium in vitro, occurring during clotting of samples with extreme thrombocytosis (Platelets > 500 x10^9/L) or leukocytosis."
    },
    {
        "category": "Electrolyte and Acid–Base Panels",
        "name": "Pseudohyponatremia",
        "icd10": "E87.1",
        "required_features": ['Sodium', 'Total_Cholesterol', 'Triglycerides'],
        "guideline": "Clinical Consensus",
        "criteria": "Factitiously lowered serum sodium (Sodium < 135 mmol/L) due to volume displacement by severe hyperlipidemia (Triglycerides > 1000 mg/dL) or hyperproteinemia."
    },
    {
        "category": "Diabetes and Metabolic Panels",
        "name": "Factitious hypoglycemia",
        "icd10": "E16.2",
        "required_features": ['FBS', 'Insulin'],
        "guideline": "Endocrine Society Guidelines",
        "criteria": "Hypoglycemia (FBS < 55 mg/dL) induced by exogenous insulin administration, marked by high insulin but low/suppressed C-peptide."
    },
    {
        "category": "CBC And Differential",
        "name": "Paraproteinemia-related laboratory syndrome",
        "icd10": "D47.2",
        "required_features": ['Total_Protein', 'Albumin'],
        "guideline": "Clinical Consensus",
        "criteria": "Elevated serum globulins (Total Protein - Albumin > 4.0 g/dL) caused by monoclonal gammopathy, leading to blood hyperviscosity or interference with clinical chemistry."
    }
]

# Quick indexing
DISEASE_GUIDELINES_MAP = {d["name"]: d for d in DISEASE_GUIDELINES}