# temperature converter
from tkinter import *
from tkinter import ttk


class TemperatureConverter:
    def __init__(self):
        self.win = Tk()
        self.win.title("Temperature Converter")
        self.win.geometry("275x75")
        self.win.configure(padx=10, pady=10)
        self.win.columnconfigure(0, weight=1)
        self.win.columnconfigure(1, weight=1)
        self.win.rowconfigure(0, weight=1)
        self.win.rowconfigure(1, weight=1)
        self.win.rowconfigure(2, weight=1)

        self.celsius = DoubleVar()
        self.fahrenheit = DoubleVar()

    def run(self):
        self.createWidgets()
        self.win.mainloop()

    def createWidgets(self):
        lblCelsius = Label(
            self.win,
            text="Celsius"
        )
        lblCelsius.grid(column=0, row=0, sticky="w")

        lblFahrenheit = Label(
            self.win,
            text="Fahrenheit"
        )
        lblFahrenheit.grid(column=1, row=0, sticky="w")

        entryCelsius = Entry(
            self.win,
            width=10,
            textvariable=self.celsius
        )
        entryCelsius.grid(column=0, row=1, sticky="w")

        entryFahrenheit = Entry(
            self.win,
            width=10,
            textvariable=self.fahrenheit
        )
        entryFahrenheit.grid(column=1, row=1, sticky="w")

        btnCel2Farh = ttk.Button(
            self.win,
            text="Convert to Fahrenheit",
            command=self.celsius2Fahrenheit
        )
        btnCel2Farh.grid(column=0, row=2, sticky="w")

        btnFarh2Cel = Button(
            self.win,
            text="Convert to Celsius",
            command=self.fahrenheit2Celsius
        )
        btnFarh2Cel.grid(column=1, row=2, sticky="w")

    def fahrenheit2Celsius(self):
        fahrenheit = self.fahrenheit.get()
        self.celsius.set(round(((fahrenheit - 32) * 5 / 9), 2))

    def celsius2Fahrenheit(self):
        celsius = self.celsius.get()
        self.fahrenheit.set(round((9 / 5 * celsius + 32), 2))


def testTemperatureConverter():
    temperatureConverter = TemperatureConverter()
    temperatureConverter.run()


testTemperatureConverter()
