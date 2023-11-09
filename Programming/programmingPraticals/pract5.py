import math
from graphics import  *
#For exercise 2
def areaOfCircle(radius):
    return math.pi * radius ** 2

#Exercise 1
def circumferenceOfCircle(radius):
    return 2*math.pi*radius

#Exercise 2
def circleInfo():
    radius = float(input("Enter the radius of a circle: "))
    print(f"The area is {areaOfCircle(radius):.3f} and the circumference is {circumferenceOfCircle(radius):.3f}")

#For exercise 3
def drawCircle(win, centre, radius, colour):
    circle = Circle(centre, radius)
    circle.setFill(colour)
    circle.setWidth(2)
    circle.draw(win)

#Exercise 3
def drawBrownEyeInCentre():
    window = GraphWin()
    drawCircle(window,Point(100,100),60,"white")
    drawCircle(window,Point(100,100),30,"brown")
    drawCircle(window,Point(100,100),15,"black")
    window.getMouse()

#Exercise 4
def drawBlockOfStars(width,height):
    for _ in range(height):
        print("*"*width)

def drawLetterE():
    drawBlockOfStars(8,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(5,2)
    drawBlockOfStars(2,2)
    drawBlockOfStars(8,2)

#Exercise 5
def drawBrownEye(win, centre, radius):
    drawCircle(win,centre,radius,"white")
    drawCircle(win,centre,radius//2,"brown")
    drawCircle(win,centre,radius//4,"black")

def drawPairOfBrownEyes():
    win = GraphWin()
    drawBrownEye(win,Point(50,100),50)
    drawBrownEye(win,Point(150,100),50)
    win.getMouse()

#Exercise 6
def distanceBetweenPoints(p1,p2):
    distance = math.sqrt((p2.getX()-p1.getX())**2+(p2.getY()-p1.getY())**2)
    return distance

#Exercise 7
def distanceCalculator():
    win=GraphWin()
    message=Text(Point(100,50),"Select point 1")
    message.draw(win)
    p1=win.getMouse()
    message.setText("Select point 2")
    p2=win.getMouse()
    message.setText(str(distanceBetweenPoints(p1,p2)))
    win.getMouse()

#Exercise 8
def drawBlocks(firstSpaces,firstAsterisks,secondSpaces,SecondAsterisks,height):
    for _ in range(height):
        print(firstSpaces*" "+firstAsterisks*"*"+secondSpaces*" "+SecondAsterisks*"*")

def drawLetterA():
    drawBlocks(1,8,1,0,2)
    drawBlocks(0,2,6,2,2)
    drawBlocks(0,10,0,0,2)
    drawBlocks(0,2,6,2,3)

#Exercise 9
def drawFourPairsOfBrownEyes():
    win=GraphWin("",400,400)
    message=Text(Point(200,50),"Select centre of left-most eye")
    message.draw(win)
    p1 = win.getMouse()
    message.setText("Select a point on the circumference of the circle")
    p2 = win.getMouse()
    message.undraw()
    radius = distanceBetweenPoints(p1,p2)
    RightEyeX = p1.getX()+2*radius
    yMulti = 0
    for _ in range(4):
        yValue = p1.getY()+yMulti*radius
        drawBrownEye(win,Point(p1.getX(),yValue),radius)
        drawBrownEye(win,Point(RightEyeX,yValue),radius)
        yMulti+=2
    win.getMouse()
    win.close()
    
#Exercise 10
def displayTextWithSpaces(win,string,size,point):
    characters=[]
    for ch in string.upper():
        characters.append(ch)
        characters.append(" ")
    message=""
    for item in characters:
        message=message+item
    text=Text(point,message)
    text.setSize(size)
    text.draw(win)

def constructVisionChart():
    win=GraphWin()
    win.setCoords(0,0,1,1)
    baseSize=30
    y=0.9
    stringList=[]
    for _ in range(6):
        userString=input("Enter string: ")
        stringList.append(userString)
    for i in range(6):
        displayTextWithSpaces(win,stringList[i],30-(5*i),Point(0.5,y-(0.16*i)))
    win.getMouse()

#Exercise 11
def drawStickFigure(win,position,size):
    head = Circle(position, 0.02*size)
    head.draw(win)

    bodyStartY=position.getY()-0.02*size
    bodyEndY=bodyStartY-0.06*size
    body = Line(Point(position.getX(), bodyStartY), Point(position.getX(), bodyEndY))
    body.draw(win)

    armsY=(bodyStartY+bodyEndY)/1.9
    arms = Line(Point(position.getX()+0.04*size,armsY),Point(position.getX()-0.04*size,armsY))
    arms.draw(win)

    leg1= Line(Point(position.getX(),bodyEndY),Point(position.getX()+0.03*size,bodyEndY-0.04*size))
    leg1.draw(win)

    leg2= Line(Point(position.getX(),bodyEndY),Point(position.getX()-0.03*size,bodyEndY-0.04*size))
    leg2.draw(win)

def drawStickFigureFamily():
    win=GraphWin("",500,500)
    win.setCoords(0,0,1,1)
    drawStickFigure(win,Point(0.3,0.8),4)
    drawStickFigure(win,Point(0.1,0.6),2)
    drawStickFigure(win,Point(0.5,0.5),1)
    drawStickFigure(win,Point(0.7,0.9),5)
    drawStickFigure(win,Point(0.9,0.5),1)
    win.getMouse()

drawStickFigureFamily()