from glyphs import Glyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.corner import draw_corner
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph


class LowercaseE3Glyph(Glyph):
    name = "lowercase_e_3"
    unicode = "0x65"
    offset = 5
    font_feature = {"ss01": 1}
    width_ratio = 1
    stroke_x_ratio = 1.00
    stroke_y_ratio = 0.96
    mid_height = 0.52
    thinning = 0.5
    stroke_x_ratio = 1.04
    stroke_y_ratio = 0.96
    cut_offset = 0.05
    tail_radius = 1.618
    tail_hy = 0.5
    overshoot_reducing = 0.65

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_bottom=True,
            overshoot_left=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = b.hx * (b.width - dc.h_overshoot) / b.width, b.hy
        ymid = self.mid_height * b.height
        xe = b.x2 + (self.tail_radius - 1) * b.width / 2
        xc = b.x2 - self.cut_offset * b.width

        # Half-top of a superellipse
        draw_superellipse_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 + self.overshoot_reducing * dc.v_overshoot,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
            cut="right",
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            sx * self.thinning,
            sy,
            xe,
            ymid,
            b.xmid,
            b.y1 + self.overshoot_reducing * dc.v_overshoot,
            b.hx * self.tail_radius,
            b.hy * self.tail_hy,
            orientation="bottom-left",
        )

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            xc,
            b.y1,
            xe + 1,
            b.y2,
        )
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        draw_corner(
            pen,
            sx,
            sy,
            b.x2 - dc.h_overshoot,
            ymid,
            b.xmid,
            b.y2,
            hx,
            hy,
            orientation="top-left",
        )

        # Middle bar
        draw_rect(
            pen,
            b.x1 + sx / 2,
            ymid,
            b.x2 - dc.h_overshoot - sx / 2,
            ymid + dc.stroke_alt / 2,
        )
        draw_rect(
            pen, b.x1 + sx / 2, ymid - dc.stroke_alt / 2, b.x2 - dc.h_overshoot, ymid
        )
