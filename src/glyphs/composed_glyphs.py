"""Accented / composed glyphs.

Each class pairs a base glyph with an accent mark. The accent_y controls
the vertical anchor. For lowercase letters with ascenders or dots (i, j),
draw_base is called to omit the dot.
"""

from config import FontConfig as fc
from glyphs.composed import ComposedGlyph

from glyphs.lowercase.a import LowercaseAGlyph
from glyphs.lowercase.e import LowercaseEGlyph
from glyphs.lowercase.i import LowercaseIGlyph
from glyphs.lowercase.o import LowercaseOGlyph
from glyphs.lowercase.u import LowercaseUGlyph
from glyphs.lowercase.n import LowercaseNGlyph
from glyphs.lowercase.c import LowercaseCGlyph
from glyphs.lowercase.y import LowercaseYGlyph
from glyphs.lowercase.s import LowercaseSGlyph

from glyphs.uppercase.a import UppercaseAGlyph
from glyphs.uppercase.e import UppercaseEGlyph
from glyphs.uppercase.i import UppercaseIGlyph
from glyphs.uppercase.o import UppercaseOGlyph
from glyphs.uppercase.u import UppercaseUGlyph
from glyphs.uppercase.n import UppercaseNGlyph
from glyphs.uppercase.c import UppercaseCGlyph
from glyphs.uppercase.y import UppercaseYGlyph
from glyphs.uppercase.s import UppercaseSGlyph

from glyphs.accents.acute import Acute
from glyphs.accents.grave import Grave
from glyphs.accents.circumflex import Circumflex
from glyphs.accents.dieresis import Dieresis
from glyphs.accents.tilde import Tilde
from glyphs.accents.caron import Caron
from glyphs.accents.ring import Ring
from glyphs.accents.cedilla import Cedilla

# Heights for accent positioning
_lc_accent = fc.accent  # lowercase accent height (above x-height)
_uc_accent = fc.cap + 80  # uppercase accent height (above cap)
_cedilla_y = 0  # baseline for cedilla


# ── Lowercase with acute ─────────────────────────────────────────────

class LowercaseAAcuteGlyph(ComposedGlyph):
    name = "lowercase_aacute"
    unicode = "0xE1"
    base_glyph_class = LowercaseAGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseEAcuteGlyph(ComposedGlyph):
    name = "lowercase_eacute"
    unicode = "0xE9"
    base_glyph_class = LowercaseEGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseIAcuteGlyph(ComposedGlyph):
    name = "lowercase_iacute"
    unicode = "0xED"
    base_glyph_class = LowercaseIGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseOAcuteGlyph(ComposedGlyph):
    name = "lowercase_oacute"
    unicode = "0xF3"
    base_glyph_class = LowercaseOGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseUAcuteGlyph(ComposedGlyph):
    name = "lowercase_uacute"
    unicode = "0xFA"
    base_glyph_class = LowercaseUGlyph
    accent_class = Acute
    accent_y = _lc_accent


class LowercaseYAcuteGlyph(ComposedGlyph):
    name = "lowercase_yacute"
    unicode = "0xFD"
    base_glyph_class = LowercaseYGlyph
    accent_class = Acute
    accent_y = _lc_accent


# ── Lowercase with grave ─────────────────────────────────────────────

class LowercaseAGraveGlyph(ComposedGlyph):
    name = "lowercase_agrave"
    unicode = "0xE0"
    base_glyph_class = LowercaseAGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseEGraveGlyph(ComposedGlyph):
    name = "lowercase_egrave"
    unicode = "0xE8"
    base_glyph_class = LowercaseEGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseIGraveGlyph(ComposedGlyph):
    name = "lowercase_igrave"
    unicode = "0xEC"
    base_glyph_class = LowercaseIGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseOGraveGlyph(ComposedGlyph):
    name = "lowercase_ograve"
    unicode = "0xF2"
    base_glyph_class = LowercaseOGlyph
    accent_class = Grave
    accent_y = _lc_accent


class LowercaseUGraveGlyph(ComposedGlyph):
    name = "lowercase_ugrave"
    unicode = "0xF9"
    base_glyph_class = LowercaseUGlyph
    accent_class = Grave
    accent_y = _lc_accent


# ── Lowercase with circumflex ────────────────────────────────────────

