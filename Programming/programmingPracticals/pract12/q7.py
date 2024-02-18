# whatTodo.py
from tkinter import *


class WhatTodo:
    def __init__(self):
        self.win = Tk()
        self.win.title("What Todo")
        self.win.geometry("200x100")
        self.win.configure(padx=10, pady=5)

        self.temp = DoubleVar()
        self.whatTodoString = StringVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblEnterTemp = Label(
            self.win,
            text="Enter Temperature"
        )
        lblEnterTemp.pack()

        entryTemp = Entry(
            self.win,
            textvariable=self.temp,
            width=10
        )
        entryTemp.pack()

        btnWhatTodo = Button(
            self.win,
            text="What to do?",
            command=self.whatTodo
        )
        btnWhatTodo.pack(pady=(5, 0))

        lblWhatTodo = Label(
            self.win,
            textvariable=self.whatTodoString
        )
        lblWhatTodo.pack()

    def whatTodo(self):
        temp = self.temp.get()
        if temp > 25:
            self.whatTodoString.set("A swim in the sea")
        elif temp > 10 and temp <= 25:
            self.whatTodoString.set("Shopping in Gunwharf Quays")
        else:
            self.whatTodoString.set("It’s best to watch a film at home")


def testWhatTodo():
    whatTodo = WhatTodo()
    whatTodo.run()


testWhatTodo()
