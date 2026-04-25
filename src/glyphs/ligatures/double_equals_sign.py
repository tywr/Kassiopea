from glyphs import ContextualLigatureGlyph
from draw.dented_rect import draw_dented_rect


class DoubleEqualsSignGlyph(ContextualLigatureGlyph):
    """Ligature glyph for == (two consecutive equals signs).

    Only fires when the run is exactly two equals — longer runs keep
    discrete glyphs thanks to the forbidden-neighbor guard.
    """

    name = "double_equals_sign"
    components = ["equals_sign", "equals_sign"]
    forbidden_neighbors = ["equals_sign"]
    number_characters = 2
    width_ratio = 1
    gap = 0.4
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        g = self.gap * b.height
        s = dc.stroke_x * self.stroke_ratio
        draw_dented_rect(
            pen,
            b.x1,
            dc.math + g / 2 - s / 2,
            dc.window_width,
            dc.math + g / 2 + s / 2,
            side="right",
        )
        draw_dented_rect(
            pen,
            dc.window_width,
            dc.math + g / 2 - s / 2,
            dc.window_width + b.x2,
            dc.math + g / 2 + s / 2,
        )
        draw_dented_rect(
            pen,
            b.x1,
            dc.math - g / 2 - s / 2,
            dc.window_width,
            dc.math - g / 2 + s / 2,
            side="right",
        )
        draw_dented_rect(
            pen,
            dc.window_width,
            dc.math - g / 2 - s / 2,
            b.x2 + dc.window_width,
            dc.math - g / 2 + s / 2,
        )
