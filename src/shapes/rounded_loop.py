from shapes.rounded_rect import rounded_rect


def rounded_loop(pen, x1, y1, x2, y2, x_offset, y_offset, stroke, stroke_left=None, stroke_right=None):
    """Draw a loop (annulus) between two concentric rounded rectangles.

    The outer rounded rect spans (x1, y1) to (x2, y2).
    The inner rounded rect is inset by stroke on top/bottom,
    and by stroke_left/stroke_right on the sides.

    Args:
        x1, y1: bottom-left corner of the outer bounding box.
        x2, y2: top-right corner of the outer bounding box.
        x_offset: horizontal control point offset for the outer shape.
        y_offset: vertical control point offset for the outer shape.
        stroke: thickness of the loop walls (top and bottom, and default for sides).
        stroke_left: left wall thickness. Defaults to stroke.
        stroke_right: right wall thickness. Defaults to stroke.
    """
    if stroke_left is None:
        stroke_left = stroke
    if stroke_right is None:
        stroke_right = stroke

    # Outer contour (CCW)
    rounded_rect(
        pen,
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        x_offset=x_offset,
        y_offset=y_offset,
        clockwise=False,
    )

    # Inner contour (CW) — scale offsets proportionally to inner dimensions
    # so the inner curve is the same shape as the outer, giving uniform stroke.
    outer_half_w = (x2 - x1) / 2
    outer_half_h = (y2 - y1) / 2
    inner_half_w = outer_half_w - (stroke_left + stroke_right) / 2
    inner_half_h = outer_half_h - stroke

    inner_x_offset = x_offset * inner_half_w / outer_half_w if outer_half_w > 0 else 0
    inner_y_offset = y_offset * inner_half_h / outer_half_h if outer_half_h > 0 else 0

    rounded_rect(
        pen,
        x1=x1 + stroke_left,
        y1=y1 + stroke,
        x2=x2 - stroke_right,
        y2=y2 - stroke,
        x_offset=inner_x_offset,
        y_offset=inner_y_offset,
        clockwise=True,
    )
