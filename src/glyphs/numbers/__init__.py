from abc import ABC
from glyphs import Glyph


class NumberGlyph(Glyph, ABC):
    """Define common class variables for all number glyphs"""

    width_ratio = 1.00
    stroke_x_ratio = 1.02
    stroke_y_ratio = 1.05
