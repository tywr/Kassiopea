from glyphs.accents import Accent
from draw.rect import draw_rect


class Dieresis(Accent):
    name = "dieresis"
    unicode = "0xA8"
    dot_width = 36
    dot_gap = 50

    def draw_at(self, pen, dc, x, y):
        r = self.dot_width / 2 + dc.stroke_x / 2
        # Left dot
        draw_rect(
            pen,
            x - self.dot_gap / 2 - r,
            y - r,
            x - self.dot_gap / 2 + r,
            y + r,
        )
        # Right dot
        draw_rect(
            pen,
            x + self.dot_gap / 2 - r,
            y - r,
            x + self.dot_gap / 2 + r,
            y + r,
        )
