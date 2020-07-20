from turtle import *
from tkinter import *

def ccurve(n, passo):
    if n == 1:
        forward(passo)
    else:
        left(45)
        ccurve(n-1, 0.75*passo)
        right(90)
        ccurve(n-1, 0.75*passo)
        left(45)

def main():
    passo = 30
    niveis = int(input())

    pensize(3)
    shapesize(2)
    color("pink")
    speed(100)

    ccurve(niveis, passo)

    done()

main()