# circleInfoGUI.py
from tkinter import *
import math
from tkinter import ttk


def areaOfCircle(radius):
    return math.pi * radius ** 2


def circumferenceOfCircle(radius):
    return 2*math.pi*radius


class CircleInfo:

    def __init__(self):
        self.win = Tk()
        self.win.title("Circle Information")
        self.win.geometry("175x125")
        self.win.configure(bg="#ababab")

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=10, pady=10, expand=True, fill="both")
        self.mainFrame.configure(bg="#ababab")

        self.buttonsFrame = Frame(self.mainFrame)
        self.buttonsFrame.pack(side="bottom", expand=True)
        self.buttonsFrame.configure(bg="#ababab")

        self.buttonsFrameRight = Frame(self.buttonsFrame)
        self.buttonsFrameRight.pack(side="left", expand=True)
        self.buttonsFrameRight.configure(bg="#ababab")

        self.buttonStyle = ttk.Style()
        self.buttonStyle.configure(
            "TButton",
            background="black",
            font=("Arial", 9),
            relief='flat'
        )
        self.buttonStyle.map("TButton", background=[("active", "#ababab")])

        self.radius = DoubleVar()
        self.areaResult = StringVar()
        self.circumferenceResult = StringVar()
        self.areaResult.set("Area: 0 cm^2")
        self.circumferenceResult.set("Circumference: 0 cm")

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblRadius = Label(
            self.mainFrame,
            text="Radius in cm:",
            bg="#ababab"
        )
        lblRadius.pack(anchor="w")

        entryRadius = Entry(
            self.mainFrame,
            width=10,
            textvariable=self.radius,
            bg="#ababab"
        )
        entryRadius.pack(anchor="w", padx=3)

        lblArea = Label(
            self.mainFrame,
            textvariable=self.areaResult,
            bg="#ababab"
        )
        lblArea.pack(anchor="w")

        lblRadius = Label(
            self.mainFrame,
            textvariable=self.circumferenceResult,
            bg="#ababab"
        )
        lblRadius.pack(anchor="w")

        btnCalculate = ttk.Button(
            self.buttonsFrameRight,
            text="Calculate",
            command=self.calculate
        )
        btnCalculate.pack(padx=5, fill="x")

        btnClose = ttk.Button(
            self.buttonsFrame,
            text="Close",
            command=self.win.destroy
        )
        btnClose.pack(fill="x")

    def calculate(self):
        radius = self.radius.get()
        area = areaOfCircle(radius)
        circumference = circumferenceOfCircle(radius)
        self.areaResult.set(f"Area: {area:.2f} cm^2")
        self.circumferenceResult.set(f"Circumference: {circumference:.2f} cm")


def main():
    app = CircleInfo()
    app.run()


main()
