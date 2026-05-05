from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseUGlyph(SquareLowercaseGlyph):
    name = "lowercase_u"
    unicode = "0x75"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            width_ratio=self.width_ratio,
        )
        arch_top = b.y2
        yl = b.y1 + self.loop_ratio * b.height

        # Bottom arch, cut at top (only lower half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            yl,
            self.hx_ratio * b.hx,
            b.hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)

        # Left stem — starts from arch midpoint
        draw_rect(pen, b.x1, (yl + b.y1) / 2, b.x1 + dc.stroke_x, dc.x_height)
