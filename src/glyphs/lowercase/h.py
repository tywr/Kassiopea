from glyphs import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.rect import draw_rect


class LowercaseHGlyph(Glyph):
    name = "lowercase_h"
    unicode = "0x68"
    offset = 0
    width_extra = 18  # Extra width beyond dc.width for the arch
    loop_ratio = 0.6  # Controls how far down the arch starts from x_height
    rx = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
        )
        # Add dampening on hx to keep ratio with the dent
        hx, hy = dc.hx * self.rx, dc.hy * self.loop_ratio

        # Top arch, cut at the bottom (only upper half drawn)
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2 - b.height * self.loop_ratio,
            b.x2,
            b.y2,
            hx,
            hy,
            dent=dc.dent + dc.v_overshoot,
            side="left",
            cut="bottom",
        )
        # Left stem — full ascent height with gap at the top
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.x_height - dc.dent)
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x - dc.gap, dc.ascent)

        # Right stem — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, b.y2 - b.height * self.loop_ratio / 2)
