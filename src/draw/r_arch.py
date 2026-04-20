import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from shapes.superellipse import Superellipse
from draw.rect import draw_rect


def draw_r_arch(
    pen,
    stroke_x,
    stroke_y,
    x1,
    y1,
    x2,
    y2,
    hx,
    hy,
    taper=0.5,
):
    h = (y2 - y1) / 2
    y_mid = y1 + h

    offset_x = taper * stroke_x
    offset_y = taper * stroke_y

    se = Superellipse(x1=x1, y1=y1, x2=x2, y2=y2, hx=hx, hy=hy)

    # Outer box
    outer_se = se.reduce(
        left=stroke_x - offset_x,
        right=stroke_x - offset_x,
    )
    inner_se = outer_se.reduce(
        left=offset_x,
        right=offset_x,
        top=stroke_y,
        bottom=stroke_y,
    )

    loop_glyph = ufoLib2.objects.Glyph()
    outer_se.draw(loop_glyph.getPen(), clockwise=False)
    inner_se.draw(loop_glyph.getPen(), clockwise=True)

    cut_glyph = ufoLib2.objects.Glyph()
    cut_pen = cut_glyph.getPen()

    draw_rect(cut_pen, x1 - 10, y1, x2 + 10, y_mid)
    draw_rect(cut_pen, (x1 + x2) / 2, y1 - 10, x2, y2 + 10)

    result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
    result.draw(pen)

    return {
        "offset_x": offset_x,
        "offset_y": offset_y,
        "outer": outer_se,
        "inner": inner_se,
    }
