from glyphs.uppercase import UppercaseGlyph
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class UppercaseDGlyph(UppercaseGlyph):
    name = "uppercase_d"
    unicode = "0x44"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="ascent",
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        arch_x1 = b.x1
        cut_x = (arch_x1 + b.x2) / 2

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)
        # Right flat portion
        draw_rect(pen, b.x2 - dc.stroke_x, 0.5 * dc.ascent, b.x2, 0.5 * dc.ascent)
        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - dc.stroke_y, cut_x, b.y2)
        draw_rect(pen, b.x1, 0, cut_x, dc.stroke_y)
        # Corner
        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            0.5 * dc.ascent,
            cut_x,
            b.y2,
            dc.hx * self.width_ratio,
            dc.hy,
            orientation="top-left",
        )
        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            0.5 * dc.ascent,
            cut_x,
            b.y1,
            dc.hx * self.width_ratio,
            dc.hy,
            orientation="bottom-left",
        )
