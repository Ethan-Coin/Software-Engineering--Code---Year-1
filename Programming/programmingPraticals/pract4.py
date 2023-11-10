from graphics import *

def personalGreeting():
    userName=input("Enter your name: ")
    print(f"Hello {userName}, nice to see you!")

def formalName():
    userGivenName=input("Enter your given name: ")
    userFamilyName=input("Enter your family name: ")
    print(f"{userGivenName[0].upper()}. {userFamilyName.capitalize()}")

def kilo2Ounces():
    kilos=float(input("Enter amount of kilos to convert to ounces: "))
    ounces= kilos*35.274
    print(f"{kilos:.2f} kilos is equal to {ounces:.2f} ounces")

def generateEmail():
    firstName=input("Enter first name: ").lower()
    surname=input("Enter surname: ").lower()
    year=input("Enter year of entry: ")
    print(f"{surname[0:4]}.{firstName[0]}.{year[2:4]}@myport.ac.uk")

def gradeTest():
    mark=int(input("Enter mark: "))
    gradeList="FFFFCCBBAAA"
    print(gradeList[mark])

def graphicLetters():
    word=input("Enter a word: ")
    win=GraphWin("",500,500)
    for ch in word:
        p1=win.getMouse()
        text=Text(p1,ch)
        text.setSize(36)
        text.draw(win)
    win.getMouse()
    win.close()

def singASong():
    songWord=input("Enter a word to sing: ")
    lines=int(input("Enter how many lines to repeat: "))
    repeat=int(input("Enter how many times for the word to repeat: "))
    for _ in range(lines):
        print("\n",end="")
        for _ in range(repeat):
            print(songWord,end=" ")

def exchangeTable():
    print(f"   Euros   |   Pounds")
    for euro in range(0,21):
        pound = euro / 1.17
        print(f"{euro:>10.2f} | {pound:.2f}")

def makeInitialism():
    phrase=input("Enter a phrase: ")
    words=[]
    words = phrase.split(" ")
    for word in words:
        print(word[0].upper(),end="")

def nameToNumber():
    name=input("Enter your name: ").lower()
    sum=0
    for ch in name:
        sum+=ord(ch)-96
    print(f"The name {name} has a numerical value of {sum}")

def fileInCaps():
    filename=input("Enter file name: ")+".txt"
    file = open(filename, "r")
    content = file.read()
    print(content.upper())

def totalSpending():
    file = open("spending.txt", "r")
    sum=0
    for line in file:
        sum+=float(line)
    print(f"The total spent this week was £{sum}")

def rainfallChart():
    file = open("rainfall.txt", "r")
    for line in file:
        words=[]
        words= line.split(" ")
        numberOfAsterisks = int(words[1])
        print(words[0], "*" * numberOfAsterisks)

def graphicalRainfallChart():
    file = open("rainfall.txt", "r")
    win = GraphWin("Rainfall Chart", 500, 500)
    win.setCoords(0,0,1,1)
    y=0.9
    for line in file:
        words=[]
        words= line.split(" ")
        numberOfAsterisks = int(words[1])
        place = Text(Point(0.1,y),words[0])
        place.setSize(12)
        place.draw(win)
        x=0.22
        for _ in range(numberOfAsterisks):
            rectangle=Rectangle(Point(x,y+0.01),Point(x+0.01,y-0.01))
            rectangle.setFill("blue")
            rectangle.draw(win)
            x+=0.015
        y-=0.1
    win.getMouse()
    win.close()

def rainfallInInches():
    file = open("rainfall.txt", "r")
    for line in file:
        words=[]
        words= line.split(" ")
        rainfallMM = int(words[-1])
        rainfallInches = rainfallMM / 25.4
        print(f"{words[0]} {rainfallInches:.2f}")

def wc():
    filename = input("Enter the file name: ")+".txt"
    file = open(filename, "r")
    chars=0
    words=0
    lines=0
    for line in file:
        line = line.strip(" \n")
        for _ in line:
            chars+=1
        wordList=[]
        wordList=line.split(" ")
        words+=len(wordList)
        print(wordList)
        lines+=1
    print(f"Characters = {chars} Words = {words} Lines = {lines}")
