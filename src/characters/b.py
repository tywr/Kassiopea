from config import FontConfig
from shapes.rounded_loop_tapered import rounded_loop_tapered
from shapes.rect import rect
from shapes.intersection_filler import intersection_filler


def draw_b(pen, font_config: FontConfig, stroke: int):
    """Draw a 'b' by adding a vertical bar on the left side of an 'o'."""
    outer_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2

    max_xo = (outer_right - outer_left) / 2
    max_yo = FontConfig.X_HEIGHT / 2
    x_offset = min(FontConfig.X_OFFSET, max_xo)
    y_offset = min(FontConfig.Y_OFFSET, max_yo)

    # Right vertical bar (ascender height)
    bar_right = outer_right - stroke
    rect(pen, bar_right, 0, outer_right, FontConfig.ASCENT)

    # Loop tapered on the right (where the stem is)
    rounded_loop_tapered(
        pen,
        x1=outer_left,
        y1=0,
        x2=outer_right,
        y2=FontConfig.X_HEIGHT,
        x_offset=x_offset,
        y_offset=y_offset,
        x_offset_taper=FontConfig.X_OFFSET_TAPER,
        y_offset_taper=FontConfig.Y_OFFSET_TAPER,
        stroke=stroke,
        ratio_taper=FontConfig.RATIO_TAPER,
        direction="right",
    )
    intersection_filler(
        pen=pen,
        stroke=stroke,
        outer_left=outer_left,
        outer_right=outer_right - stroke * FontConfig.RATIO_TAPER,
        height=FontConfig.X_HEIGHT,
        x_offset=x_offset,
        y_offset=y_offset,
        side="right",
        bar_position=bar_right,
        fill_height=FontConfig.INTERSECTION_FILL_HEIGHT,
    )

    return None
