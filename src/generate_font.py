"""Generate font."""

import importlib
import inspect
import pkgutil

import pathops
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.t2CharStringPen import T2CharStringPen

from config import FontConfig as fc
from config import DrawConfig
from glyphs import Glyph

import glyphs


def discover_glyphs():
    """Recursively import all modules under glyphs/ and return Glyph subclasses."""

    def on_error(name):
        raise ImportError(f"Failed to import {name}")

    for pkg in [glyphs]:
        for importer, modname, ispkg in pkgutil.walk_packages(
            pkg.__path__, pkg.__name__ + ".", onerror=on_error
        ):
            importlib.import_module(modname)

    def all_subclasses(cls):
        result = []
        for sub in cls.__subclasses__():
            if not inspect.isabstract(sub):
                result.append(sub)
            result.extend(all_subclasses(sub))
        return result

    return [cls() for cls in all_subclasses(Glyph)]


def draw_notdef(pen):
    pen.moveTo((50, 0))
    pen.lineTo((50, 700))
    pen.lineTo((450, 700))
    pen.lineTo((450, 0))
    pen.closePath()


def simplify_glyph(glyph, **kwargs):
    """Draw a glyph through pathops and return the simplified pathops.Path."""
    path = pathops.Path()
    glyph.draw(pathops.PathPen(path), **kwargs)
    return pathops.simplify(path, clockwise=False, keep_starting_points=True)


def record_glyph(glyph, **kwargs):
    path = simplify_glyph(glyph, **kwargs)
    pen = T2CharStringPen(fc.window_width, None)
    path.draw(pen)
    return pen.getCharString()


def build_font(output_path=None, bold=False):
    style_name = "Bold" if bold else "Regular"
    if output_path is None:
        output_path = f"fonts/{fc.family_name}-{style_name}.otf"

    dc = DrawConfig.bold() if bold else DrawConfig()

    all_glyphs = discover_glyphs()

    cmap = {0x20: "space"}
    for g in all_glyphs:
        if g.unicode:
            cmap[int(g.unicode, 16)] = g.name

    # Build charstrings
    notdef_pen = T2CharStringPen(fc.window_width, None)
    draw_notdef(notdef_pen)

    space_pen = T2CharStringPen(fc.window_width, None)

    charstrings = {
        ".notdef": notdef_pen.getCharString(),
        "space": space_pen.getCharString(),
    }
    for g in all_glyphs:
        charstrings[g.name] = record_glyph(g, dc=dc)

    glyph_names = list(charstrings.keys())

    fb = FontBuilder(fc.units_per_em, isTTF=False)
    fb.setupGlyphOrder(glyph_names)
    fb.setupCharacterMap(cmap)
    fb.setupCFF(
        psName=f"{fc.family_name}-{style_name}",
        fontInfo={"FullName": f"{fc.family_name} {style_name}"},
        charStringsDict=charstrings,
        privateDict={},
    )
    fb.setupHorizontalMetrics({name: (fc.window_width, 0) for name in glyph_names})
    fb.setupHorizontalHeader(ascent=fc.window_ascent, descent=-abs(fc.window_descent))
    fb.setupNameTable(
        {
            "familyName": fc.family_name,
            "styleName": style_name,
            "uniqueFontIdentifier": f"{fc.family_name}-{style_name}",
            "fullName": f"{fc.family_name} {style_name}",
            "version": "Version 1.000",
            "psName": f"{fc.family_name}-{style_name}",
        }
    )

    # fsSelection / macStyle flags for bold
    fs_selection = 0x0020 if bold else 0x0040  # BOLD or REGULAR
    mac_style = 0x0001 if bold else 0x0000

    fb.setupOS2(
        sTypoAscender=fc.ascent,
        sTypoDescender=fc.descent,
        sTypoLineGap=50,
        usWinAscent=fc.window_ascent,
        usWinDescent=abs(fc.window_descent),
        sxHeight=fc.x_height,
        sCapHeight=fc.cap,
        fsType=0,
        fsSelection=fs_selection,
    )
    fb.setupPost(isFixedPitch=1)
    fb.setupHead(unitsPerEm=fc.units_per_em, macStyle=mac_style)

    # Dummy DSIG so macOS validators don't complain
    from fontTools.ttLib import newTable

    dsig = newTable("DSIG")
    dsig.ulVersion = 1
    dsig.usFlag = 0
    dsig.usNumSigs = 0
    dsig.signatureRecords = []
    fb.font["DSIG"] = dsig

    fb.font.save(output_path)
    print(f"Font saved to {output_path}")

    # Build TTF version
    ttf_path = output_path.replace(".otf", ".ttf")
    build_ttf(ttf_path, style_name, all_glyphs, cmap, dc)


