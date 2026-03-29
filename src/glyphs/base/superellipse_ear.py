from shapes.superellipse import superellipse


def _draw_outer_ear(
    pen,
    stroke,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    tooth,
    side="right",
):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    p_start = (x1 + stroke, y1 + tooth)
    p_end = (x1 + stroke, y2 - tooth)

    # Trace: p_start → bottom → right side (superellipse) → top → p_end → close
    pen.moveTo(p_start)
    pen.lineTo((mid_x, y1))
    # bottom-right quarter
    pen.curveTo(
        (mid_x + hx, y1),
        (x2, mid_y - hy),
        (x2, mid_y),
    )
    # top-right quarter
    pen.curveTo(
        (x2, mid_y + hy),
        (mid_x + hx, y2),
        (mid_x, y2),
    )
    pen.lineTo(p_end)
    pen.closePath()


def draw_superellipse_ear(
    pen,
    stroke,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    tooth,
    side="right",
):
    # superellipse(pen, x1, y1, x2, y2, hx, hy, clockwise=False)
    _draw_outer_ear(
        pen,
        stroke,
        x1,
        y1,
        x2,
        y2,
        hx,
        hy,
        tooth,
        side="right",
    )

    w = (x2 - x1) / 2
    h = (y2 - y1) / 2
    inner_hx = hx * (w - stroke) / w
    inner_hy = hy * (h - stroke) / h

    superellipse(
        pen,
        x1 + stroke,
        y1 + stroke,
        x2 - stroke,
        y2 - stroke,
        inner_hx,
        inner_hy,
        clockwise=True,
    )
