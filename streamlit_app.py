"""Streamlit Cloud version of MedMultiSync.
Can be deployed 100% free forever on Streamlit Community Cloud (share.streamlit.io).
"""

import streamlit as st
from PIL import Image
import numpy as np

from medmultisync.data_presets import CLINICAL_PRESETS
from medmultisync.model import ClinicalDiagnosticEngine

st.set_page_config(
    page_title="MedMultiSync - Multimodal Healthcare AI",
    page_icon="🩺",
    layout="wide",
)


@st.cache_resource
def get_engine():
    return ClinicalDiagnosticEngine()


engine = get_engine()

st.title("🩺 MedMultiSync: Multimodal Clinical Decision Support System")
st.markdown(
    """
    **Fusing Medical Imaging, EHR Vitals, and Physician Notes (IEEE JBHI Architecture)**  
    *Speakers: Bezaleel Paul N · Adithya Ramesh · Akash Rajpurohit | B.Tech Computer Science and Engineering*
    """
)
st.divider()

# Quick Presets
st.subheader("⚡ 1. Select a Clinical Preset")
col_b1, col_b2, col_b3, col_b4 = st.columns(4)

if "current_case" not in st.session_state:
    st.session_state["current_case"] = "Bacterial Pneumonia"

if col_b1.button("📋 Case 1: Pneumonia", use_container_width=True):
    st.session_state["current_case"] = "Bacterial Pneumonia"
if col_b2.button("🫀 Case 2: Cardiomegaly", use_container_width=True):
    st.session_state["current_case"] = "Cardiomegaly"
if col_b3.button("🫁 Case 3: Atelectasis", use_container_width=True):
    st.session_state["current_case"] = "Atelectasis"
if col_b4.button("🩺 Case 4: Normal Screening", use_container_width=True):
    st.session_state["current_case"] = "Normal Baseline"

selected_preset = CLINICAL_PRESETS[st.session_state["current_case"]]
preset_v = selected_preset["vitals"]

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("📥 Patient Input Modalities")
    st.markdown("**Modality 1: Chest Radiograph**")
    uploaded_file = st.file_uploader("Upload X-Ray (or use preset below):", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        input_image = Image.open(uploaded_file)
    else:
        input_image = Image.open(selected_preset["image_path"])

    st.image(input_image, caption=selected_preset["name"], use_container_width=True)

    st.markdown("**Modality 2: EHR Vitals & Lab Biomarkers**")
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        age = st.slider("Age (years)", 18, 95, int(preset_v["age"]))
        hr = st.slider("Heart Rate (bpm)", 40, 160, int(preset_v["heart_rate"]))
        rr = st.slider("Respiration Rate (/min)", 10, 40, int(preset_v["resp_rate"]))
        spo2 = st.slider("SpO2 Saturation (%)", 70, 100, int(preset_v["spo2"]))
    with v_col2:
        temp = st.slider("Body Temp (°C)", 35.0, 41.0, float(preset_v["temp_c"]), step=0.1)
        bp = st.slider("Systolic BP (mmHg)", 80, 220, int(preset_v["systolic_bp"]))
        wbc = st.slider("WBC (x10³/µL)", 2.0, 30.0, float(preset_v["wbc"]), step=0.1)

    st.markdown("**Modality 3: Physician Notes & Chief Complaint**")
    notes = st.text_area("Patient Narrative History:", value=selected_preset["notes"], height=100)

    diagnose_clicked = st.button("🔬 Run Multimodal Diagnostic Assessment", type="primary", use_container_width=True)

with col_right:
    st.subheader("📊 Diagnostic Outputs & Explainability")

    # Run inference
    vitals_dict = {
        "age": age,
        "heart_rate": hr,
        "resp_rate": rr,
        "spo2": spo2,
        "temp_c": temp,
        "systolic_bp": bp,
        "wbc": wbc,
    }

    result = engine.diagnose(input_image, vitals_dict, notes)

    st.success(f"**Primary Consensus Verdict:** `{result['prediction'].upper()}` ({result['confidence']*100:.1f}% confidence)")

    if result["clinical_alerts"]:
        alert_str = "  ·  ".join([f"⚠️ **{k}:** {v}" for k, v in result["clinical_alerts"].items()])
        st.warning(alert_str)

    st.markdown("#### Differential Probabilities")
    for cls_name, prob in result["probabilities"].items():
        st.write(f"**{cls_name}**: `{prob*100:.1f}%`")
        st.progress(min(1.0, max(0.0, prob)))

    st.markdown("#### Grad-CAM Anatomical Saliency Heatmap")
    st.image(result["gradcam_image"], caption="Grad-CAM visual localization superimposed on radiograph", use_container_width=True)

    st.markdown("#### Modality Attribution Breakdown")
    attrib = result["modality_attribution"]
    st.table(
        {
            "Modality": ["🩻 Medical Imaging", "📈 EHR Vitals & Labs", "📝 Clinical Notes"],
            "Contribution": [f"{attrib['Medical Imaging']}%", f"{attrib['EHR Vitals & Labs']}%", f"{attrib['Clinical Notes / Symptoms']}%"],
            "Role": ["Spatial Feature Extraction (Grad-CAM)", "Physiological z-score scaling", "Symptom terminology grounding"],
        }
    )

    with st.expander("📄 View Full Clinical SOAP Note", expanded=True):
        st.markdown(result["clinical_report"])
