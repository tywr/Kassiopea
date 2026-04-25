from glyphs import ContextualLigatureGlyph
from draw.dented_rect import draw_dented_rect


class TripleEqualsSignGlyph(ContextualLigatureGlyph):
    """Ligature glyph for === (three consecutive equals signs).

    Only fires when the run is exactly three equals — longer runs keep
    discrete glyphs thanks to the forbidden-neighbor guard.
    """

    name = "triple_equals_sign"
    components = ["equals_sign", "equals_sign", "equals_sign"]
    forbidden_neighbors = ["equals_sign"]
    number_characters = 3
    width_ratio = 1
    gap = 0.4
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        g = self.gap * b.height
        s = dc.stroke_x * self.stroke_ratio
        w = dc.window_width

        # Top bar across three cells
        draw_dented_rect(
            pen,
            b.x1,
            dc.math + g / 2 - s / 2,
            w,
            dc.math + g / 2 + s / 2,
            side="right",
        )
        draw_dented_rect(
            pen,
            w,
            dc.math + g / 2 - s / 2,
            2 * w,
            dc.math + g / 2 + s / 2,
            side="left,right",
        )
        draw_dented_rect(
            pen,
            2 * w,
            dc.math + g / 2 - s / 2,
            2 * w + b.x2,
            dc.math + g / 2 + s / 2,
            side="left",
        )

        # Bottom bar across three cells
        draw_dented_rect(
            pen,
            b.x1,
            dc.math - g / 2 - s / 2,
            w,
            dc.math - g / 2 + s / 2,
            side="right",
        )
        draw_dented_rect(
            pen,
            w,
            dc.math - g / 2 - s / 2,
            2 * w,
            dc.math - g / 2 + s / 2,
            side="left,right",
        )
        draw_dented_rect(
            pen,
            2 * w,
            dc.math - g / 2 - s / 2,
            2 * w + b.x2,
            dc.math - g / 2 + s / 2,
            side="left",
        )
