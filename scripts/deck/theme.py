"""Design system: palette, typography and primitive shape helpers."""

from typing import Any

from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

# ---------------------------------------------------------------- palette ---
BG = "0B132B"
BG_SOFT = "0E1730"
PANEL = "141E3C"
PANEL_2 = "1A2647"
PANEL_3 = "223054"
HAIRLINE = "2C3C6B"

CYAN = "00B4D8"
SKY = "4CC9F0"
VIOLET = "A78BFA"
AMBER = "FBBF24"
EMERALD = "34D399"
ROSE = "FB7185"
INDIGO = "818CF8"
WHITE = "F8FAFC"
MUTED = "CBD5E1"
DIM = "94A3B8"

FONT = "Arial"
DASH = MSO_LINE_DASH_STYLE.DASH
DOT = MSO_LINE_DASH_STYLE.ROUND_DOT

ALIGN = {
    "l": PP_ALIGN.LEFT,
    "c": PP_ALIGN.CENTER,
    "r": PP_ALIGN.RIGHT,
    "j": PP_ALIGN.JUSTIFY,
}
ANCHOR = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}

SHAPE = {
    "rect": MSO_SHAPE.RECTANGLE,
    "round": MSO_SHAPE.ROUNDED_RECTANGLE,
    "oval": MSO_SHAPE.OVAL,
    "diamond": MSO_SHAPE.DIAMOND,
    "hex": MSO_SHAPE.HEXAGON,
    "chevron": MSO_SHAPE.CHEVRON,
    "pent": MSO_SHAPE.PENTAGON,
    "para": MSO_SHAPE.PARALLELOGRAM,
    "cyl": MSO_SHAPE.CAN,
    "cube": MSO_SHAPE.CUBE,
    "donut": MSO_SHAPE.DONUT,
    "cloud": MSO_SHAPE.CLOUD,
}


def I(v):
    return Inches(v)


def C(h):
    return RGBColor.from_string(h)


def mix(a, b, t):
    """Blend two hex colours, t=0 -> a, t=1 -> b."""
    ai = [int(a[i : i + 2], 16) for i in (0, 2, 4)]
    bi = [int(b[i : i + 2], 16) for i in (0, 2, 4)]
    return "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ai, bi))


# ----------------------------------------------------------------- basics ---
def new_slide(prs, bg=BG):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = C(bg)
    return slide


def _clean(shape):
    try:
        shape.shadow.inherit = False
    except Exception:
        pass
    return shape


def _fill(shape, fill):
    if fill is None:
        shape.fill.background()
    else:
        shape.fill.solid()
        shape.fill.fore_color.rgb = C(fill)


def _line(shape, line, width=1.0, dash=None):
    if line is None:
        shape.line.fill.background()
        return
    shape.line.color.rgb = C(line)
    shape.line.width = Pt(width)
    if dash:
        shape.line.dash_style = dash


def box(
    slide,
    x,
    y,
    w,
    h,
    fill: Any = PANEL,
    line: Any = None,
    lw=1.0,
    kind="round",
    radius=0.10,
    dash=None,
    rot=None,
    grad=None,
):
    sh = slide.shapes.add_shape(SHAPE[kind], I(x), I(y), I(w), I(h))
    _clean(sh)
    if kind == "round":
        try:
            sh.adjustments[0] = radius
        except Exception:
            pass
    if grad:
        _gradient(sh, grad[0], grad[1], grad[2])
    else:
        _fill(sh, fill)
    _line(sh, line, lw, dash)
    if rot:
        sh.rotation = rot
    tf = sh.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return sh


def _gradient(shape, c1, c2, angle=5400000):
    """Solid -> solid linear gradient fill (angle in 60000ths of a degree)."""
    spPr = shape.fill._xPr
    for tag in ("a:solidFill", "a:noFill", "a:gradFill", "a:blipFill", "a:pattFill"):
        el = spPr.find(qn(tag))
        if el is not None:
            spPr.remove(el)
    grad = spPr.makeelement(qn("a:gradFill"), {"flip": "none", "rotWithShape": "1"})
    lst = grad.makeelement(qn("a:gsLst"), {})
    for pos, col in ((0, c1), (100000, c2)):
        gs = grad.makeelement(qn("a:gs"), {"pos": str(pos)})
        clr = grad.makeelement(qn("a:srgbClr"), {"val": col})
        gs.append(clr)
        lst.append(gs)
    grad.append(lst)
    lin = grad.makeelement(qn("a:lin"), {"ang": str(angle), "scaled": "0"})
    grad.append(lin)
    ln = spPr.find(qn("a:ln"))
    if ln is not None:
        ln.addprevious(grad)
    else:
        spPr.append(grad)


