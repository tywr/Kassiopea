from glyph import Glyph
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class UppercaseDGlyph(Glyph):
    name = "uppercase_d"
    unicode = "0x44"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="ascent",
            overshoot_right=True,
        )
        arch_x1 = b.x1
        cut_x = (arch_x1 + b.x2) / 2

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke, dc.ascent)
        # Right flat portion
        draw_rect(pen, b.x2 - dc.stroke, 0.5 * dc.ascent, b.x2, 0.5 * dc.ascent)
        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - dc.stroke, cut_x, b.y2)
        draw_rect(pen, b.x1, 0, cut_x, dc.stroke)
        # Corner
        draw_corner(
            pen,
            dc.stroke,
            b.x2,
            0.5 * dc.ascent,
            cut_x,
            b.y2,
            dc.hx,
            dc.hy,
            orientation="top-left",
        )
        draw_corner(
            pen,
            dc.stroke,
            b.x2,
            0.5 * dc.ascent,
            cut_x,
            b.y1,
            dc.hx,
            dc.hy,
            orientation="bottom-left",
        )
