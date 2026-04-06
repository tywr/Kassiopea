from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect


class FourGlyph(NumberGlyph):
    name = "four"
    unicode = "0x34"
    offset = 0
    crossbar_ratio = 0.4  # Height of the crossbar as fraction of cap

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="cap", width_ratio=self.width_ratio
        )
        crossbar_y = b.y1 + b.height * self.crossbar_ratio

        # Vertical stem (right side)
        draw_rect(
            pen,
            b.x2 - dc.stroke_x,
            b.y1,
            b.x2,
            b.y2,
        )
        # Horizontal crossbar
        draw_rect(
            pen,
            b.x1,
            crossbar_y - dc.stroke_y / 2,
            b.x2,
            crossbar_y + dc.stroke_y / 2,
        )
        # Left diagonal approximated as a vertical + top
        draw_rect(
            pen,
            b.x1,
            crossbar_y - dc.stroke_y / 2,
            b.x1 + dc.stroke_x,
            b.y2,
        )