# ------------------------------------------------------------------ text ----
def _normalise(paras):
    if isinstance(paras, str):
        return [paras]
    return list(paras)


def _write(
    tf,
    paras,
    size,
    bold,
    color,
    align,
    spacing,
    space_after,
    font,
    italic=False,
    spc=None,
):
    tf.word_wrap = True
    items = _normalise(paras)
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = ALIGN[align]
        p.line_spacing = spacing
        p.space_after = Pt(space_after)
        runs: Any = item if isinstance(item, (list, tuple)) else [(item, {})]
        for text, opts in runs:
            r = p.add_run()
            r.text = text
            f = r.font
            f.name = opts.get("font", font)
            f.size = Pt(opts.get("size", size))
            f.bold = opts.get("bold", bold)
            f.italic = opts.get("italic", italic)
            f.color.rgb = C(opts.get("color", color))
            tracking = opts.get("spc", spc)
            if tracking:
                r._r.get_or_add_rPr().set("spc", str(int(tracking)))
    return tf


def tbox(
    slide,
    x,
    y,
    w,
    h,
    paras,
    size=12.0,
    bold=False,
    color=WHITE,
    align="l",
    anchor="t",
    wrap=True,
    spacing=1.0,
    space_after=0,
    font=FONT,
    italic=False,
    spc=None,
    shrink=False,
):
    tb = slide.shapes.add_textbox(I(x), I(y), I(w), I(h))
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = ANCHOR[anchor]
    _write(
        tf,
        paras,
        size,
        bold,
        color,
        align,
        spacing,
        space_after,
        font,
        italic=italic,
        spc=spc,
    )
    if shrink:
        tf.auto_size = None
    return tb


def label(
    slide,
    x,
    y,
    w,
    h,
    text,
    size=11,
    bold=True,
    color=WHITE,
    align="c",
    anchor="m",
    spacing=0.95,
    spc=None,
    font=FONT,
):
    return tbox(
        slide,
        x,
        y,
        w,
        h,
        text,
        size=size,
        bold=bold,
        color=color,
        align=align,
        anchor=anchor,
        spacing=spacing,
        spc=spc,
        font=font,
    )


def node(
    slide,
    x,
    y,
    w,
    h,
    text,
    fill=PANEL,
    line=HAIRLINE,
    size=10.5,
    color=WHITE,
    lw=1.0,
    kind="round",
    radius=0.14,
    bold=True,
    align="c",
    dash=None,
    spc=None,
    grad=None,
    sub=None,
    sub_size=None,
    sub_color=DIM,
    badge=None,
    badge_color=None,
):
    """Rounded card with centred label (optionally a second line)."""
    sh = box(
        slide,
        x,
        y,
        w,
        h,
        fill=fill,
        line=line,
        lw=lw,
        kind=kind,
        radius=radius,
        dash=dash,
        grad=grad,
    )
    if badge is not None:
        bc = badge_color or CYAN
        bh = min(h - 0.14, 0.30)
        by = y + (h - bh) / 2
        bx = x + 0.10
        chip = box(
            slide,
            bx,
            by,
            bh,
            bh,
            fill=mix(bc, BG, 0.80),
            line=mix(bc, BG, 0.55),
            lw=0.75,
            kind="round",
            radius=0.3,
        )
        _write(chip.text_frame, badge, 8.0, True, bc, "c", 1.0, 0, FONT)
        chip.text_frame.vertical_anchor = ANCHOR["m"]
        tbox(
            slide,
            bx + bh + 0.12,
            y,
            w - (bh + 0.32),
            h,
            text,
            size=size,
            bold=bold,
            color=color,
            align="l" if align == "c" else align,
            anchor="m",
            spacing=0.95,
            spc=spc,
        )
        return sh
    paras = [text]
    if sub:
        paras = [
            [(text, {"size": size, "bold": bold, "color": color})],
            [
                (
                    sub,
                    {"size": sub_size or size - 1.5, "bold": False, "color": sub_color},
                )
            ],
        ]
    _write(sh.text_frame, paras, size, bold, color, align, 0.95, 1, FONT, spc=spc)
    sh.text_frame.vertical_anchor = ANCHOR["m"]
    return sh