class LowercaseACircumflexGlyph(ComposedGlyph):
    name = "lowercase_acircumflex"
    unicode = "0xE2"
    base_glyph_class = LowercaseAGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseECircumflexGlyph(ComposedGlyph):
    name = "lowercase_ecircumflex"
    unicode = "0xEA"
    base_glyph_class = LowercaseEGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseICircumflexGlyph(ComposedGlyph):
    name = "lowercase_icircumflex"
    unicode = "0xEE"
    base_glyph_class = LowercaseIGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseOCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ocircumflex"
    unicode = "0xF4"
    base_glyph_class = LowercaseOGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


class LowercaseUCircumflexGlyph(ComposedGlyph):
    name = "lowercase_ucircumflex"
    unicode = "0xFB"
    base_glyph_class = LowercaseUGlyph
    accent_class = Circumflex
    accent_y = _lc_accent


# ── Lowercase with dieresis ──────────────────────────────────────────

class LowercaseADieresisGlyph(ComposedGlyph):
    name = "lowercase_adieresis"
    unicode = "0xE4"
    base_glyph_class = LowercaseAGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseEDieresisGlyph(ComposedGlyph):
    name = "lowercase_edieresis"
    unicode = "0xEB"
    base_glyph_class = LowercaseEGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseIDieresisGlyph(ComposedGlyph):
    name = "lowercase_idieresis"
    unicode = "0xEF"
    base_glyph_class = LowercaseIGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseODieresisGlyph(ComposedGlyph):
    name = "lowercase_odieresis"
    unicode = "0xF6"
    base_glyph_class = LowercaseOGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseUDieresisGlyph(ComposedGlyph):
    name = "lowercase_udieresis"
    unicode = "0xFC"
    base_glyph_class = LowercaseUGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


class LowercaseYDieresisGlyph(ComposedGlyph):
    name = "lowercase_ydieresis"
    unicode = "0xFF"
    base_glyph_class = LowercaseYGlyph
    accent_class = Dieresis
    accent_y = _lc_accent


# ── Lowercase with tilde ─────────────────────────────────────────────

class LowercaseATildeGlyph(ComposedGlyph):
    name = "lowercase_atilde"
    unicode = "0xE3"
    base_glyph_class = LowercaseAGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseNTildeGlyph(ComposedGlyph):
    name = "lowercase_ntilde"
    unicode = "0xF1"
    base_glyph_class = LowercaseNGlyph
    accent_class = Tilde
    accent_y = _lc_accent


class LowercaseOTildeGlyph(ComposedGlyph):
    name = "lowercase_otilde"
    unicode = "0xF5"
    base_glyph_class = LowercaseOGlyph
    accent_class = Tilde
    accent_y = _lc_accent


# ── Lowercase with ring ──────────────────────────────────────────────

class LowercaseARingGlyph(ComposedGlyph):
    name = "lowercase_aring"
    unicode = "0xE5"
    base_glyph_class = LowercaseAGlyph
    accent_class = Ring
    accent_y = _lc_accent


# ── Lowercase with cedilla ───────────────────────────────────────────

class LowercaseCCedillaGlyph(ComposedGlyph):
    name = "lowercase_ccedilla"
    unicode = "0xE7"
    base_glyph_class = LowercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Lowercase with caron ─────────────────────────────────────────────

class LowercaseSCaronGlyph(ComposedGlyph):
    name = "lowercase_scaron"
    unicode = "0x161"
    base_glyph_class = LowercaseSGlyph
    accent_class = Caron
    accent_y = _lc_accent


# ── Uppercase with acute ─────────────────────────────────────────────

class UppercaseAAcuteGlyph(ComposedGlyph):
    name = "uppercase_aacute"
    unicode = "0xC1"
    base_glyph_class = UppercaseAGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseEAcuteGlyph(ComposedGlyph):
    name = "uppercase_eacute"
    unicode = "0xC9"
    base_glyph_class = UppercaseEGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseIAcuteGlyph(ComposedGlyph):
    name = "uppercase_iacute"
    unicode = "0xCD"
    base_glyph_class = UppercaseIGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseOAcuteGlyph(ComposedGlyph):
    name = "uppercase_oacute"
    unicode = "0xD3"
    base_glyph_class = UppercaseOGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseUAcuteGlyph(ComposedGlyph):
    name = "uppercase_uacute"
    unicode = "0xDA"
    base_glyph_class = UppercaseUGlyph
    accent_class = Acute
    accent_y = _uc_accent


class UppercaseYAcuteGlyph(ComposedGlyph):
    name = "uppercase_yacute"
    unicode = "0xDD"
    base_glyph_class = UppercaseYGlyph
    accent_class = Acute
    accent_y = _uc_accent


