from config import FontConfig as fc
from shapes.superellipse_ear import draw_superellipse_ear
from shapes.rect import draw_rect
from shapes.corner import draw_corner


def draw_g(
    pen,
    stroke: int,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2
    y1 = 0
    x2 = fc.width / 2 + fc.o_width / 2 + stroke / 2
    y2 = fc.x_height
    draw_superellipse_ear(
        pen,
        stroke,
        x1,
        y1,
        x2,
        y2,
        fc.o_hx,
        fc.o_hy,
        fc.tooth,
        fc.cover,
        side="right",
    )
    draw_rect(pen, x2 - stroke, 0, x2, fc.x_height)
    draw_corner(
        pen,
        stroke,
        x2,
        0,
        fc.width / 2,
        fc.descent + fc.tail_offset,
        fc.g_hx,
        fc.g_hy,
        orientation="bottom-left",
    )
    draw_rect(
        pen,
        x1 + stroke / 2,
        fc.descent + fc.tail_offset,
        fc.width / 2,
        fc.descent + fc.tail_offset + stroke,
    )
