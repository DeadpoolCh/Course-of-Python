from turtle import *
from math import cos
window=Screen()
speed(0)

def rectangel(width, height):
    for _ in range(2):
        forward(width)
        right(90)
        forward(height)
        right(90)
# rectangel(int(input()),int(input()))

def triangle(side):
    for _ in range(3):
        forward(side)
        left(120)
# triangle(int(input()))

# def trisquare(side):
#     for _ in range(3):
#         left(20)
#         for _ in range(4):
#             forward(side)
#             left(90)
# trisquare(int(input()))

def square(side):
    for _ in range(4):
        forward(side)
        left(90)
# def foursquare(side):
#     for _ in range(4):
#         square(side)
#         left(90)
# def twofour(side):
#     for _ in range(2):
#         foursquare(side)
#         left(45)
# twofour(250)

def hexagon(side):
    for _ in range(6):
        forward(side)
        left(60)
# hexagon(150)

def honeycomb(side):
    for _ in range(6):
        hexagon(side)
        forward(side)
        right(60)
# honeycomb(150)

def romd(side):
    for _ in range(2):
        forward(side)
        left(60)
        forward(side)
        left(120)
# romd(150)

def icestar(side):
    right(25)
    for _ in range(10):
        romd(side)
        left(36)
# icestar(100)

def raystar(side):
    for _ in range(12):
        forward(side)
        penup()
        left(180)
        forward(side)
        pendown()
        right(180)
        left(30)
# raystar(100)


def star(side):
    for _ in range(5):
        forward(side)
        right(144)
# star(100)

def fracsquare(side):
    size=side
    for _ in range(25):
        square(size)
        size+=5
# fracsquare(20)

def labirinth(side):
    size = side
    right(90)
    for _ in range(25):
        forward(size)
        right(90)
        size-=10
# labirinth(250)

def point_line(side):
    pensize(2)
    for _ in range(side//10):
        dot()
        penup()
        forward(side//10)
# point_line(250)

def spiral(side):
    size=side
    penup()
    for _ in range(side*5):
        dot()
        forward(size//10)
        right(4)
        size*=1.05
# spiral(20)
exitonclick()