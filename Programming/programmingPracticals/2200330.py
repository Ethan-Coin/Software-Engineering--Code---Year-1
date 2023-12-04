from graphics import *

#tlx = top left x, tly = top left y, col = colour
def getInputs():
    validSizes = [5, 7, 9]
    validColours = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    colours = []
    while True:
        size = int(input("Enter the size of the patchwork (" + ", ".join(map(str,validSizes[0:-1])) + f" or {str(validSizes[-1])}): "))
        if size in validSizes:
            break
        else:
            print("Invalid input. valid inputs are 5, 7 or 9.")
    for _ in range(3):
        while True:
            colour = input("Enter a colour for the patchwork (" + ", ".join(validColours) + "): ").lower()
            if colour in validColours:
                colours.append(colour)
                break
            else:
                print(f"{colour.capitalize()} is a invalid colour. Valid colours are "+", ".join(validColours[0:-1]) + f"and {validColours[-1]}.\n")
        print("Colour added successfully\n")
    return size * 100, colours

def drawRectangle(win, p1, p2, colour):
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)
    return rectangle

def drawPatchFinal(win, tlx, tly, col):
    colour = col
    for i in range(0,50,5):
        drawRectangle(win,Point(tlx+i,tly+i),Point(tlx+100-i,tly+100-i),colour)
        if colour == col:
            colour = "white"
        else:
            colour = col

def drawCircles(win, p1, col):
    for x in range(5, 25, 10):
        for y in range(5, 25, 10):
            circle = Circle(Point(p1.getX()+x,p1.getY()+y),5)
            circle.setFill(col)
            circle.setOutline(col)
            circle.draw(win)

def drawPatchPenultimate(win, tlx, tly, col):
    colour = col
    for x in range(0, 100, 20):
        for y in range(0, 100, 20):
            if colour == col:
                drawRectangle(win, Point(tlx + x, tly + y), Point(tlx+x+20, tly + y+20), colour)
                colour = "white"
            else:
                colour = col
            drawCircles(win, Point(tlx+x,tly+y), colour)
    
def drawPatchwork(win,size,colours):
    colour=''
    for x in range(0, size + 100, 100):
        for y in range(0, size + 100, 100):
            if x >= 100 and y >= 100 and x < size - 100 and y < size - 100 :
                colour = colours[2]
                if x == y:
                    drawPatchFinal(win, x, y, colour)
                elif y % 200 == 0:
                    drawPatchPenultimate(win, x, y, colour)
                else:
                    drawRectangle(win,Point(x,y),Point(x+100,y+100),colour)
            elif y % 200 == 0:
                if x % 200:
                    colour = colours[1]
                else:
                    colour = colours[0]
                if y == x:
                    drawPatchFinal(win, x, y, colour)
                else:
                    drawPatchPenultimate(win, x, y, colour)
            else:
                colour = colours[1]
                drawRectangle(win,Point(x,y),Point(x+100,y+100),colour)

def main():
    size, colours = getInputs()
    win=GraphWin("Patchwork",size,size)
    drawPatchwork(win,size,colours)
    win.getMouse()
    win.close()

main()