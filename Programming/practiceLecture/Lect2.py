import math
def areaOfRectangle():
    length = float(input("Enter length: "))
    height = float(input("Enter width: "))
    print(f"The area of the rectangle is {round(length*height)}")

def areaOfRectangleTLBR():
    x1 = float(input("Enter top left x: "))
    y1 = float(input("Enter top left y: "))
    x2 = float(input("Enter bottom right x: "))
    y2 = float(input("Enter bottom right y: "))
    if x2 >= x1:
        length = x2 - x1
    else:
        length = x1 - x2
    if y1 >= y2:
        height = y1 - y2
    else:
        height = y2 - y1
    print(f"The are of the right angle is {length*height:.0f}")

def distanceBetweenPoints():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    dx = x2-x1
    dy = y2-y1
    dxSq = dx*dx
    dySq = dy*dy
    added = dxSq + dySq
    distance = math.sqrt(added)
    print("the distance is ", distance)

distanceBetweenPoints()