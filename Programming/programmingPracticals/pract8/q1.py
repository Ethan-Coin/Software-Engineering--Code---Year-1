import random

#Exercise 1 
def getInputs():
    numberOfFlips=int(input("Enter the number of times for the coin to be flips: "))
    return numberOfFlips

def simulateFlips(numberOfFlips):
    heads = 0 
    tails = 0
    for _ in range (numberOfFlips):
        randomNumber=random.randint(0,1)
        if randomNumber == 0:
            heads+=1
        else:
            tails+=1
    heads=heads/numberOfFlips
    tails=tails/numberOfFlips
    return abs(heads),abs(tails)

def displayResults(heads,tails):
    print(f"Heads {heads} Tails {tails}")

def main():
    numberOfFlips=getInputs()
    heads,tails=simulateFlips(numberOfFlips)
    displayResults(heads,tails)

main()