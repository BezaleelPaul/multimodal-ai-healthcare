"""Slides 9-13: the AI shift, ML lifecycle, pipeline, architecture, model evaluation."""

from .theme import (
    AMBER,
    BG,
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
    hflow,
    mix,
    new_slide,
    node,
    note_bar,
    panel,
    section_head,
    tag,
    tbox,
)

LW = 1.5


def _pill(slide, x, y, w, h, text, col, size=11.5):
    return node(
        slide,
        x,
        y,
        w,
        h,
        text,
        fill=mix(col, BG, 0.84),
        line=mix(col, BG, 0.5),
        size=size,
        color=WHITE,
        radius=0.5,
    )


def slide_ai_shift(prs):
    s = new_slide(prs)
    chrome(
        s,
        9,
        kicker="Part B  ·  Why AI changes software design",
        title="Software Engineering Meets the AI System",
        sub="The traditional pipeline still exists — it now feeds three new "
        "engineering lanes that must be designed, versioned and operated together.",
    )

    _pill(s, 4.87, 1.66, 3.6, 0.40, "SOFTWARE  ENGINEERING", CYAN, size=11)
    arrow(s, 6.67, 2.06, 6.67, 2.20, color=CYAN, w=LW)
    hflow(
        s,
        0.70,
        2.20,
        11.94,
        ["Requirements", "Architecture", "Code", "Testing", "Integration"],
        h=0.42,
        gap=0.36,
        fill=PANEL_2,
        line=mix(SKY, BG, 0.45),
        size=10.5,
        arrow_color=SKY,
        lw=LW,
    )
    arrow(s, 6.67, 2.62, 6.67, 2.80, color=SKY, w=LW)

    _pill(s, 5.17, 2.80, 3.0, 0.40, "AI  SYSTEM", AMBER, size=11)
    arrow(s, 6.67, 3.20, 6.67, 3.34, color=AMBER, w=LW)
    path_pts = [(5.60, 3.20), (5.60, 3.27), (2.55, 3.27), (2.55, 3.34)]
    for pts, hx in (
        (path_pts, 2.55),
        ([(7.74, 3.20), (7.74, 3.27), (10.79, 3.27), (10.79, 3.34)], 10.79),
    ):
        arrow(
            s, pts[0][0], pts[0][1], pts[1][0], pts[1][1], color=AMBER, w=LW, head=False
        )
        arrow(
            s, pts[1][0], pts[1][1], pts[2][0], pts[2][1], color=AMBER, w=LW, head=False
        )
        arrow(
            s, pts[2][0], pts[2][1], pts[3][0], pts[3][1], color=AMBER, w=LW, head=False
        )

    cols = [
        (
            0.62,
            VIOLET,
            "DATA",
            [
                "Data collection",
                "Cleaning & labeling",
                "Versioning",
                "Features & representation",
            ],
        ),
        (
            4.74,
            AMBER,
            "MODEL",
            ["Training runs", "Validation", "Evaluation", "Tuning & model registry"],
        ),
        (
            8.86,
            CYAN,
            "SOFTWARE",
            ["Backend & API", "Frontend & UX", "Database", "Cloud infrastructure"],
        ),
    ]
    for x, col, head, items in cols:
        node(
            s,
            x,
            3.34,
            3.86,
            0.36,
            head,
            fill=mix(col, BG, 0.80),
            line=mix(col, BG, 0.45),
            size=11,
            color=col,
            spc=140,
            radius=0.3,
        )
        panel(s, x, 3.74, 3.86, 1.52, fill=PANEL, line=mix(col, BG, 0.40))
        tbox(
            s,
            x + 0.26,
            3.90,
            3.4,
            1.24,
            [
                [("▸  ", {"color": col, "size": 10.5}), (t, {"size": 10.5})]
                for t in items
            ],
            color=MUTED,
            spacing=1.15,
            space_after=6,
        )

    for x in (2.55, 6.67, 10.79):
        if x == 6.67:
            arrow(s, x, 5.26, x, 5.76, color=EMERALD, w=LW)
        else:
            mid = 5.60 if x < 6 else 7.74
            arrow(s, x, 5.26, x, 5.60, color=EMERALD, w=LW, head=False)
            arrow(s, x, 5.60, mid, 5.60, color=EMERALD, w=LW, head=False)
            arrow(s, mid, 5.60, mid, 5.76, color=EMERALD, w=LW)

    node(
        s,
        0.62,
        5.76,
        12.1,
        0.42,
        "DEPLOYMENT",
        fill=mix(EMERALD, BG, 0.86),
        line=mix(EMERALD, BG, 0.5),
        size=11,
        color=WHITE,
        spc=160,
    )
    arrow(s, 3.55, 6.18, 3.55, 6.40, color=ROSE, w=LW)
    node(
        s,
        0.62,
        6.40,
        5.85,
        0.42,
        "MONITORING",
        fill=mix(ROSE, BG, 0.86),
        line=mix(ROSE, BG, 0.5),
        size=11,
        color=WHITE,
        spc=160,
    )
    arrow(s, 6.47, 6.61, 6.87, 6.61, color=ROSE, w=LW)
    node(
        s,
        6.87,
        6.40,
        5.85,
        0.42,
        "RETRAIN  /  UPDATE",
        fill=mix(ROSE, BG, 0.86),
        line=mix(ROSE, BG, 0.5),
        size=11,
        color=WHITE,
        spc=160,
    )

    arrow(s, 12.72, 6.61, 13.0, 6.61, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 13.0, 6.61, 13.0, 3.00, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 13.0, 3.00, 8.17, 3.00, color=ROSE, w=1.3, dashed=DASH)
    tbox(
        s,
        8.55,
        2.64,
        4.2,
        0.26,
        [
            [
                ("↺  ", {"color": ROSE, "bold": True}),
                ("retrain & redeploy from live feedback", {"color": ROSE}),
            ]
        ],
        size=9.5,
        anchor="m",
    )
    return s


