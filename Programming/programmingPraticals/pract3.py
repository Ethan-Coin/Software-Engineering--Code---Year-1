from graphics import *
from math import *

def drawStickFigure():
    win = GraphWin("Stick figure")
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(75,100),Point(125,100))
    arms.draw(win)
    leg1= Line(Point(100,120),Point(80,160))
    leg1.draw(win)
    leg2= Line(Point(100,120),Point(120,160))
    leg2.draw(win)

def drawCircle():
    radius = int(input("Enter the radius of the circle: "))
    win = GraphWin("Circle",500,500)
    circle = Circle(Point(250,250),radius)
    circle.draw(win)

def drawArcheryTarget():
    win = GraphWin("Archery target")
    circle1=Circle(Point(100,100),90)
    circle1.draw(win)
    circle1.setFill("blue")
    circle2=Circle(Point(100,100),60)
    circle2.draw(win)
    circle2.setFill("red")
    circle3=Circle(Point(100,100),30)
    circle3.draw(win)
    circle3.setFill("yellow")

def drawRectangle():
    height=int(input("Enter height of the rectangle: "))
    width=int(input("Enter width of the rectangle: "))
    win=GraphWin("Rectangle")
    rectangle = Rectangle(Point(100-width//2,100-height//2),Point(100+width//2,100+height//2))
    rectangle.draw(win)

def blueCicle():
    win = GraphWin("Canvas")
    message = Text(Point(100,100), "Click on a point")
    message.draw(win)
    pointer = win.getMouse()
    circle = Circle(pointer,50)
    circle.draw(win)
    circle.setFill("blue")
    message.setText("")

def tenLines():
    win = GraphWin("Line drawer")
    for _ in range(10):
        message = Text(Point(100, 100), "Click on first point")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on second point")
        p2 = win.getMouse()
        line = Line(p1, p2)
        line.draw(win)
        message.setText("")

def tenStrings():
    win=GraphWin("String drawer",500,500)
    for _ in range(10):
        inputBox = Entry(Point(250,250), 50)
        inputBox.draw(win)
        message = Text(Point(250,150),"Enter some text and click where you want the text")
        message.draw(win)
        p = win.getMouse()
        location = Text(p,inputBox.getText())
        location.draw(win)
        message.setText("")
        inputBox.undraw()

def tenColouredRectangles():
    win = GraphWin("Colourful rectangles",500,500)
    for _ in range(10):
        message = Text(Point(250,150),"Click on point 1")
        message.draw(win)
        p1 = win.getMouse()
        message.setText("Click on point 2")
        p2 = win.getMouse()
        inputColour = Entry(Point(250,250),25)
        inputColour.draw(win)
        inputColour.setText("blue")
        message.setText("Enter colour and click on screen")
        win.getMouse()
        message.setText("")
        inputColour.undraw()
        rectangle = Rectangle(p1,p2)
        rectangle.draw(win)
        rectangle.setFill(inputColour.getText())

def fiveClickStickFigure():
    win = GraphWin("Stick Figure")
    pointOne = win.getMouse()
    pointOne.draw(win)
    pointTwo = win.getMouse()
    radius = int(math.sqrt((pointTwo.getX()-pointOne.getX())**1.75+(pointTwo.getY()-pointOne.getY())**1.75))
    head = Circle(pointOne,radius)
    head.draw(win)
    pointThree = win.getMouse()
    bodyStart = pointOne.getY()+radius
    body = Line(Point(pointOne.getX(),bodyStart),Point(pointOne.getX(),pointThree.getY()))
    body.draw(win)
    pointFour = win.getMouse()
    rightArmLength=pointOne.getX()-pointFour.getX()
    arms = Line(Point(pointFour.getX(),(pointThree.getY()+bodyStart)//2),Point(pointOne.getX()+rightArmLength,(pointThree.getY()+bodyStart)//2))
    arms.draw(win)
    pointFive = win.getMouse()
    leftLeg = Line(Point(pointOne.getX(),pointThree.getY()),pointFive)
    legDistance=(pointOne.getX()-pointFive.getX()+pointOne.getX())
    rightLeg = Line(Point(pointOne.getX(),pointThree.getY()),Point(legDistance,pointFive.getY()))
    leftLeg.draw(win)
    rightLeg.draw(win)
    win.getMouse()

fiveClickStickFigure()

        
        
        
