"""Slides 14-19: MLOps, feedback loop, GenAI, RAG, testing, responsible AI."""

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
    vflow,
)

LW = 1.5


def slide_mlops(prs):
    s = new_slide(prs)
    chrome(
        s,
        14,
        kicker="Part D  ·  MLOps & operations",
        title="MLOps — Where Code, Data and Model Meet Operations",
        sub="Three change streams, one automated release path, and a runtime "
        "that talks back.",
    )

    lanes = [
        (
            "CODE",
            SKY,
            ["Git repository", "CI: lint & unit tests", "Build & package"],
            2.05,
        ),
        ("DATA", VIOLET, ["Data sources", "Validate & version", "Feature store"], 2.95),
        (
            "MODEL",
            AMBER,
            ["Training jobs", "Evaluate vs baseline", "Model registry"],
            3.85,
        ),
    ]
    bx = [2.35, 5.5, 8.65]
    for lab, col, items, ly in lanes:
        node(
            s,
            0.55,
            ly,
            1.05,
            0.5,
            lab,
            fill=mix(col, BG, 0.86),
            line=mix(col, BG, 0.5),
            size=9,
            spc=60,
        )
        for i, txt in enumerate(items):
            node(
                s,
                bx[i],
                ly,
                2.9,
                0.5,
                txt,
                fill=mix(col, BG, 0.91),
                line=mix(col, BG, 0.55),
                size=10.5,
            )
            if i < len(items) - 1:
                arrow(
                    s,
                    bx[i] + 2.9,
                    ly + 0.25,
                    bx[i + 1],
                    ly + 0.25,
                    color=col,
                    w=1.4,
                    head_size="sm",
                )
            else:
                arrow(
                    s,
                    bx[i] + 2.9,
                    ly + 0.25,
                    12.0,
                    ly + 0.25,
                    color=col,
                    w=1.4,
                    head_size="sm",
                )

    arrow(s, 12.0, 2.30, 12.0, 4.10, color=MUTED, w=1.3, head=False)
    arrow(s, 12.0, 4.10, 12.0, 4.55, color=EMERALD, w=LW)

    node(
        s,
        2.35,
        4.55,
        10.43,
        0.5,
        "AUTOMATED RELEASE   ·   staging  →  canary  →  production   ·   "
        "rollback on any failed check",
        fill=mix(EMERALD, BG, 0.88),
        line=mix(EMERALD, BG, 0.5),
        size=11,
        spc=30,
    )
    arrow(s, 4.02, 5.05, 4.02, 5.30, color=EMERALD, w=LW)

    runtime = [
        (2.35, 3.35, "Model serving  ·  API", CYAN),
        (5.90, 3.35, "Monitoring  ·  drift & latency", ROSE),
        (9.45, 3.33, "Alerts & retrain trigger", ROSE),
    ]
    for i, (rx, rw, txt, col) in enumerate(runtime):
        node(
            s,
            rx,
            5.30,
            rw,
            0.5,
            txt,
            fill=mix(col, BG, 0.90),
            line=mix(col, BG, 0.55),
            size=10.5,
        )
        if i < len(runtime) - 1:
            arrow(
                s,
                rx + rw,
                5.55,
                runtime[i + 1][0],
                5.55,
                color=col,
                w=1.4,
                head_size="sm",
            )

    arrow(s, 11.11, 5.80, 11.11, 6.06, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 11.11, 6.06, 1.95, 6.06, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 1.95, 6.06, 1.95, 4.10, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 1.95, 4.10, 2.35, 4.10, color=ROSE, w=1.3, dashed=DASH)
    tbox(
        s,
        4.3,
        6.12,
        6.4,
        0.26,
        "drift, a schedule or new data triggers the next training run",
        size=9,
        italic=True,
        color=ROSE,
        align="c",
    )

    note_bar(
        s,
        0.55,
        6.50,
        12.23,
        0.50,
        "MLOps is DevOps with two extra pipelines:",
        "data and model become versioned artifacts too — so every release is "
        "reproducible and every rollback is safe.",
        accent=EMERALD,
        size=11,
    )
    return s


