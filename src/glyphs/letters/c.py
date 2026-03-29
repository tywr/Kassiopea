from config import FontConfig as fc
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


def draw_c(
    pen,
    stroke: int,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2
    y1 = 0
    x2 = fc.width / 2 + fc.o_width / 2 + stroke / 2
    y2 = fc.x_height

    loop_glyph = ufoLib2.objects.Glyph()
    draw_superellipse_loop(
        loop_glyph.getPen(), stroke, x1, y1, x2, y2, fc.o_hx, fc.o_hy
    )

    cut_glyph = ufoLib2.objects.Glyph()
    draw_rect(
        cut_glyph.getPen(),
        fc.width / 2,
        fc.x_height * (1 - fc.c_opening) / 2,
        fc.width,
        fc.x_height * (1 + fc.c_opening) / 2,
    )

    result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
    result.draw(pen)
