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
TITLE_SIZE = 48
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


def render_specimen(font_path, output="specimen.pdf"):
    import os
    os.makedirs(os.path.dirname(output), exist_ok=True)
    pdfmetrics.registerFont(TTFont("Kassiopea", font_path))

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
    c.setFont("Kassiopea", TITLE_SIZE)
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

    # --- Sample text page ---
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

    # --- Page 3: Mission status report ---
    c.showPage()
    c.setFillColorRGB(*BG)
    c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

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
        "  RAAN              : 247.812 deg",
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
        "  AOCS      : reaction wheels 1-4 balanced at 1200 RPM [NOMINAL]",
        "  PAYLOAD   : Ka-band relay transponder locked         [NOMINAL]",
    ]

    # Measure box width
    box_x1 = MARGIN_X
    box_x2 = page_w - MARGIN_X

    # Draw header box
    y = page_h - 30 * mm

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
        box_x1 + inset, y - header_height + inset,
        box_x2 - box_x1 - 2 * inset, header_height - 2 * inset,
        fill=0, stroke=1,
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

    # --- Code snippet pages ---
    code_snippets = [
        ("Python", [
            "import numpy as np",
            "from dataclasses import dataclass",
            "",
            "",
            "@dataclass",
            "class Particle:",
            '    """A particle in 3D space with mass and velocity."""',
            "    position: np.ndarray",
            "    velocity: np.ndarray",
            "    mass: float = 1.0",
            "",
            "    @property",
            "    def kinetic_energy(self) -> float:",
            "        return 0.5 * self.mass * np.dot(self.velocity, self.velocity)",
            "",
            "    def step(self, force: np.ndarray, dt: float) -> None:",
            "        acceleration = force / self.mass",
            "        self.velocity += acceleration * dt",
            "        self.position += self.velocity * dt",
        ]),
        ("C++", [
            "#include <iostream>",
            "#include <vector>",
            "#include <cmath>",
            "#include <algorithm>",
            "#include <numeric>",
            "",
            "template <typename T>",
            "struct Vec3 {",
            "    T x, y, z;",
            "",
            "    Vec3 operator+(const Vec3& o) const {",
            "        return {x + o.x, y + o.y, z + o.z};",
            "    }",
            "    Vec3 operator-(const Vec3& o) const {",
            "        return {x - o.x, y - o.y, z - o.z};",
            "    }",
            "    Vec3 operator*(T s) const { return {x*s, y*s, z*s}; }",
            "    T dot(const Vec3& o) const {",
            "        return x*o.x + y*o.y + z*o.z;",
            "    }",
            "    T norm() const { return std::sqrt(dot(*this)); }",
            "};",
        ]),
        ("Haskell", [
            "module NBody where",
            "",
            "import Data.List (tails)",
            "",
            "data Vec3 = Vec3 !Double !Double !Double",
            "  deriving (Show)",
            "",
            "vadd :: Vec3 -> Vec3 -> Vec3",
            "vadd (Vec3 x1 y1 z1) (Vec3 x2 y2 z2) =",
            "  Vec3 (x1 + x2) (y1 + y2) (z1 + z2)",
            "",
            "vsub :: Vec3 -> Vec3 -> Vec3",
            "vsub (Vec3 x1 y1 z1) (Vec3 x2 y2 z2) =",
            "  Vec3 (x1 - x2) (y1 - y2) (z1 - z2)",
            "",
            "vscale :: Double -> Vec3 -> Vec3",
            "vscale s (Vec3 x y z) = Vec3 (s*x) (s*y) (s*z)",
            "",
            "vnorm :: Vec3 -> Double",
            "vnorm (Vec3 x y z) = sqrt (x*x + y*y + z*z)",
            "",
            "data Body = Body",
            "  { bodyPos  :: !Vec3",
            "  , bodyVel  :: !Vec3",
            "  , bodyMass :: !Double",
            "  } deriving (Show)",
        ]),
    ]

    for lang, lines in code_snippets:
        c.showPage()
        c.setFillColorRGB(*BG)
        c.rect(0, 0, page_w, page_h, fill=1, stroke=0)

        y = page_h - 30 * mm

        # Language label
        c.setFillColorRGB(*LABEL_COLOR)
        c.setFont("Kassiopea", LABEL_SIZE)
        c.drawString(MARGIN_X, y, lang)
        y -= LABEL_SIZE + 12

        # Code
        code_size = 10
        code_leading = code_size * 1.5
        c.setFillColorRGB(*FG)
        c.setFont("Kassiopea", code_size)
        for line in lines:
            if y < 20 * mm:
                break
            c.drawString(MARGIN_X, y, line)
            y -= code_leading

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
