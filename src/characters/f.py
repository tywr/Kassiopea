import math

import pathops

from config import FontConfig
from shapes.flat_hook import flat_hook


def draw_f(pen, font_config: FontConfig, stroke: int):
    """Draw a lowercase 'f' — left stem with a top hook curving right, and a crossbar at x-height."""
    outer_left = FontConfig.WIDTH / 2 - (FontConfig.X_WIDTH * FontConfig.F_OFFSET) / 2 - stroke / 2
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2
    cap_right = (
        FontConfig.WIDTH / 2
        + ((1 + FontConfig.F_CAP_OFFSET) * FontConfig.X_WIDTH) / 2
        + stroke / 2
    )

    # Flat hook: left stem going up to ascender, curving right
    hook = pathops.Path()
    hook_pen = hook.getPen()
    flat_hook(
        hook_pen,
        corner_x=outer_left,
        corner_y=FontConfig.ASCENT,
        vertical_end=0,
        horizontal_end=cap_right,
        x_offset=FontConfig.HOOK_X_OFFSET,
        y_offset=FontConfig.HOOK_Y_OFFSET,
        stroke=stroke,
    )

    # Crossbar at x-height, with slanted left side
    crossbar_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    slant_offset = stroke / math.tan(math.radians(FontConfig.CUT_ANGLE))
    bar = pathops.Path()
    bp = bar.getPen()
    bp.moveTo((crossbar_left + slant_offset, FontConfig.BAR_HEIGHT - stroke))
    bp.lineTo((crossbar_left, FontConfig.BAR_HEIGHT))
    bp.lineTo((outer_right, FontConfig.BAR_HEIGHT))
    bp.lineTo((outer_right, FontConfig.BAR_HEIGHT - stroke))
    bp.closePath()

    result = pathops.op(hook, bar, pathops.PathOp.UNION, fix_winding=True)

    result.draw(pen)
