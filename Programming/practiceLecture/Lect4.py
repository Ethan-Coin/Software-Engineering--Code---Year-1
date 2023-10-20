from graphics import *
import random
def seperateText():
    sentence=input("Enter a sentence: ")
    words = []
    words = sentence.split(sep=" ")
    for word in words:
        print(word)

def sentenceOnScreen():
    sentence=input("Enter a sentence: ")
    words = []
    words = sentence.split(sep=" ")
    win=GraphWin("Words On Screen",500,500)
    for _ in range(len(words)):
        point=win.getMouse()
        randomWord=words.pop(random.randint(0,len(words)-1))
        message = Text(point,randomWord)
        message.draw(win)
    win.getMouse()
    win.close()

def CoordsOnScreen():
    win=GraphWin("Coordinates on screen", 500,500)
    for x in range(10,500,100):
        for y in range(10,500,100):
            win.getMouse()
            point=Point(x,y)
            text=Text(point,f"{x}x{y}")
            text.setSize(8)
            text.draw(win)#
    win.getMouse()
    win.close()

win=GraphWin("",500,500)
colours=["blue","red"]
i=0
for x in range(0,500,100):
    for y in range(0,500,100):
        if i>1:
            i=0
        win.getMouse()
        tl=Point(x,y)
        br=Point(x+100,y+100)
        r = Rectangle(tl,br)
        r.setFill(colours[i])
        r.draw(win)
        i+=1

win.getMouse()





        


sentenceOnScreen()