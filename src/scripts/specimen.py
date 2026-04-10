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

BG = (0, 0, 0)
FG = (1, 1, 1)
LABEL_COLOR = (0.4, 0.4, 0.4)

MARGIN_X = 20 * mm
TITLE_SIZE = 48
LABEL_SIZE = 14
CHAR_SIZE = 36


def render_specimen(font_path, output="specimen.pdf"):
    import os
    os.makedirs(os.path.dirname(output), exist_ok=True)
    pdfmetrics.registerFont(TTFont("Kassiopea", font_path))

    page_w, page_h = A4
    c = canvas.Canvas(output, pagesize=A4)

    # Black background
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    y = page_h - 30 * mm

    # Title
    c.setFillColorRGB(*FG)
    c.setFont("Kassiopea", TITLE_SIZE)
    c.drawString(MARGIN_X, y, "Kassiopea")
    y -= TITLE_SIZE + 16 * mm

    for group_label, chars in GROUPS:
        # Section label
        c.setFillColorRGB(*LABEL_COLOR)
        c.setFont("Kassiopea", LABEL_SIZE)
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

    # --- Page 2: Sample text ---
    if not on_fresh_page:
        c.showPage()
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    max_text_w = page_w - 2 * MARGIN_X

    samples = [
        (
            16,
            "Cassiopeia boasted that she (or her daughter Andromeda), was more "
            "beautiful than all the Nereids, the nymph-daughters of the sea god "
            "Nereus. This brought the wrath of Poseidon, ruling god of the sea, "
            "upon the kingdom of Aethiopia.",
        ),
        (
            14,
            "Accounts differ as to whether Poseidon decided to flood the whole "
            "country or direct the sea monster Cetus to destroy it. In either "
            "case, trying to save their kingdom, Cepheus and Cassiopeia consulted "
            "an oracle of Jupiter, who told them that the only way to appease the "
            "sea gods was to sacrifice their daughter.",
        ),
        (
            12,
            "Accordingly, Andromeda was chained to a rock at the sea's edge and "
            "left to be killed by the sea monster. Perseus arrived and instead "
            "killed Cetus, saved Andromeda and married her.",
        ),
        (
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

    for sample_size, text in samples:
        leading = sample_size * 1.5

        # Section label
        c.setFillColorRGB(*LABEL_COLOR)
        c.setFont("Kassiopea", LABEL_SIZE)
        c.drawString(MARGIN_X, y, f"Sample text @{sample_size}pt")
        y -= LABEL_SIZE + sample_size + 4

        # Word-wrap and draw
        c.setFillColorRGB(*FG)
        c.setFont("Kassiopea", sample_size)

        words = text.split(" ")
        line = ""
        for word in words:
            test = f"{line} {word}".strip()
            if c.stringWidth(test, "Kassiopea", sample_size) > max_text_w:
                c.drawString(MARGIN_X, y, line)
                y -= leading
                line = word
            else:
                line = test
        if line:
            c.drawString(MARGIN_X, y, line)
            y -= leading

        y -= 10 * mm

    c.save()
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Kassiopea specimen")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/Kassiopea-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output", default="assets/specimen.pdf", help="Output filename"
    )
    args = parser.parse_args()
    render_specimen(args.font, args.output)
