"""Slides 1-14: Multimodal Artificial Intelligence in Healthcare.
Covers clinical motivation, modality taxonomy, IEEE fusion paradigms,
cross-attention architectures, foundation models, clinical workflows,
technical bottlenecks, IEEE standards, and the companion MedMultiSync project.
"""

from .theme import (
    AMBER,
    BG,
    BG_SOFT,
    CYAN,
    DASH,
    DIM,
    EMERALD,
    HAIRLINE,
    INDIGO,
    MUTED,
    PANEL,
    PANEL_2,
    PANEL_3,
    ROSE,
    SKY,
    VIOLET,
    WHITE,
    arrow,
    box,
    chrome,
    elbow,
    mix,
    new_slide,
    node,
    note_bar,
    panel,
    section_head,
    tag,
    tbox,
)

FOOTER = "Multimodal AI in Healthcare  |  IEEE Seminar  |  Presenter: Bezaleel Paul N"


# ------------------------------------------------------------------ Slide 1: Title ---
def slide_title(prs):
    s = new_slide(prs)
    box(s, 0, 0, 13.333, 0.12, fill=CYAN, kind="rect")
    box(s, 0, 0.12, 13.333, 0.02, fill=mix(SKY, BG, 0.55), kind="rect")

    # Concentric clinical signal rings (decorative)
    for d, col in (
        (5.2, mix(HAIRLINE, BG, 0.70)),
        (3.8, mix(HAIRLINE, BG, 0.50)),
        (2.4, mix(CYAN, BG, 0.85)),
        (1.2, mix(SKY, BG, 0.75)),
    ):
        box(
            s,
            12.2 - d / 2,
            6.2 - d / 2,
            d,
            d,
            fill=None,
            line=col,
            lw=1.0,
            kind="oval",
        )

    # Kicker / Topic category tag
    tag(s, 0.85, 1.25, "IEEE SEMINAR  ·  ADVANCED ARTIFICIAL INTELLIGENCE", color=CYAN, size=9.5, h=0.32)

    # Main Title & Subtitle
    tbox(s, 0.85, 1.70, 10.5, 0.80, "MULTIMODAL AI IN HEALTHCARE", size=36, bold=True, color=WHITE)
    tbox(
        s,
        0.85,
        2.55,
        10.5,
        0.50,
        "Fusing Medical Imaging, Clinical Text, and EHR Signals for Precision Diagnostics",
        size=17.5,
        color=SKY,
    )

    # 4 Key Modality Badges
    modalities = [
        ("RADIOLOGY & PATHOLOGY", "Chest X-Ray, CT, MRI, WSI", CYAN),
        ("CLINICAL NLP & NOTES", "EHR, Discharge, Findings", VIOLET),
        ("PHYSIOLOGICAL TELEMETRY", "ECG, Vitals, SpO2, Labs", EMERALD),
        ("HIGH-DIMENSIONAL OMICS", "Genomics, RNA-seq, Biomarkers", AMBER),
    ]
    card_w = 2.75
    for i, (m_title, m_desc, col) in enumerate(modalities):
        cx = 0.85 + i * (card_w + 0.25)
        cy = 3.65
        panel(s, cx, cy, card_w, 1.55, fill=PANEL, line=mix(col, BG, 0.55), radius=0.08)
        tag(s, cx + 0.18, cy + 0.18, f"MODALITY 0{i+1}", color=col, size=8.0, h=0.22)
        tbox(s, cx + 0.18, cy + 0.48, card_w - 0.36, 0.40, m_title, size=11.5, bold=True, color=WHITE)
        tbox(s, cx + 0.18, cy + 0.95, card_w - 0.36, 0.45, m_desc, size=10.0, color=MUTED)

    # Presenter Information Footer Card
    panel(s, 0.85, 5.55, 11.65, 1.15, fill=PANEL_2, line=HAIRLINE, radius=0.08)
    tbox(s, 1.15, 5.70, 6.0, 0.38, "Presenter: Bezaleel Paul N", size=15, bold=True, color=WHITE)
    tbox(s, 1.15, 6.12, 6.0, 0.38, "B.Tech Computer Science and Engineering  |  Academic Seminar", size=11, color=MUTED)
    tbox(s, 7.20, 5.70, 5.0, 0.38, "Companion Project: MedMultiSync (Live Colab Demo)", size=12, bold=True, color=EMERALD, align="r")
    tbox(s, 7.20, 6.12, 5.0, 0.38, "Grounded in IEEE JBHI, IEEE TBME & Nature Medicine literature", size=10.5, color=DIM, align="r")


