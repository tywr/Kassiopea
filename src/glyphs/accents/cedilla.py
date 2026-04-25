import ufoLib2
from glyphs.accents import Accent
from draw.loop import draw_loop
from draw.rect import draw_rect
from booleanOperations.booleanGlyph import BooleanGlyph


class Cedilla(Accent):
    name = "cedilla"
    unicode = "0xB8"
    x_ratio = 0.55
    cut_ratio = 0.7
    stroke_ratio = 0.6
    neck_length = 0.05

    def draw_at(self, pen, dc, x, y):
        h = abs(dc.descent)
        w = self.x_ratio * dc.width
        yr = h / dc.x_height
        yn = - self.neck_length * dc.x_height

        draw_rect(
            pen,
            x - dc.stroke_y / 2,
            yn - dc.stroke_y / 2,
            x + dc.stroke_y / 2,
            0,
        )
        glyph = ufoLib2.objects.Glyph()
        draw_loop(
            glyph.getPen(),
            self.stroke_ratio * dc.stroke_x,
            self.stroke_ratio * dc.stroke_y,
            x - w / 2,
            yn - h,
            x + w / 2,
            yn,
            dc.hx * self.x_ratio / 2,
            dc.hy * yr,
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            x - w / 2 - 10,
            yn-h + self.cut_ratio * h / 2,
            x,
            yn-self.cut_ratio * h / 2,
        )

        result = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
