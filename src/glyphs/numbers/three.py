from glyphs.numbers import NumberGlyph
from draw.superellipse_arch import draw_superellipse_arch
from draw.rect import draw_rect


class ThreeGlyph(NumberGlyph):
    name = "three"
    unicode = "0x33"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        hy = b.hy * 0.5

        # Upper arch
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.x2,
            b.y2,
            b.hx,
            hy,
            side="bottom",
            cut="left",
        )
        # Lower arch
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.ymid + dc.stroke_y / 2,
            b.hx,
            hy,
            side="top",
            cut="left",
        )
        # Top bar
        draw_rect(pen, b.x1, b.y2 - dc.stroke_y, b.xmid, b.y2)
        # Middle bar
        draw_rect(
            pen,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.xmid,
            b.ymid + dc.stroke_y / 2,
        )
        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.xmid, b.y1 + dc.stroke_y)
