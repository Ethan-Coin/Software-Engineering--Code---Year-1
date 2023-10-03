def TaskOne():
    x=int(input("Enter Number: "))+2
    print(x)

def TaskTwo():
    x=int(input("Enter Nummber:"))
    y = 3 * x + 2
    print(y)

def TaskThree():
    x = int(input("Enter NUmber: "))
    i = 0
    sum=0
    while i < x:
        sum += i
        i+=1
    print(sum)

def TaskFour():
    n = int(input("Enter Number: "))
    List=[]
    sum=0
    for i in range(n):
        List.append(n)
    for x in range(len(List)):
        popped=List.pop(0)
        sum+=popped
    print(sum)

TaskOne()