def slide_ml_lifecycle(prs):
    s = new_slide(prs)
    chrome(
        s,
        10,
        kicker="Part B  ·  The AI / ML lifecycle",
        title="The AI/ML Lifecycle Is a Loop, Not a Line",
    )

    col1 = [
        ("01", "Problem Definition", SKY),
        ("02", "Data Collection", VIOLET),
        ("03", "Data Preparation", VIOLET),
        ("04", "Feature Engineering", VIOLET),
        ("05", "Model Selection", AMBER),
    ]
    col2 = [
        ("10", "Retraining", ROSE),
        ("09", "Monitoring", ROSE),
        ("08", "Deployment", EMERALD),
        ("07", "Validation & Evaluation", AMBER),
        ("06", "Training", AMBER),
    ]
    tag(s, 1.3, 1.78, "PLAN  &  PREPARE", color=VIOLET, size=7.5, h=0.26, w=1.55)
    tag(s, 8.4, 1.78, "BUILD  &  OPERATE", color=AMBER, size=7.5, h=0.26, w=1.55)

    y0, h, gap = 2.14, 0.58, 0.26
    for i, (num, txt, col) in enumerate(col1):
        y = y0 + i * (h + gap)
        node(
            s,
            1.3,
            y,
            3.6,
            h,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=11,
            align="l",
            badge=num,
            badge_color=col,
        )
        if i < 4:
            arrow(s, 3.1, y + h, 3.1, y + h + gap, color=col, w=LW)
    for i, (num, txt, col) in enumerate(col2):
        y = y0 + i * (h + gap)
        node(
            s,
            8.4,
            y,
            3.6,
            h,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=11,
            align="l",
            badge=num,
            badge_color=col,
        )
        if i < 4:
            arrow(s, 10.2, y + h + gap, 10.2, y + h, color=col, w=LW)

    # bottom hand-off: col1 -> col2 (continues upward)
    arrow(s, 3.1, 6.08, 3.1, 6.36, color=AMBER, w=LW, head=False)
    arrow(s, 3.1, 6.36, 10.2, 6.36, color=AMBER, w=LW, head=False)
    arrow(s, 10.2, 6.36, 10.2, 6.10, color=AMBER, w=LW)
    tbox(
        s,
        5.6,
        6.14,
        4.0,
        0.24,
        "then build, ship and run it",
        size=9.5,
        italic=True,
        color=DIM,
        align="c",
    )

    # centre explainer fills the middle of the loop
    panel(s, 5.3, 2.70, 2.7, 2.40, fill=PANEL_2, line=mix(SKY, BG, 0.45))
    section_head(s, 5.5, 2.94, 2.4, "Why the loop never ends", color=ROSE, size=10.5)
    tbox(
        s,
        5.5,
        3.38,
        2.3,
        1.5,
        "Data drifts, requirements change and every release generates new "
        "feedback. A model that is accurate today degrades quietly — so the "
        "pipeline always returns to step 01.",
        size=10,
        color=MUTED,
        spacing=1.24,
    )
    tag(s, 5.5, 4.68, "ALWAYS  ITERATING", color=ROSE, size=7.5, h=0.26)

    # feedback loop: top of col2 back to the top of col1
    arrow(s, 10.2, 2.14, 10.2, 1.66, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 10.2, 1.66, 3.1, 1.66, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 3.1, 1.66, 3.1, 2.14, color=ROSE, w=1.3, dashed=DASH)
    tbox(
        s,
        3.4,
        1.30,
        6.6,
        0.26,
        [
            [
                ("↺   ", {"color": ROSE, "bold": True}),
                ("new data and new requirements restart the loop", {"color": ROSE}),
            ]
        ],
        size=10,
        align="c",
        anchor="m",
    )

    note_bar(
        s,
        0.55,
        6.62,
        12.23,
        0.46,
        "Iterative, not linear:",
        "Google describes ML development as ideation, experimentation, pipeline "
        "building and productionization — steps feed back into each other.",
        accent=SKY,
        size=11,
    )
    return s


