#!/usr/bin/env python3
"""Generate a font specimen PDF for Kassiopea.

Usage: python scripts/specimen.py [path/to/font.otf]
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
        "Accented Lowercase",
        "áàâãäåçéèêëíìîïñóòôõöúùûüýÿš",
    ),
    (
        "Accented Uppercase",
        "ÁÀÂÃÄÅÇÉÈÊËÍÌÎÏÑÓÒÔÕÖÚÙÛÜÝŠ",
    ),
    (
        "Punctuation & Symbols",
        '!"#$%&\'()*+,-./:;<=>?@[\\]^{|}~',
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
        y -= LABEL_SIZE + 6

        # Lay out characters
        c.setFillColorRGB(*FG)
        c.setFont("Kassiopea", CHAR_SIZE)
        x = MARGIN_X
        max_x = page_w - MARGIN_X
        for ch in chars:
            char_w = c.stringWidth(ch, "Kassiopea", CHAR_SIZE) + 8
            if x + char_w > max_x:
                y -= CHAR_SIZE + 8
                x = MARGIN_X
            c.drawString(x, y, ch)
            x += char_w

        y -= CHAR_SIZE + 14 * mm

        # New page if running out of space
        if y < 30 * mm:
            c.showPage()
            c.setFillColorRGB(*BG)
            c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
            y = page_h - 30 * mm

    c.save()
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Kassiopea specimen")
    parser.add_argument("font", nargs="?", default="Kassiopea-Regular.otf", help="Path to font file")
    parser.add_argument("-o", "--output", default="specimen.pdf", help="Output filename")
    args = parser.parse_args()
    render_specimen(args.font, args.output)
