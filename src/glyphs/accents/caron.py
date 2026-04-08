from glyphs.accents import Accent
from draw.polygon import draw_polygon


class Caron(Accent):
    name = "caron"
    unicode = "0x2C7"
    width = 100
    height = 60
    thickness = 30

    def draw_at(self, pen, dc, x, y):
        hw = self.width / 2
        hh = self.height / 2
        ht = self.thickness / 2

        # Inverted chevron
        draw_polygon(
            pen,
            points=[
                (x - hw, y + hh),
                (x, y - hh),
                (x + hw, y + hh),
                (x + hw - ht, y + hh),
                (x, y - hh + ht * 1.5),
                (x - hw + ht, y + hh),
            ],
        )
