from config import FontConfig as fc
from shapes.rect import draw_rect


def draw_l(
    pen,
    stroke: int,
):
    xmid = fc.width / 2 + fc.l_offset
    # Stem
    draw_rect(pen, xmid - stroke / 2, 0, xmid + stroke / 2, fc.ascent)
    # Footer
    draw_rect(
        pen,
        xmid - fc.l_len_left - stroke / 2,
        0,
        xmid + fc.l_len_right + stroke / 2,
        stroke,
    )
    # Left cap
    draw_rect(
        pen,
        xmid - fc.l_len_cap - stroke / 2,
        fc.ascent - stroke,
        xmid,
        fc.ascent,
    )
