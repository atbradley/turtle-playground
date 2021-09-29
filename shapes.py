"""
Some toy functions using Python's `turtle` module.
"""
from math import sin, radians
import turtle as t
from turtle import Turtle

t = Turtle()


def circle():
    """
    Draw an approximation of a circle

    (Actually a 360-sided polygon.)
    """
    t.pendown()
    for _ in range(360):
        t.forward(1)
        t.right(1)


def rect(len1: int, len2: int, direction: str = "right"):
    """
    Draw a rectangle.

    Arguments:

    `len1` and `len2`: lengths of sides.
    `dir`: The direction to turn after drawing each side ("left" or "right").
        Defaults to "right"
    """
    t.pendown()
    for x in range(4):
        t.forward(len1 if x % 2 == 0 else len2)
        if direction[0] == "l":
            t.left(90)
        else:
            t.right(90)


def square(sidelen, direction="right"):
    """
    Like, draw a square.

    Each side is `sidelen` pixels long. Turtle will turn `dir`
    ("left" or "right") at each corner (default "right")
    """
    t.pendown()
    rect(sidelen, sidelen, direction)


def rect_spiral(turn=5, size1=75, size2=75):
    """
    Draws a "spiral" of rectangles.

    Works best if `turn` is a factor of 360.
    """
    for _ in range(int(360 / turn)):
        rect(size1, size2)
        t.right(turn)


def square_spiral(turn=5, size=75):
    """
    Draws a "spiral" of squares.

    Works best if `turn` is a factor of 360.
    """
    rect_spiral(turn, size, size)


def squares_in_squares():
    """
    Draws a bunch of squares overlapping each other.
    """
    for i in range(6):
        square(i * 20, "left")
        square(i * 20)
        t.left(180)
        square(i * 20, "left")
        square(i * 20)
        t.left(180)


def eq_triangle(sidelen=40):
    """
    Draws an equilateral triangle, with each side `sidelen` pixels long.
    """
    for _ in range(3):
        t.forward(sidelen)
        t.right(120)


def polygon(sidelen=50, sides=3):
    """
    Draw a regular polygon
    """
    # Is this faster than a for loop or just harder to read and funnier?
    _ = [(t.forward(sidelen), t.right(360 // sides)) for _ in range(sides)]


def poly_spiral(sidecount=3, sidelen=75, turn=5):
    """
    Draw a spiral of polygons
    """
    for _ in range(int(360 / turn)):
        polygon(sidelen, sidecount)
        t.right(turn)


def triangle(l1: int, a2: int, a3: int):
    """
    Draws a triangle, given one side and the measure (in degrees) of the two adjacent angles.

    Here's the part where I had to look up the trigonometry I'd forgotten since high school.

    l1: length in pixels of one side.
    a2, a3: measure of the two angles adjoining l1, in degrees.
    """
    assert a2 + a3 < 180
    # https://drdjw.wordpress.com/2012/01/23/sine-cosine-and-tangent-functions/
    # l1 / sin(radians(a1)) = l2 / sin(radians(a2)) = l3 / sin(radians(a3))
    a1 = 180 - a2 - a3
    ratio = l1 / sin(radians(a1))
    l2 = ratio * sin(radians(a2))
    l3 = ratio * sin(radians(a3))

    # print(a1, a2, a3)
    # print(l1, l2, l3)

    t.forward(l1)
    t.right(180 - a2)
    t.forward(l3)
    t.right(180 - a1)
    t.forward(l2)
    t.right(180 - a3)
