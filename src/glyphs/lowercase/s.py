import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from draw.s_curve import draw_s_curve
from draw.corner import draw_corner
from draw.rect import draw_rect


class LowercaseSGlyph(Glyph):
    name = "lowercase_s"
    unicode = "0x73"
    offset = 0
    width_ratio = 1
    stroke_x_ratio = 1.00
    stroke_y_ratio = 0.96
    left_tail_offset = 0.02
    right_tail_offset = 0.015
    hx_ratio = 0.75
    hy_ratio = 0.8
    top_height_ratio = 0.28
    bottom_height_ratio = 0.29
    top_cut = 0.72
    bot_cut = 0.28
    top_thinning = 0.92
    bot_thinning = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            width_ratio=self.width_ratio,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        xl = b.x1 + self.left_tail_offset * b.width
        xr = b.x2 - self.right_tail_offset * b.width

        ltop = self.top_height_ratio * b.height
        lbot = self.bottom_height_ratio * b.height
        yr, yl = b.y1 + lbot, b.y2 - ltop
        ycut1, ycut2 = b.y1 + self.bot_cut * b.height, b.y1 + self.top_cut * b.height

        draw_corner(pen, sx, sy, xl, yl, b.xmid, b.y2, hx, hy, orientation="top-right")
        draw_corner(
            pen, sx, sy, xr, yr, b.xmid, b.y1, hx, hy, orientation="bottom-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            sx * self.top_thinning,
            sy,
            b.x2,
            yl,
            b.xmid,
            b.y2,
            hx,
            hy,
            orientation="top-left",
        )
        draw_corner(
            loop_glyph.getPen(),
            sx * self.bot_thinning,
            sy,
            b.x1,
            yr,
            b.xmid,
            b.y1,
            hx,
            hy,
            orientation="bottom-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x1, ycut1, b.x2, ycut2)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        draw_s_curve(
            pen,
            sx,
            sy,
            xl,
            yr,
            xr,
            yl,
            hx,
            hy,
            middle_y_ratio=0.53,
            dx=150,
            dy=112,
        )
