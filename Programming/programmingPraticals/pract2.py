import math
def speedCalculator():
    distanceTravelled= int(input("Enter distance travelled in km: "))
    duration = int(input("Enter duration of journey: "))
    print(f"The speed travelled at was {distanceTravelled/duration:.2f} km/h")

def circumferenceOfCircle():
    radius = float(input("Enter radius: "))
    print(f"The circumference of the circle is {2*math.pi*radius:.2f}")

def areaOfCircle():
    radius = float(input("Enter radius: "))
    print(f"The area of the circle is {math.pi*(radius**2):.2f}")

def costOfPizza():
    diameter = float(input("Enter diameter: "))
    area = math.pi*(diameter/2)**2
    costOfIngredients = (area * 3.5) / 100
    print(f"The cost of the pizza is £{costOfIngredients:.2f}")

def slopeOfLine():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    print(f"The slope of the line is {(y2-y1)/(x2-x1)}")

def distanceBetweenPoints():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(f"The distance between two points is {distance}")

def travelStatistics():
    averageSpeed = float(input("Enter average speed: "))
    duration = float(input("Enter duration of the journey: "))
    kilometers = averageSpeed * duration
    print(f"The amount of kilometers travelled was {kilometers} km;\nThe amount of fuel used was {kilometers/5:.1f} litres.")

def sumOfSquares():
    n = int(input("Enter integer: "))
    sum=0
    for i in range(1,n+1):
        sum += i**2
    print("The sum of squares is",sum)

def averageOfNumbers():
    amount=int(input("Enter amount of numbers to enter: "))
    sum=0
    for _ in range(amount):
        num=int(input("Enter number: "))
        sum += num
    print(f"The average is {sum/amount}")

def fibonacci():
    term = int(input("Enter nth term: "))
    n0, n1 = 0, 1
    if term == 0:
        print("The 0 term is 0")
    else:
        for _ in range(term-1):
            nth = n0 + n1
            n0 = n1
            n1= nth
        print(f"The {term} term is {n1}")

def selectCoins():
    pence=int(input("Enter amount of pence: "))
    twoPound, pence = pence // 200, pence % 200
    pound, pence = pence // 100, pence % 100
    fiftyPence, pence = pence // 50, pence % 50
    twentyPence, pence = pence // 20, pence % 20
    tenPence, pence = pence // 10, pence % 10
    fivePence, pence = pence // 5, pence % 5
    twoPence, pence = pence //2, pence % 2
    onePence = pence
    print(f"{twoPound} x £2, {pound} x £1, {fiftyPence} x 50p, {twentyPence} x 20p, {tenPence} x 10p, {fivePence} x 5p, {twoPence} x 2p, {onePence} x 1p")

def selectCoins2():
    pence = int(input("Enter amount of pence: "))
    currency = []
    divisors = [200,100,50,20,10,5,2,1]
    currencies =["£2","£1","50p","20p","10p","5p","2p","1p"]
    for i in range(8):
        currency.append(pence // divisors[i])
        pence = pence % divisors[i]
        print(f"{currency[i]} x {currencies[i]}", end=" ")

x=""
while x.capitalize() != "Q":
    if x == "1":
        speedCalculator()
    elif x == "2":
        circumferenceOfCircle()
    elif x == "3":
        areaOfCircle()
    elif x == "4":
        costOfPizza()
    elif x == "5":
        slopeOfLine()
    elif x == "6":
        distanceBetweenPoints()
    elif x == "7":
        travelStatistics()
    elif x == "8":
        sumOfSquares()
    elif x == "9":
        averageOfNumbers()
    elif x == "10":
        fibonacci()
    elif x == "11":
        selectCoins()
    elif x == "12":
        selectCoins2()
    x = input("\nPlease enter a option: ")