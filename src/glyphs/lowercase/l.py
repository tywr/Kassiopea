from glyphs import Glyph
from shapes.rect import draw_rect


class LowercaseLGlyph(Glyph):
    name = "lowercase_l"
    unicode = "0x6C"
    offset = 20
    rl_ratio = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, height="ascent")
        right_len = b.width * self.rl_ratio - dc.stroke_x / 2
        left_len = b.width * (1 - self.rl_ratio) - dc.stroke_x / 2

        # Stem
        draw_rect(pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.ascent)
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
            dc.ascent - dc.stroke_y,
            b.xmid,
            dc.ascent,
        )
