from graphics import *

def main():
    # `getInputs` returns two values, so we need to receive them both
    doorColour, lightsOn, sizeOfWin, doorNumber = getInputs()
    drawHouse(doorColour, lightsOn, sizeOfWin, doorNumber)

def getInputs():
    sizeOfWin=int(input("Enter the size of the window: "))
    doorNumber=int(input("Enter the door number: "))
    doorColour = input("Enter door colour: ")
    lightsYN = input("Are the lights on (y/n): ")
    # Check if the first character (index 0) of lightsOn is "y"
    lightsOn = lightsYN[0] == "y"
    # We are returning two values (observe how we receive them in main)
    return doorColour, lightsOn, sizeOfWin, doorNumber

def drawHouse(doorColour, lightsOn, sizeOfWin, doorNumber):
    win = GraphWin("House", sizeOfWin, sizeOfWin)
    win.setCoords(200, 200, 0, 0)
    roof = Polygon(Point(2, 60), Point(42, 2),
                   Point(158, 2), Point(198, 60))
    roof.setFill("pink")
    roof.draw(win)

    # draw wall and door
    drawRectangle(win, Point(2, 60), Point(198, 198), "brown")
    drawRectangle(win, Point(30, 110), Point(80, 198), doorColour)
    doorNumberText = Text(Point(55, 150), doorNumber)
    doorNumberText.draw(win)
    # draw window
    if lightsOn:
        windowColour = "yellow"
    else:
        windowColour = "black"
    drawRectangle(win, Point(110, 110), Point(170, 170), windowColour)
    win.getMouse()


def drawRectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

class A:
    def a(self):
        return "Function a in class A"
    
class B:
    def a(self):
        return "Function a in class B"
    
class C:
    pass

class D(C,A,B):
    pass

d=D()
print(d.a())

#main()