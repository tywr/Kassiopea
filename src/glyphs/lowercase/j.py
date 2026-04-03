from glyph import Glyph
from shapes.corner import draw_corner
from shapes.rect import draw_rect


class LowercaseJGlyph(Glyph):
    name = "lowercase_j"
    unicode = "0x6A"
    offset = 0
    dot_width = 30
    tail_offset = 20
    width_ratio = 0.7
    ud_ratio = 0.9

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        # Stem
        draw_rect(pen, b.x2 - dc.stroke, 0, b.x2, dc.x_height)
        # Left cap
        draw_rect(
            pen,
            b.x1 + (1 - self.ud_ratio) * b.width,
            dc.x_height - dc.stroke,
            b.x2,
            dc.x_height,
        )
        # Corner curving down-left into the descender
        draw_corner(
            pen,
            dc.stroke,
            b.x2,
            0,
            b.xmid,
            dc.descent + self.tail_offset,
            b.hx * 0.5,
            b.hy,
            orientation="bottom-left",
        )
        # Extension after the corner to the left
        draw_rect(
            pen,
            b.x1,
            dc.descent + self.tail_offset,
            b.xmid,
            dc.descent + self.tail_offset + dc.stroke,
        )
        # Accent dot
        draw_rect(
            pen,
            b.x2 - dc.stroke / 2 - self.dot_width / 2 - dc.stroke / 2,
            dc.accent - self.dot_width / 2 - dc.stroke / 2,
            b.x2 + self.dot_width / 2,
            dc.accent + dc.stroke / 2 + self.dot_width / 2,
        )