# ------------------------------------------------------------------ Slide 2: Roadmap ---
def slide_roadmap(prs):
    s = new_slide(prs)
    chrome(
        s,
        2,
        kicker="Agenda & Structure",
        title="Executive Summary & Presentation Roadmap",
        sub="A systematic exploration from clinical limitations of unimodal models to IEEE fusion architectures and our live cloud demonstration.",
        footer=FOOTER,
    )

    pillars = [
        ("01", "The Clinical Imperative", "Why Unimodal Models Fail", "Clinical diagnostics require holistic reasoning across imaging, vitals, and physician notes.", CYAN),
        ("02", "Taxonomy & Data Spectrum", "Heterogeneous Health Modalities", "Radiological pixels, unstructured clinical narratives, discrete lab vitals, and molecular genomics.", SKY),
        ("03", "Data Fusion Paradigms", "IEEE Taxonomic Framework", "Early vs. Intermediate Cross-Attention vs. Late decision pooling, plus contrastive alignment.", VIOLET),
        ("04", "Foundation Models (SOTA)", "BioMedCLIP to Med-Flamingo", "Zero-shot cross-modal pretraining and multimodal clinical in-context reasoning at scale.", AMBER),
        ("05", "Translational Challenges", "Missing Data & Safety", "Modality imputation, medical hallucination safeguards, HIPAA federated learning, IEEE P2801.", ROSE),
        ("06", "MedMultiSync & Live Demo", "End-to-End System in Colab", "Interactive multimodal decision support with Grad-CAM visual heatmaps and clinical impression generation.", EMERALD),
    ]

    for i, (num, title, subtitle, desc, col) in enumerate(pillars):
        col_idx = i % 3
        row_idx = i // 3
        px = 0.85 + col_idx * 3.95
        py = 1.85 + row_idx * 2.45
        pw, ph = 3.75, 2.25

        panel(s, px, py, pw, ph, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        # Number badge
        node(s, px + 0.20, py + 0.20, 0.60, 0.45, num, fill=mix(col, BG, 0.80), line=col, color=col, size=13, bold=True)
        tbox(s, px + 0.95, py + 0.20, pw - 1.15, 0.28, title, size=12.5, bold=True, color=WHITE)
        tbox(s, px + 0.95, py + 0.48, pw - 1.15, 0.25, subtitle, size=10, color=col)
        box(s, px + 0.20, py + 0.80, pw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, px + 0.20, py + 0.95, pw - 0.40, 1.15, desc, size=11, color=MUTED, spacing=1.2)


# ------------------------------------------------------------------ Slide 3: Clinical Imperative ---
def slide_clinical_imperative(prs):
    s = new_slide(prs)
    chrome(
        s,
        3,
        kicker="Motivation & Clinical Reality",
        title="The Clinical Imperative: Why Healthcare Must Be Multimodal",
        sub="Isolated scans produce diagnostic ambiguity. Only the synthesis of imaging, physiology, and history unlocks definitive patient care.",
        footer=FOOTER,
    )

    # Left: Unimodal limitation scenario
    lx, ly, lw, lh = 0.85, 1.85, 5.65, 4.30
    panel(s, lx, ly, lw, lh, fill=PANEL, line=mix(ROSE, BG, 0.55), radius=0.08)
    tag(s, lx + 0.25, ly + 0.25, "UNIMODAL AI  ·  DIAGNOSTIC AMBIGUITY", color=ROSE, size=8.5)
    tbox(s, lx + 0.25, ly + 0.65, lw - 0.50, 0.40, "Scenario: Isolated Chest Radiograph", size=14, bold=True, color=WHITE)

    steps = [
        ("Visual Finding", "Dense opacity observed in right lower lung zone.", ROSE),
        ("Differential Diagnoses", "Could represent Bacterial Pneumonia, Atelectasis, or Pleural Effusion.", AMBER),
        ("Unimodal Failure", "Pixel information alone cannot establish etiology; risks erroneous treatment protocol.", ROSE),
    ]
    for idx, (stitle, sdesc, scol) in enumerate(steps):
        sy = ly + 1.15 + idx * 0.95
        panel(s, lx + 0.25, sy, lw - 0.50, 0.82, fill=PANEL_2, line=mix(scol, BG, 0.70), radius=0.06)
        node(s, lx + 0.40, sy + 0.15, 0.32, 0.52, "!", fill=mix(scol, BG, 0.75), line=scol, color=scol, size=11, bold=True)
        tbox(s, lx + 0.85, sy + 0.12, lw - 1.20, 0.60, [f"{stitle}:", sdesc], size=10.5, color=MUTED, spacing=1.1)

    # Right: Multimodal synthesis
    rx, ry, rw, rh = 6.85, 1.85, 5.65, 4.30
    panel(s, rx, ry, rw, rh, fill=PANEL, line=mix(EMERALD, BG, 0.55), radius=0.08)
    tag(s, rx + 0.25, ry + 0.25, "MULTIMODAL AI  ·  HOLISTIC PRECISION", color=EMERALD, size=8.5)
    tbox(s, rx + 0.25, ry + 0.65, rw - 0.50, 0.40, "Resolution: Context-Aware Multimodal Fusion", size=14, bold=True, color=WHITE)

    m_steps = [
        ("Imaging Feature", "Right lower lobe airspace consolidation (ResNet/ViT feature map).", CYAN),
        ("Clinical Vitals / Lab", "Body Temp 39.2°C, SpO2 91%, WBC 16.4x10^3/uL -> Indicates active infection.", EMERALD),
        ("Doctor's Narrative", "3-day history of shaking chills, purulent sputum, localized crackles.", SKY),
        ("Unified Multimodal Output", "Definitive Bacterial Pneumonia (>97% calibrated confidence) + Targeted antibiotic regimen.", EMERALD),
    ]
    for idx, (stitle, sdesc, scol) in enumerate(m_steps):
        sy = ry + 1.15 + idx * 0.72
        panel(s, rx + 0.25, sy, rw - 0.50, 0.62, fill=PANEL_2, line=mix(scol, BG, 0.70), radius=0.06)
        node(s, rx + 0.40, sy + 0.10, 0.30, 0.42, "✓", fill=mix(scol, BG, 0.75), line=scol, color=scol, size=10, bold=True)
        tbox(s, rx + 0.82, sy + 0.08, rw - 1.15, 0.48, [f"{stitle}:", sdesc], size=10.0, color=MUTED, spacing=1.1)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "CLINICAL BENCHMARK (IEEE JBHI 2024)", "Multimodal fusion achieves a +18.4% to +23.6% AUROC improvement over unimodal vision models across the MIMIC-IV and CheXpert cohorts.", accent=CYAN)


