"""Slides 20-22: comparison, end-to-end diagram, closing."""

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


def slide_compare(prs):
    s = new_slide(prs)
    chrome(
        s,
        20,
        kicker="Part F  ·  Pulling it together",
        title="Traditional SE vs AI Engineering",
        sub="Same engineering profession, two different definitions of "
        '"done" — and the second one never fully closes.',
    )

    cols = [(0.55, 3.0), (3.75, 4.4), (8.35, 4.43)]
    heads = [
        ("", PANEL_3, DIM, 10),
        ("TRADITIONAL SOFTWARE ENGINEERING", mix(SKY, BG, 0.88), SKY, 10),
        ("AI / ML ENGINEERING", mix(AMBER, BG, 0.88), AMBER, 10),
    ]
    for (hx, hw), (txt, fill, col, size) in zip(cols, heads):
        node(
            s,
            hx,
            1.98,
            hw,
            0.5,
            txt,
            fill=fill,
            line=HAIRLINE,
            size=size,
            color=col,
            spc=90,
            align="c" if txt else "c",
        )

    rows = [
        (
            "Primary artifact",
            "Code, architecture documents, tests",
            "Code + data + model + pipeline",
        ),
        (
            "Definition of done",
            "Conforms to the specification",
            "Meets a statistical target on unseen data",
        ),
        (
            "Test oracle",
            "Deterministic expected outputs",
            "Metrics, distributions, human judgement",
        ),
        (
            "Typical failure",
            "Reproducible, visible bugs",
            "Silent, gradual degradation — drift",
        ),
        (
            "Change cadence",
            "Planned, versioned releases",
            "Continuous retraining and evaluation",
        ),
        (
            "Who owns it",
            "One product team",
            "Data, ML, platform and risk teams together",
        ),
    ]
    for i, (dim, se, ai) in enumerate(rows):
        ry = 2.58 + i * 0.60
        node(
            s,
            cols[0][0],
            ry,
            cols[0][1],
            0.54,
            dim,
            fill=PANEL_3,
            line=HAIRLINE,
            size=10.5,
            align="l",
            color=WHITE,
        )
        node(
            s,
            cols[1][0],
            ry,
            cols[1][1],
            0.54,
            se,
            fill=mix(SKY, BG, 0.95),
            line=mix(SKY, BG, 0.6),
            size=10,
            color=MUTED,
        )
        node(
            s,
            cols[2][0],
            ry,
            cols[2][1],
            0.54,
            ai,
            fill=mix(AMBER, BG, 0.95),
            line=mix(AMBER, BG, 0.6),
            size=10,
            color=MUTED,
        )

    note_bar(
        s,
        0.55,
        6.40,
        12.23,
        0.56,
        "Neither replaces the other:",
        "AI engineering is software engineering with two extra artifacts — data "
        "and model — and a definition of done that is measured, not written down.",
        accent=CYAN,
        size=11.5,
    )
    return s


def slide_grand(prs):
    s = new_slide(prs)
    chrome(
        s,
        21,
        kicker="Part F  ·  Pulling it together",
        title="The Whole Picture, End to End",
        sub="From a UML diagram to a monitored, governed AI system — one loop, "
        "three lanes, every artifact from this deck.",
    )

    lanes = [
        (
            "DESIGN",
            SKY,
            2.20,
            [
                "Requirements & UML",
                "Architecture & components",
                "Code + unit & system tests",
                "Release the application",
            ],
        ),
        (
            "MODEL",
            AMBER,
            3.50,
            [
                "Collect & label data",
                "Prepare & features",
                "Train & evaluate",
                "Model registry",
            ],
        ),
        (
            "OPERATE",
            EMERALD,
            4.80,
            [
                "Deploy app + model",
                "Serve predictions",
                "Monitor drift & quality",
                "Alert & retrain",
            ],
        ),
    ]
    xs = [2.45, 5.095, 7.74, 10.385]
    bw, bh = 2.395, 0.55

    for lab, col, ly, items in lanes:
        node(
            s,
            0.55,
            ly,
            1.55,
            bh,
            lab,
            fill=mix(col, BG, 0.86),
            line=mix(col, BG, 0.5),
            size=9,
            spc=60,
        )
        for i, txt in enumerate(items):
            node(
                s,
                xs[i],
                ly,
                bw,
                bh,
                txt,
                fill=mix(col, BG, 0.91),
                line=mix(col, BG, 0.55),
                size=9.5,
            )
            if i < len(items) - 1:
                arrow(
                    s,
                    xs[i] + bw,
                    ly + bh / 2,
                    xs[i + 1],
                    ly + bh / 2,
                    color=col,
                    w=1.4,
                    head_size="sm",
                )

    def handoff(y_from, y_to, col, label):
        cx = xs[-1] + bw / 2
        tx = xs[0] + bw / 2
        arrow(s, cx, y_from, cx, y_to - 0.38, color=col, w=1.4, head=False)
        arrow(s, cx, y_to - 0.38, tx, y_to - 0.38, color=col, w=1.4, head=False)
        arrow(s, tx, y_to - 0.38, tx, y_to, color=col, w=1.4)
        tbox(
            s,
            4.0,
            y_to - 0.66,
            5.6,
            0.24,
            label,
            size=8.5,
            italic=True,
            color=mix(col, BG, 0.3),
            align="c",
        )

    handoff(2.75, 3.50, SKY, "the design tells the model team what to predict")
    handoff(4.05, 4.80, AMBER, "a validated model becomes part of the release")

    arrow(
        s,
        xs[-1] + bw / 2,
        5.35,
        xs[-1] + bw / 2,
        5.68,
        color=ROSE,
        w=1.3,
        dashed=DASH,
        head=False,
    )
    arrow(
        s, xs[-1] + bw / 2, 5.68, 2.27, 5.68, color=ROSE, w=1.3, dashed=DASH, head=False
    )
    arrow(s, 2.27, 5.68, 2.27, 3.775, color=ROSE, w=1.3, dashed=DASH, head=False)
    arrow(s, 2.27, 3.775, 2.45, 3.775, color=ROSE, w=1.3, dashed=DASH)
    tbox(
        s,
        3.6,
        5.42,
        6.4,
        0.24,
        "drift, incidents and new data restart training",
        size=8.5,
        italic=True,
        color=ROSE,
        align="c",
    )

    node(
        s,
        0.55,
        5.90,
        12.23,
        0.50,
        "GOVERN  ·  MAP  ·  MEASURE  ·  MANAGE   —   policies, tests, oversight "
        "and accountability wrap every stage above",
        fill=mix(INDIGO, BG, 0.90),
        line=mix(INDIGO, BG, 0.55),
        size=10.5,
        spc=30,
    )
    note_bar(
        s,
        0.55,
        6.54,
        12.23,
        0.50,
        "One loop, not two projects:",
        "requirements, models and operations are the same delivery pipeline — "
        "with monitoring closing the loop back to design.",
        accent=SKY,
        size=11,
    )
    return s


