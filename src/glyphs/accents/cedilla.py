import ufoLib2
from glyphs.accents import Accent
from draw.superellipse_loop import draw_superellipse_loop
from draw.rect import draw_rect
from booleanOperations.booleanGlyph import BooleanGlyph


class Cedilla(Accent):
    name = "cedilla"
    unicode = "0xB8"
    x_ratio = 0.55
    cut_ratio = 0.7
    stroke_ratio = 0.55

    def draw_at(self, pen, dc, x, y):
        h = abs(dc.descent)
        w = self.x_ratio * dc.width
        yr = h / dc.x_height

        glyph = ufoLib2.objects.Glyph()
        draw_superellipse_loop(
            glyph.getPen(),
            self.stroke_ratio * dc.stroke_x,
            self.stroke_ratio * dc.stroke_y,
            x - w / 2,
            -h,
            x + w / 2,
            0,
            dc.hx * self.x_ratio / 2,
            dc.hy * yr,
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            x - w / 2 - 10,
            -h + self.cut_ratio * h / 2,
            x,
            -self.cut_ratio * h / 2,
        )

        result = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)
