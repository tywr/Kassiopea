from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm_vertical


class Grave(Accent):
    name = "grave"
    unicode = "0x60"
    height = 80
    width = 50

    def draw_at(self, pen, dc, x, y):
        draw_parallelogramm_vertical(
            pen,
            dc.stroke_x * 0.7,
            dc.stroke_y * 0.7,
            x + self.width / 2,
            y - self.height / 2,
            x - self.width / 2,
            y + self.height / 2,
        )
