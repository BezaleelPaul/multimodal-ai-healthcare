"""Slides 5-8: UML diagrams — use case/class, sequence/activity, state, component/deployment."""

from .theme import (
    AMBER,
    BG,
    CYAN,
    DASH,
    DIM,
    EMERALD,
    HAIRLINE,
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
    mix,
    new_slide,
    node,
    note_bar,
    panel,
    section_head,
    tag,
    tbox,
)


def _head(slide, x, y, w, text, color=CYAN):
    section_head(slide, x, y, w, text, color=color)


def _split_panels(slide):
    panel(slide, 0.55, 1.55, 5.9, 5.3, fill=PANEL, line=HAIRLINE)
    panel(slide, 6.68, 1.55, 6.1, 5.3, fill=PANEL, line=HAIRLINE)


def _actor(slide, cx, top, color=SKY, scale=1.0):
    d = 0.32 * scale
    box(slide, cx - d / 2, top, d, d, fill=None, line=color, lw=1.6, kind="oval")
    neck = top + d + 0.05
    body = 0.52 * scale
    arrow(slide, cx, neck, cx, neck + body, color=color, w=1.6, head=False)
    arrow(
        slide,
        cx - 0.26 * scale,
        neck + 0.13 * scale,
        cx + 0.26 * scale,
        neck + 0.13 * scale,
        color=color,
        w=1.6,
        head=False,
    )
    foot = neck + body
    arrow(
        slide,
        cx,
        foot,
        cx - 0.22 * scale,
        foot + 0.32 * scale,
        color=color,
        w=1.6,
        head=False,
    )
    arrow(
        slide,
        cx,
        foot,
        cx + 0.22 * scale,
        foot + 0.32 * scale,
        color=color,
        w=1.6,
        head=False,
    )
    return foot + 0.32 * scale


def _cls(slide, x, y, w, name, attrs, methods, color=VIOLET):
    head_h, row = 0.34, 0.235
    a_h = 0.10 + row * len(attrs)
    m_h = 0.10 + row * len(methods)
    h = head_h + a_h + m_h
    box(
        slide,
        x,
        y,
        w,
        h,
        fill=PANEL_2,
        line=mix(color, BG, 0.55),
        lw=1.2,
        kind="round",
        radius=0.05,
    )
    box(
        slide,
        x + 0.01,
        y + 0.01,
        w - 0.02,
        head_h,
        fill=mix(color, BG, 0.78),
        line=None,
        kind="rect",
    )
    tbox(
        slide,
        x,
        y,
        w,
        head_h,
        name,
        size=11,
        bold=True,
        color=WHITE,
        align="c",
        anchor="m",
    )
    box(
        slide,
        x + 0.06,
        y + head_h,
        w - 0.12,
        0.012,
        fill=mix(color, BG, 0.5),
        line=None,
        kind="rect",
    )
    tbox(
        slide,
        x + 0.14,
        y + head_h + 0.05,
        w - 0.28,
        a_h - 0.06,
        attrs,
        size=8.5,
        color=MUTED,
        spacing=1.15,
        space_after=2,
    )
    box(
        slide,
        x + 0.06,
        y + head_h + a_h,
        w - 0.12,
        0.012,
        fill=mix(color, BG, 0.5),
        line=None,
        kind="rect",
    )
    tbox(
        slide,
        x + 0.14,
        y + head_h + a_h + 0.05,
        w - 0.28,
        m_h - 0.06,
        methods,
        size=8.5,
        color=mix(color, BG, 0.35),
        spacing=1.15,
        space_after=2,
    )
    return y + h


