from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseIGlyph(Glyph):
    name = "lowercase_i"
    unicode = "0x69"
    offset = 30
    rl_ratio = 0.5
    dot_width = 20

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset)
        right_len = b.width * self.rl_ratio - dc.stroke_x / 2
        left_len = b.width * (1 - self.rl_ratio) - dc.stroke_x / 2

        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )
        # Footer
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            0,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.stroke_y,
        )
        # Left cap
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            dc.x_height - dc.stroke_y,
            b.xmid,
            dc.x_height,
        )
        # Accent dot
        draw_rect(
            pen,
            b.xmid - self.dot_width / 2 - dc.stroke_x / 2,
            dc.accent - self.dot_width / 2 - dc.stroke_x / 2,
            b.xmid + dc.stroke_x / 2 + self.dot_width / 2,
            dc.accent + dc.stroke_x / 2 + self.dot_width / 2,
        )
