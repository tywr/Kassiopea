from glyphs.uppercase import UppercaseGlyph
from shapes.superellipse_loop import draw_superellipse_loop


class UppercaseOGlyph(UppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    offset = 0

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
        draw_superellipse_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            dc.hx * self.width_ratio,
            dc.hy,
        )
