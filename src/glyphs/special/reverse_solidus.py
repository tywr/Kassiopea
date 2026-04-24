from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class ReverseSolidusGlyph(Glyph):
    name = "reverse_solidus"
    unicode = "0x5C"
    offset = 0
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ymid = dc.parenthesis
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            ymid - dc.parenthesis_length / 2,
            b.x1,
            ymid + dc.parenthesis_length / 2,
            direction="top-left"
        )
