from glyphs.accents import Accent
from draw.rect import draw_rect
from draw.corner import draw_corner


class Cedilla(Accent):
    name = "cedilla"
    unicode = "0xB8"
    drop = 70
    hook_width = 40

    def draw_at(self, pen, dc, x, y):
        stroke = dc.stroke_x * 0.7
        # Vertical drop
        draw_rect(
            pen,
            x - stroke / 2,
            y - self.drop,
            x + stroke / 2,
            y,
        )
        # Hook
        draw_corner(
            pen,
            stroke,
            stroke,
            x,
            y - self.drop / 2,
            x + self.hook_width,
            y - self.drop,
            self.hook_width * 0.5,
            self.drop * 0.3,
            orientation="bottom-right",
        )
