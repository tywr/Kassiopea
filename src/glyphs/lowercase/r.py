from glyphs import Glyph
from draw.r_arch import draw_r_arch
from draw.rect import draw_rect
from draw.polygon import draw_polygon
from draw.parallelogramm import draw_smooth_parallelogramm_vertical


class LowercaseRGlyph(Glyph):
    name = "lowercase_r"
    unicode = "0x72"
    offset = 8
    loop_ratio = 0.8
    width_ratio = 1
    wing_ratio = 0.2
    top_stroke_y = 1
    hx_ratio = 1
    taper = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset,
            overshoot_top=True,
            overshoot_right=True,
            width_ratio=self.width_ratio,
        )
        hx, hy = dc.hx * self.hx_ratio, dc.hy * self.loop_ratio
        yt = dc.x_height - dc.stroke_y - dc.v_overshoot
        xmid = b.x1 + self.wing_ratio * b.width
        xl = xmid + self.loop_ratio * b.width + dc.stroke_x

        # Top arch, cut at the bottom (only upper half drawn)
        arch_params = draw_r_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xmid,
            b.y1,
            xl,
            b.y2,
            hx,
            hy,
            taper=self.taper,
        )

        # Compute the intersection of the outer bowl with the stem
        (_, y1), (_, y2) = arch_params["outer"].intersection_x(
            x=xmid + dc.stroke_x + dc.gap
        )
        y1, y2 = min(y1, y2), max(y1, y2)

        # Fill the gap
        draw_polygon(
            pen,
            points=[
                (xmid + dc.stroke_x + dc.gap, y2),
                (xmid + dc.stroke_x, y2),
                (xmid + dc.stroke_x - dc.stroke_x * dc.taper / 2, b.ymid),
            ],
        )

        draw_smooth_parallelogramm_vertical(
            pen, dc.stroke_y, (xmid + xl) / 2, b.y2, b.x2, yt, direction="bottom-right"
        )

        # Wing
        draw_rect(pen, b.x1, dc.x_height - dc.stroke_y, xmid, dc.x_height)

        # Left stem
        draw_rect(pen, xmid, 0, xmid + dc.stroke_x, dc.x_height)
