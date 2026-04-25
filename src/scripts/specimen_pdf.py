#!/usr/bin/env python3
"""Generate a font specimen PDF for Kassiopea.

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
    ("Thin", "Kassiopea Thin"),
    ("ThinItalic", "Kassiopea Thin Italic"),
    ("ExtraLight", "Kassiopea ExtraLight"),
    ("ExtraLightItalic", "Kassiopea ExtraLight Italic"),
    ("Light", "Kassiopea Light"),
    ("LightItalic", "Kassiopea Light Italic"),
    ("Regular", "Kassiopea Regular"),
    ("Italic", "Kassiopea Italic"),
    ("Medium", "Kassiopea Medium"),
    ("MediumItalic", "Kassiopea Medium Italic"),
    ("SemiBold", "Kassiopea SemiBold"),
    ("SemiBoldItalic", "Kassiopea SemiBold Italic"),
    ("Bold", "Kassiopea Bold"),
    ("BoldItalic", "Kassiopea Bold Italic"),
]


TITLE_FONT = "Switzer"
TITLE_FONT_REGULAR = "Switzer-Regular"
TITLE_FONT_PATH = "assets/Switzer-Variable.ttf"


def _instantiate_weight(variable_path, weight):
    """Save a static instance of the variable font at the given wght axis to a temp file."""
    import tempfile
    from fontTools.ttLib import TTFont as FTTTFont
    from fontTools.varLib.instancer import instantiateVariableFont

    vf = FTTTFont(variable_path)
    instance = instantiateVariableFont(vf, {"wght": weight})
    tmp = tempfile.NamedTemporaryFile(suffix=".ttf", delete=False)
    tmp.close()
    instance.save(tmp.name)
    return tmp.name


def render_specimen(font_path, output="specimen.pdf"):
    import os

    os.makedirs(os.path.dirname(output), exist_ok=True)
    pdfmetrics.registerFont(TTFont("Kassiopea", font_path))
    pdfmetrics.registerFont(TTFont(TITLE_FONT, _instantiate_weight(TITLE_FONT_PATH, 700)))
    pdfmetrics.registerFont(TTFont(TITLE_FONT_REGULAR, _instantiate_weight(TITLE_FONT_PATH, 400)))

    # Register every available family variant for the overview page
    font_dir = os.path.dirname(font_path)
    available_variants = []
    for ps_style, display_name in FAMILY_VARIANTS:
        path = os.path.join(font_dir, f"Kassiopea-{ps_style}.ttf")
        if not os.path.exists(path):
            continue
        font_name = f"Kassiopea-{ps_style}"
        pdfmetrics.registerFont(TTFont(font_name, path))
        available_variants.append((font_name, display_name))

    page_w, page_h = A4
    c = canvas.Canvas(output, pagesize=A4)

    # --- Cover page: black background, white "Kassiopea" centered ---
    c.setFillColorRGB(0, 0, 0)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    cover_size = 72
    c.setFillColorRGB(1, 1, 1)
    c.setFont("Kassiopea", cover_size)
    cover_text = "Kassiopea"
    text_w = c.stringWidth(cover_text, "Kassiopea", cover_size)
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
    c.drawString(MARGIN_X, y, "Kassiopea")
    y -= TITLE_SIZE + 16 * mm

    for group_label, chars in GROUPS:
        # Section label
        c.setFillColorRGB(*LABEL_COLOR)
        c.setFont(TITLE_FONT, LABEL_SIZE)
        c.drawString(MARGIN_X, y, group_label)
        y -= LABEL_SIZE + CHAR_SIZE

        # Lay out characters
        c.setFillColorRGB(*FG)
        c.setFont("Kassiopea", CHAR_SIZE)
        x = MARGIN_X
        max_x = page_w - MARGIN_X
        for ch in chars:
            char_w = c.stringWidth(ch, "Kassiopea", CHAR_SIZE) + 8
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
            "Kassiopea-Bold",
            16,
            "Cassiopeia boasted that she (or her daughter Andromeda), was more "
            "beautiful than all the Nereids, the nymph-daughters of the sea god "
            "Nereus. This brought the wrath of Poseidon, ruling god of the sea, "
            "upon the kingdom of Aethiopia.",
        ),
        (
            "Medium",
            "Kassiopea-Medium",
            14,
            "Accounts differ as to whether Poseidon decided to flood the whole "
            "country or direct the sea monster Cetus to destroy it. In either "
            "case, trying to save their kingdom, Cepheus and Cassiopeia consulted "
            "an oracle of Jupiter, who told them that the only way to appease the "
            "sea gods was to sacrifice their daughter.",
        ),
        (
            "Regular",
            "Kassiopea",
            12,
            "Accordingly, Andromeda was chained to a rock at the sea's edge and "
            "left to be killed by the sea monster. Perseus arrived and instead "
            "killed Cetus, saved Andromeda and married her.",
        ),
        (
            "Light",
            "Kassiopea-Light",
            10,
            "Poseidon thought Cassiopeia should not escape punishment, so he "
            "placed her in the heavens chained to a throne in a position that "
            "referenced Andromeda's ordeal. The constellation resembles the chair "
            "that originally represented an instrument of torture. Cassiopeia is "
            "not always represented tied to the chair in torment; in some later "
            "drawings she holds a mirror, symbol of her vanity, while in others "
            "she holds a palm frond.",
        ),
    ]

    y = page_h - 30 * mm

    for family_label, font_name, sample_size, text in samples:
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

        # Word-wrap and draw the sample text in the chosen Kassiopea variant
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
        c.setFont("Kassiopea", size)
        text_w = c.stringWidth(text, "Kassiopea", size)
        c.drawString((page_w - text_w) / 2, ty, text)
        ty -= leading - size + 2

    y -= header_height + 12 * mm

    # Draw body lines
    c.setFont("Kassiopea", report_size)
    c.setFillColorRGB(*FG)
    for text in body_lines:
        c.drawString(MARGIN_X + box_padding_x, y, text)
        y -= report_leading

    c.save()
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Kassiopea specimen")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/Kassiopea-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output", default="assets/specimen.pdf", help="Output filename"
    )
    args = parser.parse_args()
    render_specimen(args.font, args.output)
