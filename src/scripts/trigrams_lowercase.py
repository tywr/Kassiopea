#!/usr/bin/env python3
"""Generate a lowercase trigram spacing proof PDF.

For each lowercase letter X (a-z), render three spacing strings for
each anchor in {o, h}:
    oXo XoX XXooXX
    hXh XhX XXhhXX

Output: benchmark/trigrams_lowercase.pdf
"""

import argparse
import os
import string
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


ANCHORS = ["o", "h"]
BG = (1, 1, 1)
FG = (0, 0, 0)
LABEL_COLOR = (0.4, 0.4, 0.4)

MARGIN_X = 20 * mm
MARGIN_Y = 25 * mm
TITLE_SIZE = 28
LABEL_SIZE = 10
LINE_SIZE = 20


def trigrams(anchor, target):
    a, x = anchor, target
    return f"{a}{x}{a} {x}{a}{x} {x}{x}{a}{a}{x}{x}"


def render(font_path, output):
    os.makedirs(os.path.dirname(output), exist_ok=True)
    pdfmetrics.registerFont(TTFont("Kassiopea", font_path))

    page_w, page_h = A4
    c = canvas.Canvas(output, pagesize=A4)

    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

    y = page_h - MARGIN_Y

    c.setFillColorRGB(*FG)
    c.setFont("Kassiopea", TITLE_SIZE)
    c.drawString(MARGIN_X, y, "Lowercase trigrams")
    y -= TITLE_SIZE + 6 * mm

    anchors_str = ", ".join(f"'{a}'" for a in ANCHORS)
    c.setFillColorRGB(*LABEL_COLOR)
    c.setFont("Kassiopea", LABEL_SIZE)
    c.drawString(MARGIN_X, y, f"anchors = {anchors_str}   pattern = AXA XAX XXAAXX")
    y -= LABEL_SIZE + 8 * mm

    leading = LINE_SIZE * 1.6
    c.setFont("Kassiopea", LINE_SIZE)
    c.setFillColorRGB(*FG)

    for letter in string.ascii_lowercase:
        for anchor in ANCHORS:
            if y < MARGIN_Y + leading:
                c.showPage()
                c.setFillColorRGB(*BG)
                c.rect(0, 0, page_w, page_h, fill=1, stroke=0)
                c.setFillColorRGB(*FG)
                c.setFont("Kassiopea", LINE_SIZE)
                y = page_h - MARGIN_Y
            c.drawString(MARGIN_X, y, trigrams(anchor, letter))
            y -= leading
        y -= leading * 0.5

    c.save()
    print(f"Saved {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate lowercase trigram PDF")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/Kassiopea-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output",
        default="benchmark/trigrams_lowercase.pdf",
        help="Output filename",
    )
    args = parser.parse_args()
    render(args.font, args.output)
