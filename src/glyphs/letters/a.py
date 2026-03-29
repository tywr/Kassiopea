from config import FontConfig as fc
from shapes.superellipse_ear import draw_superellipse_ear
from shapes.rect import draw_rect


def draw_a(
    pen,
    stroke: int,
):
    x1 = fc.width / 2 - fc.o_width / 2 - stroke / 2
    y1 = 0
    x2 = fc.width / 2 + fc.o_width / 2 + stroke / 2
    y2 = 0.6 * fc.x_height
    draw_superellipse_ear(
        pen,
        stroke,
        x1,
        y1,
        x2,
        y2,
        fc.a_hx,
        fc.a_hy,
        fc.tooth,
        fc.cover,
        side="right",
    )
    draw_rect(pen, x2 - stroke, 0, x2, fc.x_height)
