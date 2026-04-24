import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from math import tan, pi
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm_vertical
from draw.rect import draw_rect


class UppercaseWGlyph(UppercaseGlyph):
    name = "uppercase_w"
    unicode = "0x57"
    offset = 0
    width_ratio = 1.16
    inner_stroke_ratio = 0.9
    inner_thickness_ratio = 1.1
    inner_offset = 0.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin,
            height="cap",
        )
        isx, isy = (
            self.inner_stroke_ratio * dc.stroke_x,
            self.inner_stroke_ratio * dc.stroke_y,
        )
        yi2 = b.y2 - self.inner_offset * b.height

        draw_rect(
            pen,
            b.x1,
            b.y1,
            b.x1 + dc.stroke_x,
            b.y2,
        )
        draw_rect(
            pen,
            b.x2 - dc.stroke_x,
            b.y1,
            b.x2,
            b.y2,
        )

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm_vertical(
            gpen,
            isx,
            isy,
            b.x1 + dc.stroke_x + dc.gap,
            b.y1,
            b.xmid - dc.gap / 2,
            yi2,
        )
        theta, delta = draw_parallelogramm_vertical(
            gpen,
            isx,
            isy,
            b.x2 - dc.stroke_x - dc.gap,
            b.y1,
            b.xmid + dc.gap / 2,
            yi2,
            direction="top-left",
        )
        draw_rect(
            gpen,
            b.xmid - dc.gap / 2,
            yi2 - delta,
            b.xmid + dc.gap / 2,
            yi2,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 + dc.stroke_x,
            yi2 - delta / 2,
            b.x2 - dc.stroke_x,
            b.y2,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen, b.x1 + dc.stroke_x, b.y1, b.x1 + dc.stroke_x + dc.gap, b.y1 + delta
        )
        draw_rect(
            pen, b.x2 - dc.stroke_x - dc.gap, b.y1, b.x2 - dc.stroke_x, b.y1 + delta
        )
