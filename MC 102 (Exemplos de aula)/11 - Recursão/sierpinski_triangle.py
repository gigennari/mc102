from turtle import *
from tkinter import *



def triangulo(n, passo):
    if n == 1:
        for i in range(3):
            forward(passo)
            right(120)
    else:
        for i in range(3):
            triangulo(n-1, passo//2)
            forward(passo)
            right(120)
            


def main():
    niveis = int(input())
    
    pensize(2)
    shapesize(10)
    color("pink")
    speed(100)
    passo = 100

    triangulo(niveis, passo)

    done()

main()