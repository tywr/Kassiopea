from glyphs.uppercase import UppercaseGlyph
from shapes.rect import draw_rect


class UppercaseHGlyph(UppercaseGlyph):
    name = "uppercase_h"
    unicode = "0x48"
    offset = 0

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="ascent", width_ratio=self.width_ratio
        )

        # Left stem
        draw_rect(pen, b.x1, b.y1, b.x1 + dc.stroke_x, b.y2)
        # Right stem
        draw_rect(pen, b.x2 - dc.stroke_x, b.y1, b.x2, b.y2)
        # Middle bar
        draw_rect(pen, b.x1, b.ymid - dc.stroke_y / 2, b.x2, b.ymid + dc.stroke_y / 2)
