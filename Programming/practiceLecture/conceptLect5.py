from graphics import *
import time

def main():
    win = GraphWin("Moving Car",500,500) 
    win.setCoords(0,0,1,1)
    line=Line(Point(0,0.515),Point(1,0.515))
    line.draw(win)
    car = []

    carTop=Rectangle(Point(0.15,0.6),Point(0.35,0.68))
    carTop.setFill("blue")
    carTop.setOutline("black")
    carTop.draw(win)
    carChassis=Rectangle(Point(0.1,0.55),Point(0.4,0.6))
    carChassis.setFill("blue")
    carChassis.setOutline("black")
    carChassis.draw(win)
    car.append(carTop)
    car.append(carChassis)

    leftTire=Circle(Point(0.18,0.545),0.03)
    leftTire.setFill("black")
    leftTire.draw(win)
    leftRim=Circle(Point(0.18,0.545),0.02)
    leftRim.setFill("white")
    leftRim.draw(win)
    car.append(leftTire)
    car.append(leftRim)

    rightTire=Circle(Point(0.32,0.545),0.03)
    rightTire.setFill("black")
    rightTire.draw(win)
    rightRim=Circle(Point(0.32,0.545),0.02)
    rightRim.setFill("white")
    rightRim.draw(win)
    car.append(rightTire)
    car.append(rightRim)
    
    right = True
    counter=0
    x=0.005
    while counter != 10:
        counter+=1
        if right == False:
            x=-0.005
            for _ in range(100):
                time.sleep(0.01)
                for item in car:
                    item.move(x,0)
            right=True
        else:
            x=0.005 
            for _ in range(100):
                time.sleep(0.01)
                for item in car:
                    item.move(x,0)
            right = False
    win.getMouse()
    win.close()
main()