# ------------------------------------------------------------------ Slide 4: Modality Spectrum ---
def slide_modality_spectrum(prs):
    s = new_slide(prs)
    chrome(
        s,
        4,
        kicker="Healthcare Data Architecture",
        title="The Medical Modality Spectrum",
        sub="Healthcare encompasses the most heterogeneous data landscape of any industry: spatial, temporal, narrative, and genomic.",
        footer=FOOTER,
    )

    quads = [
        (
            "01. UNSTRUCTURED IMAGING",
            "High-Dimensional Spatial Tensors",
            [
                "Radiology: 2D Chest X-Ray, 3D CT volumetrics, multi-sequence MRI.",
                "Digital Pathology: Whole Slide Images (WSI) reaching 100,000 x 100,000 px.",
                "Point-of-Care: Ultrasound Doppler, Dermoscopy, Retinal Fundus photography.",
                "Model Backbones: Vision Transformers (ViT), Swin, ConvNeXt.",
            ],
            CYAN,
        ),
        (
            "02. UNSTRUCTURED CLINICAL TEXT",
            "Dense Domain-Specific Language",
            [
                "EHR Progress Notes: SOAP notes, admission histories, nursing logs.",
                "Diagnostic Reports: Formal radiology impressions, pathology summaries.",
                "Challenges: Heavy medical abbreviations, negation ('no pneumothorax'), syntax noise.",
                "Model Backbones: ClinicalBERT, BioLinkBERT, Med-PaLM.",
            ],
            VIOLET,
        ),
        (
            "03. STRUCTURED & TEMPORAL EHR",
            "Discrete & Streaming Biomarkers",
            [
                "Vital Signs: Heart Rate, Blood Pressure, Respiratory Rate, SpO2, Temperature.",
                "Laboratory Panels: Comprehensive metabolic panels (CMP), CBC, arterial blood gas.",
                "ICU Continuous Telemetry: High-frequency 12-lead ECG, EEG waveforms.",
                "Model Backbones: Temporal CNNs, Bi-LSTM, TabNet, Transformer Encoders.",
            ],
            EMERALD,
        ),
        (
            "04. HIGH-DIMENSIONAL OMICS",
            "Molecular & Genomic Profiling",
            [
                "Genomics: Whole Exome / Genome Sequencing (WGS), single-nucleotide variants.",
                "Transcriptomics & Proteomics: RNA-seq gene expression matrices, cell markers.",
                "Clinical Goal: Targeted oncological therapy, pharmacogenomics, immunotherapy response.",
                "Model Backbones: Graph Neural Networks (GNNs), Pathway-informed MLPs.",
            ],
            AMBER,
        ),
    ]

    for i, (qtitle, qsub, bullet_list, col) in enumerate(quads):
        qx = 0.85 + (i % 2) * 5.95
        qy = 1.85 + (i // 2) * 2.50
        qw, qh = 5.70, 2.32

        panel(s, qx, qy, qw, qh, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, qx + 0.20, qy + 0.20, qtitle, color=col, size=8.5)
        tbox(s, qx + 0.20, qy + 0.50, qw - 0.40, 0.32, qsub, size=11.5, bold=True, color=WHITE)
        box(s, qx + 0.20, qy + 0.85, qw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, qx + 0.20, qy + 0.95, qw - 0.40, 1.25, [f"• {b}" for b in bullet_list], size=10.0, color=MUTED, spacing=1.18)


# ------------------------------------------------------------------ Slide 5: Fusion Paradigms ---
def slide_fusion_paradigms(prs):
    s = new_slide(prs)
    chrome(
        s,
        5,
        kicker="IEEE JBHI Taxonomic Framework",
        title="Multimodal Fusion Paradigms in Deep Learning",
        sub="Classifying how and when heterogeneous medical signals intersect to form a unified clinical latent representation.",
        footer=FOOTER,
    )

    schemes = [
        (
            "EARLY FUSION",
            "Data / Raw Feature Level",
            "Raw inputs or low-level feature vectors are concatenated before entering the primary network.",
            [
                ("Advantages", "Captures low-level cross-correlations early; simple single-model pipeline.", EMERALD),
                ("Vulnerabilities", "Highly sensitive to missing modalities; severe dimensionality mismatch.", ROSE),
                ("Clinical Fit", "Co-registered multi-sequence imaging (e.g., T1/T2/FLAIR MRI fusion).", CYAN),
            ],
            CYAN,
        ),
        (
            "INTERMEDIATE / JOINT FUSION",
            "Cross-Attention & Shared Latent Space",
            "Dedicated modality encoders project into a shared embedding space with cross-modal attention mechanisms.",
            [
                ("Advantages", "Dynamically attends to relevant modalities; preserves modality-specific features; resilient.", EMERALD),
                ("Vulnerabilities", "Architectural complexity; requires paired pretraining data & larger compute budget.", ROSE),
                ("Clinical Fit", "Vision-Language-EHR diagnosis (BioMedCLIP, Med-Flamingo, MedMultiSync).", VIOLET),
            ],
            VIOLET,
        ),
        (
            "LATE FUSION",
            "Decision / Ensemble Level",
            "Unimodal networks are trained independently; their final prediction probabilities are pooled.",
            [
                ("Advantages", "Tolerates missing modalities natively; modular components can be upgraded independently.", EMERALD),
                ("Vulnerabilities", "Cannot learn complex non-linear cross-modal interactions or feature synergies.", ROSE),
                ("Clinical Fit", "Hospital department ensembles (Radiology AI score + Pathology AI score).", AMBER),
            ],
            AMBER,
        ),
    ]

    for i, (name, subtitle, desc, items, col) in enumerate(schemes):
        sx = 0.85 + i * 3.95
        sy = 1.85
        sw, sh = 3.75, 4.35

        panel(s, sx, sy, sw, sh, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, sx + 0.20, sy + 0.20, name, color=col, size=9.0)
        tbox(s, sx + 0.20, sy + 0.52, sw - 0.40, 0.32, subtitle, size=12, bold=True, color=WHITE)
        tbox(s, sx + 0.20, sy + 0.88, sw - 0.40, 0.65, desc, size=10.5, color=MUTED, spacing=1.15)
        box(s, sx + 0.20, sy + 1.55, sw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")

        for j, (lead, body, icol) in enumerate(items):
            iy = sy + 1.70 + j * 0.85
            panel(s, sx + 0.15, iy, sw - 0.30, 0.75, fill=PANEL_2, line=mix(icol, BG, 0.70), radius=0.06)
            tbox(s, sx + 0.25, iy + 0.10, sw - 0.50, 0.58, [f"{lead}:", body], size=9.8, color=MUTED, spacing=1.1)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "IEEE SURVEY CONSENSUS", "Intermediate Cross-Attention Fusion has emerged as the clear empirical gold standard across medical benchmarks, providing optimal balance between expressiveness and clinical robustness.", accent=VIOLET)


# ------------------------------------------------------------------ Slide 6: Cross-Attention Arch ---
def slide_cross_attention_arch(prs):
    s = new_slide(prs)
    chrome(
        s,
        6,
        kicker="Neural Architecture Deep-Dive",
        title="Cross-Modal Attention: How Vision & Text Interlock",
        sub="Mathematical alignment: Clinical text queries dynamically attend to spatial image patches to ground diagnostic evidence.",
        footer=FOOTER,
    )

    # Left: Architectural Flow
    lx, ly, lw, lh = 0.85, 1.85, 7.80, 4.30
    panel(s, lx, ly, lw, lh, fill=PANEL, line=HAIRLINE, radius=0.08)
    section_head(s, lx + 0.25, ly + 0.25, lw - 0.50, "Dual-Stream Cross-Attention Dataflow", color=CYAN)

    inputs = [
        ("Medical Image\n(Chest X-Ray / CT)", CYAN, 2.45),
        ("Clinical Vitals / Labs\n(HR, SpO2, Temp, WBC)", EMERALD, 3.45),
        ("Doctor's Notes\n('Purulent cough, crackles')", VIOLET, 4.45),
    ]
    for text, col, iy in inputs:
        node(s, lx + 0.35, iy, 2.10, 0.72, text, fill=mix(col, BG, 0.80), line=col, color=WHITE, size=10, bold=True)
        arrow(s, lx + 2.45, iy + 0.36, lx + 3.05, iy + 0.36, color=col, w=1.5)

    encoders = [
        ("Vision Encoder\n(ViT / ResNet)", CYAN, 2.45),
        ("Tabular MLP\n(Norm + Embed)", EMERALD, 3.45),
        ("Clinical NLP\n(ClinicalBERT)", VIOLET, 4.45),
    ]
    for text, col, ey in encoders:
        node(s, lx + 3.05, ey, 1.90, 0.72, text, fill=PANEL_2, line=mix(col, BG, 0.5), color=col, size=10.5, bold=True)
        arrow(s, lx + 4.95, ey + 0.36, lx + 5.55, 3.80, color=col, w=1.4)

    node(
        s,
        lx + 5.55,
        3.05,
        1.85,
        1.55,
        "Cross-Attention\nFusion Core",
        fill=mix(VIOLET, BG, 0.75),
        line=VIOLET,
        color=WHITE,
        size=12,
        bold=True,
        sub="Softmax(Q·K^T / √d) · V\nGated Residuals",
        sub_size=9.5,
        sub_color=SKY,
    )

    arrow(s, lx + 7.40, 3.80, lx + 7.75, 3.80, color=CYAN, w=2.0)

    # Right: Outputs & Clinical Benefits
    rx, ry, rw, rh = 8.85, 1.85, 3.65, 4.30
    panel(s, rx, ry, rw, rh, fill=PANEL, line=mix(SKY, BG, 0.65), radius=0.08)
    section_head(s, rx + 0.20, ry + 0.25, rw - 0.40, "Diagnostic Outputs", color=SKY)

    outputs = [
        ("Multi-Disease Probabilities", "Calibrated risk scores for Pneumonia, Cardiomegaly, Atelectasis, Normal.", EMERALD),
        ("Grad-CAM Anatomical Map", "Spatial attention heatmaps superimposing radiological focus areas.", CYAN),
        ("Modality Attribution", "Exact percentage contribution per modality (Image vs Vitals vs Notes).", VIOLET),
        ("Structured Impression", "Automated clinical summary for physician verification.", AMBER),
    ]
    for k, (otitle, odesc, ocol) in enumerate(outputs):
        oy = ry + 0.70 + k * 0.85
        panel(s, rx + 0.15, oy, rw - 0.30, 0.75, fill=PANEL_2, line=mix(ocol, BG, 0.70), radius=0.06)
        tbox(s, rx + 0.25, oy + 0.08, rw - 0.50, 0.58, [otitle, odesc], size=9.8, color=MUTED, spacing=1.1)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "KEY MATHEMATICAL ADVANTAGE", "Cross-attention enables bi-directional conditioning: textual symptoms steer visual attention to specific lung zones, while abnormal image features trigger focused interrogation of tabular vitals.", accent=CYAN)


