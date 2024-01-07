from graphics import * 

def drawRectangle(win,p1,p2,colour):
    rectangle = Rectangle(p1,p2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)

def patchOne(win, tlx, tly, colour):
    for i in range(0,100,10):
        drawRectangle(win, Point(tlx + i, tly + 90 - i), Point(tlx+100 , tly+100),colour)

def drawSquare(win,p1,p2,colour):
    rectangle = Rectangle(p1,p2)
    rectangle.setFill(colour)
    rectangle.draw(win)

def patchFive(win,tlx,tly,colour):
    flip=False
    for x in range(0,100,20):
        for y in range(0,100,20):
            col=colour
            flipColour=False
            if y == 20 or y == 60:
                flipColour = not flipColour
            if flip == False:
                for i in range(0,20,5):
                    if col == colour and flipColour:
                        col = "white"
                    else:
                        col = colour
                    drawSquare(win,Point(tlx+x+i,tly+y),Point(tlx+x+i+5,tly+y+20),col)
                    flipColour = not flipColour 
            else:
                for i in range(0,20,5):
                    if col == colour and flipColour:
                        col = "white"
                    else:
                        col = colour
                    drawSquare(win,Point(tlx+x,tly+y+i),Point(tlx+x+20,tly+y+i+5),col)
                    flipColour = not flipColour
            flip = not flip

def drawPatchWork(win,size,colours):
    colour=''
    flip = False
    if size % 200 == 100:
        flip=True
    for x in range(0,size,100):
        for y in range(0,size,100):
            if x == 0 or x == size - 100 or y == size//2 -50:
                colour = colours[0]
                if y % 200 == 0 and x % (size-100) == 0:
                    patchOne(win,x,y,colour)                
                elif x % 200 == 0 and y == size//2-50 and flip ==False: 
                    patchOne(win,x,y,colour)
                elif x % 200 == 100 and flip: 
                    patchOne(win,x,y,colour)
                else:
                    drawRectangle(win,Point(x,y),Point(x+100,y+100),colour) 
            elif y < size // 2 -50:
                colour = colours[1]
                if x % 200 == 100 and y % 200 == 0:
                    patchFive(win,x,y,colour)
                elif x % 200 == 0 and y % 200 == 100:
                    patchFive(win,x,y,colour)
                else:
                    patchOne(win,x,y,colour)
            else:
                colour = colours[2]
                if x % 200 == 100 and y % 200 == 0:
                    patchFive(win,x,y,colour)
                elif x % 200 == 0 and y % 200 == 100:
                    patchFive(win,x,y,colour)
                else:
                    patchOne(win,x,y,colour)
                
def getInputs():
    colours=[]
    while True:
        size = int(input("Enter the size of the window (5,7,9): "))
        if size in [5,7,9]:
            break
        else:
            print("Invalid input, has to be 5,7 or 9.\n")
    for _ in range(3):
        while True:
            colour = input("Enter a colour for the patchwork (red, green, blue, magenta, orange, yellow, cyan): ").lower()
            if colour in ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]:
                colours.append(colour)
                break
            else:
                print(f"{colour.capitalize()} is a invalid colour. Valid colours are blue, orange, red, green, yellow and black.\n")
        print("Colour added successfully\n")
    return size * 100, colours

def main():
    size, colours = getInputs()
    win = GraphWin("Patchwork", size, size)
    win.setBackground("white")
    drawPatchWork(win, size, colours)
    win.getMouse()
    win.close()

main()