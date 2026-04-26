#!/usr/bin/env python3
"""Generate a font specimen PDF for Nordwand Mono.

Usage: python scripts/specimen.py [path/to/font.ttf]
"""

import argparse
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# Character groups
GROUPS = [
    ("Uppercase", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    ("Lowercase", "abcdefghijklmnopqrstuvwxyz"),
    ("Numbers", "0123456789"),
    (
        "Punctuation & Symbols",
        "!\"#$%&'()*+,-./:;<=>?@[\\]^{|}~",
    ),
    (
        "Accented Lowercase",
        "áàâãäåçéèêëíìîïñóòôõöúùûüýÿš",
    ),
]

BG = (1, 1, 1)
FG = (0, 0, 0)
LABEL_COLOR = (0.5, 0.5, 0.5)

MARGIN_X = 20 * mm
TITLE_SIZE = 24
LABEL_SIZE = 14
CHAR_SIZE = 28


FAMILY_VARIANTS = [
    ("Thin", "Nordwand Mono Thin"),
    ("ThinItalic", "Nordwand Mono Thin Italic"),
    ("ExtraLight", "Nordwand Mono ExtraLight"),
    ("ExtraLightItalic", "Nordwand Mono ExtraLight Italic"),
    ("Light", "Nordwand Mono Light"),
    ("LightItalic", "Nordwand Mono Light Italic"),
    ("Regular", "Nordwand Mono Regular"),
    ("Italic", "Nordwand Mono Italic"),
    ("Medium", "Nordwand Mono Medium"),
    ("MediumItalic", "Nordwand Mono Medium Italic"),
    ("SemiBold", "Nordwand Mono SemiBold"),
    ("SemiBoldItalic", "Nordwand Mono SemiBold Italic"),
    ("Bold", "Nordwand Mono Bold"),
    ("BoldItalic", "Nordwand Mono Bold Italic"),
]


TITLE_FONT = "Switzer"
TITLE_FONT_REGULAR = "Switzer-Regular"

# Sentinel: when found in the samples list, force a new page before the next sample.
SAMPLE_SEP = object()


def _find_macos_font(filename):
    """Locate a font file by basename in the standard macOS font directories."""
    import os

    dirs = [
        os.path.expanduser("~/Library/Fonts"),
        "/Library/Fonts",
        "/System/Library/Fonts",
        "/System/Library/Fonts/Supplemental",
    ]
    for d in dirs:
        path = os.path.join(d, filename)
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"Font '{filename}' not found in macOS font directories")


def _otf_to_ttf(otf_path):
    """Convert an OTF (CFF outlines) to a temp TTF (glyf outlines) for reportlab."""
    import tempfile
    from fontTools.ttLib import TTFont as FTTTFont, newTable
    from fontTools.pens.cu2quPen import Cu2QuPen
    from fontTools.pens.ttGlyphPen import TTGlyphPen

    font = FTTTFont(otf_path)
    if "glyf" in font:
        return otf_path  # already TTF

    glyph_set = font.getGlyphSet()
    glyph_order = font.getGlyphOrder()

    glyf_data = {}
    for name in glyph_order:
        ttf_pen = TTGlyphPen(None)
        cu2qu_pen = Cu2QuPen(ttf_pen, max_err=1.0, reverse_direction=True)
        glyph_set[name].draw(cu2qu_pen)
        glyf_data[name] = ttf_pen.glyph()

    for tag in ("CFF ", "CFF2"):
        if tag in font:
            del font[tag]

    glyf = newTable("glyf")
    glyf.glyphs = glyf_data
    glyf.glyphOrder = glyph_order
    font["glyf"] = glyf
    font["loca"] = newTable("loca")

    font.sfntVersion = "\x00\x01\x00\x00"
    font["head"].indexToLocFormat = 0

    maxp = font["maxp"]
    maxp.tableVersion = 0x00010000
    for attr, default in (
        ("maxZones", 1),
        ("maxTwilightPoints", 0),
        ("maxStorage", 0),
        ("maxFunctionDefs", 0),
        ("maxInstructionDefs", 0),
        ("maxStackElements", 0),
        ("maxSizeOfInstructions", 0),
        ("maxComponentElements", 0),
        ("maxComponentDepth", 0),
    ):
        if not hasattr(maxp, attr):
            setattr(maxp, attr, default)

    tmp = tempfile.NamedTemporaryFile(suffix=".ttf", delete=False)
    tmp.close()
    font.save(tmp.name)
    return tmp.name


