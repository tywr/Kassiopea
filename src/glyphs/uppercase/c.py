import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from shapes.superellipse_loop import draw_superellipse_loop
from shapes.rect import draw_rect


class UppercaseCGlyph(UppercaseGlyph):
    name = "uppercase_c"
    unicode = "0x43"
    offset = 0
    opening = 280  # Opening height at x_height, scaled to ascent in draw

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="ascent",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        opening = self.opening * dc.ascent / dc.x_height

        loop_glyph = ufoLib2.objects.Glyph()
        draw_superellipse_loop(
            loop_glyph.getPen(),
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            dc.hx * self.width_ratio,
            dc.hy,
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            b.ymid - opening / 2 + dc.stroke_y / 2,
            b.xmid + dc.window_width,
            b.ymid + opening / 2 - dc.stroke_y / 2,
        )

        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
