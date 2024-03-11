def sumList(numbers, count):
    try:
        total = 0
        for i in range(count):
            total += numbers[i]
    except IndexError:
        print("Error: The list does not have that many numbers.")
        return None
    except TypeError:
        print("Error: The list contains non-numeric values.")
        return None
    return total


def getNumber():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: That was not a number.")
        number = getNumber()
    return number


def main():
    numbers = []
    while True:
        print("Enter a non-negative number to add to the list.")
        print("Or enter a negative number to stop.")
        number = getNumber()
        if number >= 0:
            numbers.append(number)
        else:
            break

    while True:
        print("Enter many numbers from the list would you like to sum up.")
        print("Or enter a negative number to stop.")
        count = getNumber()
        if count >= 0:
            total = sumList(numbers, count)
            print(f"The sum of the first {count} numbers is {total}")
        else:
            break


main()
