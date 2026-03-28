import pathops

from config import FontConfig
from shapes.rounded_loop_tapered import rounded_loop_tapered


def draw_d(pen, font_config: FontConfig, stroke: int):
    """Draw a 'd' — a tapered loop on the right side with a vertical ascender bar."""
    outer_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2

    max_xo = (outer_right - outer_left) / 2
    max_yo = FontConfig.X_HEIGHT / 2
    x_offset = min(FontConfig.X_OFFSET, max_xo)
    y_offset = min(FontConfig.Y_OFFSET, max_yo)

    # Loop tapered on the right (where the stem is)
    loop = pathops.Path()
    loop_pen = loop.getPen()
    rounded_loop_tapered(
        loop_pen,
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

    # Right vertical bar (ascender height)
    bar_left = outer_right - stroke
    bar = pathops.Path()
    bar_pen = bar.getPen()
    bar_pen.moveTo((bar_left, 0))
    bar_pen.lineTo((bar_left, FontConfig.ASCENT))
    bar_pen.lineTo((outer_right, FontConfig.ASCENT))
    bar_pen.lineTo((outer_right, 0))
    bar_pen.closePath()

    result = pathops.op(loop, bar, pathops.PathOp.UNION)
    result.draw(pen)
