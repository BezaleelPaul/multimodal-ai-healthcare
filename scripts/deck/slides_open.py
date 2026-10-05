"""Slides 1-4: title, roadmap, traditional design, UML toolkit."""

from .theme import (
    AMBER,
    BG,
    BG_SOFT,
    CYAN,
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
    swatch_legend,
    tag,
    tbox,
)


def slide_title(prs):
    s = new_slide(prs)
    box(s, 0, 0, 13.333, 0.10, fill=CYAN, kind="rect")
    box(s, 0, 0.10, 13.333, 0.02, fill=mix(SKY, BG, 0.55), kind="rect")

    # decorative rings, bottom right
    for d, col in (
        (4.6, mix(HAIRLINE, BG, 0.75)),
        (3.3, mix(HAIRLINE, BG, 0.55)),
        (2.0, mix(HAIRLINE, BG, 0.4)),
    ):
        box(
            s,
            11.15 - d / 2 + 1.5,
            6.05 - d / 2 + 1.2,
            d,
            d,
            fill=None,
            line=col,
            lw=1.0,
            kind="oval",
        )

    tbox(
        s,
        0.9,
        1.28,
        9.0,
        0.26,
        "B.TECH CSE   ·   SEMINAR PRESENTATION",
        size=11,
        bold=True,
        color=CYAN,
        spc=220,
    )
    tbox(
        s,
        0.9,
        1.62,
        11.4,
        1.6,
        ["AI in Software Design", "& Engineering"],
        size=45,
        bold=True,
        color=WHITE,
        spacing=1.02,
    )
    box(s, 0.9, 3.34, 0.95, 0.05, fill=CYAN, kind="rect")
    tbox(
        s,
        0.9,
        3.56,
        11.0,
        0.34,
        "From UML modeling to AI systems, ML pipelines and MLOps",
        size=17,
        color=SKY,
    )

    rows = [
        (
            4.20,
            "TRADITIONAL SE",
            SKY,
            ["Requirements", "Design", "Code", "Test", "Deploy", "Maintain"],
            PANEL_2,
            HAIRLINE,
        ),
        (
            5.02,
            "AI / ML ENGINEERING",
            VIOLET,
            ["Data", "Train", "Evaluate", "Deploy", "Monitor", "Retrain"],
            mix(VIOLET, BG, 0.86),
            mix(VIOLET, BG, 0.55),
        ),
    ]
    for y, lab, col, items, fill, line in rows:
        tbox(
            s, 0.9, y, 1.55, 0.52, lab, size=9, bold=True, color=col, spc=90, anchor="m"
        )
        x0, wtot, gap = 2.6, 9.85, 0.30
        bw = (wtot - gap * (len(items) - 1)) / len(items)
        cx = x0
        for i, it in enumerate(items):
            node(
                s,
                cx,
                y,
                bw,
                0.52,
                it,
                fill=fill,
                line=line,
                size=10.5,
                color=WHITE if fill == PANEL_2 else WHITE,
            )
            if i < len(items) - 1:
                arrow(s, cx + bw, y + 0.26, cx + bw + gap, y + 0.26, color=col, w=1.4)
            cx += bw + gap

    box(s, 0.9, 6.10, 11.55, 0.02, fill=HAIRLINE, kind="rect")
    tbox(
        s,
        0.9,
        6.28,
        7.0,
        0.32,
        [
            [
                ("Presenter   ", {"color": DIM, "size": 12}),
                ("Bezaleel Paul N", {"color": WHITE, "size": 15, "bold": True}),
            ]
        ],
        anchor="m",
    )
    tbox(
        s,
        7.0,
        6.30,
        5.45,
        0.28,
        "UML  →  AI/ML  →  MLOps  →  Responsible AI",
        size=11.5,
        bold=True,
        color=CYAN,
        align="r",
        anchor="m",
        spc=40,
    )
    tbox(
        s,
        0.9,
        6.66,
        11.55,
        0.28,
        "B.Tech Computer Science Engineering   |   Seminar deck  ·  22 slides  ·  20+ diagrams",
        size=11,
        color=DIM,
        anchor="m",
    )
    return s