def slide_close(prs):
    s = new_slide(prs)
    chrome(
        s,
        22,
        kicker="Wrap-up",
        title="Five Things to Take Away",
        sub="If the audience remembers nothing else from these 22 slides, "
        "it should be these.",
    )

    points = [
        (
            "Design still comes first",
            "UML and architecture describe the system. AI adds artifacts — it does "
            "not replace the diagrams.",
            CYAN,
        ),
        (
            "Data and models are software artifacts",
            "Version them, test them and govern them exactly like source code.",
            VIOLET,
        ),
        (
            "Ship pipelines, not notebooks",
            "Automated, validated, reproducible releases are the only way models "
            "survive contact with production.",
            AMBER,
        ),
        (
            "Deployed means monitored",
            "Drift is the default. The loop on slide 15 never actually closes.",
            ROSE,
        ),
        (
            "Trust is engineered",
            "Three test suites, a risk framework and a human in the loop — from "
            "the first requirement to the alert.",
            INDIGO,
        ),
    ]
    for i, (head, desc, col) in enumerate(points):
        py = 1.95 + i * 0.82
        panel(s, 0.55, py, 7.55, 0.72, fill=PANEL, line=HAIRLINE)
        box(s, 0.55, py, 0.05, 0.72, fill=col, kind="rect")
        node(
            s,
            0.78,
            py + 0.16,
            0.4,
            0.4,
            str(i + 1),
            fill=mix(col, BG, 0.85),
            line=mix(col, BG, 0.5),
            size=11,
            kind="round",
            radius=0.3,
        )
        tbox(s, 1.36, py + 0.12, 6.5, 0.28, head, size=12.5, bold=True, color=WHITE)
        tbox(s, 1.36, py + 0.42, 6.6, 0.26, desc, size=9.5, color=MUTED)

    section_head(s, 8.45, 1.6, 4.33, "What comes next", color=SKY)
    panel(s, 8.45, 1.95, 4.33, 2.28, fill=PANEL, line=HAIRLINE)
    nexts = [
        ("Agentic systems", "models that call tools and take actions"),
        ("Evaluation at scale", "automated, continuous quality gates"),
        ("Edge & on-device AI", "smaller models, private data, low latency"),
        ("Regulation & audits", "EU AI Act, NIST, ISO — evidence on demand"),
    ]
    for i, (name, desc) in enumerate(nexts):
        ny = 2.18 + i * 0.52
        box(s, 8.7, ny + 0.14, 0.1, 0.1, fill=SKY, line=None, kind="oval")
        tbox(
            s,
            8.94,
            ny,
            3.7,
            0.44,
            [
                [
                    (name + "  ", {"bold": True, "color": WHITE, "size": 10.5}),
                    (desc, {"color": DIM, "size": 9.5}),
                ]
            ],
            anchor="m",
            spacing=1.1,
        )

    section_head(s, 8.45, 4.42, 4.33, "Sources", color=VIOLET)
    panel(s, 8.45, 4.76, 4.33, 1.4, fill=PANEL_2, line=HAIRLINE)
    tbox(
        s,
        8.7,
        4.94,
        3.9,
        1.1,
        [
            "Microsoft — UML diagram guide",
            "Google — ML engineering & production pipelines",
            "NIST — AI Risk Management Framework 1.0",
            "ISO/IEC 23894 — AI risk management",
        ],
        size=9.5,
        color=MUTED,
        spacing=1.2,
        space_after=4,
    )

    box(
        s,
        0.55,
        6.42,
        12.23,
        0.62,
        fill=mix(CYAN, BG, 0.92),
        line=mix(CYAN, BG, 0.55),
        lw=1.0,
        radius=0.16,
    )
    box(s, 0.551, 6.56, 0.055, 0.34, fill=CYAN, kind="rect")
    tbox(
        s,
        0.85,
        6.52,
        11.6,
        0.42,
        [
            [
                ("Thank you.   ", {"bold": True, "color": CYAN, "size": 14}),
                (
                    "Questions welcome — Bezaleel Paul N  ·  B.Tech CSE  ·  "
                    "AI in Software Design & Engineering",
                    {"color": MUTED, "size": 11.5},
                ),
            ]
        ],
        anchor="m",
    )
    return s
