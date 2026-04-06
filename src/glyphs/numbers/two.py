from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.superellipse_arch import draw_superellipse_arch
from draw.parallelogramm import draw_parallelogramm


class TwoGlyph(NumberGlyph):
    name = "two"
    unicode = "0x32"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )

        # Top arch
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.ymid,
            b.x2,
            b.y2,
            b.hx,
            b.hy * 0.5,
            side="bottom",
            cut="left",
        )
        # Diagonal stroke
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            dc.stroke_y,
            b.x2,
            b.ymid,
        )
        # Bottom bar
        draw_rect(pen, b.x1, 0, b.x2, dc.stroke_y)
