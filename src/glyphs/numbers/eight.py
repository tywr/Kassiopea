from glyphs.numbers import NumberGlyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.cross_curve import draw_cross_curve


class EightGlyph(NumberGlyph):
    name = "eight"
    unicode = "0x38"
    offset = 0
    loop_ratio = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        hx, hy = b.hx, b.hy * self.loop_ratio

        loop_len = b.y2 * self.loop_ratio
        ym1 = b.y1 + loop_len - dc.stroke_y / 2
        ym2 = b.y2 - loop_len + dc.stroke_y / 2

        # Bottom loop
        draw_superellipse_loop(
            pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, ym1, hx, hy
        )
        # Top loop
        draw_superellipse_loop(
            pen, dc.stroke_x, dc.stroke_y, b.x1, ym2, b.x2, b.y2, hx, hy
        )
        # Middle cross junction connecting the two loops
        draw_cross_curve(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            (b.y1 + ym1) / 2,
            b.x2,
            (b.y2 + ym2) / 2,
            b.hx,
            b.hy / 2,
        )