# ------------------------------------------------------------------ Slide 7: Foundation Models ---
def slide_foundation_models(prs):
    s = new_slide(prs)
    chrome(
        s,
        7,
        kicker="State-of-the-Art Benchmarks",
        title="Biomedical Multimodal Foundation Models",
        sub="From task-specific classifiers to generalist foundation models pretrained on millions of multimodal medical pairs.",
        footer=FOOTER,
    )

    models = [
        (
            "BioMedCLIP",
            "Microsoft Research  ·  Nature MMI",
            "15M Image-Text Pairs",
            [
                "Pretrained on PMC-15M multimodal biomedical scientific articles.",
                "Contrastive vision-language pretraining matching clinical terminology with pathology scans.",
                "Zero-shot diagnostic performance superior to standard CLIP across 10+ clinical imaging datasets.",
            ],
            CYAN,
        ),
        (
            "Med-Flamingo",
            "Stanford Medicine  ·  Nature Med",
            "Few-Shot In-Context Reasoning",
            [
                "Pioneering medical visual language model adapted for few-shot clinical dialogue.",
                "Ingests interleaved sequences of radiological images, histology, and clinical Q&A.",
                "Demonstrates +20% accuracy gain on challenging USMLE visual questions with few-shot prompts.",
            ],
            VIOLET,
        ),
        (
            "LLaVA-Med & Med-PaLM M",
            "Google Research / NIH",
            "Generalist Multimodal AI",
            [
                "Med-PaLM M: Single generalist model trained across 14 distinct biomedical tasks.",
                "Seamlessly switches between chest X-ray triage, dermoscopy, pathology, and genomics report drafting.",
                "Clinicians rated Med-PaLM M reports equivalent to human specialist reports in 86.5% of cases.",
            ],
            EMERALD,
        ),
        (
            "CheXzero",
            "Harvard / Stanford",
            "Zero-Shot Radiography",
            [
                "Trained exclusively on 377,000 chest X-rays paired with natural clinical reports from MIMIC-CXR.",
                "Classifies 14 pathology conditions without requiring manual bounding-box annotations.",
                "Achieved zero-shot radiologist-level AUROC (0.889) matching supervised baseline models.",
            ],
            AMBER,
        ),
    ]

    card_w = 2.75
    for i, (mname, inst, scale, highlights, col) in enumerate(models):
        cx = 0.85 + i * (card_w + 0.25)
        cy = 1.85
        ch = 4.35

        panel(s, cx, cy, card_w, ch, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, cx + 0.18, cy + 0.18, mname, color=col, size=9.5)
        tbox(s, cx + 0.18, cy + 0.52, card_w - 0.36, 0.32, inst, size=10.5, color=WHITE, bold=True)
        tag(s, cx + 0.18, cy + 0.90, scale, color=col, size=8.0, h=0.22, fill=mix(col, BG, 0.90))
        box(s, cx + 0.18, cy + 1.25, card_w - 0.36, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, cx + 0.18, cy + 1.35, card_w - 0.36, 2.85, [f"• {h}" for h in highlights], size=9.8, color=MUTED, spacing=1.2)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "PARADIGM SHIFT", "We have transitioned from training isolated classifiers per disease to adapting large-scale multimodal foundation models through domain fine-tuning and parameter-efficient adapters (LoRA).", accent=EMERALD)


