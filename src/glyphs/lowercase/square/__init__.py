from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    hx_ratio = 1.15
    taper = 0.8
    width_ratio = 1
    ending_thickness = 0.8
