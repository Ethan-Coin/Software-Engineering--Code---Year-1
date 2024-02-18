from graphics import *

# tlx = top left x, tly = top left y, col = colour


def get_size():
    """User enters a size for the window"""
    valid_sizes = [5, 7, 9]
    while True:
        print("Valid sizes of the patchwork (" + ", ".join(map(str,
              valid_sizes[0:-1])), "or", str(valid_sizes[-1]) + ")")
        size = input("Enter Size: ")
        if size in map(str, valid_sizes):
            break
        else:
            print("Invalid input. valid inputs are " + ", ".join(map(str,
                  valid_sizes[0:-1])), "or", str(valid_sizes[-1]) + ".\n")
    return int(size)


def get_colours():
    """User enters three colours for the patchwork"""
    valid_colours = ["red", "green", "blue",
                     "magenta", "orange", "yellow", "cyan"]
    colours = []
    for _ in range(3):
        while True:
            print("Colours for the patchwork (" + ", ".join(valid_colours)+")")
            colour = input("Enter Colour: ")
            colour = colour.lower()
            if colour in valid_colours or colour in colours:
                colours.append(colour)
                break
            else:
                print(colour.capitalize(), "is a invalid colour. Valid colours are"
                      + ", ".join(valid_colours[0:-1]), "and", valid_colours[-1]+".\n")
        print("Colour added successfully\n")
    return colours


def get_inputs():
    """Retrieves the inputs and multiplies the size by 100"""
    size = get_size()
    colours = get_colours()
    return size * 100, colours


def draw_rectangle(win, p1, p2, colour):
    """Draws a rectangle and sets it to a solid colour"""
    rectangle = Rectangle(p1, p2)
    rectangle.setFill(colour)
    rectangle.setOutline(colour)
    rectangle.draw(win)


def draw_patch_final(win, tlx, tly, col):
    """Draws the final patch design"""
    colour = col
    for i in range(0, 50, 5):
        draw_rectangle(win, Point(tlx+i, tly+i),
                       Point(tlx+100-i, tly+100-i), colour)
        if colour == col:
            colour = "white"
        else:
            colour = col


def draw_circles(win, p1, col):
    """Draws the circles for the penultimate design"""
    for x in range(5, 25, 10):
        for y in range(5, 25, 10):
            circle = Circle(Point(p1.getX()+x, p1.getY()+y), 5)
            circle.setFill(col)
            circle.setOutline(col)
            circle.draw(win)


def draw_patch_penultimate(win, tlx, tly, col):
    """Draws the penultimate patch design"""
    colour = col
    for x in range(0, 100, 20):
        for y in range(0, 100, 20):
            if colour == col:
                draw_rectangle(win, Point(tlx + x, tly + y),
                               Point(tlx+x+20, tly + y+20), colour)
                colour = "white"
            else:
                colour = col
            draw_circles(win, Point(tlx+x, tly+y), colour)


def draw_patchwork(win, size, colours):
    """Draws the patch work design with the other patches"""
    colour = ''
    for x in range(0, size, 100):
        for y in range(0, size, 100):
            if x >= 100 and y >= 100 and x < size - 100 and y < size - 100:
                colour = colours[2]
                if x == y:
                    draw_patch_final(win, x, y, colour)
                elif y % 200 == 0:
                    draw_patch_penultimate(win, x, y, colour)
                else:
                    draw_rectangle(win, Point(x, y),
                                   Point(x+100, y+100), colour)
            elif y % 200 == 0:
                if x % 200:
                    colour = colours[1]
                else:
                    colour = colours[0]
                if y == x:
                    draw_patch_final(win, x, y, colour)
                else:
                    draw_patch_penultimate(win, x, y, colour)
            else:
                colour = colours[1]
                draw_rectangle(win, Point(x, y), Point(x+100, y+100), colour)


def main():
    """main function to execute the code"""
    size, colours = get_inputs()
    win = GraphWin("Patchwork", size, size)
    win.setBackground("white")
    draw_patchwork(win, size, colours)
    win.getMouse()
    win.close()


main()
