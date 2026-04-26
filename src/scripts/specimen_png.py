#!/usr/bin/env python3
"""Generate a compact PNG specimen image for the GitHub README.

Usage: python -m scripts.specimen_png [path/to/font.ttf]
"""

import argparse
import os

from PIL import Image, ImageDraw, ImageFont


BG = "#FFFFFF"
FG = "#000000"

# High-res scale factor (render at 2x for retina)
SCALE = 2

# Base dimensions (before scaling)
WIDTH = 1200
PADDING_X = 40
PADDING_Y = 30
LINE_GAP = 20

LINES = [
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "abcdefghijklmnopqrstuvwxyz",
    "0123456789",
    "!\"#$%&'()*+,-./:;<=>?@[\\]^{|}~",
]


def render_specimen(font_path, output="specimen.png"):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    s = SCALE
    w = WIDTH * s
    px = PADDING_X * s
    py = PADDING_Y * s
    lg = LINE_GAP * s
    content_w = w - 2 * px

    font = ImageFont.truetype(font_path, 40 * s)

    # Measure line height using font metrics
    dummy = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy)
    ascent, descent = font.getmetrics()
    line_h = ascent + descent

    total_h = 2 * py + len(LINES) * line_h + (len(LINES) - 1) * lg

    # Render
    img = Image.new("RGB", (w, total_h), BG)
    draw = ImageDraw.Draw(img)

    y = py + ascent
    for chars in LINES:
        # Measure each character width
        widths = []
        for ch in chars:
            bb = draw.textbbox((0, 0), ch, font=font, anchor="ls")
            widths.append(bb[2] - bb[0])

        total_char_w = sum(widths)
        gap = (content_w - total_char_w) / max(len(chars) - 1, 1)

        x = px
        for ch, cw in zip(chars, widths):
            draw.text((x, y), ch, font=font, fill=FG, anchor="ls")
            x += cw + gap

        y += line_h
        if chars != LINES[-1]:
            y += lg

    # Crop to equal padding around actual content
    import numpy as np
    arr = np.array(img)
    rows_with_content = np.any(arr < 245, axis=(1, 2))
    first_row = int(np.argmax(rows_with_content))
    last_row = int(len(rows_with_content) - 1 - np.argmax(rows_with_content[::-1]))
    crop_top = first_row - py
    crop_bottom = (img.height - 1 - last_row) - py
    trim = min(crop_top, crop_bottom)
    img = img.crop((0, int(crop_top - trim), img.width, int(img.height - (crop_bottom - trim))))

    img.save(output, optimize=True)
    print(f"Saved {output} ({img.width}x{img.height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Nordwand Mono PNG specimen")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/NordwandMono-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output", default="assets/specimen.png", help="Output filename"
    )
    args = parser.parse_args()
    render_specimen(args.font, args.output)
