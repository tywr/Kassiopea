from glyphs.accents import Accent
from draw.superellipse_loop import draw_superellipse_loop


class Ring(Accent):
    name = "ring"
    unicode = "0x2DA"
    radius = 40

    def draw_at(self, pen, dc, x, y):
        r = self.radius
        stroke = dc.stroke_x * 0.5
        draw_superellipse_loop(
            pen,
            stroke,
            stroke,
            x - r,
            y - r,
            x + r,
            y + r,
            r * 0.55,
            r * 0.55,
        )
