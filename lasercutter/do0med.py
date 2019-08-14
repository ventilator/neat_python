# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 14:20:14 2019

lets try to generate a laser cutter mask

get cairo from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo for windows
as pointed out here: https://github.com/florianfesti/boxes/issues/83#issuecomment-438944318
"""

import cairo
import math
from math import pi


def draw(cr, width, height):
    cr.scale(width, height)
    cr.set_line_width(0.04)

    xc = 0.5
    yc = 0.5
    radius = 0.4
    angle1 = 45.0 * (pi / 180.0)  # angles are specified
    angle2 = 180.0 * (pi / 180.0)  # in radians

    cr.arc(xc, yc, radius, angle1, angle2)
    cr.stroke()

    # draw helping lines
    cr.set_source_rgba(1, 0.2, 0.2, 0.6)
    cr.arc(xc, yc, 0.05, 0, 2 * pi)
    cr.fill()
    cr.set_line_width(0.03)
    cr.arc(xc, yc, radius, angle1, angle1)
    cr.line_to(xc, yc)
    cr.arc(xc, yc, radius, angle2, angle2)
    cr.line_to(xc, yc)
    cr.stroke()

def draws(ctx, width, height):
    wd = .02 * width
    hd = .02 * height

    width -= 2
    height -= 2

    ctx.move_to(width + 1, 1 - hd)
    for i in range(9):
        ctx.rel_line_to(0, height - hd * (2 * i - 1))
        ctx.rel_line_to(-(width - wd * (2 * i)), 0)
        ctx.rel_line_to(0, -(height - hd * (2 * i)))
        ctx.rel_line_to(width - wd * (2 * i + 1), 0)

    ctx.set_source_rgb(0, 0, 1)
    ctx.stroke()

with cairo.SVGSurface("example.svg", 200, 200) as surface:
    context = cairo.Context(surface)
#    x, y, x1, y1 = 0.1, 0.5, 0.4, 0.9
#    x2, y2, x3, y3 = 0.6, 0.1, 0.9, 0.5
#    context.scale(200, 200)
#    context.set_line_width(0.04)
#    context.move_to(x, y)
#    context.curve_to(x1, y1, x2, y2, x3, y3)
#    context.stroke()
#    context.set_source_rgba(1, 0.2, 0.2, 0.6)
#    context.set_line_width(0.02)
#    context.move_to(x, y)
#    context.line_to(x1, y1)
#    context.move_to(x2, y2)
#    context.line_to(x3, y3)
#    context.stroke()
    
#    draw(context, 200, 200)
    draws(context, 200, 200)