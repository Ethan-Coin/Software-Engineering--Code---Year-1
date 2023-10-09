def biscuitCutting():
    numberOfBiscuits=int(input("Enter number of biscuits to be cut: "))
    radiusOfBiscuit=int(input("Enter radius of the biscuit: "))
    diameter = 2*radiusOfBiscuit
    print(f"The width of the mixture is {diameter} cm.\nThe length of the biscuit is {diameter*numberOfBiscuits} cm.")
biscuitCutting()