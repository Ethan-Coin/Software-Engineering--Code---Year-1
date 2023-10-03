def sayName():
    print("Ethan Schultz")

def sayHello2():
    print("Hello")
    print("World")

def dollars2Pounds():
    dollars = float(input("Enter a value in dollars: "))
    pounds = dollars * 0.80
    print(f"The value in pounds is £{pounds:.2f}")

def tenHellos():
    for _ in range(10):
        print("Hello World")

def railFareIncrease():
    print("The current price for a ticket from Southampton to Portsmouth is £16.50")
    price = 16.50
    for i in range(11):
        price = price * 1.02
    print(f"The price in 11 months is £{price:.2f}")

def countTo():
    num = int(input("Enter number to count to: "))
    for i in range(1, num+1):
        print(i, end=' ')
    
def countFromTo():
    startCount = int(input("Enter number to start from: "))
    endCount = int(input("Enter number to count to: "))
    x = startCount
    for i in range(startCount, endCount+1):
        print(x, end=' ')
        x+=1

def changeCounter():
    onePence = int(input("Enter amount of 1p's: "))
    twoPence = int(input("Enter amount of 2p's: "))
    fivePence = int(input("Enter amount of 5p's: "))
    print(f"You have {onePence + (twoPence * 2) + (fivePence * 5)}p")

def weightsTable():
    print("Kgs | Ounces\n=============")
    for i in range(10,60,10):
        ounces = i * 35.274
        print(f"{i} | {ounces}")

def futureRailFare():
    fare = float(input("Enter inital rail fare price: "))
    months = int(input("Enter number of months: "))
    for i in range(months):
        fare = fare * 1.02
    print(f"The cost of this ticket will be £{fare:.2f}")

x=""
while x.capitalize() != "Q":
    if x == "1":
        sayName()
    elif x == "2":
        sayHello2()
    elif x == "3":
        dollars2Pounds()
    elif x == "4":
        tenHellos()
    elif x == "5":
        railFareIncrease()
    elif x == "6":
        countTo()
    elif x == "7":
        countFromTo()
    elif x == "8":
        changeCounter()
    elif x == "9":
        weightsTable()
    elif x == "10":
        futureRailFare()
    x = input("\nPlease enter a option: ")