def slide_ml_pipeline(prs):
    s = new_slide(prs)
    chrome(
        s,
        11,
        kicker="Part C  ·  AI architecture & pipelines",
        title="Production ML Pipeline",
        sub="Automated, validated and versioned — a model only ships when the "
        "pipeline says it is good enough.",
    )

    x, w = 3.6, 3.4
    steps = [
        ("RAW DATA", "para", VIOLET),
        ("Data Ingestion", "round", VIOLET),
        ("Data Validation", "round", VIOLET),
        ("Data Transformation", "round", VIOLET),
        ("Model Training", "round", AMBER),
        ("Model Validation", "round", AMBER),
    ]
    y = 1.58
    h, gap = 0.38, 0.12
    for i, (txt, kind, col) in enumerate(steps):
        node(
            s,
            x,
            y,
            w,
            h,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=10,
            kind=kind,
            radius=0.16,
        )
        if i < len(steps) - 1:
            arrow(s, x + w / 2, y + h, x + w / 2, y + h + gap, color=col, w=LW)
        y += h + gap

    dx, dy = x + w / 2 - 0.55, y + 0.14
    box(
        s,
        dx,
        dy,
        1.1,
        0.64,
        fill=mix(AMBER, BG, 0.85),
        line=mix(AMBER, BG, 0.55),
        lw=1.2,
        kind="diamond",
    )
    tbox(
        s,
        dx,
        dy,
        1.1,
        0.64,
        "PASS?",
        size=9,
        bold=True,
        color=WHITE,
        align="c",
        anchor="m",
    )

    # FAIL branch -> back to training
    fy = dy + 0.32
    arrow(s, dx, fy, 1.9, fy, color=ROSE, w=1.3, head=False)
    arrow(s, 1.9, fy, 1.9, 3.77, color=ROSE, w=1.3, head=False)
    arrow(s, 1.9, 3.77, x, 3.77, color=ROSE, w=1.3, dashed=DASH)
    tbox(
        s,
        0.66,
        4.32,
        1.14,
        0.86,
        [
            [("FAIL", {"color": ROSE, "bold": True, "size": 9.5})],
            [("retrain on", {"color": ROSE, "size": 9})],
            [("more data", {"color": ROSE, "size": 9})],
        ],
        spacing=1.15,
        space_after=2,
    )

    arrow(s, x + w / 2, dy + 0.64, x + w / 2, 5.56, color=EMERALD, w=LW)
    tbox(s, 5.44, 5.34, 1.4, 0.24, "PASS", size=9.5, bold=True, color=EMERALD)

    y = 5.56
    bottom = [
        ("Model Registry", EMERALD),
        ("Deployment", EMERALD),
        ("Prediction service", CYAN),
    ]
    for i, (txt, col) in enumerate(bottom):
        node(
            s,
            x,
            y,
            w,
            h,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=10,
        )
        if i < len(bottom) - 1:
            arrow(s, x + w / 2, y + h, x + w / 2, y + h + gap, color=col, w=LW)
        y += h + gap

    panel(s, 7.4, 1.58, 5.38, 2.56)
    section_head(s, 7.65, 1.78, 4.9, "What the pipeline automates", color=CYAN)
    tbox(
        s,
        7.65,
        2.16,
        4.9,
        1.86,
        [
            [
                ("▸  ", {"color": CYAN}),
                ("Schema & data-quality gates on every run", {}),
            ],
            [
                ("▸  ", {"color": CYAN}),
                ("Reproducible, parameterised training jobs", {}),
            ],
            [
                ("▸  ", {"color": CYAN}),
                ("Automatic model validation against a baseline", {}),
            ],
            [("▸  ", {"color": CYAN}), ("Versioned model registry with lineage", {})],
            [("▸  ", {"color": CYAN}), ("Triggered retraining when metrics drop", {})],
        ],
        size=10.5,
        color=MUTED,
        spacing=1.16,
        space_after=6,
    )

    panel(s, 7.4, 4.32, 5.38, 2.56, fill=PANEL_2, line=mix(ROSE, BG, 0.45))
    section_head(s, 7.65, 4.54, 4.9, "Why a pipeline, not a notebook?", color=ROSE)
    tbox(
        s,
        7.65,
        4.96,
        4.9,
        1.7,
        "Models go stale as the real world changes. Google recommends production "
        "ML pipelines because a one-off training run cannot keep up with data "
        "drift, and manual hand-offs break auditability.",
        size=11,
        color=MUTED,
        spacing=1.22,
    )
    return s