def slide_feedback(prs):
    s = new_slide(prs)
    chrome(
        s,
        15,
        kicker="Part D  ·  MLOps & operations",
        title="The Feedback Loop: Monitoring, Drift & Retraining",
        sub="A deployed model is never finished — production data keeps moving, so "
        "measurement has to keep running.",
    )

    panel(s, 0.55, 1.95, 4.3, 4.35, fill=PANEL, line=HAIRLINE)
    section_head(s, 0.78, 2.14, 3.9, "Why models rot in production", color=ROSE)
    cards = [
        (
            2.58,
            "Data drift",
            "Inputs change shape — new devices, seasons, users, formats.",
            VIOLET,
        ),
        (
            3.72,
            "Concept drift",
            "The input → outcome relationship itself changes over time.",
            AMBER,
        ),
        (
            4.86,
            "Label lag",
            "Ground truth arrives late, so quality decays unnoticed.",
            ROSE,
        ),
    ]
    for cy, title, desc, col in cards:
        panel(s, 0.75, cy, 3.9, 1.02, fill=mix(col, BG, 0.93), line=mix(col, BG, 0.5))
        box(s, 0.75, cy, 0.05, 1.02, fill=col, kind="rect")
        tbox(s, 0.98, cy + 0.14, 3.5, 0.28, title, size=12, bold=True, color=WHITE)
        tbox(s, 0.98, cy + 0.46, 3.5, 0.5, desc, size=9.5, color=MUTED, spacing=1.15)

    section_head(s, 5.3, 1.6, 7.4, "The monitoring loop that never sleeps", color=SKY)

    node(
        s,
        5.9,
        2.05,
        3.1,
        0.58,
        "1 · Live traffic & requests",
        fill=PANEL_2,
        line=HAIRLINE,
        size=10.5,
    )
    node(
        s,
        9.5,
        2.05,
        3.28,
        0.58,
        "2 · Log inputs, outputs, latency",
        fill=PANEL_2,
        line=HAIRLINE,
        size=10.5,
    )
    arrow(s, 9.0, 2.34, 9.5, 2.34, color=SKY, w=1.4, head_size="sm")

    node(
        s,
        9.5,
        3.20,
        3.28,
        0.58,
        "3 · Ground truth & labels arrive",
        fill=PANEL_2,
        line=HAIRLINE,
        size=10.5,
    )
    arrow(s, 11.14, 2.63, 11.14, 3.20, color=SKY, w=1.4)

    box(
        s,
        10.19,
        4.18,
        1.9,
        1.0,
        fill=mix(AMBER, BG, 0.86),
        line=mix(AMBER, BG, 0.55),
        lw=1.2,
        kind="diamond",
    )
    tbox(
        s,
        10.19,
        4.18,
        1.9,
        1.0,
        ["drift or metric", "drop detected?"],
        size=9,
        bold=True,
        color=WHITE,
        align="c",
        anchor="m",
        spacing=1.1,
    )
    arrow(s, 11.14, 3.78, 11.14, 4.18, color=AMBER, w=1.4)

    node(
        s,
        6.6,
        4.42,
        3.1,
        0.58,
        "Keep serving · no change",
        fill=mix(EMERALD, BG, 0.90),
        line=mix(EMERALD, BG, 0.55),
        size=10.5,
    )
    arrow(s, 10.19, 4.68, 9.7, 4.68, color=EMERALD, w=1.4)
    tbox(s, 9.74, 4.40, 0.5, 0.24, "no", size=9, bold=True, color=EMERALD)

    node(
        s,
        6.6,
        5.62,
        3.1,
        0.58,
        "Alert & auto-retrain",
        fill=mix(ROSE, BG, 0.90),
        line=mix(ROSE, BG, 0.55),
        size=10.5,
    )
    arrow(s, 11.14, 5.18, 11.14, 5.91, color=ROSE, w=1.4, head=False)
    arrow(s, 11.14, 5.91, 9.7, 5.91, color=ROSE, w=1.4)
    tbox(s, 10.0, 5.44, 1.2, 0.24, "yes", size=9, bold=True, color=ROSE)

    arrow(s, 6.6, 5.91, 5.4, 5.91, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 5.4, 5.91, 5.4, 2.34, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 5.4, 2.34, 5.9, 2.34, color=ROSE, w=1.3, dashed=DASH)
    loop = tbox(
        s,
        4.42,
        4.05,
        2.4,
        0.26,
        "retrained model back into service",
        size=9,
        bold=True,
        color=ROSE,
        align="c",
        anchor="m",
    )
    loop.rotation = 270

    note_bar(
        s,
        5.3,
        6.50,
        7.48,
        0.50,
        "Monitoring is the new testing:",
        "the same metrics you measured before release keep being measured "
        "after it — and they trigger the next release.",
        accent=SKY,
        size=11,
    )
    return s


