from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseZGlyph(Glyph):
    name = "lowercase_z"
    unicode = "0x7A"
    offset = 0
    diag_stroke_ratio = 0.96

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)

        # Top and bottom bars
        draw_rect(pen, b.x1, dc.x_height - dc.stroke_y, b.x2, dc.x_height)
        draw_rect(pen, b.x1, 0, b.x2, dc.stroke_y)
        dsx = self.diag_stroke_ratio * dc.stroke_x
        dsy = self.diag_stroke_ratio * dc.stroke_y

        # Diagonal stroke
        theta, delta = draw_parallelogramm(
            pen,
            dsx,
            dsy,
            b.x1,
            b.y1 + dc.stroke_y + dc.gap,
            b.x2,
            b.y2 - dc.stroke_y - dc.gap,
        )

        # Fill the gaps
        draw_rect(
            pen,
            b.x2 - delta,
            b.y2 - dc.stroke_y - dc.gap,
            b.x2,
            b.y2 - dc.stroke_y,
        )
        draw_rect(
            pen,
            b.x1,
            b.y1 + dc.stroke_y,
            b.x1 + delta,
            b.y1 + dc.stroke_y + dc.gap,
        )
