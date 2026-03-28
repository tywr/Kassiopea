def flat_hook(pen, corner_x, corner_y, vertical_end, horizontal_end, x_offset, y_offset, stroke):
    """Draw a thick L-shaped stroke with a rounded corner.

    The shape is a vertical line that curves into a horizontal line via a
    cubic bezier. The curve passes through the midpoint of each arm,
    tangent to the edge, matching the rounded_rect curve model.

    Args:
        corner_x, corner_y: the outer corner point — where the vertical
                            and horizontal edges would meet if sharp.
        vertical_end: y coordinate where the vertical part ends (away from
                      the corner). Above corner_y = upward, below = downward.
        horizontal_end: x coordinate where the horizontal part ends (away
                        from the corner). Right of corner_x = rightward,
                        left = leftward.
        x_offset: horizontal control point offset for the curve.
        y_offset: vertical control point offset for the curve.
        stroke: thickness of the stroke.
    """
    # Determine directions
    goes_up = vertical_end > corner_y
    goes_right = horizontal_end > corner_x

    sx = 1 if goes_right else -1
    sy = 1 if goes_up else -1

    # Outer curve: from midpoint of vertical arm to midpoint of horizontal arm
    v_mid = (corner_y + vertical_end) / 2
    h_mid = (corner_x + horizontal_end) / 2

    # Outer edge points
    ov_end = (corner_x, vertical_end)
    ov_curve_start = (corner_x, v_mid)
    oh_curve_end = (h_mid, corner_y)
    oh_end = (horizontal_end, corner_y)

    # Inner edge points
    iv_end = (corner_x + sx * stroke, vertical_end)
    ih_end = (horizontal_end, corner_y + sy * stroke)

    # Inner curve midpoints
    inner_v_mid = v_mid
    inner_h_mid = h_mid

    # Inner curve start/end
    iv_curve_start = (corner_x + sx * stroke, inner_v_mid)
    ih_curve_end = (inner_h_mid, corner_y + sy * stroke)

    # Outer control points
    outer_cp1 = (corner_x, v_mid - sy * y_offset)
    outer_cp2 = (h_mid - sx * x_offset, corner_y)

    # Inner control points — scale proportionally for uniform stroke
    outer_v_half = abs(vertical_end - corner_y) / 2
    outer_h_half = abs(horizontal_end - corner_x) / 2
    inner_v_half = abs(vertical_end - (corner_y + sy * stroke)) / 2
    inner_h_half = abs(horizontal_end - (corner_x + sx * stroke)) / 2

    inner_y_off = y_offset * inner_v_half / outer_v_half if outer_v_half > 0 else 0
    inner_x_off = x_offset * inner_h_half / outer_h_half if outer_h_half > 0 else 0

    inner_cp1 = (corner_x + sx * stroke, inner_v_mid - sy * inner_y_off)
    inner_cp2 = (inner_h_mid - sx * inner_x_off, corner_y + sy * stroke)

    # Draw CCW contour
    pen.moveTo(ov_end)
    pen.lineTo(ov_curve_start)
    pen.curveTo(outer_cp1, outer_cp2, oh_curve_end)
    pen.lineTo(oh_end)
    pen.lineTo(ih_end)
    pen.lineTo(ih_curve_end)
    pen.curveTo(inner_cp2, inner_cp1, iv_curve_start)
    pen.lineTo(iv_end)
    pen.closePath()