def slide_genai(prs):
    s = new_slide(prs)
    chrome(
        s,
        16,
        kicker="Part D  ·  Generative AI & LLM systems",
        title="How a Large Language Model Actually Works",
        sub="A transformer predicts one token at a time — everything else in the "
        "system exists to steer, ground and check those predictions.",
    )

    section_head(s, 0.55, 1.6, 5.6, "Generation, one token at a time", color=AMBER)
    vflow(
        s,
        1.35,
        1.98,
        3.4,
        [
            "Prompt: system rules, history, user input",
            "Tokenise — text becomes token IDs",
            "Embeddings — each token becomes a vector",
            "Attention over transformer blocks (context)",
            "Logits → probability of every next token",
            "Sample one token, append, repeat",
        ],
        h=0.5,
        gap=0.18,
        fill=mix(AMBER, BG, 0.92),
        line=mix(AMBER, BG, 0.55),
        size=10,
        arrow_color=AMBER,
    )
    arrow(s, 3.05, 5.88, 3.05, 6.06, color=AMBER, w=1.3, dashed=DASH, head=False)
    arrow(s, 3.05, 6.06, 0.9, 6.06, color=AMBER, w=1.3, dashed=DASH, head=False)
    arrow(s, 0.9, 6.06, 0.9, 2.23, color=AMBER, w=1.3, dashed=DASH, head=False)
    arrow(s, 0.9, 2.23, 1.35, 2.23, color=AMBER, w=1.3, dashed=DASH)
    tbox(
        s,
        1.4,
        6.12,
        3.6,
        0.26,
        "repeats until a stop token or length limit",
        size=9,
        italic=True,
        color=AMBER,
        align="c",
    )

    section_head(s, 6.2, 1.6, 6.58, "What goes into one request", color=SKY)
    panel(s, 6.2, 1.98, 6.58, 2.2, fill=PANEL, line=HAIRLINE)
    chips = [
        (6.45, "System prompt", INDIGO),
        (7.99, "History", SKY),
        (9.53, "User message", CYAN),
        (11.07, "Retrieved ctx", VIOLET),
    ]
    for cx, txt, col in chips:
        node(
            s,
            cx,
            2.32,
            1.42,
            0.44,
            txt,
            fill=mix(col, BG, 0.88),
            line=mix(col, BG, 0.5),
            size=9,
        )
    arrow(s, 9.47, 2.76, 9.47, 3.00, color=SKY, w=1.4)
    node(
        s,
        8.4,
        3.00,
        2.15,
        0.46,
        "LLM  ·  forward pass",
        fill=mix(AMBER, BG, 0.88),
        line=mix(AMBER, BG, 0.5),
        size=10,
    )
    arrow(s, 9.47, 3.46, 9.47, 3.66, color=SKY, w=1.4)
    node(
        s,
        7.55,
        3.66,
        3.85,
        0.42,
        "Response: tokens · text · stop reason",
        fill=PANEL_3,
        line=HAIRLINE,
        size=9.5,
    )

    section_head(s, 6.2, 4.36, 6.58, "Knobs an engineer actually tunes", color=VIOLET)
    knobs = [
        ("temperature", "creativity vs determinism"),
        ("top-p / top-k", "how wide the sampling pool is"),
        ("max tokens", "cost and latency ceiling"),
        ("tools / JSON mode", "structured, actionable output"),
        ("guardrails", "refusals, filters, allowed topics"),
        ("eval & budget", "quality per rupee, per request"),
    ]
    for i, (name, desc) in enumerate(knobs):
        cx = 6.2 + (i % 3) * 2.24
        cy = 4.74 + (i // 3) * 0.72
        panel(s, cx, cy, 2.1, 0.62, fill=PANEL_2, line=HAIRLINE)
        box(s, cx, cy, 0.05, 0.62, fill=VIOLET, kind="rect")
        tbox(s, cx + 0.16, cy + 0.09, 1.86, 0.24, name, size=10, bold=True, color=WHITE)
        tbox(s, cx + 0.16, cy + 0.33, 1.86, 0.24, desc, size=8.5, color=DIM)

    note_bar(
        s,
        0.55,
        6.50,
        12.23,
        0.50,
        "GenAI changes the interface, not the discipline:",
        "prompts, models and datasets still need versioning, evaluation, "
        "monitoring and rollback — the loop on slide 15 applies unchanged.",
        accent=VIOLET,
        size=11,
    )
    return s


def slide_rag(prs):
    s = new_slide(prs)
    chrome(
        s,
        17,
        kicker="Part D  ·  Generative AI & LLM systems",
        title="RAG — Grounding the Model in Your Own Data",
        sub="Retrieve first, generate second: the model answers from passages it "
        "was given, and can cite them.",
    )

    rows = [
        (
            2.02,
            VIOLET,
            ["Source documents", "Chunk & clean", "Embed chunks", "Vector database"],
            "INGESTION  ·  runs offline",
        ),
        (
            3.32,
            SKY,
            ["User question", "Embed the query", "Similarity search", "Top-k passages"],
            "RETRIEVAL  ·  runs per request",
        ),
        (
            4.62,
            CYAN,
            [
                "Question + passages",
                "LLM generates",
                "Answer + citations",
                "Retrieval eval",
            ],
            "GENERATION  ·  runs per request",
        ),
    ]
    xs = [0.55, 3.65, 6.75, 9.85]
    for ry, col, items, cap in rows:
        tbox(s, 0.55, ry - 0.26, 5.0, 0.22, cap, size=8, bold=True, color=DIM, spc=140)
        for i, txt in enumerate(items):
            node(
                s,
                xs[i],
                ry,
                2.93,
                0.55,
                txt,
                fill=mix(col, BG, 0.91),
                line=mix(col, BG, 0.55),
                size=10.5,
            )
            if i < len(items) - 1:
                arrow(
                    s,
                    xs[i] + 2.93,
                    ry + 0.275,
                    xs[i + 1],
                    ry + 0.275,
                    color=col,
                    w=1.4,
                    head_size="sm",
                )

    arrow(s, 11.31, 2.57, 11.31, 2.94, color=VIOLET, w=1.4, head=False)
    arrow(s, 11.31, 2.94, 8.21, 2.94, color=VIOLET, w=1.4, head=False)
    arrow(s, 8.21, 2.94, 8.21, 3.32, color=VIOLET, w=1.4)

    arrow(s, 11.31, 3.87, 11.31, 4.22, color=SKY, w=1.4, head=False)
    arrow(s, 11.31, 4.22, 2.01, 4.22, color=SKY, w=1.4, head=False)
    arrow(s, 2.01, 4.22, 2.01, 4.62, color=SKY, w=1.4)

    opts = [
        (
            0.55,
            "Prompt-only",
            "Cheap and instant, but the model only knows what its weights already "
            "contain — and the context window is finite.",
            DIM,
            PANEL_2,
        ),
        (
            4.65,
            "RAG  ·  retrieval-augmented",
            "Answers are grounded in live, permissioned data; passages are cited, "
            "the index updates without retraining, and cost stays predictable.",
            CYAN,
            mix(CYAN, BG, 0.90),
        ),
        (
            8.75,
            "Fine-tuning",
            "Bakes style, format and behaviour into the weights — expensive, hard "
            "to undo, and it does not add new facts.",
            VIOLET,
            PANEL_2,
        ),
    ]
    for ox, title, desc, col, fill in opts:
        panel(s, ox, 5.42, 4.0, 0.9, fill=fill, line=mix(col, BG, 0.5))
        box(s, ox, 5.42, 0.05, 0.9, fill=col, kind="rect")
        tbox(s, ox + 0.2, 5.54, 3.6, 0.26, title, size=11.5, bold=True, color=WHITE)
        tbox(s, ox + 0.2, 5.84, 3.62, 0.44, desc, size=9, color=MUTED, spacing=1.15)

    note_bar(
        s,
        0.55,
        6.50,
        12.23,
        0.50,
        "RAG is a software architecture,",
        "not a model trick — chunking, embeddings, index freshness and citation "
        "checks are all engineering decisions you can test.",
        accent=CYAN,
        size=11,
    )
    return s


def slide_testing(prs):
    s = new_slide(prs)
    chrome(
        s,
        18,
        kicker="Part E  ·  Testing & responsible AI",
        title="Testing AI Systems — Three Suites, One Discipline",
        sub="Unit tests still matter. They are simply no longer sufficient: you "
        "must also test the data, the statistics and the failure modes.",
    )

    hflow(
        s,
        0.55,
        1.98,
        12.23,
        [
            "Spec & requirements",
            "Unit & integration",
            "Model evaluation tests",
            "Adversarial & safety",
            "Runtime monitoring",
        ],
        h=0.5,
        gap=0.30,
        fill=PANEL_2,
        line=HAIRLINE,
        size=10.5,
        arrow_color=mix(SKY, BG, 0.35),
        lw=1.4,
    )
    tbox(
        s,
        0.55,
        2.56,
        12.23,
        0.24,
        "THE FULL TEST PYRAMID FOR AN AI-ENABLED SYSTEM",
        size=8,
        bold=True,
        color=DIM,
        align="c",
        spc=160,
    )

    suites = [
        (
            0.55,
            VIOLET,
            "1  ·  Data & statistical tests",
            [
                "Schema, null and range checks on every batch",
                "Train / serve skew and feature drift",
                "Label leakage and train-test contamination",
                "Drift thresholds that trip the retrain job",
            ],
            "catches bad input before it becomes a bad model",
        ),
        (
            4.68,
            AMBER,
            "2  ·  Model & behavioural tests",
            [
                "Metric vs baseline on a held-out test set",
                "Quality sliced by segment, group and region",
                "Robustness to noise, perturbation and edge cases",
                "Fairness, calibration and confidence intervals",
            ],
            "judges the model by statistics, not a spec",
        ),
        (
            8.81,
            SKY,
            "3  ·  Software & system tests",
            [
                "API contract, schema and version tests",
                "Latency, load and cost under peak traffic",
                "Failure paths: timeouts, fallbacks, degraded mode",
                "Prompt regression & red-team attack suites",
            ],
            "treats the whole service like ordinary software",
        ),
    ]
    for sx, col, title, items, foot in suites:
        panel(s, sx, 2.95, 3.97, 3.2, fill=PANEL, line=mix(col, BG, 0.45))
        box(s, sx, 2.95, 3.97, 0.05, fill=col, kind="rect")
        tbox(s, sx + 0.24, 3.16, 3.5, 0.3, title, size=12.5, bold=True, color=WHITE)
        box(s, sx + 0.24, 3.56, 3.49, 0.015, fill=HAIRLINE, kind="rect")
        tbox(
            s,
            sx + 0.24,
            3.72,
            3.5,
            1.9,
            [[("▸  ", {"color": col, "size": 10}), (t, {"size": 10})] for t in items],
            color=MUTED,
            spacing=1.16,
            space_after=8,
        )
        tbox(
            s,
            sx + 0.24,
            5.72,
            3.5,
            0.3,
            foot,
            size=9,
            italic=True,
            color=mix(col, BG, 0.35),
        )

    note_bar(
        s,
        0.55,
        6.36,
        12.23,
        0.62,
        "The oracle changes, the discipline does not:",
        "repeatable inputs, expected outputs, regression suites and a gate that "
        "blocks the release — applied to data and behaviour as well as code.",
        accent=AMBER,
        size=11.5,
    )
    return s


def slide_responsible(prs):
    s = new_slide(prs)
    chrome(
        s,
        19,
        kicker="Part E  ·  Testing & responsible AI",
        title="Responsible AI — The NIST AI RMF",
        sub="Four functions run as a cycle around one goal: systems that are "
        "trustworthy enough to be used, and defended.",
    )

    quads = [
        (
            0.55,
            2.15,
            "GOVERN",
            INDIGO,
            "Policies, roles, accountability, risk appetite and culture — set "
            "before anything is built.",
        ),
        (
            3.80,
            2.15,
            "MAP",
            SKY,
            "Context and intended use: who is affected, what can go wrong, and "
            "where the system sits.",
        ),
        (
            3.80,
            4.20,
            "MEASURE",
            AMBER,
            "Run the tests from slide 18 — accuracy, drift, robustness, fairness, "
            "latency and cost.",
        ),
        (
            0.55,
            4.20,
            "MANAGE",
            EMERALD,
            "Prioritise, treat and respond: incident playbooks, human override "
            "and retraining decisions.",
        ),
    ]
    for qx, qy, name, col, desc in quads:
        panel(s, qx, qy, 2.9, 1.75, fill=PANEL, line=mix(col, BG, 0.5))
        box(s, qx, qy, 2.9, 0.05, fill=col, kind="rect")
        tbox(
            s,
            qx + 0.22,
            qy + 0.2,
            2.5,
            0.3,
            name,
            size=13,
            bold=True,
            color=col,
            spc=120,
        )
        tbox(s, qx + 0.22, qy + 0.6, 2.5, 1.0, desc, size=9.5, color=MUTED, spacing=1.2)

    arrow(s, 3.45, 3.02, 3.80, 3.02, color=INDIGO, w=1.4, head_size="sm")
    arrow(s, 5.25, 3.90, 5.25, 4.20, color=SKY, w=1.4, head_size="sm")
    arrow(s, 3.80, 5.07, 3.45, 5.07, color=AMBER, w=1.4, head_size="sm")
    arrow(s, 2.0, 4.20, 2.0, 3.90, color=EMERALD, w=1.4, head_size="sm")
    tbox(
        s,
        0.55,
        6.06,
        6.15,
        0.26,
        "cyclical and continuous — each pass raises the risk bar",
        size=9,
        italic=True,
        color=DIM,
        align="c",
    )

    section_head(s, 7.05, 1.6, 5.73, "Seven traits of trustworthy AI", color=CYAN)
    panel(s, 7.05, 1.98, 5.73, 3.5, fill=PANEL, line=HAIRLINE)
    traits = [
        ("Valid & reliable", AMBER),
        ("Safe", EMERALD),
        ("Secure & resilient", CYAN),
        ("Accountable & transparent", INDIGO),
        ("Explainable & interpretable", VIOLET),
        ("Privacy-enhanced", SKY),
        ("Fair — harmful bias managed", ROSE),
    ]
    for i, (txt, col) in enumerate(traits):
        ty = 2.22 + i * 0.44
        box(s, 7.3, ty + 0.12, 0.12, 0.12, fill=col, line=None, kind="oval")
        tbox(s, 7.58, ty, 5.0, 0.34, txt, size=11, color=MUTED, anchor="m")
        if i < len(traits) - 1:
            box(s, 7.3, ty + 0.37, 5.2, 0.01, fill=mix(HAIRLINE, BG, 0.6), kind="rect")

    panel(s, 7.05, 5.66, 5.73, 0.74, fill=mix(ROSE, BG, 0.92), line=mix(ROSE, BG, 0.5))
    box(s, 7.05, 5.66, 0.05, 0.74, fill=ROSE, kind="rect")
    tbox(
        s,
        7.3,
        5.78,
        5.3,
        0.54,
        [
            [
                ("Human in the loop.   ", {"color": ROSE, "bold": True, "size": 10.5}),
                (
                    "High-impact decisions stay reviewable, appealable and logged.",
                    {"color": MUTED, "size": 10.5},
                ),
            ]
        ],
        anchor="m",
        spacing=1.15,
    )

    note_bar(
        s,
        0.55,
        6.50,
        12.23,
        0.50,
        "Governance is not a gate at the end:",
        "it is the frame around every step — from requirements on slide 3 to "
        "monitoring on slide 15.",
        accent=INDIGO,
        size=11,
    )
    return s
