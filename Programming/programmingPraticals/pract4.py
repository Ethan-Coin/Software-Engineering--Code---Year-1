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
    print(f"{kilos} kilos is equal to {ounces} ounces")

def generateEmail():
    firstName=input("Enter first name: ").lower()
    surname=input("Enter surname: ").lower()
    year=input("Enter year of entry: ")
    print(f"{surname[0:4]}.{firstName[0]}.{year[2:4]}@myport.ac.uk")

def gradeTest():
    mark=input("Enter mark: ")
    mark = mark.replace("10","A")
    mark = mark.replace("9","A")
    mark = mark.replace("8","A")
    mark = mark.replace("7","B")
    mark = mark.replace("6","B")
    mark = mark.replace("5","C")
    mark = mark.replace("4","C")
    mark = mark.replace("3","F")
    mark = mark.replace("2","F")
    mark = mark.replace("1","F")
    mark = mark.replace("0","F")
    print(mark)

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
        pound = euro * 1.17
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
    file = open("quotation.txt", "r")
    for line in file():
        print(line).upper()

fileInCaps()