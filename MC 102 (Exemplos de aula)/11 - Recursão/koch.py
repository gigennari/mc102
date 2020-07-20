from turtle import *
from tkinter import *

PASSO = 2

def koch(n):
    if n == 0:
        forward(PASSO)
    else:
        koch(n-1)
        left(60)
        koch(n-1)
        right(120)
        koch(n-1)
        left(60)
        koch(n-1)


def main():
    n = int(input())
    pensize(2)
    shapesize(5)
    color("pink")
    speed(50)

    koch(n)

    done()

main()