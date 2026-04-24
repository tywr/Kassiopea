from glyphs import Glyph
from draw.rect import draw_rect


class HyphenMinusGlyph(Glyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    offset = 0
    width = 320

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=0)
        w = self.width
        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.math + dc.stroke_y / 2,
            b.xmid + w / 2,
            dc.math - dc.stroke_y / 2,
        )
