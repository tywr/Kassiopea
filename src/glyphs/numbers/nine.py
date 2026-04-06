from glyphs.numbers import NumberGlyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.rect import draw_rect


class NineGlyph(NumberGlyph):
    name = "nine"
    unicode = "0x39"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )

        # Top loop
        draw_superellipse_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.x2,
            b.y2,
            b.hx,
            b.hy * 0.5,
        )
        # Right stem extending down from the loop
        draw_rect(
            pen,
            b.x2 - dc.stroke_x,
            b.y1,
            b.x2,
            b.ymid + dc.stroke_y / 2,
        )
        # Bottom cap
        draw_rect(
            pen,
            b.xmid,
            b.y1,
            b.x2,
            b.y1 + dc.stroke_y,
        )