def tag(slide, x, y, text, color=CYAN, size=8.0, w=None, h=0.24, fill=None):
    """Small pill label."""
    w = w or (0.16 + 0.070 * len(text))
    sh = box(
        slide,
        x,
        y,
        w,
        h,
        fill=fill or mix(color, BG, 0.82),
        line=mix(color, BG, 0.5),
        lw=0.75,
        radius=0.5,
    )
    _write(sh.text_frame, text, size, True, color, "c", 1.0, 0, FONT, spc=40)
    sh.text_frame.vertical_anchor = ANCHOR["m"]
    return sh


# --------------------------------------------------------------- arrows -----
def _arrow_head(conn, size="med", both=False):
    ln = conn.line._get_or_add_ln()
    if both:
        he = ln.makeelement(
            qn("a:headEnd"), {"type": "triangle", "w": size, "len": size}
        )
        ln.append(he)
    te = ln.makeelement(qn("a:tailEnd"), {"type": "triangle", "w": size, "len": size})
    ln.append(te)


def arrow(
    slide,
    x1,
    y1,
    x2,
    y2,
    color=CYAN,
    w=1.5,
    dashed=False,
    head=True,
    both=False,
    head_size="med",
):
    conn = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, I(x1), I(y1), I(x2), I(y2)
    )
    conn.line.color.rgb = C(color)
    conn.line.width = Pt(w)
    if dashed:
        conn.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    if head:
        _arrow_head(conn, head_size, both)
    return conn


def path(slide, pts, color=CYAN, w=1.5, dashed=False, head=True, head_size="med"):
    """Poly-line through inch coordinates; arrow-head on the final segment."""
    n = len(pts) - 1
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[i + 1]
        if x1 == x2 and y1 == y2:
            continue
        arrow(
            slide,
            x1,
            y1,
            x2,
            y2,
            color=color,
            w=w,
            dashed=dashed,
            head=head and i == n - 1,
            head_size=head_size,
        )


def elbow(slide, x1, y1, x2, y2, color=CYAN, w=1.5, dashed=False, mid=None, head=True):
    """Right-angle connector: horizontal then vertical (or explicit mid point)."""
    if mid is None:
        mid = x2 if abs(x2 - x1) > abs(y2 - y1) else y1
    if abs(x2 - x1) > abs(y2 - y1):
        pts = [(x1, y1), (mid, y1), (mid, y2), (x2, y2)]
    else:
        pts = [(x1, y1), (x1, mid), (x2, mid), (x2, y2)]
    path(slide, pts, color=color, w=w, dashed=dashed, head=head)


def loop_arrow(
    slide,
    x,
    y,
    w,
    h,
    color=ROSE,
    w_pt=1.5,
    dashed=True,
    label_text=None,
    label_size=8.5,
    flip=False,
):
    """Arc-style feedback arrow drawn as a 3-segment bracket."""
    if not flip:
        pts = [(x, y), (x, y + h / 2), (x + w, y + h / 2), (x + w, y)]
    else:
        pts = [(x + w, y), (x + w, y + h / 2), (x, y + h / 2), (x, y)]
    path(slide, pts, color=color, w=w_pt, dashed=dashed, head=True)
    if label_text:
        tbox(
            slide,
            x,
            y + h / 2 - 0.42,
            w,
            0.3,
            label_text,
            size=label_size,
            bold=True,
            color=color,
            align="c",
            anchor="b",
        )


# ------------------------------------------------------------ page frame ----
FOOTER_TEXT = "AI in Software Design & Engineering   |   From UML to AI / MLOps"


def chrome(slide, page, title=None, kicker=None, sub=None, footer=FOOTER_TEXT):
    """Title bar, accent rule, footer strip and page number."""
    box(slide, 0, 7.16, 13.333, 0.34, fill=BG_SOFT, line=None, kind="rect")
    box(slide, 0, 7.16, 13.333, 0.02, fill=HAIRLINE, line=None, kind="rect")
    tbox(slide, 0.55, 7.24, 8.5, 0.2, footer, size=8.5, color=DIM, anchor="m")
    tbox(
        slide,
        12.0,
        7.24,
        0.78,
        0.2,
        f"{page:02d}",
        size=8.5,
        bold=True,
        color=CYAN,
        align="r",
        anchor="m",
    )
    if kicker:
        tbox(
            slide,
            0.55,
            0.34,
            8.0,
            0.2,
            kicker.upper(),
            size=9,
            bold=True,
            color=CYAN,
            spc=180,
        )
    if title:
        tbox(
            slide,
            0.55,
            0.56,
            11.0,
            0.46,
            title,
            size=25,
            bold=True,
            color=WHITE,
            anchor="t",
        )
        box(slide, 0.55, 1.10, 0.62, 0.045, fill=CYAN, line=None, kind="rect")
        box(slide, 1.20, 1.10, 11.58, 0.045, fill=HAIRLINE, line=None, kind="rect")
    if sub:
        tbox(slide, 0.55, 1.24, 12.2, 0.34, sub, size=12, color=MUTED, spacing=1.1)


