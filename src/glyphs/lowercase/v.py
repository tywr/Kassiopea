from math import atan, cos, sin
from glyphs import Glyph
from shapes.polygon import draw_polygon
from shapes.parallelogramm import draw_parallelogramm


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    offset = 0
    width_ratio = 1.2
    overlap = 0.075

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - self.overlap * b.width,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + self.overlap * b.width,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
