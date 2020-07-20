from turtle import *
from tkinter import *

PASSO = 100 

def quadrado():
    for i in range(4):
        forward(PASSO)
        right(90)


def main():
    pensize(3)
    shapesize(2)
    color("pink")
    speed(3)

    quadrado()

    done()

main()