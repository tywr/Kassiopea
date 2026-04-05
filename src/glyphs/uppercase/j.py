from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.superellipse_loop import draw_superellipse_loop


class UppercaseJGlyph(UppercaseGlyph):
    name = "uppercase_j"
    unicode = "0x4A"
    offset = 0
    width_ratio = 1.05
    loop_ratio = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )
        hx, hy = dc.hx * self.width_ratio, self.loop_ratio * dc.hy

        # Vertical stem (centered)
        draw_rect(
            pen, b.x2 - dc.stroke_x, b.y1 + self.loop_ratio * b.height / 2, b.x2, b.y2
        )

        # Top bar
        draw_rect(pen, b.x1, b.y2 - dc.stroke_y, b.x2, b.y2)

        # Down loop
        draw_superellipse_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            b.y1 + self.loop_ratio * b.height,
            hx,
            hy,
            cut="top",
        )
