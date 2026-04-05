from glyphs import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.rect import draw_rect


class LowercaseUGlyph(Glyph):
    name = "lowercase_u"
    unicode = "0x75"
    offset = 0
    loop_ratio = 0.6  # Controls how far up the arch reaches from baseline
    rx = 0.8          # Horizontal curve dampening (dc.hx * rx)

    def draw(self, pen, dc):
        b = dc.body_bounds(offset=self.offset, overshoot_bottom=True, overshoot_top=True)
        hx, hy = dc.hx * self.rx, dc.hy * self.loop_ratio
        arch_top = self.loop_ratio * b.y2

        # Bottom arch, cut at top (only lower half drawn)
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            arch_top,
            hx,
            hy,
            dent=dc.dent + dc.v_overshoot,
            side="right",
            cut="top",
        )
        # Right stem — full x_height with gap at baseline
        draw_rect(pen, b.x2 - dc.stroke_x, dc.dent, b.x2, dc.x_height)
        draw_rect(pen, b.x2 - dc.stroke_x + dc.gap, 0, b.x2, dc.x_height)
        # Left stem — starts from arch midpoint
        draw_rect(pen, b.x1, (arch_top + b.y1) / 2, b.x1 + dc.stroke_x, dc.x_height)
