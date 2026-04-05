from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseLGlyph(UppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    offset = 0
    width_ratio = 1.2
    overlap = 0.05
    depth = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        ov = self.overlap * b.width
        ymid = (1 - self.depth) * b.height

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + dc.stroke_x, b.y2)
        draw_rect(pen, b.x2 - dc.stroke_x, b.y1, b.x2, b.y2)

        # Branches
        draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.xmid - ov, ymid, b.x2 - ov, b.y2
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            ymid,
            b.x1 + ov,
            b.y2,
            direction="top-left",
        )
