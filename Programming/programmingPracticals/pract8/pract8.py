from graphics import *
import random

#Exercise 1 
def getInputs():
    numberOfFlips=int(input("Enter the number of times for the coin to be flips: "))
    return numberOfFlips

def simulateFlips(numberOfFlips):
    heads = 0 
    tails = 0
    for _ in range (numberOfFlips):
        randomNumber=random.randint(0,1)
        if randomNumber == 0:
            heads+=1
        else:
            tails+=1
    heads=heads/numberOfFlips
    tails=tails/numberOfFlips
    return abs(heads),abs(tails)

def displayResults(heads,tails):
    print(f"Heads {heads} Tails {tails}")

def main():
    numberOfFlips=getInputs()
    heads,tails=simulateFlips(numberOfFlips)
    displayResults(heads,tails)
# main()

#Exercise 2


def main():
    # `getInputs` returns two values, so we need to receive them both
    doorColour, lightsOn = getInputs()
    drawHouse(doorColour, lightsOn)

def getInputs():
    sizeOfWin=int(input("Enter the size of the window: "))
    doorNumber=int(input("Enter the number of doors: "))
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    # Check if the first character (index 0) of lightsOn is "y"
    lightsOn = lightsYN[0] == "y"
    # We are returning two values (observe how we receive them in main)
    return doorColour, lightsOn

def drawHouse(doorColour, lightsOn):
    win = GraphWin("House", 200, 200)
    win.setCoords(0, 0, 200, 200)
    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198, 60))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)

    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)


def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

main()