def slide_usecase_class(prs):
    s = new_slide(prs)
    chrome(
        s,
        5,
        kicker="Part A  ·  UML diagrams  1 / 4",
        title="Use-Case Diagram & Class Diagram",
        sub="One view for WHAT the system must do, one for HOW it is structured.",
    )
    _split_panels(s)

    # ------------------------------------------------------------ use case --
    _head(s, 0.78, 1.74, 5.4, "Use case — functionality from the user's view")
    bx, by, bw, bh = 1.30, 2.16, 4.9, 4.30
    box(
        s,
        bx,
        by,
        bw,
        bh,
        fill=mix(CYAN, BG, 0.95),
        line=mix(CYAN, BG, 0.55),
        lw=1.1,
        kind="rect",
        dash=DASH,
    )
    tbox(
        s,
        bx + 0.1,
        by + 0.1,
        bw - 0.2,
        0.24,
        "SYSTEM   ·   ONLINE LEARNING PLATFORM",
        size=8,
        bold=True,
        color=mix(CYAN, BG, 0.35),
        align="c",
        spc=90,
    )

    actor_end = _actor(s, 0.95, 2.72)
    tbox(
        s,
        0.5,
        actor_end + 0.06,
        0.9,
        0.22,
        "Learner",
        size=8.5,
        bold=True,
        color=SKY,
        align="c",
    )

    ovals = [
        (2.5, 2.50, "Log in"),
        (2.5, 3.28, "Browse catalogue"),
        (2.5, 4.06, "Enrol in course"),
        (2.5, 4.98, "Make payment"),
        (2.5, 5.76, "Track progress"),
    ]
    for x, y, txt in ovals:
        node(
            s,
            x,
            y,
            2.5,
            0.58,
            txt,
            fill=mix(SKY, BG, 0.88),
            line=mix(SKY, BG, 0.5),
            size=10,
            kind="oval",
        )
        arrow(s, 1.15, 3.35, x, y + 0.29, color=mix(MUTED, BG, 0.35), w=1.1, head=False)
    arrow(s, 3.75, 4.70, 3.75, 4.98, color=AMBER, w=1.3, dashed=DASH)
    tbox(s, 3.9, 4.72, 1.5, 0.24, "«include»", size=8.5, bold=True, color=AMBER)
    tbox(
        s,
        0.78,
        6.58,
        5.4,
        0.24,
        "oval = a goal  ·  actor = who performs it  ·  dashed = reuse",
        size=8.5,
        color=DIM,
    )

    # --------------------------------------------------------------- class --
    _head(s, 6.9, 1.74, 5.6, "Class — static structure of the domain", color=VIOLET)
    learner_end = _cls(
        s,
        6.95,
        2.16,
        2.6,
        "Learner",
        ["- learnerId: String", "- name: String"],
        ["+ enrol(): void", "+ progress(): Float"],
    )
    _cls(
        s,
        10.0,
        2.16,
        2.6,
        "Course",
        ["- courseCode: String", "- title: String"],
        ["+ seatsLeft(): Int", "+ publish(): void"],
    )
    enr_end = _cls(
        s,
        8.45,
        4.72,
        2.6,
        "Enrollment",
        ["- date: DateTime", "- status: Enum"],
        ["+ complete(): void", "+ refund(): Boolean"],
    )

    arrow(s, 9.55, 2.85, 10.0, 2.85, color=mix(VIOLET, BG, 0.35), w=1.3)
    tbox(s, 9.5, 2.56, 0.3, 0.2, "1", size=8.5, bold=True, color=AMBER, align="c")
    tbox(s, 9.85, 2.56, 0.3, 0.2, "*", size=8.5, bold=True, color=AMBER, align="c")

    arrow(s, 8.25, 3.60, 8.25, 5.44, color=mix(VIOLET, BG, 0.35), w=1.3, head=False)
    arrow(s, 8.25, 5.44, 8.45, 5.44, color=mix(VIOLET, BG, 0.35), w=1.3)
    arrow(s, 11.3, 3.60, 11.3, 5.44, color=mix(VIOLET, BG, 0.35), w=1.3, head=False)
    arrow(s, 11.3, 5.44, 11.05, 5.44, color=mix(VIOLET, BG, 0.35), w=1.3)
    tbox(s, 8.34, 3.66, 0.3, 0.2, "1", size=8.5, bold=True, color=AMBER)
    tbox(s, 8.54, 5.2, 0.3, 0.2, "*", size=8.5, bold=True, color=AMBER)

    tbox(
        s,
        6.95,
        6.55,
        5.6,
        0.24,
        "box = class (name · attributes · operations)  ·  line = relationship",
        size=8.5,
        color=DIM,
    )
    return s


