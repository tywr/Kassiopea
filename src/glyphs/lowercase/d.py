from glyphs import Glyph
from shapes.superellipse_arch import draw_superellipse_arch
from shapes.rect import draw_rect


class LowercaseDGlyph(Glyph):
    name = "lowercase_d"
    unicode = "0x64"
    offset = -26

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
        )
        draw_superellipse_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            dc.hx,
            dc.hy,
            dent=dc.dent + dc.v_overshoot,
            side="right",
        )
        # Stem
        draw_rect(pen, b.x2 - dc.stroke_x + dc.gap, 0, b.x2, dc.ascent)
        draw_rect(pen, b.x2 - dc.stroke_x, dc.dent, b.x2, dc.x_height - dc.dent)
