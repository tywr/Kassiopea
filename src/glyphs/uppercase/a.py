from math import atan, sin, cos
from glyph import Glyph
from shapes.polygon import draw_polygon
from shapes.parallelogramm import draw_parallelogramm
from shapes.rect import draw_rect


class UppercaseAGlyph(Glyph):
    name = "uppercase_a"
    unicode = "0x41"
    offset = 0
    width_ratio = 1.25
    bar_height = 320
    overlap = 0.05

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        half_width = b.width / 2 - dc.stroke_x / 2
        ov = self.overlap * b.width
        # Left branch
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            b.y1,
            b.xmid - ov,
            b.y2,
            direction="top-left",
        )
        # Right branch
        theta, delta = draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.xmid + ov, b.y2
        )
        # Crossbar
        draw_rect(
            pen,
            b.xmid - half_width + (self.bar_height - dc.stroke_y) * cos(theta),
            self.bar_height - dc.stroke_y,
            b.xmid + half_width - (self.bar_height - dc.stroke_y) * cos(theta),
            self.bar_height,
        )