def slide_sequence_activity(prs):
    s = new_slide(prs)
    chrome(
        s,
        6,
        kicker="Part A  ·  UML diagrams  2 / 4",
        title="Sequence Diagram & Activity Diagram",
        sub="Behaviour over time: who talks to whom, and in what order the work happens.",
    )
    _split_panels(s)

    # ----------------------------------------------------------- sequence ---
    _head(s, 0.78, 1.74, 5.4, "Sequence — messages exchanged over time")
    actors = [
        ("  : UI Screen", 0.85),
        ("  : Controller", 2.75),
        ("  : Order Service", 4.65),
    ]
    centers = []
    for name, x in actors:
        node(
            s,
            x,
            2.16,
            1.6,
            0.4,
            name,
            fill=PANEL_3,
            line=mix(SKY, BG, 0.5),
            size=9,
            align="l",
        )
        centers.append(x + 0.8)
    for cx in centers:
        arrow(
            s,
            cx,
            2.56,
            cx,
            6.3,
            color=mix(HAIRLINE, BG, 0.4),
            w=1.0,
            head=False,
            dashed=DASH,
        )

    acts = [(centers[0], 3.0, 5.7), (centers[1], 3.2, 5.5), (centers[2], 3.7, 5.0)]
    for cx, t, b in acts:
        box(
            s,
            cx - 0.08,
            t,
            0.16,
            b - t,
            fill=mix(SKY, BG, 0.72),
            line=None,
            kind="rect",
        )

    msgs = [
        (0, 1, 3.35, "1:  submit(order)", False),
        (1, 2, 3.95, "2:  validateStock()", False),
        (2, 1, 4.55, "3:  OK · total ₹2,499", True),
        (1, 0, 5.15, "4:  render(receipt)", False),
    ]
    for a, b, y, txt, ret in msgs:
        x1, x2 = centers[a], centers[b]
        if ret:
            arrow(s, x1, y, x2, y, color=AMBER, w=1.4, dashed=DASH, head_size="sm")
        else:
            arrow(s, x1, y, x2, y, color=SKY, w=1.4, head_size="sm")
        tbox(
            s,
            min(x1, x2),
            y - 0.26,
            abs(x2 - x1),
            0.24,
            txt,
            size=8.5,
            bold=True,
            color=MUTED,
            align="c",
        )
    tbox(
        s,
        0.78,
        6.55,
        5.4,
        0.24,
        "top → bottom = time  ·  dashed arrow = return message",
        size=8.5,
        color=DIM,
    )

    # ------------------------------------------------------------- activity --
    _head(
        s,
        6.9,
        1.74,
        5.6,
        "Activity — workflow with a decision & parallelism",
        color=AMBER,
    )
    cx = 9.72
    box(s, cx - 0.13, 2.04, 0.26, 0.26, fill=SKY, line=None, kind="oval")
    arrow(s, cx, 2.30, cx, 2.46, color=AMBER, w=1.4)
    node(
        s,
        cx - 1.1,
        2.46,
        2.2,
        0.46,
        "Receive request",
        fill=mix(AMBER, BG, 0.87),
        line=mix(AMBER, BG, 0.5),
        size=10,
    )
    arrow(s, cx, 2.92, cx, 3.16, color=AMBER, w=1.4)
    box(
        s,
        cx - 0.4,
        3.16,
        0.8,
        0.64,
        fill=mix(AMBER, BG, 0.85),
        line=mix(AMBER, BG, 0.55),
        lw=1.2,
        kind="diamond",
    )
    tbox(
        s,
        cx - 0.4,
        3.16,
        0.8,
        0.64,
        "valid?",
        size=8,
        bold=True,
        color=WHITE,
        align="c",
        anchor="m",
    )

    arrow(s, cx + 0.4, 3.48, 11.0, 3.48, color=EMERALD, w=1.4)
    tbox(s, cx + 0.44, 3.22, 0.6, 0.22, "yes", size=8.5, bold=True, color=EMERALD)
    node(
        s,
        11.0,
        3.25,
        1.7,
        0.46,
        "Process order",
        fill=mix(EMERALD, BG, 0.87),
        line=mix(EMERALD, BG, 0.5),
        size=9.5,
    )

    arrow(s, cx - 0.4, 3.48, 8.6, 3.48, color=ROSE, w=1.4)
    tbox(s, 8.66, 3.22, 0.6, 0.22, "no", size=8.5, bold=True, color=ROSE)
    node(
        s,
        6.9,
        3.25,
        1.7,
        0.46,
        "Reject order",
        fill=mix(ROSE, BG, 0.87),
        line=mix(ROSE, BG, 0.5),
        size=9.5,
    )

    arrow(s, 7.75, 3.71, 7.75, 4.2, color=AMBER, w=1.4, head=False)
    arrow(s, 7.75, 4.2, cx, 4.2, color=AMBER, w=1.4, head=False)
    arrow(s, 11.85, 3.71, 11.85, 4.2, color=AMBER, w=1.4, head=False)
    arrow(s, 11.85, 4.2, cx, 4.2, color=AMBER, w=1.4, head=False)
    arrow(s, cx, 4.2, cx, 4.4, color=AMBER, w=1.4)
    box(s, cx - 1.1, 4.4, 2.2, 0.13, fill=AMBER, line=None, kind="rect")
    arrow(s, 8.65, 4.53, 8.65, 4.72, color=AMBER, w=1.4)
    arrow(s, 10.8, 4.53, 10.8, 4.72, color=AMBER, w=1.4)
    node(s, 7.7, 4.72, 1.9, 0.46, "Save order", fill=PANEL_2, line=HAIRLINE, size=9.5)
    node(
        s,
        9.9,
        4.72,
        1.9,
        0.46,
        "Notify customer",
        fill=PANEL_2,
        line=HAIRLINE,
        size=9.5,
    )
    arrow(s, 8.65, 5.18, 8.65, 5.36, color=AMBER, w=1.4)
    arrow(s, 10.8, 5.18, 10.8, 5.36, color=AMBER, w=1.4)
    box(s, cx - 1.1, 5.36, 2.2, 0.13, fill=AMBER, line=None, kind="rect")
    arrow(s, cx, 5.49, cx, 5.78, color=AMBER, w=1.4)
    box(s, cx - 0.15, 5.78, 0.3, 0.3, fill=None, line=SKY, lw=1.6, kind="oval")
    box(s, cx - 0.07, 5.86, 0.14, 0.14, fill=SKY, line=None, kind="oval")

    tbox(
        s,
        6.9,
        6.2,
        5.7,
        0.24,
        "● start   ◆ decision   ▬ fork / join (parallel)   ◎ final",
        size=8.5,
        color=DIM,
    )
    tbox(
        s,
        6.9,
        6.55,
        5.7,
        0.24,
        "Activity diagrams show flow, not which object is responsible.",
        size=8.5,
        color=DIM,
    )
    return s


