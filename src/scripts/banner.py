#!/usr/bin/env python3
"""Generate a banner image for the GitHub README.

Usage: python scripts/banner.py [path/to/font.ttf]
"""

import argparse
from PIL import Image, ImageDraw, ImageFont


BG = "#000000"
FG = "#91c7d9"
TEXT = "Nordwand Mono"
FONT_SIZE = 360
PADDING_X = 240
PADDING_Y = 150


def render_banner(font_path, output="banner.png"):
    import os
    os.makedirs(os.path.dirname(output), exist_ok=True)
    font = ImageFont.truetype(font_path, FONT_SIZE)

    # Measure text to size the image
    dummy = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy)
    bbox = draw.textbbox((0, 0), TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    img_w = text_w + 2 * PADDING_X
    img_h = text_h + 2 * PADDING_Y

    img = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    x = (img_w - text_w) / 2 - bbox[0]
    y = (img_h - text_h) / 2 - bbox[1]
    draw.text((x, y), TEXT, font=font, fill=FG)

    img.save(output)
    print(f"Saved {output} ({img_w}x{img_h})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Nordwand Mono banner")
    parser.add_argument("font", nargs="?", default="fonts/ttf/NordwandMono-Regular.ttf", help="Path to font file")
    parser.add_argument("-o", "--output", default="assets/banner.png", help="Output filename")
    args = parser.parse_args()
    render_banner(args.font, args.output)
