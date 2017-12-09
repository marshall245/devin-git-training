# a library of little functions


__author__ = "Marshall Markham"


def traingles(n):
    """Returns the triangle number n * ( n + 1 ) / 2"""
    return n * (n + 1) / 2


def handshake(n):
    """Returns the handshake number n * (n - 1) / 2"""
    return n * (n - 1) / 2


def circle_perimeter(radius):
    """Returns the perimeter of a circle """
    return 3.14 * radius ** 2


def square_perimeter(side):
    """Returns the perimeter of a square"""
    return 4 * side


def rectangle_perimeter(len, width):
    """Returns the perimeter of a rectangle"""
    return 2 * len + 2 * width 
