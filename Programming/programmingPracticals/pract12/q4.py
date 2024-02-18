from tkinter import *


class Calculator:

    def __init__(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry("200x200")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10, expand=True)

        self.secondaryFrame = Frame(self.win)
        self.secondaryFrame.pack(expand=True)
        self.buttonFrameRight = Frame(self.secondaryFrame)
        self.buttonFrameRight.pack(side="left", expand=True)

        self.buttonClose = Frame(self.win)
        self.buttonClose.pack(side="bottom", expand=True)

        self.num1 = IntVar()
        self.num2 = IntVar()
        self.result = StringVar()
        self.result.set("Result: 0")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblNum1 = Label(self.mainFrame, text="Number 1:")
        lblNum1.pack()

        entryNum1 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num1
        )
        entryNum1.pack()

        lblNum2 = Label(self.mainFrame, text="Number 2:")
        lblNum2.pack()

        entryNum2 = Entry(
            self.mainFrame,
            width=20,
            textvariable=self.num2
        )
        entryNum2.pack()

        lblResult = Label(
            self.mainFrame,
            textvariable=self.result
        )
        lblResult.pack()

        btnMultiply = Button(
            self.secondaryFrame,
            text="Multiply",
            command=self.multiply
        )
        btnMultiply.pack(padx=15)

        btnAdd = Button(
            self.secondaryFrame,
            text="Addition",
            command=self.add
        )
        btnAdd.pack(padx=13)

        btnSubtract = Button(
            self.buttonFrameRight,
            text="Subtract",
            command=self.subtract
        )
        btnSubtract.pack(padx=10)

        btnDivide = Button(
            self.buttonFrameRight,
            text="Divide",
            command=self.divide
        )
        btnDivide.pack(padx=18)

        btnClose = Button(
            self.buttonClose,
            text="Close",
            command=self.win.destroy
        )
        btnClose.pack(side="right")

    def multiply(self):
        num1 = self.num1.get()
        num2 = self.num2.get()

        result = num1 * num2
        self.result.set(f"Result: {result}")

    def add(self):
        num1 = self.num1.get()
        num2 = self.num2.get()

        result = num1 + num2
        self.result.set(f"Result: {result}")

    def subtract(self):
        num1 = self.num1.get()
        num2 = self.num2.get()

        result = num1 - num2
        self.result.set(f"Result: {result}")

    def divide(self):
        num1 = self.num1.get()
        num2 = self.num2.get()
        try:
            result = num1 / num2
            self.result.set(f"Result: {result}")
        except ZeroDivisionError:
            self.result.set("Result: Cannot divide by zero.")


def main():
    calc = Calculator()
    calc.run()


main()
