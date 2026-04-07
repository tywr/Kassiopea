import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.superellipse_arch import draw_superellipse_arch
from draw.superellipse_loop import draw_superellipse_loop
from draw.rect import draw_rect


class FiveGlyph(NumberGlyph):
    name = "five"
    unicode = "0x33"
    offset = 0
    width_ratio = 1.1


    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
            number=True,
        )

        base_glyph = ufoLib2.objects.Glyph()
        ry = (b.y2 - b.ymid + dc.stroke_y / 2) / b.height

        # Bottom loop
        draw_superellipse_loop(
            base_glyph.getPen(),
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.ymid + dc.stroke_y / 2,
            b.hx,
            b.hy * ry,
        )

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1,
            b.y1 + (b.ymid + dc.stroke_y / 2 - b.y1) / 2,
            b.xmid,
            300,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