def slide_roadmap(prs):
    s = new_slide(prs)
    chrome(
        s,
        2,
        kicker="Roadmap",
        title="How This Deck Zooms In",
        sub="Every diagram answers one question — why do we need the next one?",
    )

    parts = [
        (
            "01",
            "The Basics",
            "Traditional software design",
            [
                "Software development lifecycle",
                "The eight UML diagrams",
                "Design artifacts & views",
            ],
            "Slides 3-8",
            CYAN,
        ),
        (
            "02",
            "The Shift",
            "Why AI changes design",
            [
                "Software engineering meets AI",
                "New artifacts: data, model",
                "The AI / ML lifecycle",
            ],
            "Slides 9-10",
            SKY,
        ),
        (
            "03",
            "The System",
            "AI architecture & pipelines",
            ["Production ML pipeline", "AI system architecture", "Models & evaluation"],
            "Slides 11-13",
            AMBER,
        ),
        (
            "04",
            "The Operations",
            "MLOps, GenAI & monitoring",
            ["MLOps architecture", "Feedback loop & drift", "LLM and RAG architecture"],
            "Slides 14-17",
            EMERALD,
        ),
        (
            "05",
            "The Safeguard",
            "Testing & responsible AI",
            ["Three AI test suites", "NIST AI RMF", "SE vs AI engineering"],
            "Slides 18-22",
            ROSE,
        ),
    ]
    x, w, gap, y, h = 0.55, 2.302, 0.18, 1.92, 3.30
    for num, title, sub, bullets, rng, col in parts:
        panel(s, x, y, w, h, fill=PANEL, line=HAIRLINE)
        box(s, x, y, w, 0.05, fill=col, kind="rect")
        tbox(
            s,
            x + 0.22,
            y + 0.24,
            w - 0.44,
            0.5,
            num,
            size=27,
            bold=True,
            color=mix(col, BG, 0.55),
        )
        tbox(
            s, x + 0.22, y + 0.80, w - 0.44, 0.3, title, size=14, bold=True, color=WHITE
        )
        tbox(
            s,
            x + 0.22,
            y + 1.10,
            w - 0.44,
            0.44,
            sub,
            size=10.5,
            color=col,
            spacing=1.1,
        )
        box(s, x + 0.22, y + 1.62, w - 0.44, 0.015, fill=HAIRLINE, kind="rect")
        tbox(
            s,
            x + 0.22,
            y + 1.78,
            w - 0.40,
            1.1,
            [
                [
                    ("▸  ", {"color": col, "size": 9.5}),
                    (b, {"color": MUTED, "size": 9.5}),
                ]
                for b in bullets
            ],
            spacing=1.15,
            space_after=5,
        )
        tag(s, x + 0.22, y + 2.88, rng, color=col, size=8, h=0.26)
        x += w + gap

    tbox(
        s,
        0.55,
        5.50,
        4.0,
        0.24,
        "ZOOM-IN PATH",
        size=9,
        bold=True,
        color=DIM,
        spc=160,
        anchor="m",
    )
    chain = [
        "Software",
        "UML",
        "AI system",
        "ML lifecycle",
        "Model",
        "Pipeline",
        "MLOps",
        "GenAI",
        "Monitoring",
        "Responsible AI",
    ]
    hflow(
        s,
        0.55,
        5.82,
        12.23,
        chain,
        h=0.5,
        gap=0.14,
        fill=PANEL_2,
        line=HAIRLINE,
        size=8.5,
        arrow_color=mix(SKY, BG, 0.35),
        lw=1.1,
        bold=False,
    )
    note_bar(
        s,
        0.55,
        6.50,
        12.23,
        0.56,
        "Design does not disappear.",
        "AI systems still need architecture and UML — they simply add data, model, "
        "experimentation, evaluation and risk artifacts around the software.",
        accent=SKY,
        size=11.5,
    )
    return s


