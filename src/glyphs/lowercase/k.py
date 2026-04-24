from math import tan
from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    offset = 34
    width_ratio = 1.00
    branch_ratio = 0.75
    mid_ratio = 0.52
    upper_branch_offset = 0.055

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            width_ratio=self.width_ratio,
            overshoot_right=True,
            overshoot_left=True,
        )
        x_branch = b.x1 + (1 - self.branch_ratio) * b.width
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Lower branch
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x_branch,
            ymid + dc.stroke_y / 2,
            b.x2,
            b.y1,
            direction="bottom-right",
        )

        # Upper branch
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x_branch,
            ymid - dc.stroke_y / 2,
            xtop,
            b.y2,
        )

        # Neck
        draw_rect(
            pen,
            b.x1,
            ymid - dc.stroke_y / 2,
            x_branch + delta + dc.gap / tan(theta),
            ymid + dc.stroke_y / 2,
        )
