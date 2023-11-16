from graphics import *
import time
import random
from pract6 import *
from pract5 import *

def countDown():
    i = 10
    while i > 0:
        print(i, "...", end=" ")
        i = i - 1
    print("Blast Off!")


# Note: msg == "" needs to appear twice here
def getString1():
    msg = ""
    while msg == "":
        msg = input("Enter a non-empty string: ")
        if msg == "":
            print("You didn't enter anything!")
    return msg


def getString2():
    while True:
        msg = input("Enter a non-empty string: ")
        if msg != "":
            break
        print("You didn't enter anything!")
    return msg


def addUpNumbers1():
    total = 0
    more = "y"
    while more == "y":  # The loop runs while `more` is "y"
        number = int(input("Enter a number "))
        total = total + number
        more = input("Any more numbers? ")
    print("The total is", total)


def addUpNumbers2():
    total = 0
    number = int(input("Number (0 to stop): "))
    while number != 0:  # The loop runs while `number` is not 0
        total = total + number
        number = int(input("Number (0 to stop): "))
    print("The total is", total)


def addUpNumbers3():
    total = 0
    nStr = input("Number (hit enter to stop): ")
    while nStr != "":  # The loop runs while `nStr` is not empty
        number = int(nStr)  # Assumes that `nStr` contains a number
        total = total + number
        nStr = input("Number (hit enter to stop): ")
    print("The total is", total)


def addUpNumbers4():
    total = 0
    while True:  # The loop runs until we break it
        nStr = input("Number (anything else to stop): ")
        if not nStr.isdigit():
            break  # Break the loop if `nStr` is not a number
        number = int(nStr)
        total = total + number
    print("The total is", total)

# For exercise 6
def fahrenheit2Celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius2Fahrenheit(celsius):
    return 9 / 5 * celsius + 32

#Exercise 1
def getName(name):
    while name.isalpha() != True:
        name = input("Enter your name: ")
    return name

#Exercise 2
def trafficLights():
    win = GraphWin()
    red = Circle(Point(100, 50), 20)
    red.setFill("red")
    red.draw(win)
    amber = Circle(Point(100, 100), 20)
    amber.setFill("black")
    amber.draw(win)
    green = Circle(Point(100, 150), 20)
    green.setFill("black")
    green.draw(win)
    while True:
        red.setFill("red")
        time.sleep(0.5)
        amber.setFill("yellow")
        time.sleep(0.5)
        red.setFill("black")
        amber.setFill("black")
        green.setFill("green")
        time.sleep(0.5)
        green.setFill("black")
        amber.setFill("yellow")
        time.sleep(0.5)
        amber.setFill("black")
    
#Exercise 3
def gradeCoursework():
    mark = int(input("Enter mark: "))
    while mark > 20 or mark < 0:
        print("Please enter a valid mark")
        mark= int(input("Enter mark: "))
    print(calculateGrade(mark))

#Exercise 4
def orderPrice():
    unitPrices=[]
    quantities=[]
    condition="y"
    while condition.capitalize()=="Y":
        unitPrice=0
        while unitPrice <= 0:
            unitPrice=float(input("Enter the unit price of the product in pounds: "))
        quantity=0
        while quantity < 1:
            quantity = int(input("Enter the quantity of that product: "))
        unitPrices.append(unitPrice)
        quantities.append(quantity)
        condition=input("Do you want to add another product? (Y/N): ")
    total=0
    for i in range(len(unitPrices)):
        total+=unitPrices[i]*quantities[i]
    print(f"The total price is £{total:.2f}")

#Exercise 5
def clickableEye():
    win = GraphWin("Clickable Eye", 400, 400)
    drawBrownEye(win,Point(200,200),100)
    message =  Text(Point(200, 350), "")
    message.draw(win)
    while True:
        p1 = win.getMouse()
        if distanceBetweenPoints(p1,Point(200,200)) <= 100/4:
            message.setText("Pupil")
        elif distanceBetweenPoints(p1,Point(200,200)) <= 100/2:
            message.setText("Iris")
        elif distanceBetweenPoints(p1,Point(200,200)) <= 100:
            message.setText("Sclera")
        else:
            win.close()
    
#Exercise 6
def temperatureConverter():
    while True:
        print("1. Fahrenheit to Celsius 2. Celsius to Fahrenheit 3. Quit")
        choice=int(input("Enter your choice: "))
        if choice == 1:
            fahrenheit=float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit:.2f}F = {fahrenheit2Celsius(fahrenheit):.2f}C")
        elif choice == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius:.2f}C = {celsius2Fahrenheit(celsius):.2f}F")
        else:
            break

