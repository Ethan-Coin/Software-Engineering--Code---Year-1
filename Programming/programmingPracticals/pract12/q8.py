# truthTable.py
from tkinter import *


class TruthTable:
    def __init__(self):
        self.window = Tk()
        self.window.title("Truth Table")
        self.window.geometry("400x300")
        self.window.configure(padx=10, pady=10)

        self.answers = [BooleanVar(), BooleanVar(), BooleanVar(), BooleanVar()]
        self.finalResult = StringVar()

        self.window.columnconfigure((0, 1, 2), weight=1)
        self.window.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

    def run(self):
        self.createWidgets()
        self.window.mainloop()

    def createWidgets(self):
        Label(self.window, text="XOR Gate").grid(
            column=0, columnspan=3, row=0, sticky="nwse")

        lblA = Label(
            self.window,
            text="A"
        )
        lblA.grid(column=0, row=1, sticky="nwse")

        lblB = Label(
            self.window,
            text="B"
        )
        lblB.grid(column=1, row=1, sticky="nwse")

        lblResult = Label(
            self.window,
            text="Result"
        )
        lblResult.grid(column=2, row=1)

        for i in range(2, 6):
            textVar = StringVar()
            if i % 2 == 0:
                textVar.set("True")
            else:
                textVar.set("False")
            Label(
                self.window,
                textvariable=textVar
            ).grid(column=0, row=i, sticky="nwse")
            if i >= 3:
                textVar.set("True")
            else:
                textVar.set("False")
            Label(
                self.window,
                textvariable=textVar
            ).grid(column=1, row=i, sticky="nwse")
            entry = Entry(
                self.window,
                textvariable=self.answers[i-2]
            )
            entry.grid(column=2, row=i, sticky="nwse")

        btnSubmit = Button(
            self.window,
            text="Submit",
            command=self.submit
        )
        btnSubmit.grid(column=1, row=6, sticky="nwse")

        self.lblResult = Label(
            self.window,
            textvariable=self.finalResult
        )
        self.lblResult.grid(column=2, row=6, sticky="nwse")

    def submit(self):
        answers = [False, True, True, False]
        count = 0
        result = 0
        for ans in self.answers:
            if ans.get() == answers[count]:
                result += 1
            count += 1
        self.finalResult.set(f"{round((result/len(answers)))*100}%")


def testTruthTable():
    truthTable = TruthTable()
    truthTable.run()


testTruthTable()
