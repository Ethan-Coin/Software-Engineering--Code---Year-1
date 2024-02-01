from graphics import *
from random import random
import math


def displayDate(day, month, year):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    print(day, months[month-1], year)


def wordLengths(strings):
    for word in strings:
        count = 0
        for letter in word:
            count += 1
        print(word, count)


def drawHexagon():
    win = GraphWin()
    points = []
    for _ in range(6):
        point = win.getMouse()
        points.append(point)
    polygon = Polygon(points)
    polygon.setFill("red")
    polygon.draw(win)
    win.getMouse()


def testMark():
    marks = []
    students = [0, 0, 0, 0, 0, 0]
    while True:
        mark = input("Enter mark: ")
        if mark == "q":
            break
        marks.append(int(mark))
    for mark in marks:
        students[mark] += 1
    count = 0
    for student in students:
        print(f"{student} student(s) got {count} mark(s)")
        count += 1


def drawBarChart(integers):
    for i in range(1, max(integers)+1):
        for integer in integers:
            if i <= integer:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


def uniqueModules(mod_names):
    unique = []
    for module in mod_names:
        if module not in unique:
            unique.append(module)
    for i in unique:
        print(i)


def distanceBetweenPoints(point1, point2):
    print(math.sqrt((point2.getX() - point1.getX())**2 +
          (point2.getY() - point1.getY())**2))


def countCharacter():
    string = input("Enter a string: ")
    characterCount = []
    for ch in string:
        if ch in characterCount:
            index = characterCount.index(ch) + 1
            count = characterCount[index] + 1
            characterCount[index] = count
        else:
            characterCount.append(ch)
            characterCount.append(1)
    for i in range(0, len(characterCount)-1, 2):
        print(f"{characterCount[i+1]} occurrences of '{characterCount[i]}'")


def traceWalk():

    def n():
        numberOfSquares = int(input("Enter number of squares: "))
        return numberOfSquares

    def main(n):
        pavement = [0] * n
        i = n//2
        while i > 0 and i < n:
            chance = random()
            if chance > 0.5:
                i += 1
            else:
                i -= 1
            if i < 0 or i >= n:
                break
            count = pavement[i] + 1
            pavement[i] = count
        print("Square Steps")
        for i in range(0, len(pavement)):
            print(f" {i+1}\t{pavement[i]}")

    main(n())


traceWalk()
