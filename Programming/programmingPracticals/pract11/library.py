class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False

    def returnBook(self):
        if not self.available:
            self.available = True

    def getAvailabilityString(self):
        if self.available:
            return "The book is available to borrow"
        else:
            return "The book is not available to borrow"

    def __str__(self):
        output = f"Book title: {self.title}\nAuthor: {self.author}"
        output += f"\nISBN: {self.isbn}\nAvailable: {self.available}"
        return output


def testBook():
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book.borrow()
    print(book.getAvailabilityString())
    book.returnBook()
    print(book)


class DigitalBook(Book):
    validCompatibilities = ("PDF", "Kindle", "Apple")

    def __init__(self, title, author, isbn, compatibility):
        super().__init__(title, author, isbn)
        self.compatibilities = set()
        if compatibility in self.validCompatibilities:
            self.compatibilities.add(compatibility)

    def borrow(self):
        pass

    def addCompatibility(self, compatibility):
        if compatibility in self.validCompatibilities:
            self.compatibilities.add(compatibility)

    def __str__(self):
        output = f"Book title: {self.title}\nAuthor: {self.author}"
        output += f"\nISBN: {self.isbn}\nAvailable: {self.available}"
        output += f"\nCompatibilities:"
        for i in self.compatibilities:
            output += f"\n- {i}"
        return output


def testDigitalBook():
    digitalBook = DigitalBook("1984", "George Orwell",
                              "978-0451524935", "Kindle")
    digitalBook.borrow()
    print(digitalBook.getAvailabilityString())
    print(digitalBook)
    digitalBook.addCompatibility("PDF")
    print(digitalBook)
    digitalBook.addCompatibility("Android")
    print(digitalBook)


class Library:

    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def __str__(self):
        output = f"Books in Library:"
        for book in self.books:
            output += f"\n - {book.title}\n   - Available: {book.available}"
        return output + "\n"

    def borrowBook(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.borrow()

    def returnBook(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.returnBook()


def testLibrary():
    library = Library()
    print(library)
    library.addBook(
        Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565"))
    print(library)
    library.addBook(Book("1984", "George Orwell", "978-0451524935"))
    print(library)
    library.addBook(DigitalBook("1984", "George Orwell",
                    "978-0451524935", "Kindle"))
    print(library)
    library.borrowBook("978-0743273565")
    library.borrowBook("978-0451524935")
    print(library)
    library.returnBook("978-0743273565")
    library.borrowBook("978-0451524935")
    print(library)


testLibrary()