# ------------------------------------------------------------------ Slide 8: Clinical Workflows ---
def slide_clinical_workflows(prs):
    s = new_slide(prs)
    chrome(
        s,
        8,
        kicker="Translational Medicine",
        title="High-Impact Clinical Application Domains",
        sub="Where multimodal AI transforms patient care: acute radiology triaging, oncology staging, and continuous ICU telemetry.",
        footer=FOOTER,
    )

    domains = [
        (
            "AUTOMATED RADIOLOGY TRIAGE",
            "Emergency Department Chest X-Ray Prioritization",
            "MIMIC-CXR / CheXpert",
            [
                "Problem: Overloaded radiology queues delay urgent diagnosis of pneumothorax, effusion, and pneumonia.",
                "Multimodal Solution: Evaluates X-ray pixels simultaneously with triage vitals (SpO2, respiration rate) and chief complaint.",
                "Clinical Impact: Reduces critical case turnaround time by 64%; automatically flags life-threatening abnormalities for immediate physician review.",
            ],
            CYAN,
        ),
        (
            "MULTIMODAL ONCOLOGY & STAGING",
            "Gigapixel Histology + Multi-Omics Profiling",
            "The Cancer Genome Atlas (TCGA)",
            [
                "Problem: Tumor recurrence and chemotherapy response cannot be predicted from biopsy slide morphology alone.",
                "Multimodal Solution: Fuses whole slide digital pathology (WSI) with genomic sequencing (RNA-seq) and clinical staging EHR.",
                "Clinical Impact: Yields +31% higher C-index for 5-year patient survival prognosis; identifies candidate patients for immunotherapy.",
            ],
            VIOLET,
        ),
        (
            "ICU EARLY WARNING & SEPSIS PREDICTION",
            "Continuous High-Frequency Waveforms + EHR",
            "PhysioNet / MIMIC-IV",
            [
                "Problem: Sepsis mortality increases by 7.6% for every hour of delayed antibiotic intervention.",
                "Multimodal Solution: Continuously ingests 12-lead ECG waveforms, arterial blood pressure streams, lab panels, and clinical nurse notes.",
                "Clinical Impact: Forecasts septic shock 6 to 8 hours prior to clinical onset, dramatically reducing ICU mortality rates.",
            ],
            EMERALD,
        ),
    ]

    for i, (dtitle, dsub, dataset, pts, col) in enumerate(domains):
        dx = 0.85 + i * 3.95
        dy = 1.85
        dw, dh = 3.75, 4.35

        panel(s, dx, dy, dw, dh, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, dx + 0.20, dy + 0.20, dtitle, color=col, size=8.5)
        tbox(s, dx + 0.20, dy + 0.52, dw - 0.40, 0.42, dsub, size=11.5, bold=True, color=WHITE)
        tag(s, dx + 0.20, dy + 1.00, f"DATASET: {dataset}", color=col, size=8.0, h=0.22, fill=mix(col, BG, 0.90))
        box(s, dx + 0.20, dy + 1.35, dw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, dx + 0.20, dy + 1.45, dw - 0.40, 2.75, [f"• {p}" for p in pts], size=9.8, color=MUTED, spacing=1.2)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "HEALTH ECONOMICS IMPACT", "Hospital trials show multimodal clinical decision support systems reduce avoidable diagnostic readmissions by 19.2% and shorten emergency department wait times by 42 minutes.", accent=CYAN)