def slide_ai_architecture(prs):
    s = new_slide(prs)
    chrome(
        s,
        12,
        kicker="Part C  ·  AI architecture & pipelines",
        title="AI System Architecture",
        sub="The AI model is one component inside an ordinary software system — "
        "and it needs its own internal pipeline.",
    )

    section_head(s, 0.55, 1.60, 5.6, "System context — who calls the model", color=CYAN)
    section_head(s, 7.4, 1.60, 5.4, "AI service — what happens inside", color=AMBER)

    node(
        s,
        2.5,
        1.98,
        2.0,
        0.40,
        "USER",
        fill=mix(SKY, BG, 0.84),
        line=mix(SKY, BG, 0.5),
        size=11,
        radius=0.5,
        spc=140,
    )
    arrow(s, 3.5, 2.38, 3.5, 2.50, color=CYAN, w=LW)
    node(
        s,
        1.7,
        2.50,
        3.6,
        0.50,
        "Flutter / Web App",
        fill=PANEL_2,
        line=HAIRLINE,
        size=11,
    )
    arrow(s, 3.5, 3.00, 3.5, 3.15, color=CYAN, w=LW)
    node(
        s,
        1.7,
        3.15,
        3.6,
        0.50,
        "API Layer  ·  auth · rate limits",
        fill=PANEL_2,
        line=HAIRLINE,
        size=11,
    )
    arrow(s, 3.0, 3.65, 2.4, 3.65, color=CYAN, w=LW, head=False)
    arrow(s, 2.4, 3.65, 2.4, 3.85, color=CYAN, w=LW)
    arrow(s, 4.0, 3.65, 4.6, 3.65, color=CYAN, w=LW, head=False)
    arrow(s, 4.6, 3.65, 4.6, 3.85, color=CYAN, w=LW)
    node(
        s,
        1.15,
        3.85,
        2.5,
        0.55,
        "AI Service",
        fill=mix(AMBER, BG, 0.88),
        line=mix(AMBER, BG, 0.5),
        size=11,
    )
    node(
        s,
        3.7,
        3.85,
        2.5,
        0.55,
        "Database",
        fill=mix(VIOLET, BG, 0.88),
        line=mix(VIOLET, BG, 0.5),
        size=11,
    )
    tbox(
        s,
        3.7,
        4.46,
        2.5,
        0.28,
        "cases · images · audit log",
        size=9,
        color=DIM,
        align="c",
    )

    y = 4.40
    for txt, col in (
        ("Preprocessing", AMBER),
        ("Model inference", AMBER),
        ("Prediction + confidence", AMBER),
        ("Explainability layer", INDIGO),
    ):
        arrow(s, 2.4, y, 2.4, y + 0.16, color=AMBER, w=LW)
        node(
            s,
            1.15,
            y + 0.16,
            2.5,
            0.44,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=10,
        )
        y += 0.56
    last_cy = y - 0.56 + 0.16 + 0.22
    arrow(s, 1.15, last_cy, 0.62, last_cy, color=INDIGO, w=1.3, head=False)
    arrow(s, 0.62, last_cy, 0.62, 2.75, color=INDIGO, w=1.3, head=False)
    arrow(s, 0.62, 2.75, 1.7, 2.75, color=INDIGO, w=1.3, dashed=DASH)
    ret = tbox(
        s,
        0.07,
        4.37,
        1.7,
        0.26,
        "result returned to the app",
        size=8.5,
        bold=True,
        color=mix(INDIGO, BG, 0.3),
        align="c",
        anchor="m",
    )
    ret.rotation = 270

    chain = [
        ("Image", VIOLET),
        ("Quality check", VIOLET),
        ("Preprocessing", VIOLET),
        ("Feature extraction", VIOLET),
        ("Neural network", AMBER),
        ("Prediction", AMBER),
        ("Confidence score", AMBER),
        ("Explainability", INDIGO),
        ("Final result", EMERALD),
    ]
    y = 1.95
    h, gap = 0.42, 0.13
    for i, (txt, col) in enumerate(chain):
        node(
            s,
            7.4,
            y,
            5.0,
            h,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=10.5,
            align="l",
            badge=str(i + 1).zfill(2),
            badge_color=col,
        )
        if i < len(chain) - 1:
            arrow(s, 9.9, y + h, 9.9, y + h + gap, color=col, w=1.3)
        y += h + gap
    return s


