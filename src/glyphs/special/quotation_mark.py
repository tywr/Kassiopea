from glyphs import Glyph
from draw.rect import draw_rect


class QuotationMarkGlyph(Glyph):
    name = "quotation_mark"
    unicode = "0x22"
    offset = 0
    width_ratio = 1
    height_ratio = 0.7
    gap = 0.3

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        g = self.gap * b.width
        h = self.height_ratio * b.height
        s = dc.stroke_x
        xm1 = b.xmid - g / 2 - dc.stroke_x / 2
        xm2 = b.xmid + g / 2 + dc.stroke_x / 2

        draw_rect(pen, xm1 - s / 2, dc.ascent - h, xm1 + s / 2, dc.ascent)
        draw_rect(pen, xm2 - s / 2, dc.ascent - h, xm2 + s / 2, dc.ascent)
