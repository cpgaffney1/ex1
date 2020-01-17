import pyglet
import math
from pyglet.gl import *


def make_circle(center, radius, color, num_points=50):
    assert len(center) == 2
    assert len(color) == 3
    verts = []
    colors = []
    for i in range(num_points):
        angle = math.radians(float(i)/num_points * 360.0)
        x = radius * math.cos(angle) + center[0]
        y = radius * math.sin(angle) + center[1]
        verts += [x, y]
        colors += [color[0], color[1], color[2]]
    circle = pyglet.graphics.vertex_list(num_points,
                                         ('v2f', verts),
                                         ('c3B', colors)
                                         )
    return circle


def make_filled_circle(center, radius, color):
    """
    We want a pixel perfect circle. To get one,
    we have to approximate it densely with triangles.
    Each triangle thinner than a pixel is enough
    to do it. Sin and cosine are calculated once
    and then used repeatedly to rotate the vector.
    I dropped 10 iterations intentionally for fun.
    """
    glColor3f(*color)

    x, y = center
    iterations = 25# int(2 * radius * math.pi)
    s = math.sin(2 * math.pi / iterations)
    c = math.cos(2 * math.pi / iterations)

    dx, dy = radius, 0

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for _ in range(iterations + 1):
        glVertex2f(x + dx, y + dy)
        dx, dy = (dx * c - dy * s), (dy * c + dx * s)
    glEnd()
