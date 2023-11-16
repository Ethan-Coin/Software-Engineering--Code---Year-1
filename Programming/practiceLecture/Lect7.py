from graphics import *
"""
def colourSelector(x,y,width,height):
    colours=["blue","orange","red","green"]
    hWidth=width/2
    hHeight=height/2
    if x < hWidth and y < hHeight:
        return colours[0]
    elif x >= hWidth and y < hHeight:
        return colours[1]
    elif x< hWidth and y >= hHeight:
        return colours[2]
    else:
        return colours[3]
"""
def colourSelector(x,y,width,height):
    colours=["blue","orange","red","green","yellow","black"]
    hWidth=width/3
    hHeight=height/2
    if x< hWidth and y < hHeight:
        return colours[0]
    elif x > hWidth and x < hWidth*2 and y<hHeight:
        return colours[1]
    elif x>hWidth*2 and y<hHeight:
        return colours[2]
    elif x< hWidth and y >= hHeight:
        return colours[3]
    elif x > hWidth and x < hWidth*2 and y>= hHeight:
        return colours[4]
    else:
        return colours[5]
''' 
def drawRectangle(win,x,y,size,colour):
    tl= Point(x,y)
    br=Point(x+size,y+size)
    rectangle=Rectangle(tl,br)
    rectangle.setFill(colour)
    rectangle.draw(win)
    return rectangle
'''
def drawCircle(win,x,y,size,colour):
    centre=Point(x,y)
    circle=Circle(centre,size)
    circle.setFill(colour)
    circle.draw(win)
    return circle

def main():
    width=600
    height=300
    radius=20
    diameter=2*radius
    win=GraphWin("",width,height)
    for rows in range(radius,3*diameter,diameter):
        for columns in range(radius,5*diameter,diameter):
            point=win.getMouse()
            x= point.getX()
            y=point.getY()
            colour = colourSelector(x,y,width,height)
            drawCircle(win,columns,rows,radius,colour)
            #drawRectangle(win,x,y,size,colour)
    win.getMouse()
main()