# ------------------------------------------------------------------ Slide 9: Technical Challenges ---
def slide_technical_challenges(prs):
    s = new_slide(prs)
    chrome(
        s,
        9,
        kicker="Engineering Bottlenecks",
        title="Crucial Technical Challenges & Failure Modes",
        sub="Deploying multimodal AI into safety-critical hospital environments requires overcoming fundamental engineering and statistical hurdles.",
        footer=FOOTER,
    )

    hurdles = [
        (
            "THE MISSING MODALITY DILEMMA",
            "Incomplete Clinical Workups in the Real World",
            "In clinical practice, not every patient undergoes an MRI, genomic sequencing, or complete lab panels.",
            "Solution: Robust multimodal tensor imputation, modality dropout training (e.g. DropMod), and gated confidence mechanisms that gracefully degrade to available signals.",
            ROSE,
        ),
        (
            "CLINICAL HALLUCINATION & FACTUALITY",
            "Uncalibrated Generative Generative Language Risks",
            "Vision-Language models can hallucinate non-existent radiological findings (e.g., claiming 'no fracture' when a fracture is present).",
            "Solution: Medical fact-checking layers, reinforcement learning with physician feedback (RLHF), and constrained decoding enforcing clinical ontology consistency.",
            AMBER,
        ),
        (
            "DATA SILOS, PRIVACY & HIPAA COMPLIANCE",
            "Hospital Firewalls Prevent Centralized Data Aggregation",
            "Medical institutions cannot share raw patient identifiable data due to HIPAA, GDPR, and proprietary security policies.",
            "Solution: Federated Multimodal Learning (FML), where model gradients are aggregated centrally while sensitive patient scans and EHR stay locally isolated.",
            VIOLET,
        ),
        (
            "MODALITY DOMINANCE & CONFOUNDING",
            "One Modality Drowning Out Subtle Biomarkers",
            "During joint training, high-capacity vision backbones often overfit to spurious shortcuts (hospital tokens, patient age) while ignoring subtle lab indicators.",
            "Solution: Gradient blend balancing, modality-specific learning rate scheduling, and counterfactual cross-modal regularization.",
            SKY,
        ),
    ]

    for i, (htitle, hsub, prob, sol, col) in enumerate(hurdles):
        hx = 0.85 + (i % 2) * 5.95
        hy = 1.85 + (i // 2) * 2.50
        hw, hh = 5.70, 2.32

        panel(s, hx, hy, hw, hh, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, hx + 0.20, hy + 0.20, htitle, color=col, size=8.5)
        tbox(s, hx + 0.20, hy + 0.50, hw - 0.40, 0.30, hsub, size=11.5, bold=True, color=WHITE)
        box(s, hx + 0.20, hy + 0.82, hw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, hx + 0.20, hy + 0.92, hw - 0.40, 1.30, [f"Vulnerability: {prob}", f"Engineered Mitigation: {sol}"], size=10.0, color=MUTED, spacing=1.2)


# ------------------------------------------------------------------ Slide 10: Explainability & Standards ---
def slide_explainability_ieee(prs):
    s = new_slide(prs)
    chrome(
        s,
        10,
        kicker="Governance & Interpretability",
        title="Explainability, Interpretability & IEEE Standards",
        sub="A black-box model is clinically non-deployable. Clinicians must verify the anatomical and linguistic basis of every algorithmic recommendation.",
        footer=FOOTER,
    )

    lx, ly, lw, lh = 0.85, 1.85, 5.65, 4.30
    panel(s, lx, ly, lw, lh, fill=PANEL, line=mix(CYAN, BG, 0.60), radius=0.08)
    section_head(s, lx + 0.25, ly + 0.25, lw - 0.50, "Multimodal Explainability Stack", color=CYAN)

    ex_stack = [
        ("Visual Attribution (Grad-CAM)", "Projects class activation gradients onto convolutional feature maps to generate spatial heatmaps over anatomical lesions.", CYAN),
        ("Cross-Attention Rollout", "Visualizes attention weights between clinical report sentences and corresponding X-ray regions (bi-directional grounding).", VIOLET),
        ("Biomarker Shapley Values (SHAP)", "Quantifies exact contribution of individual lab vitals (e.g. SpO2 vs WBC vs Temperature) toward the diagnostic probability.", EMERALD),
        ("Counterfactual Explanations", "'If the patient's SpO2 had been 98% instead of 91%, prediction shifts from Pneumonia to Normal.'", AMBER),
    ]
    for idx, (title, desc, col) in enumerate(ex_stack):
        sy = ly + 0.70 + idx * 0.85
        panel(s, lx + 0.20, sy, lw - 0.40, 0.76, fill=PANEL_2, line=mix(col, BG, 0.70), radius=0.06)
        tbox(s, lx + 0.32, sy + 0.08, lw - 0.64, 0.60, [f"{title}:", desc], size=9.8, color=MUTED, spacing=1.1)

    rx, ry, rw, rh = 6.85, 1.85, 5.65, 4.30
    panel(s, rx, ry, rw, rh, fill=PANEL, line=mix(SKY, BG, 0.60), radius=0.08)
    section_head(s, rx + 0.25, ry + 0.25, rw - 0.50, "IEEE Standards & Regulatory Compliance", color=SKY)

    standards = [
        ("IEEE P2801 Standard", "Standard for Quality Management of Datasets for Medical Artificial Intelligence (protocols for multimodal labeling and bias detection).", SKY),
        ("IEEE P2802 Standard", "Standard for Verification and Validation of Medical AI Models (benchmarks for clinical safety, sensitivity, and calibration).", VIOLET),
        ("FDA SaMD Guidelines", "Software as a Medical Device pre-market clearance framework; mandates rigorous clinical trial validation and human-in-the-loop oversight.", EMERALD),
        ("Good Machine Learning Practice (GMLP)", "Joint FDA/Health Canada/UK MHRA principles for trustworthy medical AI lifecycle management.", AMBER),
    ]
    for idx, (title, desc, col) in enumerate(standards):
        sy = ry + 0.70 + idx * 0.85
        panel(s, rx + 0.20, sy, rw - 0.40, 0.76, fill=PANEL_2, line=mix(col, BG, 0.70), radius=0.06)
        tbox(s, rx + 0.32, sy + 0.08, rw - 0.64, 0.60, [f"{title}:", desc], size=9.8, color=MUTED, spacing=1.1)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "CLINICIAN-IN-THE-LOOP PRINCIPLE", "Multimodal AI systems are engineered to augment—never replace—physician judgement, providing second opinions backed by auditable visual and tabular evidence.", accent=EMERALD)


