from glyphs.numbers import NumberGlyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.superellipse_arch import draw_superellipse_arch
from draw.rect import draw_rect


class SixGlyph(NumberGlyph):
    name = "six"
    unicode = "0x36"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )

        # Bottom loop
        draw_superellipse_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.ymid + dc.stroke_y / 2,
            b.hx,
            b.hy * 0.5,
        )
        # Left stem extending up from the loop
        draw_rect(
            pen,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.x1 + dc.stroke_x,
            b.y2,
        )
        # Top cap
        draw_rect(
            pen,
            b.x1,
            b.y2 - dc.stroke_y,
            b.xmid,
            b.y2,
        )
