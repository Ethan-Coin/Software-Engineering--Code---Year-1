import random
from graphics import *
from q3 import distanceBetweenPoints

def main():
    distance, numWalks = 100, 5
    takeWalks(numWalks, distance)

def getInputs():
    while True:
        distance=int(input("Enter distance to walk [0-100]: "))
        if distance >= 0 and distance <= 100:
            break
        else:
            print("Invalid distance has to be between 0 and 100")
    while True:
        numWalks=int(input("Enter number of walks: "))
        if numWalks >= 0:
            break
        else:
            print("Invalid number of walks has to be greater than 0")
    return distance, numWalks

def drawCircle(win,distance):
    circle=Circle(Point(0,0),distance)
    circle.setWidth(3)
    circle.draw(win)

def drawLine(win, x1, y1, x2, y2):
    line=Line(Point(x1,y1),Point(x2,y2))
    line.setWidth(2)
    line.draw(win)

def drawWalk(win, distance):
    x1,x2 = 0,0
    y1,y2 = 0,0
    while True:
        rand = random.randint(1,4)
        if rand == 1:
            x2 += 5  
        elif rand == 2:
            x2 -= 5
        elif rand == 3:
            y2 += 5
        else:
            y2 -=5
        drawLine(win, x1, y1, x2, y2)
        x1 = x2
        y1 = y2
        if distanceBetweenPoints(0,x2,0,y2) >= distance:
            break

def takeWalks(numWalks, distance):
    win = GraphWin("Walks", 500, 500)
    win.setCoords(-100,-100,100,100)
    drawCircle(win,distance)
    for _ in range(numWalks):
        drawWalk(win, distance)
    win.getMouse()
    win.close()

main()