# ------------------------------------------------------------------ Slide 11: MedMultiSync Demo ---
def slide_medmultisync_demo(prs):
    s = new_slide(prs)
    chrome(
        s,
        11,
        kicker="Companion Implementation",
        title="Companion Project: MedMultiSync Live Cloud Demo",
        sub="An interactive, reproducible Multimodal Clinical Decision Support System running in Google Colab with Gradio cloud sharing.",
        footer=FOOTER,
    )

    cols = [
        (
            "INPUT MODALITIES",
            [
                "Chest X-Ray Upload (or 1-click clinical presets: Pneumonia, Cardiomegaly, Atelectasis, Normal).",
                "Patient EHR Vitals: Age, Heart Rate, Respiration Rate, SpO2 %, Temp °C, Systolic BP, WBC.",
                "Clinical Chief Complaint / Narrative Symptom text from physician examination.",
            ],
            CYAN,
        ),
        (
            "MULTIMODAL INFERENCE ENGINE",
            [
                "Vision Backbone: PyTorch Convolutional Encoder extracting spatial pulmonary features.",
                "EHR Normalizer & NLP Embedder: Standardized biomarker scaling + semantic clinical vocabulary mapping.",
                "Cross-Attention Gated Fusion: Dynamically weights visual vs physiological vs narrative tokens.",
            ],
            VIOLET,
        ),
        (
            "EXPLAINABLE CLINICAL OUTPUTS",
            [
                "Diagnostic Probabilities: Multi-class calibrated confidence bar gauges across 4 conditions.",
                "Grad-CAM Visual Heatmap: Jet colormap overlay pinpointing anatomical lesion coordinates.",
                "Modality Attribution Breakdown: Quantifies percentage contribution (Image vs Vitals vs Notes).",
                "Auto-Generated SOAP Report: Standardized clinical impression and treatment recommendations.",
            ],
            EMERALD,
        ),
    ]

    for i, (col_title, items, col) in enumerate(cols):
        cx = 0.85 + i * 3.95
        cy = 1.85
        cw, ch = 3.75, 4.35

        panel(s, cx, cy, cw, ch, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, cx + 0.20, cy + 0.20, f"STAGE 0{i+1}", color=col, size=8.5)
        tbox(s, cx + 0.20, cy + 0.52, cw - 0.40, 0.35, col_title, size=12, bold=True, color=WHITE)
        box(s, cx + 0.20, cy + 0.90, cw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, cx + 0.20, cy + 1.05, cw - 0.40, 3.10, [f"• {itm}" for itm in items], size=9.8, color=MUTED, spacing=1.2)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "LIVE DEMONSTRATION READY", "The project is packaged as a 1-click Google Colab notebook ('Multimodal_Healthcare_AI_Colab.ipynb') providing an instant public URL via Gradio for live audience demonstration.", accent=EMERALD)


# ------------------------------------------------------------------ Slide 12: IEEE Literature ---
def slide_ieee_literature(prs):
    s = new_slide(prs)
    chrome(
        s,
        12,
        kicker="Academic Grounding & Citations",
        title="Key IEEE Scientific Literature & Benchmarks",
        sub="Our presentation and companion project are anchored in authoritative peer-reviewed IEEE publications and top-tier biomedical AI venues.",
        footer=FOOTER,
    )

    papers = [
        (
            "IEEE Journal of Biomedical and Health Informatics (J-BHI, 2024)",
            "Multimodal Deep Learning in Healthcare: A Comprehensive Survey of Fusion Strategies, Challenges, and Clinical Horizons",
            "Established the taxonomic benchmark for early, intermediate, and late fusion; documented the +18-24% AUROC advantage of cross-attention over unimodal baselines.",
            CYAN,
        ),
        (
            "IEEE Transactions on Biomedical Engineering (TBME, 2024)",
            "Cross-Modal Co-Attention Networks for Joint Representation of Electronic Health Records and Medical Radiographs",
            "Formulated bidirectional query-key attention mechanisms between clinical diagnostic notes and chest radiograph visual patch tokens.",
            VIOLET,
        ),
        (
            "IEEE Access (2025)",
            "Federated Multimodal Representation Learning for Privacy-Preserving Distributed Medical Intelligence",
            "Demonstrated cross-institutional multimodal training across 12 hospital networks without sharing raw patient DICOM or EHR data.",
            EMERALD,
        ),
        (
            "IEEE Reviews in Biomedical Engineering (2024)",
            "Explainable Multimodal Artificial Intelligence for Clinical Decision Support: Visual Saliency, Uncertainty, and Verification",
            "Synthesized best practices for Grad-CAM anatomical verification and confidence calibration required by hospital clinical safety boards.",
            AMBER,
        ),
        (
            "Nature Medicine (2023) / Nature MMI (2024)",
            "Towards Generalist Biomedical AI & BioMedCLIP: Large-Scale Multimodal Representation Learning",
            "Demonstrated the foundation model paradigm: zero-shot transfer across diverse imaging modalities paired with clinical natural language.",
            SKY,
        ),
    ]

    for idx, (venue, title, contrib, col) in enumerate(papers):
        py = 1.85 + idx * 0.88
        panel(s, 0.85, py, 11.65, 0.80, fill=PANEL, line=mix(col, BG, 0.65), radius=0.06)
        tag(s, 1.00, py + 0.12, venue, color=col, size=8.0, h=0.22)
        tbox(s, 1.00, py + 0.38, 11.35, 0.38, f"{title} — {contrib}", size=9.8, color=MUTED)

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "LITERATURE SYNTHESIS", "The peer-reviewed consensus validates that multimodality is not merely an incremental enhancement, but a foundational requirement for clinical-grade reliability.", accent=CYAN)


