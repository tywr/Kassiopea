from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseIGlyph(Glyph):
    name = "lowercase_i"
    unicode = "0x69"
    offset = 16
    width_ratio = 1.1
    cap = 0.5
    dot_height = 0.25
    rl_ratio = 0.5

    def draw_base(self, pen, dc):
        """Draw the letter without the dot (for use with accents)."""
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)
        right_len = self.rl_ratio * b.width - dc.stroke_x / 2
        left_len = (1 - self.rl_ratio) * b.width - dc.stroke_x / 2

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
            b.xmid - b.width * self.cap,
            dc.x_height - dc.stroke_y,
            b.xmid,
            dc.x_height,
        )

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
        b = dc.body_bounds(offset=self.offset, width_ratio=self.width_ratio)

        # Accent dot
        dh = self.dot_height * b.height
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            dc.accent - dh / 2,
            b.xmid + dc.stroke_x / 2,
            dc.accent + dh / 2,
        )
