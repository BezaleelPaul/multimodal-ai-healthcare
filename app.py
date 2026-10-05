"""MedMultiSync: Multimodal Clinical Decision Support System.
Interactive Gradio Application for Live Cloud & Local Demonstrations.
Fuses Chest Radiography, EHR Vitals, and Physician Notes (IEEE JBHI Architecture).
"""

import sys
from pathlib import Path
from PIL import Image
import gradio as gr

# Ensure medmultisync package is in path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from medmultisync.data_presets import CLINICAL_PRESETS
from medmultisync.model import ClinicalDiagnosticEngine

# Initialize diagnostic engine
print("Loading MedMultiSync Multimodal Engine...")
engine = ClinicalDiagnosticEngine()
print("Ready!")


def analyze_multimodal_case(
    image,
    age,
    heart_rate,
    resp_rate,
    spo2,
    temp_c,
    systolic_bp,
    wbc,
    clinical_notes,
):
    """Run multimodal diagnostic inference."""
    if image is None:
        # Default to normal sample if none uploaded
        sample_path = BASE_DIR / "samples" / "case_normal.png"
        image = Image.open(sample_path)
    elif not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    vitals = {
        "age": float(age),
        "heart_rate": float(heart_rate),
        "resp_rate": float(resp_rate),
        "spo2": float(spo2),
        "temp_c": float(temp_c),
        "systolic_bp": float(systolic_bp),
        "wbc": float(wbc),
    }

    result = engine.diagnose(image, vitals, clinical_notes or "")

    # Format probability dictionary for Gradio Label
    probs_dict = {k: round(v, 4) for k, v in result["probabilities"].items()}

    # Format modality attribution string
    attrib = result["modality_attribution"]
    attrib_md = (
        f"| Modality | Contribution | Role |\n"
        f"| :--- | :--- | :--- |\n"
        f"| 🩻 **Medical Imaging (Chest X-Ray)** | **{attrib['Medical Imaging']}%** | Spatial feature extraction (Grad-CAM) |\n"
        f"| 📈 **EHR Vitals & Lab Biomarkers** | **{attrib['EHR Vitals & Labs']}%** | Physiological z-score risk scaling |\n"
        f"| 📝 **Clinical Notes & History** | **{attrib['Clinical Notes / Symptoms']}%** | Semantic symptomatology grounding |\n"
    )

    return (
        probs_dict,
        result["gradcam_image"],
        attrib_md,
        result["clinical_report"],
    )


def load_preset(case_name):
    """Load clinical preset values into UI components."""
    preset = CLINICAL_PRESETS[case_name]
    img = Image.open(preset["image_path"])
    v = preset["vitals"]
    return (
        img,
        v["age"],
        v["heart_rate"],
        v["resp_rate"],
        v["spo2"],
        v["temp_c"],
        v["systolic_bp"],
        v["wbc"],
        preset["notes"],
    )


