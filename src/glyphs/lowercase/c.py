from glyphs import Glyph
from draw.superellipse_loop import draw_superellipse_loop
from draw.rect import draw_rect
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.parallelogramm import draw_smooth_parallelogramm_vertical


class LowercaseCGlyph(Glyph):
    name = "lowercase_c"
    unicode = "0x63"
    offset = 8
    stroke_x_ratio = 1.0
    tail_offset = 0.08

    def draw(self, pen, dc):

        b = dc.body_bounds(
            offset=self.offset,
            overshoot_bottom=True,
            overshoot_top=True,
            overshoot_left=True,
            overshoot_right=True,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        yt_top = dc.x_height - sy - dc.v_overshoot
        yt_bot = sy + dc.v_overshoot
        xt = b.x2 - self.tail_offset * b.width

        draw_superellipse_loop(
            pen, sx, sy, b.x1, b.y1, b.x2, b.y2, dc.hx, dc.hy, cut="right"
        )

        draw_smooth_parallelogramm_vertical(
            pen, sy, b.xmid, b.y2, xt, yt_top, direction="bottom-right"
        )
        draw_smooth_parallelogramm_vertical(
            pen, sy, b.xmid, b.y1, xt, yt_bot, direction="top-right"
        )