def slide_model_eval(prs):
    s = new_slide(prs)
    chrome(
        s,
        13,
        kicker="Part C  ·  AI architecture & pipelines",
        title="The Model: Representation, Computation, Output",
        sub="A neural network is just another component — but it is judged by "
        "statistics, not by a specification.",
    )

    # --------------------------------------------------------- neural net ---
    panel(s, 0.55, 1.60, 6.1, 5.30)
    section_head(s, 0.8, 1.82, 5.6, "A model, drawn simply", color=AMBER)

    in_x, hid_x, out_x = 1.55, 3.45, 5.35
    d = 0.46
    in_y = [2.60, 3.35, 4.10, 4.85]
    hid_y = in_y
    out_y = [3.35, 4.10]

    for y1 in in_y:
        for y2 in hid_y:
            arrow(
                s,
                in_x + d / 2,
                y1 + d / 2,
                hid_x + d / 2,
                y2 + d / 2,
                color=mix(AMBER, BG, 0.78),
                w=0.75,
                head=False,
            )
    for y1 in hid_y:
        for y2 in out_y:
            arrow(
                s,
                hid_x + d / 2,
                y1 + d / 2,
                out_x + d / 2,
                y2 + d / 2,
                color=mix(AMBER, BG, 0.78),
                w=0.75,
                head=False,
            )

    for i, y in enumerate(in_y):
        node(
            s,
            in_x,
            y,
            d,
            d,
            f"x{i + 1}",
            fill=mix(SKY, BG, 0.86),
            line=mix(SKY, BG, 0.5),
            size=9,
            kind="oval",
        )
    for y in hid_y:
        node(
            s,
            hid_x,
            y,
            d,
            d,
            "",
            fill=mix(AMBER, BG, 0.84),
            line=mix(AMBER, BG, 0.5),
            size=9,
            kind="oval",
        )
    labels = ["A  0.82", "B  0.18"]
    for y, lab in zip(out_y, labels):
        node(
            s,
            out_x,
            y,
            d,
            d,
            "",
            fill=mix(EMERALD, BG, 0.84),
            line=mix(EMERALD, BG, 0.5),
            size=9,
            kind="oval",
        )
        tbox(
            s,
            out_x + d + 0.12,
            y,
            1.3,
            d,
            lab,
            size=9.5,
            bold=True,
            color=WHITE,
            anchor="m",
        )

    tbox(s, 0.9, 2.14, 1.4, 0.24, "INPUT", size=8, bold=True, color=SKY, spc=120)
    tbox(s, 2.8, 2.14, 1.6, 0.24, "HIDDEN", size=8, bold=True, color=AMBER, spc=120)
    tbox(s, 4.9, 2.14, 1.6, 0.24, "OUTPUT", size=8, bold=True, color=EMERALD, spc=120)

    hflow(
        s,
        0.9,
        5.55,
        5.4,
        ["Input", "Representation", "Computation", "Output"],
        h=0.42,
        gap=0.16,
        fill=PANEL_2,
        line=HAIRLINE,
        size=9.5,
        arrow_color=mix(SKY, BG, 0.3),
        lw=1.2,
    )
    tbox(
        s,
        0.9,
        6.14,
        5.4,
        0.6,
        "Weights are learned from examples; the architecture (layers, size, "
        "connections) is a design decision an engineer makes.",
        size=10.5,
        color=MUTED,
        spacing=1.2,
    )

    # ------------------------------------------------------------ metrics ---
    section_head(s, 6.95, 1.68, 5.8, "How an AI model is judged", color=CYAN)
    metrics = [
        ("Accuracy", "share of all predictions that are right", CYAN),
        ("Precision", "of those flagged positive, how many are", VIOLET),
        ("Recall", "of the real positives, how many did we find", AMBER),
        ("F1 score", "harmonic mean of precision and recall", EMERALD),
        ("ROC-AUC", "ranking quality across all thresholds", INDIGO),
        ("Calibration", "does a 0.8 confidence happen 80% of the time?", ROSE),
    ]
    w, gap = 1.83, 0.14
    for i, (name, desc, col) in enumerate(metrics):
        cx = 6.95 + (i % 3) * (w + gap)
        cy = 2.08 + (i // 3) * 1.16
        panel(s, cx, cy, w, 1.02, fill=PANEL, line=mix(col, BG, 0.45))
        box(s, cx, cy, 0.05, 1.02, fill=col, kind="rect")
        tbox(
            s,
            cx + 0.18,
            cy + 0.14,
            w - 0.3,
            0.26,
            name,
            size=11.5,
            bold=True,
            color=WHITE,
        )
        tbox(
            s,
            cx + 0.18,
            cy + 0.44,
            w - 0.32,
            0.5,
            desc,
            size=8.5,
            color=MUTED,
            spacing=1.12,
        )

    section_head(s, 6.95, 4.52, 5.8, "And beyond raw accuracy", color=INDIGO)
    chips = ["Robustness", "Fairness", "Explainability", "Latency", "Cost", "Drift"]
    for i, c in enumerate(chips):
        cx = 6.95 + (i % 3) * (w + gap)
        cy = 4.90 + (i // 3) * 0.5
        node(
            s,
            cx,
            cy,
            w,
            0.4,
            c,
            fill=PANEL_2,
            line=HAIRLINE,
            size=9.5,
            color=mix(INDIGO, BG, 0.3),
        )

    note_bar(
        s,
        6.95,
        6.02,
        5.8,
        0.88,
        "Software is tested against a spec.",
        "A model is measured on data it has never seen — and the data keeps "
        "changing, so measurement never stops.",
        accent=ROSE,
        size=11,
    )
    return s