def slide_traditional(prs):
    s = new_slide(prs)
    chrome(
        s,
        3,
        kicker="Part A  ·  Traditional software engineering",
        title="How Traditional Software Is Designed",
        sub="Requirements drive an architecture, the architecture drives code, and "
        "tests prove the result behaves exactly as specified.",
    )

    hflow(
        s,
        0.55,
        1.98,
        12.23,
        ["Requirements", "Design", "Code", "Testing", "Deployment", "Maintenance"],
        h=0.54,
        gap=0.32,
        fill=mix(CYAN, BG, 0.88),
        line=mix(CYAN, BG, 0.55),
        size=11.5,
        arrow_color=CYAN,
        lw=1.6,
    )
    tbox(
        s,
        0.55,
        2.62,
        12.23,
        0.24,
        "THE SOFTWARE DEVELOPMENT LIFE CYCLE (SDLC)",
        size=8.5,
        bold=True,
        color=DIM,
        align="c",
        spc=160,
    )

    panel(s, 0.55, 3.02, 6.0, 3.02)
    section_head(s, 0.8, 3.24, 5.5, "Design artifacts engineers produce", color=CYAN)
    tbox(
        s,
        0.8,
        3.64,
        5.5,
        2.2,
        [
            [("▸  ", {"color": CYAN}), ("Use-case model — actors and goals", {})],
            [("▸  ", {"color": CYAN}), ("Class model — domain objects and rules", {})],
            [("▸  ", {"color": CYAN}), ("Sequence & activity — runtime behaviour", {})],
            [
                ("▸  ", {"color": CYAN}),
                ("Component & deployment — structure and hosting", {}),
            ],
            [
                ("▸  ", {"color": CYAN}),
                ("Architecture document — layers, data flow", {}),
            ],
        ],
        size=11.5,
        color=MUTED,
        spacing=1.2,
        space_after=9,
    )
    tbox(
        s,
        0.8,
        5.66,
        5.5,
        0.3,
        "Drawn on slides 5-8",
        size=10,
        bold=True,
        color=DIM,
        spc=60,
    )

    panel(s, 6.78, 3.02, 6.0, 3.02, fill=PANEL_2)
    section_head(s, 7.03, 3.24, 5.5, 'What makes it "traditional"', color=SKY)
    tbox(
        s,
        7.03,
        3.64,
        5.5,
        2.2,
        [
            [
                ("▸  ", {"color": SKY}),
                ("Behaviour is deterministic — same input, same output", {}),
            ],
            [
                ("▸  ", {"color": SKY}),
                ("Correctness = conformance to the specification", {}),
            ],
            [
                ("▸  ", {"color": SKY}),
                ("Changes are planned, versioned and released", {}),
            ],
            [
                ("▸  ", {"color": SKY}),
                ("Tests are repeatable and failures are visible", {}),
            ],
            [
                ("▸  ", {"color": SKY}),
                ("Once deployed, it does not degrade on its own", {}),
            ],
        ],
        size=11.5,
        color=MUTED,
        spacing=1.2,
        space_after=9,
    )
    tbox(
        s,
        7.03,
        5.66,
        5.5,
        0.3,
        "Hold this thought — AI breaks the last two",
        size=10,
        bold=True,
        color=DIM,
        spc=60,
    )

    note_bar(
        s,
        0.55,
        6.32,
        12.23,
        0.62,
        "Next:",
        "the eight diagrams engineers use to describe a system before a single "
        "line of code is written.",
        accent=CYAN,
        size=12,
    )
    return s


def slide_uml_toolkit(prs):
    s = new_slide(prs)
    chrome(
        s,
        4,
        kicker="Part A  ·  Traditional software engineering",
        title="The UML Toolkit — Eight Diagrams, Two Views",
        sub="Structural diagrams describe what the system IS. Behavioural diagrams "
        "describe what it DOES.",
    )

    cards = [
        (
            "Use Case",
            "BEHAVIOURAL",
            "Who interacts with the system and what they are allowed to do.",
            CYAN,
        ),
        (
            "Class",
            "STRUCTURAL",
            "Objects, attributes, methods and the relationships between them.",
            VIOLET,
        ),
        (
            "Sequence",
            "BEHAVIOURAL",
            "Messages exchanged between objects, ordered in time.",
            CYAN,
        ),
        (
            "Activity",
            "BEHAVIOURAL",
            "Workflow: actions, decisions, branches and parallel paths.",
            CYAN,
        ),
        (
            "State Machine",
            "BEHAVIOURAL",
            "States and transitions of one object or of the system.",
            CYAN,
        ),
        (
            "Component",
            "STRUCTURAL",
            "Major parts of the system and the interfaces between them.",
            VIOLET,
        ),
        (
            "Deployment",
            "STRUCTURAL",
            "Nodes, artifacts and where the software actually runs.",
            VIOLET,
        ),
        (
            "Architecture",
            "STRUCTURAL",
            "The big picture: layers, services, data and external systems.",
            VIOLET,
        ),
    ]
    w, gap, h = 2.91, 0.20, 2.06
    for i, (name, kind, desc, col) in enumerate(cards):
        x = 0.55 + (i % 4) * (w + gap)
        y = 1.98 + (i // 4) * (h + 0.16)
        panel(s, x, y, w, h, fill=PANEL, line=HAIRLINE)
        box(s, x, y, 0.05, h, fill=col, kind="rect")
        tag(s, x + 0.24, y + 0.22, kind, color=col, size=7.5, h=0.24)
        tbox(
            s, x + 0.24, y + 0.66, w - 0.48, 0.34, name, size=15, bold=True, color=WHITE
        )
        box(s, x + 0.24, y + 1.10, w - 0.48, 0.015, fill=HAIRLINE, kind="rect")
        tbox(
            s,
            x + 0.24,
            y + 1.26,
            w - 0.48,
            0.7,
            desc,
            size=10,
            color=MUTED,
            spacing=1.22,
        )

    note_bar(
        s,
        0.55,
        6.44,
        12.23,
        0.56,
        "Architecture diagrams",
        "sit on top of UML: they compose these views into one picture of the "
        "deployable system.   Source: Microsoft UML diagram documentation.",
        accent=VIOLET,
        size=11.5,
    )
    return s
