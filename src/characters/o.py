from config import FontConfig
from shapes.rounded_loop import rounded_loop
from shapes.rect import rect
from shapes.intersect import rounded_rect_intersect_x


def draw_o(
    pen,
    font_config: FontConfig,
    stroke: int,
    taper=None,
    taper_ratio=1.0,
    center_x=None,
    x_ratio=1.0,
    height=None,
):
    """Draw a tall rounded-rectangle 'o' with generous corner rounding.

    Args:
        taper: "left" or "right" — which side gets a thinner stroke.
               None means uniform stroke on both sides.
        taper_ratio: 0.0 to 1.0 — fraction of stroke on the tapered side.
                     1.0 = full stroke (no taper), 0.0 = zero stroke.
        center_x: horizontal center of the glyph. Defaults to FontConfig.WIDTH / 2.
        x_ratio: horizontal compression factor. 1.0 = normal, <1.0 = narrower.
                 Scales the counter width and horizontal corner radius,
                 but keeps stroke unchanged.
    """
    if center_x is None:
        center_x = FontConfig.WIDTH / 2
    if height is None:
        height = FontConfig.X_HEIGHT
    half_width = FontConfig.X_WIDTH / 2 * x_ratio
    inner_left = center_x - half_width + stroke / 2
    inner_right = center_x + half_width - stroke / 2

    # Outer edges — full stroke by default, reduced on tapered side
    left_stroke = stroke * taper_ratio if taper == "left" else stroke
    right_stroke = stroke * taper_ratio if taper == "right" else stroke

    outer_left = inner_left - left_stroke
    outer_right = inner_right + right_stroke

    # Control point offsets — clamped to half the shape dimensions
    max_xo = (outer_right - outer_left) / 2
    max_yo = height / 2
    x_offset = min(FontConfig.X_OFFSET, max_xo)
    y_offset = min(FontConfig.Y_OFFSET, max_yo)

    rounded_loop(
        pen,
        x1=outer_left,
        y1=0,
        x2=outer_right,
        y2=height,
        x_offset=x_offset,
        y_offset=y_offset,
        stroke=stroke,
        stroke_left=left_stroke,
        stroke_right=right_stroke,
    )

    # Ink trap squares at tapered side junctions
    # The square sticks out from the curve at the intersection point,
    # extending away from the loop (toward the stem side).
    ink = FontConfig.INK_TRAP
    if taper == "left" and ink > 0:
        full_left = inner_left - stroke
        hits = rounded_rect_intersect_x(
            outer_left,
            0,
            outer_right,
            height,
            x_offset,
            y_offset,
            inner_left,
        )
        if len(hits) >= 2:
            _, y_bottom = hits[0]
            _, y_top = hits[-1]
            # Bottom: square below and left of the curve
            rect(pen, inner_left, y_bottom - ink, inner_left + stroke / 2, y_bottom)
            # Top: square above and left of the curve
            rect(pen, inner_left, y_top, inner_left + stroke / 2, y_top + ink)

    elif taper == "right" and ink > 0:
        full_right = inner_right + stroke
        hits = rounded_rect_intersect_x(
            outer_left,
            0,
            outer_right,
            height,
            x_offset,
            y_offset,
            inner_right,
        )
        if len(hits) >= 2:
            _, y_bottom = hits[0]
            _, y_top = hits[-1]
            # Bottom: square below and right of the curve
            rect(pen, inner_right - stroke / 2, y_bottom - ink, inner_right, y_bottom)
            # Top: square above and right of the curve
            rect(pen, inner_right - stroke / 2, y_top, inner_right, y_top + ink)
