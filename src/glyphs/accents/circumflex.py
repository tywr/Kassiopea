from glyphs.accents import Accent
from draw.polygon import draw_polygon


class Circumflex(Accent):
    name = "circumflex"
    unicode = "0x5E"
    width = 100
    height = 60
    thickness = 30

    def draw_at(self, pen, dc, x, y):
        hw = self.width / 2
        hh = self.height / 2
        ht = self.thickness / 2

        # Outer chevron
        draw_polygon(
            pen,
            points=[
                (x - hw, y - hh),
                (x, y + hh),
                (x + hw, y - hh),
                (x + hw - ht, y - hh),
                (x, y + hh - ht * 1.5),
                (x - hw + ht, y - hh),
            ],
        )
