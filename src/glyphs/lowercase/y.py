from math import tan, pi
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.2
    overlap = 0.285
    dent_ratio = 0.1

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        dent_height = self.dent_ratio * b.height
        ov = self.overlap * dc.stroke_x

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            dent_height,
            b.x1,
            b.y2,
            direction="top-left",
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            dent_height,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov + delta,
            dent_height,
            b.xmid - ov - (abs(dc.descent) + dent_height) / tan(theta),
            dc.descent,
            direction="bottom-left",
        )

        # Fill the gap
        h = dc.gap / (2 * tan(0.5 * pi - theta))
        p = ov * tan(theta)
        draw_rect(
            pen,
            b.xmid - ov,
            dent_height,
            b.xmid + ov,
            dent_height + p + h,
        )
