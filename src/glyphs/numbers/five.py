from glyphs.numbers import NumberGlyph
from draw.superellipse_arch import draw_superellipse_arch
from draw.rect import draw_rect


class FiveGlyph(NumberGlyph):
    name = "five"
    unicode = "0x35"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            overshoot_bottom=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )

        # Lower arch (right side bowl)
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.ymid + dc.stroke_y / 2,
            b.hx,
            b.hy * 0.5,
            side="top",
            cut="left",
        )
        # Left vertical stem (upper half)
        draw_rect(
            pen,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.x1 + dc.stroke_x,
            b.y2,
        )
        # Top bar
        draw_rect(pen, b.x1, b.y2 - dc.stroke_y, b.x2, b.y2)
        # Middle bar connecting stem to arch
        draw_rect(
            pen,
            b.x1,
            b.ymid - dc.stroke_y / 2,
            b.xmid,
            b.ymid + dc.stroke_y / 2,
        )
        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.xmid, b.y1 + dc.stroke_y)
