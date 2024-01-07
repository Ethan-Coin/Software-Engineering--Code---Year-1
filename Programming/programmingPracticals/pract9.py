from graphics import *

def displayDate(day,month,year):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    print(day,months[month-1],year)

def wordLengths(strings):
    for word in strings:
        count=0
        for letter in word:
            count+=1
        print(word,count)

def drawHexagon():
    win=GraphWin()
    points=[]
    for _ in range(6):
        point=win.getMouse()
        points.append(point)
    polygon=Polygon(points)
    polygon.setFill("red")
    polygon.draw(win)
    win.getMouse()

def testMark():
    marks=[]
    students=[0,0,0,0,0,0]
    while True:
        mark=input("Enter mark: ")
        if mark == "q":
            break
        marks.append(int(mark))
    for mark in marks:
        students[mark]+=1
    count=0
    for student in students:
        print(f"{student} student(s) got {count} mark(s)")
        count+=1

testMark()
