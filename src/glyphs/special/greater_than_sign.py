from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm_vertical


class GreaterThenSignGlyph(Glyph):
    name = "greater_than_sign"
    unicode = "0x3E"
    offset = 0
    width_ratio = 1
    overlap = 0.6
    span = 0.85
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x * self.stroke_ratio
        draw_parallelogramm_vertical(
            pen,
            s,
            s,
            b.x2,
            ymid - s/2,
            b.x1,
            ymid + h / 2,
            direction="top-left",
            delta=s,
        )
        draw_parallelogramm_vertical(
            pen,
            s,
            s,
            b.x1,
            ymid - h / 2,
            b.x2,
            ymid + s / 2,
            direction="top-right",
            delta=s,
        )
