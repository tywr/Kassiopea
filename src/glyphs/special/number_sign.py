from glyphs import Glyph
from draw.rect import draw_rect


class NumberSignGlyph(Glyph):
    name = "number_sign"
    unicode = "0x23"
    offset = 0
    width_ratio = 1.32
    gap = 0.42
    height = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        g = self.gap * b.width
        h = self.height * b.height
        sx, sy = dc.stroke_x / 2, dc.stroke_y / 2
        xm1, xm2 = b.xmid - g / 2, b.xmid + g / 2
        ym1, ym2 = dc.math - g / 2, dc.math + g / 2
        y1, y2 = dc.math - h / 2, dc.math + h / 2

        draw_rect(pen, xm1 - sx, y1, xm1 + sx, y2)
        draw_rect(pen, xm2 - sx, y1, xm2 + sx, y2)
        draw_rect(pen, b.x1, ym1 - sy, b.x2, ym1 + sy)
        draw_rect(pen, b.x1, ym2 - sy, b.x2, ym2 + sy)
