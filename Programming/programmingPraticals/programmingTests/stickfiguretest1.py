from graphics import *

def quit(win):
    win.getMouse()
    win.close()

def theWaiter():
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(200, 60), 20)
    head.draw(win)
    body = Line(Point(200, 80), Point(200, 120))
    body.draw(win)
    arm1 = Line(Point(200, 90), Point(160, 80))
    arm1.draw(win)
    arm2 = Line(Point(200, 90), Point(240, 80))
    arm2.draw(win)
    leg1 = Line(Point(200, 120), Point(170, 170))
    leg1.draw(win)
    leg2 = Line(Point(200, 120), Point(230, 170))
    leg2.draw(win)
    
    tray=Rectangle(Point(140,75),Point(180,80))
    tray.setFill("brown")
    tray.draw(win)
    cup=Rectangle(Point(147,60),Point(159,75))
    cup.setFill("black")
    cup.draw(win)
    orange=Circle(Point(170,68),7)
    orange.setFill("orange")
    orange.draw(win)

    message="Smash!"
    text=Text(Point(100,25),"")
    text.draw(win)
    count=0
    for _ in range(6):
        win.getMouse()
        text.setText(message[0:count+1])
        cup.move(0,15)
        count+=1
    win.getMouse()
    cup.undraw()

    quit(win)

theWaiter()