def draw_rect(pen, x1, y1, x2, y2, clockwise=False):
    """Draw a simple rectangle between two corner points."""
    if not clockwise:
        pen.moveTo((x1, y1))
        pen.lineTo((x2, y1))
        pen.lineTo((x2, y2))
        pen.lineTo((x1, y2))
    else:
        pen.moveTo((x1, y1))
        pen.lineTo((x1, y2))
        pen.lineTo((x2, y2))
        pen.lineTo((x2, y1))
    pen.closePath()
