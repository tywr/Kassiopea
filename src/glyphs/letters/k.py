from math import atan, cos, sin
from config import FontConfig as fc
from shapes.rect import draw_rect
from shapes.polygon import draw_polygon


def draw_k(
    pen,
    stroke: int,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2 + fc.k_offset
    y1 = 0
    x2 = x1 + fc.k_width + stroke / 2
    y2 = fc.x_height

    # Angle of each branch
    a = fc.k_width - fc.k_neck_len
    b = fc.x_height / 2
    theta = atan(b / a)
    delta = stroke / sin(theta)
    x_neck = x1 + fc.k_neck_len + stroke - delta / 2


    # Left ascender line
    draw_rect(pen, x1, 0, x1 + stroke, fc.ascent)
    # Middle junction
    draw_rect(
        pen,
        x1 + stroke,
        fc.x_height / 2 - stroke / 2,
        x_neck,
        fc.x_height / 2 + stroke / 2,
    )
    # Upper branch
    draw_polygon(
        pen,
        points=[
            (x_neck, fc.x_height / 2 + stroke / 2),
            (x2 - delta / 2, fc.x_height),
            (x2 + delta / 2, fc.x_height),
            (x_neck + delta, fc.x_height / 2 + stroke / 2),
            (
                x_neck + delta - stroke * cos(theta),
                fc.x_height / 2 + stroke / 2 - stroke * sin(theta),
            ),
            (x_neck, fc.x_height / 2 - stroke / 2),
        ],
    )
    # Lower branch
    draw_polygon(
        pen,
        points=[
            (x_neck, fc.x_height / 2 + stroke / 2),
            (
                x_neck + delta - stroke * cos(theta),
                fc.x_height / 2 - stroke / 2 + stroke * sin(theta),
            ),
            (x_neck + delta, fc.x_height / 2 - stroke / 2),
            (x2 + delta / 2, 0),
            (x2 - delta / 2, 0),
            (x_neck, fc.x_height / 2 - stroke / 2),
        ],
    )