def _register_macos_otf(reportlab_name, filename):
    pdfmetrics.registerFont(
        TTFont(reportlab_name, _otf_to_ttf(_find_macos_font(filename)))
    )


def render_specimen(font_path, output="specimen.pdf"):
    import os

    os.makedirs(os.path.dirname(output), exist_ok=True)
    pdfmetrics.registerFont(TTFont("Nordwand Mono", font_path))
    _register_macos_otf(TITLE_FONT, "Switzer-Bold.otf")
    _register_macos_otf(TITLE_FONT_REGULAR, "Switzer-Regular.otf")

    # Register every available family variant for the overview page
    font_dir = os.path.dirname(font_path)
    available_variants = []
    for ps_style, display_name in FAMILY_VARIANTS:
        path = os.path.join(font_dir, f"Nordwand Mono-{ps_style}.ttf")
        if not os.path.exists(path):
            continue
        font_name = f"Nordwand Mono-{ps_style}"
        pdfmetrics.registerFont(TTFont(font_name, path))
        available_variants.append((font_name, display_name))

    page_w, page_h = A4
    c = canvas.Canvas(output, pagesize=A4)

    # --- Cover page: black background, white "Nordwand Mono" centered ---
    c.setFillColorRGB(0, 0, 0)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    cover_size = 72
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Nordwand Mono", cover_size)
    cover_text = "NORDWAND MONO"
    text_w = c.stringWidth(cover_text, "Nordwand Mono", cover_size)
    c.drawString((page_w - text_w) / 2, (page_h - cover_size) / 2, cover_text)
    c.showPage()

    # --- Family Overview page ---
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    y = page_h - 30 * mm
    c.setFillColorRGB(*FG)
    c.setFont(TITLE_FONT, TITLE_SIZE)
    c.drawString(MARGIN_X, y, "Family Overview")

    regulars = [v for v in available_variants if "Italic" not in v[0]]
    italics = [v for v in available_variants if "Italic" in v[0]]

    variant_size = 22
    variant_leading = variant_size * 1.7

    title_bottom = page_h - 30 * mm - TITLE_SIZE
    mid = page_h / 2
    bottom_margin = 30 * mm

    def draw_block(variants, y_low, y_high):
        if not variants:
            return
        block_h = (len(variants) - 1) * variant_leading
        y = (y_low + y_high) / 2 + block_h / 2
        for font_name, display_name in variants:
            c.setFont(font_name, variant_size)
            c.drawString(MARGIN_X, y, display_name)
            y -= variant_leading

    c.setFillColorRGB(*FG)
    draw_block(regulars, mid, title_bottom)
    draw_block(italics, bottom_margin, mid)

    c.showPage()

    # White background for the rest of the specimen
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    y = page_h - 30 * mm

    # Title
    c.setFillColorRGB(*FG)
    c.setFont(TITLE_FONT, TITLE_SIZE)
    c.drawString(MARGIN_X, y, "Nordwand Mono")
    y -= TITLE_SIZE + 16 * mm

    for group_label, chars in GROUPS:
        # Section label
        c.setFillColorRGB(*LABEL_COLOR)
        c.setFont(TITLE_FONT, LABEL_SIZE)
        c.drawString(MARGIN_X, y, group_label)
        y -= LABEL_SIZE + CHAR_SIZE

        # Lay out characters
        c.setFillColorRGB(*FG)
        c.setFont("Nordwand Mono", CHAR_SIZE)
        x = MARGIN_X
        max_x = page_w - MARGIN_X
        for ch in chars:
            char_w = c.stringWidth(ch, "Nordwand Mono", CHAR_SIZE) + 8
            if x + char_w > max_x:
                y -= CHAR_SIZE + 10
                x = MARGIN_X
            c.drawString(x, y, ch)
            x += char_w

        y -= 14 * mm

        # New page if running out of space
        if y < 30 * mm:
            c.showPage()
            c.setFillColorRGB(*BG)
            c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
            y = page_h - 30 * mm
            on_fresh_page = True
        else:
            on_fresh_page = False

    # --- Sample text page ---
    if not on_fresh_page:
        c.showPage()
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    max_text_w = page_w - 2 * MARGIN_X

    samples = [
        (
            "Bold",
            "Nordwand Mono-Bold",
            12,
            "The Eiger is a 3,967-metre (13,015 ft) mountain of the Bernese Alps, overlooking Grindelwald and Lauterbrunnen in the Bernese Oberland of Switzerland, just north of the main watershed and border with Valais.",
        ),
        (
            "Medium",
            "Nordwand Mono-Medium",
            12,
            "It is the easternmost peak of a ridge crest that extends across the Mönch to the Jungfrau at 4,158 m (13,642 ft), constituting one of the most emblematic sights of the Swiss Alps.",
        ),
        (
            "Regular",
            "Nordwand Mono",
            12,
            "While the northern side of the mountain rises more than 3,000 m (10,000 ft) above the two valleys of Grindelwald and Lauterbrunnen, the southern side faces the large glaciers of the Jungfrau-Aletsch area, the most glaciated region in the Alps.",
        ),
        (
            "Light",
            "Nordwand Mono-Light",
            12,
            "The most notable feature of the Eiger is its nearly 1,800-metre-high (5,900 ft) north face of rock and ice, named Eiger-Nordwand, Eigerwand or just Nordwand, which is the biggest north face in the Alps.",
        ),
        (
            "Thin",
            "Nordwand Mono-Thin",
            12,
            "The first ascent of the Eiger was made by Swiss guides Christian Almer and Peter Bohren and Irishman Charles Barrington, who climbed the west flank on August 11, 1858.",
        ),
        SAMPLE_SEP,
        (
            "Bold",
            "Nordwand Mono-Bold",
            10,
            "The north face, the last problem of the Alps, considered amongst the most challenging and dangerous ascents, was first climbed in 1938 by an Austrian-German expedition.",
        ),
        (
            "Medium",
            "Nordwand Mono-Medium",
            10,
            "The Eiger has been highly publicized for the many tragedies involving climbing expeditions. Since 1935, at least 64 climbers have died attempting the north face, earning it the German nickname Mordwand, literally \"murder(ous) wall\"—a pun on its correct title of Nordwand (North Wall).",
        ),
        (
            "Regular",
            "Nordwand Mono",
            10,
            "Although the summit of the Eiger can be reached by experienced climbers only, a railway tunnel runs inside the mountain, and two internal stations provide easy access to viewing-windows carved into the rock face.",
        ),
        (
            "Light",
            "Nordwand Mono-Light",
            10,
            "They are both part of the Jungfrau Railway line, running from Kleine Scheidegg to the Jungfraujoch, between the Mönch and the Jungfrau, at the highest railway station in Europe.",
        ),
        (
            "Thin",
            "Nordwand Mono-Thin",
            10,
            "The two stations within the Eiger are Eigerwand (behind the north face) and Eismeer (behind the south face), at around 3,000 metres. The Eigerwand station has not been regularly served since 2016.",
        ),
    ]

    y = page_h - 30 * mm

    for sample in samples:
        if sample is SAMPLE_SEP:
            c.showPage()
            c.setFillColorRGB(*BG)
            c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
            y = page_h - 30 * mm
            continue

        family_label, font_name, sample_size, text = sample
        leading = sample_size * 1.5

        # Solid separator line
        c.setStrokeColorRGB(*FG)
        c.setLineWidth(0.5)
        c.line(MARGIN_X, y, page_w - MARGIN_X, y)
        y -= LABEL_SIZE + 4

        # Label: family name in Switzer Bold, size in Switzer Regular
        c.setFillColorRGB(*FG)
        c.setFont(TITLE_FONT, LABEL_SIZE)
        c.drawString(MARGIN_X, y, family_label)
        family_w = c.stringWidth(family_label + " ", TITLE_FONT, LABEL_SIZE)
        c.setFont(TITLE_FONT_REGULAR, LABEL_SIZE)
        c.drawString(MARGIN_X + family_w, y, f"{sample_size}pt")
        y -= LABEL_SIZE + 8 + leading

        # Word-wrap and draw the sample text in the chosen Nordwand Mono variant
        c.setFont(font_name, sample_size)

        words = text.split(" ")
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, font_name, sample_size) > max_text_w:
                c.drawString(MARGIN_X, y, line)
                y -= leading
                line = word
            else:
                line = test
        if line:
            c.drawString(MARGIN_X, y, line)
            y -= leading

        y -= 8 * mm

    # --- Page 3: Mission status report ---
    c.showPage()
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    # Page title
    y = page_h - 30 * mm
    c.setFillColorRGB(*FG)
    c.setFont(TITLE_FONT, TITLE_SIZE)
    c.drawString(MARGIN_X, y, "Technical Document")

    report_size = 12
    report_leading = report_size * 1.6
    box_padding_x = 12
    box_padding_y = 10

    header_lines = [
        (14, "NATIONAL AERONAUTICS AND SPACE ADMINISTRATION"),
        (14, "GODDARD SPACE FLIGHT CENTER"),
        (14, "MISSION STATUS REPORT -- DSR-7"),
    ]

    body_lines = [
        "MISSION DESIGNATION : ORION DEEP SKY RELAY -- SEGMENT 7 (DSR-7)",
        "REPORT DATE         : 2026-APR-11   UTC 09:42:15",
        "PREPARED BY         : FLIGHT DYNAMICS OFFICER -- C. VASQUEZ",
        "CLASSIFICATION      : UNCLASSIFIED // FOR PUBLIC RELEASE",
        "",
        "1. EXECUTIVE SUMMARY",
        "-------------------------------------------------------------------",
        "The DSR-7 relay satellite completed its third orbital correction",
        "maneuver at 07:18 UTC. All subsystems nominal. Telemetry confirms",
        "stable attitude within 0.003 deg of target orientation. Downlink",
        "rate sustained at 1.2 Gbps through Goldstone and Canberra stations.",
        "",
        "2. ORBITAL PARAMETERS",
        "-------------------------------------------------------------------",
        "  SEMI-MAJOR AXIS   : 42,164.00 km",
        "  ECCENTRICITY      : 0.000142",
        "  INCLINATION       : 0.0471 deg",
        "  ARG OF PERIGEE    : 312.004 deg",
        "  TRUE ANOMALY      : 89.441 deg",
        "  PERIOD            : 23h 56m 04.09s",
        "",
        "3. SUBSYSTEM STATUS",
        "-------------------------------------------------------------------",
        "  POWER     : 4.82 kW generated / 3.17 kW consumed     [NOMINAL]",
        "  THERMAL   : +22.4 C bus avg / radiator delta -1.2 C  [NOMINAL]",
        "  PROPULSN  : 48.7 kg hydrazine remaining (62%)        [NOMINAL]",
        "  COMMS     : X-band primary / S-band backup active    [NOMINAL]",
    ]

    # Measure box width
    box_x1 = MARGIN_X
    box_x2 = page_w - MARGIN_X

    # Draw header box (shifted down to leave room for the page title)
    y = page_h - 30 * mm - TITLE_SIZE - 16 * mm

    header_height = box_padding_y * 2
    for size, _ in header_lines:
        header_height += size * 1.6
    header_height += (len(header_lines) - 1) * 2  # extra spacing

    # Draw double-line box around header
    c.setStrokeColorRGB(*FG)
    c.setLineWidth(1.5)
    c.rect(box_x1, y - header_height, box_x2 - box_x1, header_height, fill=0, stroke=1)
    c.setLineWidth(0.5)
    inset = 3
    c.rect(
        box_x1 + inset,
        y - header_height + inset,
        box_x2 - box_x1 - 2 * inset,
        header_height - 2 * inset,
        fill=0,
        stroke=1,
    )

    # Draw header text centered
    ty = y - box_padding_y
    for size, text in header_lines:
        leading = size * 1.6
        ty -= size  # move down by font size (baseline)
        c.setFillColorRGB(*FG)
        c.setFont("Nordwand Mono", size)
        text_w = c.stringWidth(text, "Nordwand Mono", size)
        c.drawString((page_w - text_w) / 2, ty, text)
        ty -= leading - size + 2

    y -= header_height + 12 * mm

    # Draw body lines
    c.setFont("Nordwand Mono", report_size)
    c.setFillColorRGB(*FG)
    for text in body_lines:
        c.drawString(MARGIN_X + box_padding_x, y, text)
        y -= report_leading

    c.save()
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Nordwand Mono specimen")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/NordwandMono-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output", default="assets/specimen.pdf", help="Output filename"
    )
    args = parser.parse_args()
    render_specimen(args.font, args.output)
