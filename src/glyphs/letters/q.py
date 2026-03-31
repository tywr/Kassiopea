from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_ear import draw_superellipse_ear
from shapes.rect import draw_rect


class LowercaseQGlyph(Glyph):
    name = "q"
    unicode = "0x71"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = 320
        hx = 200
        hy = 230

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = -fc.overshoot
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset
        y2 = fc.x_height + fc.overshoot

        # Right-ear
        draw_superellipse_ear(
            pen,
            stroke,
            x1,
            y1,
            x2,
            y2,
            hx,
            hy,
            fc.tooth,
            fc.cover,
            side="right",
        )
        # Descender
        draw_rect(pen, x2 - stroke, fc.descent, x2, fc.x_height)