# ── Uppercase with grave ─────────────────────────────────────────────

class UppercaseAGraveGlyph(ComposedGlyph):
    name = "uppercase_agrave"
    unicode = "0xC0"
    base_glyph_class = UppercaseAGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseEGraveGlyph(ComposedGlyph):
    name = "uppercase_egrave"
    unicode = "0xC8"
    base_glyph_class = UppercaseEGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseIGraveGlyph(ComposedGlyph):
    name = "uppercase_igrave"
    unicode = "0xCC"
    base_glyph_class = UppercaseIGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseOGraveGlyph(ComposedGlyph):
    name = "uppercase_ograve"
    unicode = "0xD2"
    base_glyph_class = UppercaseOGlyph
    accent_class = Grave
    accent_y = _uc_accent


class UppercaseUGraveGlyph(ComposedGlyph):
    name = "uppercase_ugrave"
    unicode = "0xD9"
    base_glyph_class = UppercaseUGlyph
    accent_class = Grave
    accent_y = _uc_accent


# ── Uppercase with circumflex ────────────────────────────────────────

class UppercaseACircumflexGlyph(ComposedGlyph):
    name = "uppercase_acircumflex"
    unicode = "0xC2"
    base_glyph_class = UppercaseAGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseECircumflexGlyph(ComposedGlyph):
    name = "uppercase_ecircumflex"
    unicode = "0xCA"
    base_glyph_class = UppercaseEGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseICircumflexGlyph(ComposedGlyph):
    name = "uppercase_icircumflex"
    unicode = "0xCE"
    base_glyph_class = UppercaseIGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseOCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ocircumflex"
    unicode = "0xD4"
    base_glyph_class = UppercaseOGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


class UppercaseUCircumflexGlyph(ComposedGlyph):
    name = "uppercase_ucircumflex"
    unicode = "0xDB"
    base_glyph_class = UppercaseUGlyph
    accent_class = Circumflex
    accent_y = _uc_accent


# ── Uppercase with dieresis ──────────────────────────────────────────

class UppercaseADieresisGlyph(ComposedGlyph):
    name = "uppercase_adieresis"
    unicode = "0xC4"
    base_glyph_class = UppercaseAGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseEDieresisGlyph(ComposedGlyph):
    name = "uppercase_edieresis"
    unicode = "0xCB"
    base_glyph_class = UppercaseEGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseIDieresisGlyph(ComposedGlyph):
    name = "uppercase_idieresis"
    unicode = "0xCF"
    base_glyph_class = UppercaseIGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseODieresisGlyph(ComposedGlyph):
    name = "uppercase_odieresis"
    unicode = "0xD6"
    base_glyph_class = UppercaseOGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


class UppercaseUDieresisGlyph(ComposedGlyph):
    name = "uppercase_udieresis"
    unicode = "0xDC"
    base_glyph_class = UppercaseUGlyph
    accent_class = Dieresis
    accent_y = _uc_accent


# ── Uppercase with tilde ─────────────────────────────────────────────

class UppercaseATildeGlyph(ComposedGlyph):
    name = "uppercase_atilde"
    unicode = "0xC3"
    base_glyph_class = UppercaseAGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseNTildeGlyph(ComposedGlyph):
    name = "uppercase_ntilde"
    unicode = "0xD1"
    base_glyph_class = UppercaseNGlyph
    accent_class = Tilde
    accent_y = _uc_accent


class UppercaseOTildeGlyph(ComposedGlyph):
    name = "uppercase_otilde"
    unicode = "0xD5"
    base_glyph_class = UppercaseOGlyph
    accent_class = Tilde
    accent_y = _uc_accent


# ── Uppercase with ring ──────────────────────────────────────────────

class UppercaseARingGlyph(ComposedGlyph):
    name = "uppercase_aring"
    unicode = "0xC5"
    base_glyph_class = UppercaseAGlyph
    accent_class = Ring
    accent_y = _uc_accent


# ── Uppercase with cedilla ───────────────────────────────────────────

class UppercaseCCedillaGlyph(ComposedGlyph):
    name = "uppercase_ccedilla"
    unicode = "0xC7"
    base_glyph_class = UppercaseCGlyph
    accent_class = Cedilla
    accent_y = _cedilla_y


# ── Uppercase with caron ─────────────────────────────────────────────

class UppercaseSCaronGlyph(ComposedGlyph):
    name = "uppercase_scaron"
    unicode = "0x160"
    base_glyph_class = UppercaseSGlyph
    accent_class = Caron
    accent_y = _uc_accent
