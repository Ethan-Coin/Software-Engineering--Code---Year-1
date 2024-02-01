from graphics import *


class Car:

    def __init__(self, colour, engine):
        self.colour = colour
        self.engine = engine
        self.speed = 0

    def getEngine(self):
        return self.engine

    def getColour(self):
        return self.colour

    def getSpeed(self):
        return self.speed

    def setColour(self, colour):
        if colour in ["red", "green", "blue", "yellow"]:
            self.colour = colour

    def brake(self):
        self.speed = 0

    def accelerate(self):
        if self.speed <= 60:
            self.speed += 10

    def __str__(self):
        output = f"{self.colour} {self.engine} car"
        output += f"travelling at {self.speed} mph"
        return output


def testCar():
    myCar = Car("red", "electric")
    print("My car's engine is", myCar.getEngine())
    print("And it's colour is", myCar.getColour())

    myCar.setColour("blue")
    print("My car's colour is now", myCar.getColour())

    print("My car is going", myCar.getSpeed(), "mph")
    myCar.accelerate()
    print("My car is now going", myCar.getSpeed(), "mph")
    myCar.brake()
    print("After braking, my car's speed is", myCar.getSpeed(), "mph")

    print(myCar)


class MyPoint:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        output = f"MyPoint({self.x}, {self.y})"
        return output


def testMyPoint():
    myPoint = MyPoint(100, 50)
    print("myPoint's x coordinate is", myPoint.getX())  # 100
    print("myPoint's y coordinate is", myPoint.getY())  # 50

    myPoint.move(10, -20)

    print("myPoint's x coordinate is", myPoint.getX())  # 110
    print("myPoint's y coordinate is", myPoint.getY())  # 30

    print("myPoint is:", myPoint)  # myPoint is: MyPoint(110, 30)


def testPoint():
    p = Point(100, 50)

    print("p is of type:", type(p))  # <class 'graphics.Point'>

    print("p's x coordinate is", p.getX())  # 100.0
    print("p's y coordinate is", p.getY())  # 50.0

    p.move(10, -20)

    print("p's x coordinate is", p.getX())  # 110.0
    print("p's y coordinate is", p.getY())  # 30.0

    print("p is:", p)  # p is: Point(110.0, 30.0)


class Square():

    def __init__(self, p1, side):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fillColour = "black"
        self.outlineColour = "black"

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        output = f"Square({self.p1}, {self.p2})"
        return output

    def validColour(self, setColour, colour):
        """"""
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            return colour
        else:
            return setColour

    def setFillColour(self, colour):
        self.fillColour = self.validColour(self.fillColour, colour)

    def setOutlineColour(self, colour):
        self.outlineColour = self.validColour(self.outlineColour, colour)

    def getPerimeter(self):
        return self.side * 4

    def getArea(self):
        return self.side ** 2

    def getCenter(self):
        return MyPoint(self.p1.getX() + self.side/2, self.p1.getY() + self.side/2)

    def scale(self, scaleFactor):
        center = self.getCenter()
        self.side = self.side * scaleFactor
        halfSide = self.side/2
        self.p1 = MyPoint(center.getX() - halfSide, center.getY() - halfSide)
        self.p2 = MyPoint(center.getX() + halfSide, center.getY() + halfSide)


def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print("Changing square's fill colour to red")
    square.setFillColour("red")
    print("square's fill colour is", square.fillColour)  # red
    print("Changing square's fill colour to leopard print!")
    square.setFillColour("leopard print")
    print("square's fill colour is", square.fillColour)  # red

    print("Changing square's outline colour to blue")
    square.setOutlineColour("blue")
    print("square's outline colour is", square.outlineColour)  # blue
    print("Changing square's outline colour to polka dot!")
    square.setOutlineColour("polka dot")
    print("square's outline colour is", square.outlineColour)  # blue

    print("square's perimeter is", square.getPerimeter())  # 200
    print("square's area is", square.getArea())  # 2500
    print("square center is", square.getCenter())  # MyPoint(135.0, 55.0)

    print("Scaling square by a factor of 3")
    square.scale(3)
    print("square's center is", square.getCenter())
    print("square's p1 is", square.getP1())
    print("square's p2 is", square.getP2())


testSquare()


class MyCircle():

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def getCenter(self):
        return self.center

    def getRadius(self):
        return self.radius

    def move(self, dx, dy):
        self.center.move(dx, dy)

    def __str__(self):
        output = f"Circle({self.center}, {self.radius})"
        return output


def test_my_circle():
    p1 = MyPoint(100, 50)
    circle = MyCircle(p1, 50)
    print("circle's center is", circle.getCenter())
    print("circle's radius is", circle.getRadius())

    circle.move(10, -20)
    print("After the move ...")
    print("circle's radius is", circle.getRadius())
    print("circle's center is", circle.getCenter())

    print(circle)


class BankAccount():

    def __init__(self, account_holder, interest):
        self.account_holder = account_holder
        self.balance = 0
        self.interest = interest

    def getAccountHolder(self):
        return self.account_holder

    def getBalance(self):
        return f"£{self.balance:.2f}"

    def getInterest(self):
        return f"{self.interest:.2f}%"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return
        else:
            self.balance -= amount

    def __str__(self):
        return f"Account name: {self.account_holder}\nBalance: £{self.balance}"


def testBankAccount():
    bank_account = BankAccount("Matthew Poole", 3.5)
    print("The name of the account holder is",
          bank_account.getAccountHolder())  # Matthew Poole
    print("The initial balance of the account is",
          bank_account.getBalance())  # 0.00
    print("The interest rate of the bank account is", bank_account.getInterest())

    bank_account.deposit(100)
    print("After depositing £100, the balance is",
          bank_account.getBalance())  # 100.00

    bank_account.withdraw(50)
    print("After withdrawing £50, the balance is",
          bank_account.getBalance())  # 50.00

    bank_account.withdraw(100)
    print("After trying to withdraw £100, the balance is",
          bank_account.getBalance())  # 50.00

    print(bank_account)


class Aeroplane():

    def __init__(self, departure, destination):
        self.fuel = 0
        self.altitude = 0
        self.departure = departure
        self.destination = destination

    def setFuel(self, fuel):
        if fuel > 150000:
            print("Too much fuel, the maximum amount is 150000 litres")
        else:
            self.fuel = fuel

    def increaseAltitude(self):
        self.altitude += 10000

    def decreaseAltitude(self):
        self.altitude -= 10000

    def setDeparture(self, departure):
        self.departure = departure

    def setDestination(self, destination):
        self.destination = destination

    def land(self):
        self.departure = self.destination
        self.destination = ""
        self.altitude = 0

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination

    def getAltitude(self):
        return f"{self.altitude}m"

    def getFuel(self):
        return self.fuel

    def __str__(self):
        return f"Fuel amount: {self.fuel}\nAltitude: {self.altitude}m\nDeparture: {self.departure}\nDestination: {self.destination}"


def testAeroplane():
    departure = input("Enter departure: ")
    destination = input("Enter destination: ")
    airplane = Aeroplane(departure, destination)
    print(airplane)

    while airplane.getFuel() <= 0:
        fuel = int(input("Enter the amount of fuel (litres): "))
        airplane.setFuel(fuel)
    print(airplane)

    airplane.increaseAltitude()
    print(airplane)

    airplane.increaseAltitude()
    print(airplane)

    airplane.decreaseAltitude()
    print(airplane)

    airplane.land()
    print(airplane)


testAeroplane()