def slide_state_machine(prs):
    s = new_slide(prs)
    chrome(
        s,
        7,
        kicker="Part A  ·  UML diagrams  3 / 4",
        title="State Machine Diagram",
        sub="One object, many states — every transition is triggered by an event "
        "and may carry a guard condition.",
    )

    for i, (sym, txt) in enumerate(
        [
            ("●", "initial state"),
            ("rounded box", "a state"),
            ("◆", "decision / guard"),
            ("◎", "final state"),
        ]
    ):
        x = 0.55 + i * 2.55
        tbox(
            s,
            x,
            2.05,
            2.4,
            0.26,
            [
                [
                    (sym + "   ", {"color": CYAN, "bold": True}),
                    (txt, {"color": MUTED, "bold": False}),
                ]
            ],
            size=9.5,
            anchor="m",
        )

    y = 3.38
    box(s, 0.85, y - 0.13, 0.26, 0.26, fill=SKY, line=None, kind="oval")
    arrow(s, 1.11, y, 1.55, y, color=CYAN, w=1.5)
    tbox(s, 1.0, 2.78, 1.2, 0.24, "submit", size=8.5, bold=True, color=DIM, align="c")

    node(s, 1.55, y - 0.33, 1.6, 0.66, "Idle", fill=PANEL_3, line=HAIRLINE, size=11)
    arrow(s, 3.15, y, 3.75, y, color=CYAN, w=1.5)
    tbox(s, 3.1, 2.78, 1.0, 0.24, "start", size=8.5, bold=True, color=DIM, align="c")

    node(
        s,
        3.75,
        y - 0.33,
        1.8,
        0.66,
        "Validating",
        fill=mix(SKY, BG, 0.86),
        line=mix(SKY, BG, 0.5),
        size=11,
    )
    arrow(s, 5.55, y, 6.15, y, color=CYAN, w=1.5)
    tbox(s, 5.4, 2.78, 1.1, 0.24, "rules ok", size=8.5, bold=True, color=DIM, align="c")

    box(
        s,
        6.15,
        y - 0.4,
        1.0,
        0.8,
        fill=mix(AMBER, BG, 0.85),
        line=mix(AMBER, BG, 0.55),
        lw=1.2,
        kind="diamond",
    )
    tbox(
        s,
        6.15,
        y - 0.4,
        1.0,
        0.8,
        "valid?",
        size=8.5,
        bold=True,
        color=WHITE,
        align="c",
        anchor="m",
    )

    arrow(s, 7.15, y, 7.85, y, color=EMERALD, w=1.5)
    tbox(s, 7.16, 3.06, 0.7, 0.24, "yes", size=8.5, bold=True, color=EMERALD, align="c")
    node(
        s,
        7.85,
        y - 0.33,
        1.9,
        0.66,
        "Processing",
        fill=mix(AMBER, BG, 0.87),
        line=mix(AMBER, BG, 0.5),
        size=11,
    )
    arrow(s, 9.75, y, 10.25, y, color=EMERALD, w=1.5)
    tbox(s, 9.7, 3.06, 0.9, 0.24, "done", size=8.5, bold=True, color=EMERALD, align="c")
    node(
        s,
        10.25,
        y - 0.33,
        1.85,
        0.66,
        "Completed",
        fill=mix(EMERALD, BG, 0.87),
        line=mix(EMERALD, BG, 0.5),
        size=11,
    )
    arrow(s, 12.1, y, 12.35, y, color=EMERALD, w=1.5)
    box(s, 12.35, y - 0.18, 0.36, 0.36, fill=None, line=SKY, lw=1.6, kind="oval")
    box(s, 12.44, y - 0.09, 0.18, 0.18, fill=SKY, line=None, kind="oval")

    # error branch
    arrow(s, 6.65, 3.78, 6.65, 4.6, color=ROSE, w=1.5)
    tbox(s, 6.75, 3.95, 0.7, 0.24, "no", size=8.5, bold=True, color=ROSE)
    node(
        s,
        5.75,
        4.6,
        1.8,
        0.66,
        "Error",
        fill=mix(ROSE, BG, 0.87),
        line=mix(ROSE, BG, 0.5),
        size=11,
    )

    # retry loop
    arrow(s, 5.75, 4.93, 2.35, 4.93, color=ROSE, w=1.4, head=False)
    arrow(s, 2.35, 4.93, 2.35, 3.74, color=ROSE, w=1.4)
    tbox(s, 3.0, 4.64, 1.0, 0.24, "retry", size=8.5, bold=True, color=ROSE, align="c")

    # timeout
    arrow(s, 8.8, 3.74, 8.8, 4.93, color=ROSE, w=1.4, head=False)
    arrow(s, 8.8, 4.93, 7.55, 4.93, color=ROSE, w=1.4, dashed=DASH)
    tbox(s, 7.7, 4.64, 1.1, 0.24, "timeout", size=8.5, bold=True, color=ROSE, align="c")

    note_bar(
        s,
        0.55,
        6.2,
        12.23,
        0.62,
        "Why it matters for AI:",
        "an AI service is a state machine too — idle → receiving → inferring → "
        "returning, with failed and degraded states plus drift-triggered transitions.",
        accent=SKY,
        size=11.5,
    )
    return s


