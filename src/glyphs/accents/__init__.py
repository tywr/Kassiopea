from abc import ABC, abstractmethod
from glyphs import Glyph


class Accent(Glyph, ABC):
    """Base class for accent/diacritical marks.

    Accents are full glyphs (can be visualized standalone) and also
    provide draw_at(pen, dc, x, y) for positioning by ComposedGlyph.
    """

    offset = 0

    @abstractmethod
    def draw_at(self, pen, dc, x, y):
        """Draw the accent centered horizontally at x, vertically at y."""
        ...

    def draw(self, pen, dc):
        """Draw the accent at the default position (centered in the cell)."""
        b = dc.body_bounds(offset=self.offset)
        self.draw_at(pen, dc, x=b.xmid, y=dc.accent)
