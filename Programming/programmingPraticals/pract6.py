from graphics import *
from pract3 import drawArcheryTarget
import math

def greet(name):
    print("Hello", name + ".")
    if len(name) > 20:
        print("That's a long name!")


def canYouVote(age):
    if age >= 18:
        print("You can vote")
    else:
        print("Sorry, you can't vote")


def getDegreeClass(mark):
    if mark >= 70:
        return "1st"
    elif mark >= 60:
        return "2:1"
    elif mark >= 50:
        return "2:2"
    elif mark >= 40:
        return "3rd"
    else:
        return "Fail"


# We will simplify this function later in the term
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def daysInMonth(month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 31


def overlyComplexDaysInMonth(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
       month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif isLeapYear(year):
        return 29
    else:
        return 28


def countDown():
    for i in range(10, 0, -1):
        print(i, "...", end=" ")
    print("Blast Off!")


def numberedTriangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# For exercises 8 & 11
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)



#Exercise 1
def fastFoodOrderPrice():
    price = float(input("Enter the price of the order: "))
    if price < 20:
        price+=2.50
    print(f"The total price of your order is £{price}")

#Exercise 2
def whatToDoToday():
    temperature=int(input("Enter today's temperature: "))
    if temperature > 25:
        print("A swim in the sea")
    elif temperature > 10 and temperature <= 25:
        print("Shopping in Gunwharf Quays")
    else:
        print("It’s best to watch a film at home")


#Exercise 3
def displaySquareRoot(start,end):
    for i in range (start,end+1):
        sqrt = math.sqrt(i)
        print(f"The square root of {i} is {sqrt:.3f}")

#Exercise 4
def calculateGrade(mark):
    grade=""
    if mark >= 16 and mark <=20:
        grade="A"
    elif mark >= 12 and mark <=15:
        grade = "B"
    elif mark >=8 and mark <=11:
        grade = "C"
    elif mark >=0 and mark <= 7:
        grade = "F"
    else:
        grade = "X"
    return grade

#Exercise 5
def peasInAPod():
    numberOfPeas=int(input("Enter the number of peas: "))
    screenX=100*numberOfPeas
    window=GraphWin("Peas",screenX,100)
    for i in range(numberOfPeas):
        pea=Circle(Point(50+i*100,50),50)
        pea.setFill("#66ff66")
        pea.setOutline("#66ff66")
        pea.draw(window)
    window.getMouse()

#Exercise 6
def ticketPrice(jDistance,pAge):
    ticketCost=10+0.15*jDistance
    if pAge >= 60 or pAge <= 15:
        ticketCost=ticketCost*0.6
    return ticketCost

#Exercise 7
def numberSquare(n):
    for row in range(n,0,-1):
        print("\n",end="")
        for col in range(4):
            print(row+col,end=" ")

# For exercise 8
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

def drawColouredEye(win, centre, radius, colour):
    drawCircle(win,centre,radius,"white")
    drawCircle(win,centre,radius//2,colour)
    drawCircle(win,centre,radius//4,"black")

def eyePicker():
    win = GraphWin("",400,400)
    x=int(input("Enter the x coordinate of the eye: "))
    while x < 0 or x > 400:
        print("eye centre not in window")
        x=int(input("Enter the x coordinate of the eye: "))
    y=int(input("Enter the y coordinate of the eye: "))
    while y < 0 or y > 400:
        print("eye centre not in window")
        y=int(input("Enter the y coordinate of the eye: "))
    radius=int(input("Enter the radius of the eye: "))
    colour=input("Enter colour of the eye: ")
    while colour not in ["blue","grey","green","brown"]:
        print("not a valid eye colour")
        colour=input("Enter colour of the eye: ")
    drawColouredEye(win,Point(x,y),radius,colour)
    win.getMouse()

#Exercise 9
def drawPatchWindow():
    win=GraphWin()
    colour="red"
    for i in range(10):
        multi=5*i
        rectangle = Rectangle(Point(0+multi,0+multi),Point(100-multi,100-multi))
        rectangle.setFill(colour)
        rectangle.setOutline(colour)
        rectangle.draw(win)
        if colour == "red":
            colour = "white"
        else:
            colour = "red"
    win.getMouse()

#Exercise 10
def drawPatch(win,x,y,col):
    colour = col
    for i in range(10):
        multi=5*i
        rectangle = Rectangle(Point(x+multi,y+multi),Point((x+100)-multi,(y+100)-multi))
        rectangle.setFill(colour)
        rectangle.setOutline(colour)
        rectangle.draw(win)
        if colour == col:
            colour = "white"
        else:
            colour = col

def drawPatchwork():
    win=GraphWin("",300,200)
    winW=win.getWidth()
    winH=win.getHeight()
    for x in range(0,winW,100):
        for y in range(0,winH,100):
            print(x,y)
            drawPatch(win,x,y,"blue")
    win.getMouse()

#Exercise 11
def eyesAllAround():
    win=GraphWin("",500,500)
    colours=["blue","grey","green","brown"]
    for i in range(30):
        centre = win.getMouse()
        drawColouredEye(win,centre,30,colours[i%4])
    win.getMouse()

#Exercise 12
