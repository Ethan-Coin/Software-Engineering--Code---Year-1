def wc(filename):
    with open(filename, 'r') as f:
        text = f.read()
    numberOfCharacters = len(text)
    listOfWords = text.split()
    numberOfWords = len(listOfWords)
    numberOfLines = text.count('\n')
    return numberOfCharacters, numberOfWords, numberOfLines


def main():
    try:
        filename = input("Enter the name of the file: ")
        chars, words, lines = wc(filename)
        print(f"Characters: {chars}, Words: {words}, Lines: {lines}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")


main()
