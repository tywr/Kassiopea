import pathops
from fontTools.pens.recordingPen import RecordingPen

from config import FontConfig
from shapes.flat_hook import flat_hook
from shapes.rect import rect


def draw_j(pen, font_config: FontConfig, stroke: int):
    """Draw a lowercase 'j' — stem aligned to the right side of the cell, with a descender hook."""
    outer_right = FontConfig.WIDTH / 2 + FontConfig.X_WIDTH / 2 + stroke / 2
    outer_left = FontConfig.WIDTH / 2 - FontConfig.X_WIDTH / 2 - stroke / 2
    stem_right = outer_right
    stem_left = outer_right - stroke

    cap_length = ((1 + FontConfig.IJ_OFFSET) * FontConfig.X_WIDTH) / 2 + stroke / 2

    # Vertical stem
    stem = pathops.Path()
    sp = stem.getPen()
    sp.moveTo((stem_left, 0))
    sp.lineTo((stem_left, FontConfig.X_HEIGHT))
    sp.lineTo((stem_right, FontConfig.X_HEIGHT))
    sp.lineTo((stem_right, 0))
    sp.closePath()

    # Top horizontal bar
    top_bar = pathops.Path()
    tp = top_bar.getPen()
    tp.moveTo((stem_right - cap_length, FontConfig.X_HEIGHT - stroke))
    tp.lineTo((stem_right - cap_length, FontConfig.X_HEIGHT))
    tp.lineTo((stem_right, FontConfig.X_HEIGHT))
    tp.lineTo((stem_right, FontConfig.X_HEIGHT - stroke))
    tp.closePath()

    result = pathops.op(stem, top_bar, pathops.PathOp.UNION, fix_winding=True)

    # Flat hook descending from stem, curving left (same as g)
    hook = pathops.Path()
    hook_pen = hook.getPen()
    flat_hook(
        hook_pen,
        corner_x=outer_right,
        corner_y=FontConfig.DESCENT + FontConfig.LOWER_HOOK_OFFSET,
        vertical_end=FontConfig.X_HEIGHT,
        horizontal_end=outer_left,
        x_offset=FontConfig.HOOK_X_OFFSET,
        y_offset=FontConfig.HOOK_Y_OFFSET,
        stroke=stroke,
    )

    result = pathops.op(result, hook, pathops.PathOp.UNION, fix_winding=True)

    result.draw(pen)

    # Dot above the stem
    dot_left = stem_right - FontConfig.X_WIDTH * FontConfig.IJ_DOT_WIDTH
    rect(
        pen,
        dot_left,
        FontConfig.ACCENT + stroke / 2,
        stem_right,
        FontConfig.ACCENT - stroke / 2,
    )
