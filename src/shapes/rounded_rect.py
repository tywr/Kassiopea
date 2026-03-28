def rounded_rect_asym(
    pen, x1, y1, x2, y2,
    x_offset_left, y_offset_left,
    x_offset_right, y_offset_right,
    clockwise=False,
):
    """Draw a rounded rectangle with independent offsets for left and right sides.

    Each quarter-curve connects two adjacent side midpoints via a cubic bezier.
    The left two quarters use x_offset_left/y_offset_left, the right two use
    x_offset_right/y_offset_right.

    Args:
        x1, y1: bottom-left corner of the bounding box.
        x2, y2: top-right corner of the bounding box.
        x_offset_left: horizontal control point offset for the left side quarters.
        y_offset_left: vertical control point offset for the left side quarters.
        x_offset_right: horizontal control point offset for the right side quarters.
        y_offset_right: vertical control point offset for the right side quarters.
        clockwise: winding direction (True for inner counter / hole).
    """
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    if not clockwise:
        # CCW: bottom → right → top → left
        pen.moveTo((mid_x, y1))
        # Bottom-right quarter
        pen.curveTo(
            (mid_x + x_offset_right, y1),
            (x2, mid_y - y_offset_right),
            (x2, mid_y),
        )
        # Top-right quarter
        pen.curveTo(
            (x2, mid_y + y_offset_right),
            (mid_x + x_offset_right, y2),
            (mid_x, y2),
        )
        # Top-left quarter
        pen.curveTo(
            (mid_x - x_offset_left, y2),
            (x1, mid_y + y_offset_left),
            (x1, mid_y),
        )
        # Bottom-left quarter
        pen.curveTo(
            (x1, mid_y - y_offset_left),
            (mid_x - x_offset_left, y1),
            (mid_x, y1),
        )
    else:
        # CW: bottom → left → top → right
        pen.moveTo((mid_x, y1))
        # Bottom-left quarter
        pen.curveTo(
            (mid_x - x_offset_left, y1),
            (x1, mid_y - y_offset_left),
            (x1, mid_y),
        )
        # Top-left quarter
        pen.curveTo(
            (x1, mid_y + y_offset_left),
            (mid_x - x_offset_left, y2),
            (mid_x, y2),
        )
        # Top-right quarter
        pen.curveTo(
            (mid_x + x_offset_right, y2),
            (x2, mid_y + y_offset_right),
            (x2, mid_y),
        )
        # Bottom-right quarter
        pen.curveTo(
            (x2, mid_y - y_offset_right),
            (mid_x + x_offset_right, y1),
            (mid_x, y1),
        )
    pen.closePath()


def rounded_rect(pen, x1, y1, x2, y2, x_offset, y_offset, clockwise=False):
    """Draw a symmetric rounded rectangle. Delegates to rounded_rect_asym."""
    rounded_rect_asym(
        pen, x1, y1, x2, y2,
        x_offset_left=x_offset, y_offset_left=y_offset,
        x_offset_right=x_offset, y_offset_right=y_offset,
        clockwise=clockwise,
    )
