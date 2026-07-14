# calculators.py

def calc_bmi(weight: float, height: float) -> float | None:
    if not height or height <= 0:
        return None
    return round(weight / ((height / 100.0) ** 2), 1)

def calc_egfr(creatinine: float, age: float, gender: str) -> float | None:
    if not creatinine or creatinine <= 0 or not age or age <= 0:
        return None
    k = 0.7 if gender == "female" else 0.9
    alpha = -0.241 if gender == "female" else -0.302
    factor = 1.012 if gender == "female" else 1.0
    
    part1 = 142.0
    part2 = min(creatinine / k, 1.0) ** alpha
    part3 = max(creatinine / k, 1.0) ** -1.200
    part4 = 0.9938 ** age
    
    return round(part1 * part2 * part3 * part4 * factor, 1)

def calc_tsat(iron: float, tibc: float) -> float | None:
    if not tibc or tibc <= 0:
        return None
    return round((iron / tibc) * 100.0, 1)

def calc_homa_ir(insulin: float, fbs: float) -> float | None:
    if not insulin or not fbs:
        return None
    return round((insulin * fbs) / 405.0, 2)

def calc_vldl(trig: float) -> float | None:
    if not trig:
        return None
    return round(trig / 5.0, 1)

def calc_non_hdl(total: float, hdl: float) -> float | None:
    if not total or not hdl:
        return None
    return round(total - hdl, 1)

def calc_ast_alt_ratio(ast: float, alt: float) -> float | None:
    if not alt or alt <= 0:
        return None
    return round(ast / alt, 2)

def calc_indirect_bilirubin(total: float, direct: float) -> float | None:
    if total is None or direct is None:
        return None
    return round(total - direct, 2)

def calc_anion_gap(na: float, cl: float, hco3: float) -> float | None:
    if na is None or cl is None or hco3 is None:
        return None
    return round(na - (cl + hco3), 1)

def calc_acr(urine_alb: float, urine_cr: float) -> float | None:
    # Accept zero values (e.g., 0 albumin), only skip if truly None or invalid urine creatinine
    if urine_alb is None or urine_cr is None or urine_cr <= 0:
        return None
    # Convert urine creatinine from mg/dL to g/dL for mg/g calculation:
    # ACR (mg/g) = (urine albumin in mg/L) / (urine creatinine in g/L)
    # Assuming urine_alb is in mg/L, urine_cr in mg/dL.
    # 1 mg/dL = 0.01 g/L, so urine_cr (g/L) = urine_cr (mg/dL) * 0.01
    # ACR = urine_alb / (urine_cr * 0.01) = (urine_alb * 100) / urine_cr
    return round((urine_alb * 100.0) / urine_cr, 1)

def calc_pcr(urine_protein: float, urine_cr: float) -> float | None:
    # Same fix: allow zero protein
    if urine_protein is None or urine_cr is None or urine_cr <= 0:
        return None
    # PCR (mg/g) = (urine protein in mg/L) / (urine creatinine in g/L)
    # urine protein in mg/L, creatinine in mg/dL -> same conversion
    return round((urine_protein * 100.0) / urine_cr, 1)

def compute_all_derived(inputs: dict, age: float, gender: str) -> dict:
    derived = {}
    
    weight = inputs.get("Weight")
    height = inputs.get("Height")
    if weight is not None and height is not None:
        bmi = calc_bmi(weight, height)
        if bmi is not None:
            derived["BMI"] = bmi
            
    creatinine = inputs.get("Creatinine")
    if creatinine is not None and age is not None:
        egfr = calc_egfr(creatinine, age, gender)
        if egfr is not None:
            derived["eGFR"] = egfr
            
    iron = inputs.get("SerumIron")
    tibc = inputs.get("TIBC")
    if iron is not None and tibc is not None:
        tsat = calc_tsat(iron, tibc)
        if tsat is not None:
            derived["Transferrin_Sat"] = tsat
            
    insulin = inputs.get("Insulin")
    fbs = inputs.get("FBS")
    if insulin is not None and fbs is not None:
        homa = calc_homa_ir(insulin, fbs)
        if homa is not None:
            derived["HOMA_IR"] = homa
            
    trig = inputs.get("Triglycerides")
    if trig is not None:
        vldl = calc_vldl(trig)
        if vldl is not None:
            derived["VLDL"] = vldl
            
    tc = inputs.get("Total_Cholesterol")
    hdl = inputs.get("HDL")
    if tc is not None and hdl is not None:
        non_hdl = calc_non_hdl(tc, hdl)
        if non_hdl is not None:
            derived["Non_HDL"] = non_hdl
            
    ast = inputs.get("AST")
    alt = inputs.get("ALT")
    if ast is not None and alt is not None:
        ratio = calc_ast_alt_ratio(ast, alt)
        if ratio is not None:
            derived["AST_ALT_Ratio"] = ratio
            
    t_bil = inputs.get("Total_Bilirubin")
    d_bil = inputs.get("Direct_Bilirubin")
    if t_bil is not None and d_bil is not None:
        indir = calc_indirect_bilirubin(t_bil, d_bil)
        if indir is not None:
            derived["Indirect_Bilirubin"] = indir
            
    na = inputs.get("Sodium")
    cl = inputs.get("Chloride")
    hco3 = inputs.get("Bicarbonate")
    if na is not None and cl is not None and hco3 is not None:
        gap = calc_anion_gap(na, cl, hco3)
        if gap is not None:
            derived["Anion_Gap"] = gap
            
    urine_alb = inputs.get("UrineAlbumin")
    urine_cr = inputs.get("UrineCreatinine")
    if urine_alb is not None and urine_cr is not None:
        acr = calc_acr(urine_alb, urine_cr)
        if acr is not None:
            derived["ACR"] = acr

    # For PCR, we need a quantitative urine protein value (mg/L).
    # If such a field exists (e.g., "UrineProteinQuantitative"), use it.
    urine_prot_quant = inputs.get("UrineProteinQuantitative")
    if urine_prot_quant is not None and urine_cr is not None:
        pcr = calc_pcr(urine_prot_quant, urine_cr)
        if pcr is not None:
            derived["PCR"] = pcr
            
    return derived