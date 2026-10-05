"""Clinical case presets for MedMultiSync demonstration.
Includes raw vital signs, chief complaints, and image filepaths for:
1. Bacterial Pneumonia
2. Cardiomegaly / Congestive Heart Failure
3. Atelectasis / Pulmonary Volume Loss
4. Normal Baseline Radiograph
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SAMPLES_DIR = BASE_DIR / "samples"

CLINICAL_PRESETS = {
    "Bacterial Pneumonia": {
        "name": "Case 1: Acute Bacterial Lobar Pneumonia",
        "description": "64-year-old male presenting with acute high fever, purulent cough, and right lower lobe consolidation.",
        "image_path": str(SAMPLES_DIR / "case_pneumonia.png"),
        "vitals": {
            "age": 64,
            "heart_rate": 108,
            "resp_rate": 26,
            "spo2": 91,
            "temp_c": 39.2,
            "systolic_bp": 118,
            "wbc": 16.4,
        },
        "notes": (
            "Patient presents to the Emergency Department with 3 days of shaking chills, "
            "high fevers, and acute productive cough with rust-colored sputum. Right-sided "
            "pleuritic chest pain on inspiration. Auscultation reveals bronchial breath sounds "
            "and localized coarse inspiratory crackles in the right lower lung base. Suspected "
            "bacterial pneumonia consolidation."
        ),
        "expected_diagnosis": "Bacterial Pneumonia",
    },
    "Cardiomegaly": {
        "name": "Case 2: Cardiomegaly & Congestive Heart Failure",
        "description": "72-year-old female presenting with progressive orthopnea, bilateral pedal edema, and cardiomegaly.",
        "image_path": str(SAMPLES_DIR / "case_cardiomegaly.png"),
        "vitals": {
            "age": 72,
            "heart_rate": 96,
            "resp_rate": 22,
            "spo2": 93,
            "temp_c": 36.8,
            "systolic_bp": 168,
            "wbc": 7.8,
        },
        "notes": (
            "Patient reports 2-week history of worsening shortness of breath and dyspnea on exertion. "
            "Notable 3-pillow orthopnea and paroxysmal nocturnal dyspnea. Physical exam shows "
            "bilateral 2+ pitting lower extremity edema and elevated jugular venous pressure. "
            "Radiograph demonstrates massive cardiomegaly with cardiothoracic ratio exceeding 0.60 "
            "and prominent hilar vascular engorgement."
        ),
        "expected_diagnosis": "Cardiomegaly / Heart Failure",
    },
    "Atelectasis": {
        "name": "Case 3: Bibasilar Plate Atelectasis",
        "description": "58-year-old post-operative patient with shallow respiration, splinting, and lung volume loss.",
        "image_path": str(SAMPLES_DIR / "case_atelectasis.png"),
        "vitals": {
            "age": 58,
            "heart_rate": 84,
            "resp_rate": 18,
            "spo2": 93,
            "temp_c": 37.7,
            "systolic_bp": 128,
            "wbc": 9.2,
        },
        "notes": (
            "Post-operative Day 2 following upper abdominal laparoscopic surgery. Patient exhibiting "
            "shallow tidal breathing due to incisional splinting pain. Auscultation notes diminished "
            "breath sounds at bilateral lung bases with faint end-expiratory crackles. Chest radiograph "
            "reveals linear band-like bibasilar opacities and slight diaphragm elevation consistent "
            "with compressive discoid atelectasis."
        ),
        "expected_diagnosis": "Atelectasis / Infiltration",
    },
    "Normal Baseline": {
        "name": "Case 4: Healthy Baseline Checkup",
        "description": "45-year-old healthy adult presenting for routine executive health clearance.",
        "image_path": str(SAMPLES_DIR / "case_normal.png"),
        "vitals": {
            "age": 45,
            "heart_rate": 72,
            "resp_rate": 14,
            "spo2": 99,
            "temp_c": 36.9,
            "systolic_bp": 120,
            "wbc": 6.8,
        },
        "notes": (
            "Asymptomatic 45-year-old individual presenting for routine annual corporate health checkup. "
            "No complaints of cough, fever, chest pain, or shortness of breath. Clear bilateral vesicular "
            "breath sounds. Chest radiograph confirms well-expanded lung fields, sharp bilateral "
            "costophrenic sulci, and normal cardiac contours without focal consolidation or effusion."
        ),
        "expected_diagnosis": "Normal / Clear Study",
    },
}