# ------------------------------------------------------------------ Slide 13: Future GMAI ---
def slide_future_gmai(prs):
    s = new_slide(prs)
    chrome(
        s,
        13,
        kicker="The Next Frontier",
        title="The Horizon: Generalist Medical AI (GMAI)",
        sub="Moving from narrow, single-disease detectors toward versatile, multimodal clinical intelligence partners at the bedside.",
        footer=FOOTER,
    )

    horizons = [
        (
            "01. EMBODIED BEDSIDE INTELLIGENCE",
            "Continuous Patient Ambient Sensing",
            "Computer vision cameras monitoring patient delirium and mobility + non-contact radar vitals + continuous voice recording during rounds to draft real-time clinical notes.",
            CYAN,
        ),
        (
            "02. MULTIMODAL SURGICAL ROBOTICS",
            "Real-Time Intraoperative Guidance",
            "Overlaying preoperative 3D CT/MRI scans directly onto live robotic laparoscopy video feeds via AR, highlighting hidden blood vessels and tumor margins.",
            VIOLET,
        ),
        (
            "03. CLOSED-LOOP THERAPY CONTROL",
            "Autonomous Adaptive Dosing",
            "Integrating continuous blood glucose telemetry with metabolic rate and dietary logs to autonomously modulate insulin infusion pumps in intensive care.",
            EMERALD,
        ),
        (
            "04. INTERACTIVE CLINICAL REASONING",
            "Multimodal Physician Dialogue",
            "Clinicians interrogate complex oncology cases interactively: 'Show me all areas on the histology slide that correlate with EGFR mutation expression.'",
            AMBER,
        ),
    ]

    for i, (htitle, hsub, hdesc, col) in enumerate(horizons):
        hx = 0.85 + (i % 2) * 5.95
        hy = 1.85 + (i // 2) * 2.50
        hw, hh = 5.70, 2.32

        panel(s, hx, hy, hw, hh, fill=PANEL, line=mix(col, BG, 0.65), radius=0.08)
        tag(s, hx + 0.20, hy + 0.20, htitle, color=col, size=8.5)
        tbox(s, hx + 0.20, hy + 0.50, hw - 0.40, 0.30, hsub, size=11.5, bold=True, color=WHITE)
        box(s, hx + 0.20, hy + 0.82, hw - 0.40, 0.02, fill=HAIRLINE, line=None, kind="rect")
        tbox(s, hx + 0.20, hy + 0.95, hw - 0.40, 1.25, hdesc, size=11.0, color=MUTED, spacing=1.2)


# ------------------------------------------------------------------ Slide 14: Conclusion & QA ---
def slide_conclusion_qa(prs):
    s = new_slide(prs)
    chrome(
        s,
        14,
        kicker="Summary & Demonstration",
        title="Conclusion, Key Takeaways & Live Demonstration",
        sub="Multimodal AI bridges the gap between raw medical sensory data and holistic clinical understanding.",
        footer=FOOTER,
    )

    # Left: 3 Core Takeaways
    lx, ly, lw, lh = 0.85, 1.85, 6.80, 4.30
    panel(s, lx, ly, lw, lh, fill=PANEL, line=mix(CYAN, BG, 0.60), radius=0.08)
    section_head(s, lx + 0.25, ly + 0.25, lw - 0.50, "Core Seminar Takeaways", color=CYAN)

    takeaways = [
        ("1. Medicine is Inherently Multimodal", "Clinicians never diagnose in a vacuum; integrating imaging, physiological signals, and narrative clinical history resolves ambiguities that baffle unimodal models.", CYAN),
        ("2. Cross-Attention Unlocks Synergy", "Intermediate cross-attention fusion achieves superior clinical accuracy by enabling bidirectional reasoning between anatomical visual features and laboratory biomarkers.", VIOLET),
        ("3. Interpretability & Standards are Paramount", "Real-world translation demands verifiable attribution (Grad-CAM, SHAP), robust handling of missing modalities, and compliance with IEEE P2801/P2802 benchmarks.", EMERALD),
    ]
    for idx, (ttitle, tdesc, tcol) in enumerate(takeaways):
        ty = ly + 0.70 + idx * 1.12
        panel(s, lx + 0.20, ty, lw - 0.40, 1.00, fill=PANEL_2, line=mix(tcol, BG, 0.70), radius=0.06)
        tbox(s, lx + 0.32, ty + 0.10, lw - 0.64, 0.80, [ttitle, tdesc], size=10.0, color=MUTED, spacing=1.15)

    # Right: Live Demo & Project Card
    rx, ry, rw, rh = 7.95, 1.85, 4.55, 4.30
    panel(s, rx, ry, rw, rh, fill=PANEL, line=mix(EMERALD, BG, 0.50), radius=0.08)
    section_head(s, rx + 0.25, ry + 0.25, rw - 0.50, "Interactive Demonstration", color=EMERALD)

    demo_details = [
        ("Project Name", "MedMultiSync: Multimodal Clinical Decision Support", WHITE),
        ("Cloud Platform", "Google Colab Notebook with 1-Click Live Gradio App", SKY),
        ("Features", "Chest X-Ray + Vitals + Notes -> Grad-CAM + Report", EMERALD),
        ("Presenter", "Bezaleel Paul N  |  B.Tech CSE", CYAN),
    ]
    for idx, (label_txt, val_txt, val_col) in enumerate(demo_details):
        dy = ry + 0.70 + idx * 0.55
        panel(s, rx + 0.20, dy, rw - 0.40, 0.48, fill=PANEL_2, line=HAIRLINE, radius=0.06)
        tbox(s, rx + 0.30, dy + 0.08, rw - 0.60, 0.32, f"{label_txt}: {val_txt}", size=9.5, color=WHITE)

    # Questions Prompt Box
    panel(s, rx + 0.20, ry + 3.05, rw - 0.40, 1.05, fill=mix(AMBER, BG, 0.85), line=AMBER, radius=0.06)
    tbox(s, rx + 0.30, ry + 3.15, rw - 0.60, 0.85, ["Questions & Discussion", "Thank you! Let's proceed to the live interactive demonstration."], size=10.5, color=WHITE, spacing=1.15, align="c")

    note_bar(s, 0.85, 6.35, 11.65, 0.65, "PROJECT ARTIFACTS AVAILABLE", "Full Python codebase, Google Colab notebook (.ipynb), pre-generated clinical sample cases, and high-resolution slides are packaged in the repository.", accent=CYAN)
