from tkinter import *

win = Tk()
win.geometry('300x100')
selectedOption = StringVar(win)
selectedOption.set("Option 1")
optionMenu = OptionMenu(
    win,
    selectedOption,
    "Option 1",
    "Option 2",
    "Option 3",
    command=lambda _: print(selectedOption.get())
)
optionMenu.pack()
win.mainloop()