def build_ttf(output_path, style_name, all_glyphs, cmap, dc):
    """Build a TTF font with quadratic outlines from scratch."""
    from fontTools.pens.cu2quPen import Cu2QuPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen
    from fontTools.ttLib import newTable

    def record_ttf_glyph(glyph):
        path = simplify_glyph(glyph, dc=dc)
        ttf_pen = TTGlyphPen(None)
        cu2qu_pen = Cu2QuPen(ttf_pen, max_err=1.0, reverse_direction=False)
        path.draw(cu2qu_pen)
        return ttf_pen.glyph()

    # .notdef
    notdef_pen = TTGlyphPen(None)
    draw_notdef(notdef_pen)

    # space (empty)
    space_pen = TTGlyphPen(None)
    space_pen.glyph()  # finalize empty glyph

    glyph_table = {".notdef": notdef_pen.glyph(), "space": TTGlyphPen(None).glyph()}
    for g in all_glyphs:
        glyph_table[g.name] = record_ttf_glyph(g)

    glyph_names = list(glyph_table.keys())

    fb = FontBuilder(fc.units_per_em, isTTF=True)
    fb.setupGlyphOrder(glyph_names)
    fb.setupCharacterMap(cmap)
    fb.setupGlyf(glyph_table)
    # LSB must match glyf xMin for correct TTF rendering
    metrics = {}
    for name in glyph_names:
        g = glyph_table[name]
        lsb = g.xMin if hasattr(g, "xMin") and g.numberOfContours > 0 else 0
        metrics[name] = (fc.window_width, lsb)
    fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=fc.window_ascent, descent=-abs(fc.window_descent))
    fb.setupNameTable(
        {
            "familyName": fc.family_name,
            "styleName": style_name,
            "uniqueFontIdentifier": f"{fc.family_name}-{style_name}",
            "fullName": f"{fc.family_name} {style_name}",
            "version": "Version 1.000",
            "psName": f"{fc.family_name}-{style_name}",
        }
    )

    fs_selection = 0x0020 if style_name == "Bold" else 0x0040
    mac_style = 0x0001 if style_name == "Bold" else 0x0000

    fb.setupOS2(
        sTypoAscender=fc.ascent,
        sTypoDescender=fc.descent,
        sTypoLineGap=50,
        usWinAscent=fc.window_ascent,
        usWinDescent=abs(fc.window_descent),
        sxHeight=fc.x_height,
        sCapHeight=fc.cap,
        fsType=0,
        fsSelection=fs_selection,
    )
    fb.setupPost(isFixedPitch=1)
    fb.setupHead(unitsPerEm=fc.units_per_em, macStyle=mac_style)

    dsig = newTable("DSIG")
    dsig.ulVersion = 1
    dsig.usFlag = 0
    dsig.usNumSigs = 0
    dsig.signatureRecords = []
    fb.font["DSIG"] = dsig

    fb.font.save(output_path)
    print(f"Font saved to {output_path}")


if __name__ == "__main__":
    build_font(bold=False)
    build_font(bold=True)
