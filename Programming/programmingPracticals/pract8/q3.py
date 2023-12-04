from random import random
from math import sqrt


def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)


def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def distanceBetweenPoints(x1,x2,y1,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def takeWalks(numWalks, numSteps):
    totalNorth = 0
    totalEast = 0
    for walk in range(numWalks):
        stepsNorth, stepsEast = takeAWalk(numSteps)
        totalNorth = totalNorth + stepsNorth
        totalEast = totalEast + stepsEast
    average = distanceBetweenPoints(0,totalEast/numWalks,0,totalNorth/numWalks)
    return average


def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)


def takeAWalk(numSteps):
    stepsNorth = 0
    stepsEast = 0
    for step in range(numSteps):
        if random() < 0.25:
            stepsNorth = stepsNorth - 1
        elif random() < 0.5:
            stepsNorth = stepsNorth + 1 
        elif random() < 0.75:
            stepsEast = stepsEast - 1
        else:
            stepsEast = stepsEast + 1
    return stepsNorth, stepsEast
