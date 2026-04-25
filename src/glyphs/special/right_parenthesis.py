from glyphs import Glyph
from draw.loop import draw_loop


class RightParenthesisGlyph(Glyph):
    name = "right_parenthesis"
    unicode = "0x29"
    offset = 0
    width_ratio = 0.4
    stroke_x_ratio = 1.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        ymid = dc.parenthesis
        draw_loop(
            pen,
            sx,
            sy,
            b.x2 - 2 * (b.x2 - b.x1),
            ymid - dc.parenthesis_length / 2,
            b.x2,
            ymid + dc.parenthesis_length / 2,
            b.hx * 2,
            b.hy * dc.parenthesis_length / b.height,
            cut="left",
        )
