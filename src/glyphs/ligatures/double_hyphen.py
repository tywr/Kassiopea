from glyphs import ContextualLigatureGlyph
from draw.dented_rect import draw_dented_rect


class DoubleHyphenGlyph(ContextualLigatureGlyph):
    """Ligature glyph for -- (two consecutive hyphens).

    Only fires when the run is exactly two hyphens — longer runs keep
    discrete glyphs thanks to the forbidden-neighbor guard.
    """

    name = "double_hyphen"
    components = ["hyphen_minus", "hyphen_minus"]
    forbidden_neighbors = ["hyphen_minus"]
    number_characters = 2
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            offset=self.offset, height="x_height", width_ratio=self.width_ratio
        )
        sy = dc.stroke_y
        # Draw a bar that spans two full glyph widths edge-to-edge
        draw_dented_rect(
            pen, b.x1, dc.math - sy / 2, dc.window_width, dc.math + sy / 2, side="right"
        )
        draw_dented_rect(
            pen,
            dc.window_width,
            dc.math - sy / 2,
            b.x2 + dc.window_width,
            dc.math + sy / 2,
            side="left",
        )
