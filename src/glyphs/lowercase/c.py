from config import FontConfig as fc
from glyphs import Glyph
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


class LowercaseCGlyph(Glyph):
    name = "lowercase_c"
    unicode = "0x63"
    offset = 0
    opening = 280

    def draw(self, pen, dc):

        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_superellipse_loop(
            loop_glyph.getPen(), dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2, dc.hx, dc.hy
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            b.ymid - self.opening / 2 + dc.stroke_y / 2,
            b.xmid + b.width,
            b.ymid + self.opening / 2 - dc.stroke_y / 2,
        )

        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