#Exercise 7
def tableTennisScorer():
    win=GraphWin("Table Tennis Scorer",400,400)
    player1Score=0
    player2Score=0
    player1ScoreText=Text(Point(100,200),player1Score)
    player1ScoreText.setSize(20)
    player1ScoreText.draw(win)
    player2ScoreText=Text(Point(300,200),player2Score)
    player2ScoreText.setSize(20)
    player2ScoreText.draw(win)
    line=Line(Point(200,0),Point(200,400))
    line.draw(win)
    while player2Score < 11 and player1Score < 11:
        p1=win.getMouse()
        if p1.getX() < 200:
            player1Score+=1
            player1ScoreText.setText(player1Score)
        else:
            player2Score+=1
            player2ScoreText.setText(player2Score)
    message=Text(Point(100,350),"Winner")
    message.setSize(20)
    message.draw(win)
    if player2Score == 11:
        message.move(200,0)
    win.getMouse()

#Exercise 8
def guessTheNumber():
    randomNumber=random.randint(1,100)
    guess=int(input("Guess the number: "))
    count=1
    while guess != randomNumber:
        if guess > randomNumber:
            print("Too high")
        else:
            print("Too low")
        count+=1
        guess=int(input("Guess the number: "))
    if count <=7:
        print(f"You win! You took {count} guesses")
    else:
        print(f"You lose! You took {count} guesses")

#Exercise 9
def clickableBoxOfEyes(rows,columns):
    width=100+100*columns
    height=100+100*rows
    win = GraphWin("Clickable Box of Eyes", width, height)
    tl = Point(50,50)
    br = Point(width-50,height-50)
    rectangle=Rectangle(tl,br)
    rectangle.draw(win)
    eyes=[]
    for i in range(rows):
        for j in range(columns):
            drawColouredEye(win,Point(100+100*j,100+100*i),50,"blue")
            circle=Circle(Point(100+100*j,100+100*i),50)
            eyes.append(circle)
    message =  Text(Point(width/2, height-25), "")
    message.draw(win)
    while True:
        p1 = win.getMouse()
        gap=False
        for i in range(len(eyes)):
            if distanceBetweenPoints(p1,eyes[i].getCenter()) <= 50:
                message.setText(f"Eye at row {i//columns+1} column {i%columns+1}")
                gap=False
                break
            elif p1.getX()<=50 or p1.getX()>=width-50 or p1.getY()<=50 or p1.getY()>=height-50:
                win.close()
            else:
                gap=True
        if gap:
            message.setText("Between eyes")  
    
#Exercise 10
def findTheCircle():
    win=GraphWin("Find the Circle",400,400)
    win.setBackground("white")
    win.setCoords(-100,-100,100,100)
    size=1
    round=1
    pointTotal=0    
    message=Text(Point(0,-90),"")
    message.draw(win)
    guessText=Text(Point(80,90),"")
    guessText.draw(win)
    while True:
        if size < 0.1:
            message.setText(f"You win! You scored {pointTotal} points")
            circle.undraw()
            break
        randomX=random.randint(-100,100)
        randomY=random.randint(-100,100)
        circle=Circle(Point(randomX,randomY),30*size)
        circle.setOutline("white")
        circle.draw(win)
        points=10
        guessText.setText("Guess: 1")
        pClick=win.getMouse()
        message.setText("")
        if distanceBetweenPoints(pClick,circle.getCenter()) <= 30*size:
            pointTotal+=points
            circle.setFill("blue")
        else:
            points-=1
            while points > 0:
                pLast=pClick
                pointCircle=Circle(pLast,3)
                pointCircle.setFill("black")
                pointCircle.draw(win)
                guessText.setText(f"Guess: {11-points}")
                pClick=win.getMouse()
                if distanceBetweenPoints(pClick,circle.getCenter()) <= 30*size:
                    pointTotal+=points
                    circle.setFill("blue")
                    break
                elif distanceBetweenPoints(pClick,circle.getCenter()) < distanceBetweenPoints(pLast,circle.getCenter()):
                    message.setText("getting closer")
                    pointCircle.undraw()
                    points-=1
                else:
                    message.setText("getting further away")
                    pointCircle.undraw()
                    points-=1
        if points == 0:
            message.setText(f"You lose! You scored {pointTotal} points")
            pointCircle.undraw()
            circle.undraw()
            break
        else:
            round = round + 1
            size-=0.1
            message.setText("click to continue")
            pointCircle.undraw()
            win.getMouse()
            message.setText(f"round {round}")
            circle.undraw()
    win.getMouse()