def slide_component_deployment(prs):
    s = new_slide(prs)
    chrome(
        s,
        8,
        kicker="Part A  ·  UML diagrams  4 / 4",
        title="Component Diagram & Deployment Diagram",
        sub="Two structural views: the parts the software is made of, and the "
        "machines those parts run on.",
    )

    _head(s, 0.55, 1.6, 8.0, "Component — major parts and the interfaces between them")
    comps = [
        (0.75, 2.9, "Presentation", "UI layer · web & mobile", SKY),
        (4.15, 3.1, "Business Logic", "services · rules · workflows", CYAN),
        (7.75, 2.9, "Data Access", "repositories · ORM · caching", VIOLET),
        (11.15, 1.6, "External", "payments · email", AMBER),
    ]
    xs = []
    for x, w, name, sub, col in comps:
        box(
            s,
            x,
            2.05,
            w,
            1.0,
            fill=PANEL_2,
            line=mix(col, BG, 0.55),
            lw=1.2,
            kind="round",
            radius=0.10,
        )
        box(s, x + 0.01, 2.06, 0.05, 0.98, fill=col, kind="rect")
        tbox(s, x + 0.22, 2.2, w - 0.4, 0.3, name, size=12, bold=True, color=WHITE)
        tbox(s, x + 0.22, 2.55, w - 0.4, 0.36, sub, size=9, color=MUTED)
        # component "port" glyph
        box(s, x + w - 0.34, 2.16, 0.2, 0.08, fill=col, line=None, kind="rect")
        box(
            s,
            x + w - 0.24,
            2.26,
            0.2,
            0.08,
            fill=mix(col, BG, 0.5),
            line=None,
            kind="rect",
        )
        xs.append((x, w))
    for i in range(3):
        x1 = xs[i][0] + xs[i][1]
        x2 = xs[i + 1][0]
        arrow(s, x1, 2.55, x2, 2.55, color=mix(SKY, BG, 0.35), w=1.4, head_size="sm")
    tbox(
        s,
        0.55,
        3.2,
        12.23,
        0.26,
        "«interface»    IOrderView   ·   IOrderService   ·   IRepository   ·   "
        "IPaymentGateway",
        size=9.5,
        bold=True,
        color=DIM,
        align="c",
        spc=40,
    )

    _head(
        s,
        0.55,
        3.72,
        8.0,
        "Deployment — nodes, artifacts, and where it runs",
        color=VIOLET,
    )
    nodes = [
        (
            0.75,
            3.3,
            "«node»   User Device",
            "App.apk",
            "Flutter app · local cache",
            SKY,
        ),
        (
            5.05,
            3.3,
            "«node»   App Server · Docker",
            "app.jar",
            "API · AI service · training jobs",
            CYAN,
        ),
        (
            9.35,
            3.4,
            "«node»   Data Server",
            "schema.sql",
            "PostgreSQL · object store · registry",
            VIOLET,
        ),
    ]
    for x, w, head, art, desc, col in nodes:
        box(
            s,
            x,
            4.15,
            w,
            1.55,
            fill=PANEL,
            line=mix(col, BG, 0.5),
            lw=1.2,
            kind="round",
            radius=0.06,
        )
        box(
            s,
            x + 0.01,
            4.16,
            w - 0.02,
            0.36,
            fill=mix(col, BG, 0.84),
            line=None,
            kind="rect",
        )
        tbox(
            s,
            x + 0.16,
            4.16,
            w - 0.3,
            0.36,
            head,
            size=9.5,
            bold=True,
            color=mix(col, BG, 0.25),
            anchor="m",
        )
        box(
            s,
            x + 0.2,
            4.66,
            1.5,
            0.4,
            fill=mix(col, BG, 0.88),
            line=mix(col, BG, 0.5),
            lw=1.0,
            kind="round",
            radius=0.18,
        )
        tbox(
            s,
            x + 0.2,
            4.66,
            1.5,
            0.4,
            art,
            size=9,
            bold=True,
            color=WHITE,
            align="c",
            anchor="m",
        )
        tbox(s, x + 0.2, 5.18, w - 0.4, 0.45, desc, size=9.5, color=MUTED, spacing=1.15)
    arrow(s, 4.05, 5.0, 5.05, 5.0, color=SKY, w=1.5)
    tbox(
        s, 4.05, 4.66, 1.0, 0.28, "REST / JSON", size=8, bold=True, color=SKY, align="c"
    )
    arrow(s, 8.35, 5.0, 9.35, 5.0, color=VIOLET, w=1.5)
    tbox(
        s,
        8.35,
        4.66,
        1.0,
        0.28,
        "SQL / TLS",
        size=8,
        bold=True,
        color=VIOLET,
        align="c",
    )

    note_bar(
        s,
        0.55,
        6.14,
        12.23,
        0.62,
        "Same system, two views:",
        "the component diagram names the pieces and their contracts; the deployment "
        "diagram shows the runtime topology an operator has to monitor.",
        accent=VIOLET,
        size=11.5,
    )
    return s
