from math import tan, pi
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class UppercaseMGlyph(UppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    offset = 0
    overlap = 0.65
    overlap_middle = 0.5
    depth = 0.6
    inner_stroke_ratio = 0.9
    inner_thickness_ratio = 1.16
    inner_height_ratio = 1.2
    width_ratio = 1.16

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            height="cap",
            width_ratio=self.width_ratio,
            min_margin=dc.min_margin,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        isx, isy = (
            self.inner_stroke_ratio * dc.stroke_x,
            self.inner_stroke_ratio * dc.stroke_y,
        )
        th = self.inner_thickness_ratio * dc.stroke_x
        yi = b.y2 - self.inner_height_ratio * b.height

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm_vertical(
            gpen,
            isx,
            isy,
            b.x1 + dc.stroke_x + dc.gap,
            b.y2,
            b.xmid + th / 2,
            yi,
            direction="bottom-right",
        )
        theta, delta = draw_parallelogramm_vertical(
            gpen,
            isx,
            isy,
            b.x2 - dc.stroke_x - dc.gap,
            b.y2,
            b.xmid - th / 2,
            yi,
            direction="bottom-left",
        )
        h = tan(pi / 2 - theta) * th
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid - th / 2,
            yi,
            b.xmid + th / 2,
            yi + h,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        draw_rect(
            pen, b.x1 + dc.stroke_x, b.y2 - delta, b.x1 + dc.stroke_x + dc.gap, b.y2
        )
        draw_rect(
            pen, b.x2 - dc.stroke_x - dc.gap, b.y2 - delta, b.x2 - dc.stroke_x, b.y2
        )
        draw_rect(
            pen,
            b.xmid - dc.gap / 2,
            yi + h / 2 + delta,
            b.xmid + dc.gap / 2,
            yi + h / 2 + delta + 0.5 * dc.gap / tan(theta),
        )
