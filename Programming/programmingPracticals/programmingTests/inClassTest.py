from graphics import *

def drawCircles():
    def drawCircle(win,center,colour):
        circle=Circle(center,40)
        circle.setFill(colour)
        circle.draw(win)
        return circle
    
    def colourPicker(point):
        colours=["red","white","blue","green"]
        if point.getX() < 200:
            return colours[0]
        elif point.getX() < 400:
            return colours[1]
        elif point.getX() < 600:
            return colours[2]
        else:
            return colours[3]
    
    win=GraphWin("Circles",800,600)
    for _ in range(15):
        point=win.getMouse()
        drawCircle(win,point,colourPicker(point))
    win.getMouse()
    win.close()
#drawCircles()

def drawCircles2():

    def drawCircle(win,center,colour):
        circle=Circle(center,40)
        circle.setFill(colour)
        circle.draw(win)
        return circle
    
    def colourPicker(point):
        colours=["red","white","blue","green"]
        if point.getX() < 200:
            return colours[0]
        elif point.getX() < 400:
            return colours[1]
        elif point.getX() < 600:
            return colours[2]
        else:
            return colours[3]
    
    win=GraphWin("Circles",800,600)
    radius=40
    for row in range(radius,radius*8,80):
        for column in range(radius*7,radius*15,80):
            point = win.getMouse()
            drawCircle(win,Point(column,row),colourPicker(point))
    win.getMouse()
    win.close()
drawCircles2()