# Build Gradio UI
with gr.Blocks(
    title="MedMultiSync: Multimodal AI in Healthcare",
    theme=gr.themes.Soft(primary_hue="cyan", neutral_hue="slate"),
) as demo:
    gr.Markdown(
        """
        # 🩺 MedMultiSync: Multimodal Clinical Decision Support System
        ### Fusing Medical Imaging, EHR Vitals, and Physician Notes (IEEE JBHI Architecture)
        **Speakers:** Bezaleel Paul N · Adithya Ramesh · Akash Rajpurohit &nbsp;|&nbsp; **Academic Seminar:** B.Tech Computer Science and Engineering  
        *Grounded in IEEE Journal of Biomedical and Health Informatics & IEEE Transactions on Biomedical Engineering.*
        ---
        """
    )

    gr.Markdown("### ⚡ Step 1: Select a Clinical Preset or Enter Custom Data")
    with gr.Row():
        btn_pneu = gr.Button("📋 Case 1: Bacterial Pneumonia", variant="primary")
        btn_card = gr.Button("🫀 Case 2: Cardiomegaly / Heart Failure", variant="primary")
        btn_atel = gr.Button("🫁 Case 3: Bibasilar Atelectasis", variant="primary")
        btn_norm = gr.Button("🩺 Case 4: Normal Healthy Checkup", variant="secondary")

    with gr.Row():
        # Left column: Multimodal inputs
        with gr.Column(scale=5):
            gr.Markdown("### 📥 Patient Input Modalities")
            input_image = gr.Image(
                label="Modality 1: Chest Radiograph (X-Ray)",
                type="pil",
                height=320,
            )

            with gr.Accordion("Modality 2: Patient EHR Vitals & Laboratory Biomarkers", open=True):
                with gr.Row():
                    age_slider = gr.Slider(18, 95, value=64, step=1, label="Age (years)")
                    hr_slider = gr.Slider(40, 160, value=108, step=1, label="Heart Rate (bpm)")
                    rr_slider = gr.Slider(10, 40, value=26, step=1, label="Respiration Rate (/min)")

                with gr.Row():
                    spo2_slider = gr.Slider(70, 100, value=91, step=1, label="SpO2 Oxygen Saturation (%)")
                    temp_slider = gr.Slider(35.0, 41.0, value=39.2, step=0.1, label="Body Temperature (°C)")

                with gr.Row():
                    bp_slider = gr.Slider(80, 220, value=118, step=1, label="Systolic BP (mmHg)")
                    wbc_slider = gr.Slider(2.0, 30.0, value=16.4, step=0.1, label="WBC Count (x10³/µL)")

            notes_input = gr.Textbox(
                label="Modality 3: Physician Chief Complaint & Examination Notes",
                lines=4,
                placeholder="Enter patient narrative history, auscultation findings, and presenting symptoms...",
                value=CLINICAL_PRESETS["Bacterial Pneumonia"]["notes"],
            )

            diagnose_btn = gr.Button("🔬 Run Multimodal Diagnostic Assessment", variant="primary", size="lg")

        # Right column: Explainable outputs
        with gr.Column(scale=5):
            gr.Markdown("### 📊 Diagnostic Outputs & Multimodal Explainability")
            pred_label = gr.Label(label="Multimodal Diagnostic Probability Consensus", num_top_classes=4)

            with gr.Row():
                gradcam_out = gr.Image(
                    label="Explainability: Grad-CAM Anatomical Saliency Heatmap",
                    type="numpy",
                    height=300,
                )

            gr.Markdown("#### ⚖️ Modality Attribution Decomposition (Cross-Attention Gating)")
            attrib_table = gr.Markdown()

            with gr.Accordion("📄 Full Clinical SOAP Impression Report", open=True):
                report_out = gr.Markdown()

    # Preset button click handlers
    btn_pneu.click(
        fn=lambda: load_preset("Bacterial Pneumonia"),
        outputs=[input_image, age_slider, hr_slider, rr_slider, spo2_slider, temp_slider, bp_slider, wbc_slider, notes_input],
    )
    btn_card.click(
        fn=lambda: load_preset("Cardiomegaly"),
        outputs=[input_image, age_slider, hr_slider, rr_slider, spo2_slider, temp_slider, bp_slider, wbc_slider, notes_input],
    )
    btn_atel.click(
        fn=lambda: load_preset("Atelectasis"),
        outputs=[input_image, age_slider, hr_slider, rr_slider, spo2_slider, temp_slider, bp_slider, wbc_slider, notes_input],
    )
    btn_norm.click(
        fn=lambda: load_preset("Normal Baseline"),
        outputs=[input_image, age_slider, hr_slider, rr_slider, spo2_slider, temp_slider, bp_slider, wbc_slider, notes_input],
    )

    # Diagnostic trigger
    diagnose_btn.click(
        fn=analyze_multimodal_case,
        inputs=[input_image, age_slider, hr_slider, rr_slider, spo2_slider, temp_slider, bp_slider, wbc_slider, notes_input],
        outputs=[pred_label, gradcam_out, attrib_table, report_out],
    )


if __name__ == "__main__":
    # Initialize with default preset image
    default_img = Image.open(CLINICAL_PRESETS["Bacterial Pneumonia"]["image_path"])
    demo.launch(server_name="127.0.0.1", server_port=7860, share=True)
