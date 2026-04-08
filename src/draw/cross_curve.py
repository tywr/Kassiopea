def draw_cross_curve(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    invert=False,
):
    """Draw a center-symmetric S-curve stroke from (x1,y1) to (x2,y2).

    The curve starts at the bottom-left corner, crosses through the center
    of the bounding box, and ends at the top-right corner.

    At the corners the tangent is vertical; at the center it is horizontal.
    """
    from math import sqrt

    if invert:
        x1, y1, x2, y2 = x1, y2, x2, y1
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    sign = -1 if invert else 1
    inv = 1 if invert else 0

    # Compute perpendicular stroke at the midpoint based on the diagonal angle,
    # matching the parallelogramm stroke formula
    w = x2 - x1
    h = abs(y2 - y1)

    diag = sqrt(w**2 + h**2)
    s = sqrt((stroke_x * h / diag) ** 2 + (stroke_y * w / diag) ** 2)

    s2x = s / 2 * h / diag
    s2y = stroke_y / 2

    # Outer edges get increased handle, inner edges get decreased handle
    ohy = hy
    ihy = hy - 2 * s2y

    hx = hx - s2x

    if invert:
        ihy, ohy = ohy, ihy

    # Outer edge: (x1,y1) → upper mid → (x2,y2)
    pen.moveTo((x1 + inv * stroke_x, y1))
    pen.curveTo(
        (x1 + inv * stroke_x, y1 + sign * ohy),
        (mid_x - sign * s2x - hx, mid_y + s2y),
        (mid_x - sign * s2x, mid_y + s2y),
    )
    pen.curveTo(
        (mid_x - sign * s2x + hx, mid_y + s2y),
        (x2 - (1 - inv) * stroke_x, y2 - sign * ihy),
        (x2 - (1 - inv) * stroke_x, y2),
    )
    # Inner edge: (x2-stroke_x,y2) → lower mid → (x1+stroke_x,y1)
    pen.lineTo((x2 - inv * stroke_x, y2))
    pen.curveTo(
        (x2 - inv * stroke_x, y2 - sign * ohy),
        (mid_x + sign * s2x + hx, mid_y - s2y),
        (mid_x + sign * s2x, mid_y - s2y),
    )
    pen.curveTo(
        (mid_x + sign * s2x - hx, mid_y - s2y),
        (x1 + (1 - inv) * stroke_x, y1 + sign * ihy),
        (x1 + (1 - inv) * stroke_x, y1),
    )
    pen.closePath()


def draw_cross_curve_2(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    invert=False,
):
    """Draw a center-symmetric S-curve stroke from (x1,y1) to (x2,y2).

    Variant without hx in the curve handles — uses doubled control points instead.
    """
    from math import sqrt

    if invert:
        x1, y1, x2, y2 = x1, y2, x2, y1
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    hh = (y2 - y1) / 2

    sign = -1 if invert else 1
    inv = 1 if invert else 0

    # Compute perpendicular stroke at the midpoint based on the diagonal angle,
    # matching the parallelogramm stroke formula
    w = x2 - x1
    h = abs(y2 - y1)
    diag = sqrt(w**2 + h**2)
    s = sqrt((stroke_x * h / diag) ** 2 + (stroke_y * w / diag) ** 2)
    s2x = s / 2 * h / diag
    s2y = s / 2 * w / diag

    # Outer edges get increased handle, inner edges get decreased handle
    ahh = abs(hh)
    ohy = hy * (ahh + s2y) / ahh
    ihy = hy * (ahh - s2y) / ahh
    if invert:
        ihy, ohy = ohy, ihy

    # Outer edge: (x1,y1) → upper mid → (x2,y2)
    pen.moveTo((x1 + inv * stroke_x, y1))
    pen.curveTo(
        (x1 + inv * stroke_x, y1 + sign * ohy),
        (x1 + inv * stroke_x, y1 + sign * ohy),
        (mid_x - sign * s2x, mid_y + s2y),
    )
    pen.curveTo(
        (x2 - (1 - inv) * stroke_x, y2 - sign * ihy),
        (x2 - (1 - inv) * stroke_x, y2 - sign * ihy),
        (x2 - (1 - inv) * stroke_x, y2),
    )
    # Inner edge: (x2-stroke_x,y2) → lower mid → (x1+stroke_x,y1)
    pen.lineTo((x2 - inv * stroke_x, y2))
    pen.curveTo(
        (x2 - inv * stroke_x, y2 - sign * ohy),
        (x2 - inv * stroke_x, y2 - sign * ohy),
        (mid_x + sign * s2x, mid_y - s2y),
    )
    pen.curveTo(
        (x1 + (1 - inv) * stroke_x, y1 + sign * ihy),
        (x1 + (1 - inv) * stroke_x, y1 + sign * ihy),
        (x1 + (1 - inv) * stroke_x, y1),
    )
    pen.closePath()


def draw_cross_curve_2_h(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    invert=False,
):
    """Draw a center-symmetric S-curve stroke from (x1,y1) to (x2,y2).

    Horizontal variant: tangents are horizontal at corners, vertical at the midpoint.
    """
    from math import sqrt

    if invert:
        x1, y1, x2, y2 = x2, y1, x1, y2
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    hw = (x2 - x1) / 2

    sign = -1 if invert else 1
    inv = 1 if invert else 0

    # Compute perpendicular stroke at the midpoint based on the diagonal angle,
    # matching the parallelogramm stroke formula
    w = abs(x2 - x1)
    h = y2 - y1
    diag = sqrt(w**2 + h**2)
    s = sqrt((stroke_x * h / diag) ** 2 + (stroke_y * w / diag) ** 2)
    s2x = stroke_x / 2
    s2y = s / 2 * w / diag

    # Outer edges get increased handle, inner edges get decreased handle
    ahw = abs(hw)
    ohx = hx * (ahw + s2x) / ahw
    ihx = hx * (ahw - s2x) / ahw
    if invert:
        ihx, ohx = ohx, ihx

    # Outer edge: (x1,y1) → right mid → (x2,y2)
    pen.moveTo((x1, y1 + inv * stroke_y))
    pen.curveTo(
        (x1 + sign * ihx, y1 + inv * stroke_y),
        (x1 + sign * ihx, y1 + inv * stroke_y),
        (mid_x - s2x, mid_y - sign * s2y),
    )
    pen.curveTo(
        (x2 - sign * ohx, y2 - (1 - inv) * stroke_y),
        (x2 - sign * ohx, y2 - (1 - inv) * stroke_y),
        (x2, y2 - (1 - inv) * stroke_y),
    )
    # Inner edge: (x2,y2-stroke_y) → left mid → (x1,y1+stroke_y)
    pen.lineTo((x2, y2 - inv * stroke_y))
    pen.curveTo(
        (x2 - sign * ihx, y2 - inv * stroke_y),
        (x2 - sign * ihx, y2 - inv * stroke_y),
        (mid_x + s2x, mid_y + sign * s2y),
    )
    pen.curveTo(
        (x1 + sign * ohx, y1 + (1 - inv) * stroke_y),
        (x1 + sign * ohx, y1 + (1 - inv) * stroke_y),
        (x1, y1 + (1 - inv) * stroke_y),
    )
    pen.closePath()
