from time import *
from graphics import *
from utilities import *
from Car import *

# PROGRAM


def main():
    win = GraphWin('', 800, 500)

    bmw = Car(100, 130, 150, 70, 30, "blue", win)
    bmw.buildCar()
    win.getMouse()
    for _ in range(1000):
        sleep(.01)
        bmw.move(1, 0)
    win.getMouse()


main()
