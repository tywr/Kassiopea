from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


class LowercaseCGlyph(Glyph):
    name = "c"
    unicode = "0x63"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = fc.body_width + 2 * fc.h_overshoot
        hx = fc.hx
        hy = fc.hy
        opening = 280

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = -fc.overshoot
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset
        y2 = fc.x_height + fc.overshoot
        xmid = x1 + (x2 - x1) / 2
        ymid = fc.x_height / 2

        loop_glyph = ufoLib2.objects.Glyph()
        draw_superellipse_loop(loop_glyph.getPen(), stroke, x1, y1, x2, y2, hx, hy)

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            xmid,
            ymid - opening / 2 + stroke / 2,
            xmid + fc.width,
            ymid + opening / 2 - stroke / 2,
        )

        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