def section_head(slide, x, y, w, text, color=CYAN, size=11.5):
    box(slide, x, y + 0.04, 0.05, 0.2, fill=color, line=None, kind="rect")
    tbox(
        slide,
        x + 0.16,
        y,
        w - 0.16,
        0.26,
        text.upper(),
        size=size,
        bold=True,
        color=color,
        anchor="m",
        spc=60,
    )


def panel(slide, x, y, w, h, fill=PANEL, line=HAIRLINE, radius=0.06, lw=1.0, dash=None):
    return box(
        slide,
        x,
        y,
        w,
        h,
        fill=fill,
        line=line,
        lw=lw,
        kind="round",
        radius=radius,
        dash=dash,
    )


def note_bar(slide, x, y, w, h, lead, body, accent=SKY, size=11.5):
    box(
        slide,
        x,
        y,
        w,
        h,
        fill=mix(accent, BG, 0.90),
        line=mix(accent, BG, 0.62),
        lw=1.0,
        radius=0.16,
    )
    box(
        slide, x + 0.001, y + 0.14, 0.055, h - 0.28, fill=accent, line=None, kind="rect"
    )
    tbox(
        slide,
        x + 0.24,
        y + 0.1,
        w - 0.44,
        h - 0.2,
        [
            [
                (lead + "   ", {"bold": True, "color": accent, "size": size}),
                (body, {"bold": False, "color": MUTED, "size": size - 0.5}),
            ]
        ],
        anchor="m",
        spacing=1.05,
    )


def swatch_legend(slide, x, y, items, size=8.5, gap=1.42, dot=0.115):
    for i, (col, txt) in enumerate(items):
        cx = x + i * gap
        box(slide, cx, y + 0.045, dot, dot, fill=col, line=None, kind="oval")
        tbox(
            slide,
            cx + dot + 0.08,
            y,
            gap - dot - 0.1,
            0.2,
            txt,
            size=size,
            color=MUTED,
            anchor="m",
        )


def vflow(
    slide,
    x,
    y,
    w,
    labels,
    h=0.44,
    gap=0.2,
    fill=PANEL,
    line=HAIRLINE,
    color=WHITE,
    size=10.0,
    arrow_color=CYAN,
    lw=1.4,
    align="c",
    badges=False,
    badge_color=CYAN,
):
    """Stack of boxes joined by down-arrows. Returns list of (top, bottom) pairs."""
    boxes = []
    cy = y
    for i, lab in enumerate(labels):
        node(
            slide,
            x,
            cy,
            w,
            h,
            lab,
            fill=fill,
            line=line,
            size=size,
            color=color,
            align=align,
            badge=(str(i + 1).zfill(2) if badges else None),
            badge_color=badge_color,
        )
        boxes.append((cy, cy + h))
        if i < len(labels) - 1:
            arrow(
                slide,
                x + w / 2,
                cy + h,
                x + w / 2,
                cy + h + gap,
                color=arrow_color,
                w=lw,
            )
        cy += h + gap
    return boxes, cy


def hflow(
    slide,
    x,
    y,
    w,
    labels,
    h=0.44,
    gap=0.24,
    fill=PANEL,
    line=HAIRLINE,
    color=WHITE,
    size=10.0,
    arrow_color=CYAN,
    lw=1.4,
    align="c",
    bold=True,
):
    """Row of boxes joined by right-arrows. Returns list of (left, right) pairs."""
    n = len(labels)
    bw = (w - gap * (n - 1)) / n
    boxes = []
    cx = x
    for i, lab in enumerate(labels):
        node(
            slide,
            cx,
            y,
            bw,
            h,
            lab,
            fill=fill,
            line=line,
            size=size,
            color=color,
            align=align,
            bold=bold,
        )
        boxes.append((cx, cx + bw))
        if i < n - 1:
            arrow(
                slide,
                cx + bw,
                y + h / 2,
                cx + bw + gap,
                y + h / 2,
                color=arrow_color,
                w=lw,
            )
        cx += bw + gap
    return boxes
