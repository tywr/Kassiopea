from shapes.superellipse import draw_superellipse
from shapes.rect import draw_rect


def _draw_outer_ear_left(
    pen,
    stroke,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    tooth,
    cover,
):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    p_start = (x1 + stroke, y1 + tooth - stroke / 2)
    p_end = (x1 + stroke, y2 - tooth + stroke / 2)

    pen.moveTo(p_start)
    pen.curveTo((p_start[0], y1), (mid_x, y1), (mid_x, y1))
    pen.curveTo(
        (mid_x + hx, y1),
        (x2, mid_y - hy),
        (x2, mid_y),
    )
    pen.curveTo(
        (x2, mid_y + hy),
        (mid_x + hx, y2),
        (mid_x, y2),
    )
    pen.curveTo((mid_x, y2), (p_end[0], y2), (p_end[0], p_end[1]))
    pen.closePath()


def _draw_outer_ear_right(
    pen,
    stroke,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    tooth,
    cover,
):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    p_start = (x2 - stroke, y1 + tooth - stroke / 2)
    p_end   = (x2 - stroke, y2 - tooth + stroke / 2)

    pen.moveTo(p_end)                                        # start top-right
    pen.curveTo((p_end[0], y2), (mid_x, y2), (mid_x, y2))  # → top-middle
    pen.curveTo(                                             # top-left quarter
        (mid_x - hx, y2),
        (x1, mid_y + hy),
        (x1, mid_y),
    )
    pen.curveTo(                                             # bottom-left quarter
        (x1, mid_y - hy),
        (mid_x - hx, y1),
        (mid_x, y1),
    )
    pen.curveTo((mid_x, y1), (p_start[0], y1), p_start)    # → bottom-right
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
    cover,
    side="right",
):
    if side == "left":
        _draw_outer_ear_left(
            pen,
            stroke,
            x1,
            y1,
            x2,
            y2,
            hx,
            hy,
            tooth,
            cover,
        )
    if side == "right":
        _draw_outer_ear_right(
            pen,
            stroke,
            x1,
            y1,
            x2,
            y2,
            hx,
            hy,
            tooth,
            cover,
        )

    w = (x2 - x1) / 2
    h = (y2 - y1) / 2
    inner_hx = hx * (w - stroke) / w
    inner_hy = hy * (h - stroke) / h

    draw_superellipse(
        pen,
        x1 + stroke,
        y1 + stroke,
        x2 - stroke,
        y2 - stroke,
        inner_hx,
        inner_hy,
        clockwise="left",
    )

    # Draw the covers
    junction_x = x1 + stroke if side == "left" else x2 - stroke
    xl = junction_x if side == "left" else junction_x - stroke / 4
    xr = junction_x if side == "right" else junction_x + stroke / 4
    y_low = y1 + tooth - stroke / 2
    y_high = y2 - tooth + stroke / 2
    draw_rect(pen, xl, y_low - cover, xr, y_low)
    draw_rect(pen, xl, y_high, xr, y_high + cover)
