from math import tan, cos, sin, pi
from draw.parallelogramm import draw_parallelogramm_vertical
from utils.pens import NullPen


def draw_s_curve(
    pen,
    sx: float,
    sy: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    hx: float,
    hy: float,
    dx: float,
    dy: float,
    middle_y_ratio=0.52,
    thinning=1.6,
) -> None:
    rtop = 2 * (1 - middle_y_ratio)
    rbot = 2 * middle_y_ratio
    ihx, ihy = max(0, hx - sx), max(0, hy - sy)

    # Substract the stroke to the initial dx/dy of the inner side
    dx = dx - sx / 2
    dy = dy - sy / 2

    xi1, yi1 = x2 - sx - dx, y1 + dy * rbot
    xi2, yi2 = x1 + sx + dx, y2 - dy * rtop
    theta, delta = draw_parallelogramm_vertical(NullPen(), sx, sy, xi1, yi1, xi2, yi2)

    eps = pi / 2 - theta
    px, py = delta * sin(eps) * cos(eps), delta * sin(eps) ** 2
    xe1, ye1 = xi1 + px, yi1 + delta - py
    xe2, ye2 = xi2 - px, yi2 - delta + py

    pen.moveTo((xi1, yi1))
    pen.lineTo((xe1, ye1))
    pen.lineTo((xi2, yi2))
    pen.lineTo((xe2, ye2))

    # Upper part, from parallelogramm, to top-left
    pen.moveTo((xi2, yi2))
    pen.curveTo(
        (xi2 - sin(theta) * ihx, yi2 + cos(theta) * ihx * rtop),
        (x1 + sx, y2 - ihy * rtop),
        (x1 + sx, y2),
    )
    pen.lineTo((x1, y2))
    pen.curveTo(
        (x1, y2 - ihy * rtop - sy / 2),
        (xe2 - sin(theta) * hx, ye2 + cos(theta) * hx * rtop),
        (xe2, ye2),
    )
    pen.closePath()

    # # Lower part, from parallelogramm to bottom right
    pen.moveTo((xi1, yi1))
    pen.curveTo(
        (xi1 + sin(theta) * ihx, yi1 - cos(theta) * ihx * rbot),
        (x2 - sx, y1 + ihy * rbot),
        (x2 - sx, y1),
    )
    pen.lineTo((x2, y1))
    pen.curveTo(
        (x2, y1 + ihy * rbot + sy / 2),
        (xe1 + sin(theta) * hx, ye1 - cos(theta) * hx * rbot),
        (xe1, ye1),
    )
