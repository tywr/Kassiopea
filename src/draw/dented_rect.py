def draw_dented_rect(pen, x1, y1, x2, y2, dent=0.75, side="left", direction="down"):
    """Draw a simple rectangle between two corner points."""
    h = y2 - y1
    sides = side.split(",")

    if "right" in sides:
        pen.moveTo((x2 - 0.5 * dent * h, y1))
        pen.lineTo((x2, y2 - 0.6 * h))
        pen.lineTo((x2, y2 - 0.4 * h))
        pen.lineTo((x2 - 0.5 * dent * h, y2))
    else:
        pen.moveTo((x2, y1))
        pen.lineTo((x2, y2))

    if "left" in sides:
        pen.lineTo((x1 + 0.5 * dent * h, y2))
        pen.lineTo((x1, y2 - 0.4 * h))
        pen.lineTo((x1, y2 - 0.6 * h))
        pen.lineTo((x1 + 0.5 * dent * h, y1))
    else:
        pen.lineTo((x1, y2))
        pen.lineTo((x1, y1))

    pen.closePath()

