from glyphs.accents import Accent
from draw.cross_curve import draw_cross_curve


class Tilde(Accent):
    name = "tilde"
    unicode = "0x7E"
    width = 110
    height = 40

    def draw_at(self, pen, dc, x, y):
        hw = self.width / 2
        hh = self.height / 2
        draw_cross_curve(
            pen,
            dc.stroke_x * 0.6,
            dc.stroke_y * 0.6,
            x - hw,
            y - hh,
            x + hw,
            y + hh,
            hw * 0.4,
            hh * 1.2,
        )
