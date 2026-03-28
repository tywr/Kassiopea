import math

import pathops

from config import FontConfig
from shapes.flat_hook import flat_hook


def draw_t(pen, font_config: FontConfig, stroke: int):
    """Draw a lowercase 't' — left stem from x-height, flat hook at bottom curving right, crossbar."""
    outer_left = FontConfig.WIDTH / 2 - (FontConfig.X_WIDTH * FontConfig.T_OFFSET) / 2 - stroke / 2
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2
    foot_right = (
        FontConfig.WIDTH / 2
        + ((1 + FontConfig.T_FOOT_OFFSET) * FontConfig.X_WIDTH) / 2
        + stroke / 2
    )

    # Flat hook: left stem going down to baseline, curving right
    hook = pathops.Path()
    hook_pen = hook.getPen()
    flat_hook(
        hook_pen,
        corner_x=outer_left,
        corner_y=0,
        vertical_end=FontConfig.ASCENT,
        horizontal_end=foot_right,
        x_offset=FontConfig.HOOK_X_OFFSET,
        y_offset=FontConfig.HOOK_Y_OFFSET,
        stroke=stroke,
    )

    # Crossbar at bar height, with slanted right side
    crossbar_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    slant_offset = stroke / math.tan(math.radians(180 - FontConfig.CUT_ANGLE))
    bar = pathops.Path()
    bp = bar.getPen()
    bp.moveTo((crossbar_left + slant_offset, FontConfig.BAR_HEIGHT - stroke))
    bp.lineTo((crossbar_left, FontConfig.BAR_HEIGHT))
    bp.lineTo((outer_right, FontConfig.BAR_HEIGHT))
    bp.lineTo((outer_right, FontConfig.BAR_HEIGHT - stroke))
    bp.closePath()

    result = pathops.op(hook, bar, pathops.PathOp.UNION, fix_winding=True)

    result.draw(pen)
