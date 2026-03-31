from config import FontConfig as fc
from glyph import Glyph
from shapes.superellipse_loop import draw_superellipse_loop


class LowercaseOGlyph(Glyph):
    name = "o"
    unicode = "0x6F"

    def draw(
        self,
        pen,
        stroke: int,
    ):
        offset = 0
        width = fc.body_width + 2 * fc.h_overshoot
        hx = fc.hx
        hy = fc.hy

        x1 = fc.width / 2 - width / 2 - stroke / 2 + offset
        y1 = -fc.overshoot
        x2 = fc.width / 2 + width / 2 + stroke / 2 + offset
        y2 = fc.x_height + fc.overshoot
        draw_superellipse_loop(pen, stroke, x1, y1, x2, y2, hx, hy)
