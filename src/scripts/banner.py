#!/usr/bin/env python3
"""Generate a banner image for the GitHub README.

Overlays "NORDWAND MONO" in white at the center of assets/banner-raw.jpg.

Usage: python -m scripts.banner [path/to/font.ttf]
"""

import argparse
from PIL import Image, ImageDraw, ImageFont


TEXT = "NORDWAND MONO"
FG = "#ffffff"
FONT_SIZE = 260
INPUT = "assets/banner-raw.jpg"


def render_banner(font_path, output="assets/banner.png"):
    import os
    os.makedirs(os.path.dirname(output), exist_ok=True)

    img = Image.open(INPUT).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, FONT_SIZE)

    bbox = draw.textbbox((0, 0), TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (img.width - text_w) / 2 - bbox[0]
    y = (img.height - text_h) / 2 - bbox[1]
    draw.text((x, y), TEXT, font=font, fill=FG)

    img.save(output)
    print(f"Saved {output} ({img.width}x{img.height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Nordwand Mono banner")
    parser.add_argument("font", nargs="?", default="fonts/ttf/NordwandMono-Regular.ttf", help="Path to font file")
    parser.add_argument("-o", "--output", default="assets/banner.png", help="Output filename")
    args = parser.parse_args()
    render_banner(args.font, args.output)
