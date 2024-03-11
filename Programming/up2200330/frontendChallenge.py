from tkinter import *
from tkinter import colorchooser as tkColorChooser, filedialog as tkFileDialog
from backendChallenge import SmartHome, SmartLight, SmartPlug
import os


def setUpHome():  # Function to create a new Smart Home
    def newSmartHome():  # Function to create a new Smart Home
        for _ in range(5):
            error = "\nInvalid Option please enter a valid option\n"
            while True:
                device = input(
                    "Enter a device to add (Smart Plug [1] or Smart Light [2]): ")
                device = device.lower().replace(" ", "")
                if device in ["smartplug", "1", "smartlight", "2"]:
                    if device in ["smartplug", "1"]:
                        while True:
                            consumption = input(
                                "Enter consumption rate (0-150): ")
                            if consumption.isdigit():
                                consumption = int(consumption)
                                if 0 <= consumption <= 150:
                                    break  # Checks if the consumption rate is between 0 and 150
                                else:
                                    print(error)
                            else:
                                print(error)
                        smartHome.addDevice(SmartPlug(consumption))
                        break
                    else:
                        smartHome.addDevice(SmartLight())
                        break
                else:
                    print(error)

    smartHome = SmartHome()  # Creates a new Smart Home
    savedSmartHome = input("Do you want to load a saved Smart Home? (Y/N): ")
    if savedSmartHome[0].lower() == "y":
        win = Tk()
        win.geometry("0x0")  # Hides the window
        types = [("CSV Files", "*.csv"), ("Text Files", "*.txt")]
        filename = tkFileDialog.askopenfile(
            title="Open File",
            filetypes=types,
            defaultextension=types[0][1]
        )  # Opens a file dialog to select a file
        if filename is not None:  # If a file is selected it will load the Smart Home
            data = filename.read()
            filename.close()
            devices = data.split("\n")
            for device in devices:
                deviceAttributes = device.split(",")
                if deviceAttributes[0] == "Plug":
                    smartHome.addDevice(SmartPlug(int(deviceAttributes[2])))
                elif deviceAttributes[0] == "Light":
                    smartHome.addDevice(SmartLight())
                    smartHome.getDeviceAt(-1).setBrightness(
                        int(deviceAttributes[2]))
                try:  # Checks if the device is switched on and switches it on if it is
                    if deviceAttributes[1] == "True":
                        smartHome.toggleSwitch(-1)
                except:  # The last line of the file is empty so it will raise an error
                    pass
            win.destroy()
        else:
            win.destroy()  # Closes the window if no file is selected
            newSmartHome()  # Makes the user create a new Smart Home
    else:
        newSmartHome()
    return smartHome


class SmartHomeSystem:

    def __init__(self, smartHome):
        self.smartHome = smartHome

        # Main Window Configuration
        self.win = Tk()
        self.win.title("Smart Home System")
        self.win.attributes('-topmost', True)
        self.width = 550
        self.height = 175
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)

        # Variables for the Smart Home System
        self.font = ("TkDefaultFont", 11)  # Font for widgets
        self.bgColour = "white"  # Background Colour
        self.btnBGColour = "SystemButtonFace"  # Button Background Colour
        self.textColour = "black"  # Text Colour
        self.theme = "Light"  # Theme
        self.optionVars = []  # List for the option variables
        self.time = IntVar()
        self.clock = StringVar(value="Clock: 00:00")
        self.onTimes = []
        self.offTimes = []

        self.win.configure(bg=self.bgColour)

        # Main Frame for widgets
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column=0, row=0, sticky="nwse", padx=5, pady=5)
        self.mainFrame.configure(bg=self.bgColour)
        self.mainFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.mainFrame.rowconfigure((0, 1, 3), weight=1)
        # Keeps the other widgets smaller
        self.mainFrame.rowconfigure(2, weight=40)

        # Lists for widgets
        self.deviceWidgets = []
        self.smartHomeWidgets = []

        # Frame for devices
        self.deviceFrame = Frame(self.mainFrame)
        self.deviceFrame.grid(column=0, row=2, columnspan=5, sticky="nwse")
        self.deviceFrame.configure(bg=self.bgColour)
        self.deviceFrame.columnconfigure(0, weight=3)
        self.deviceFrame.columnconfigure((1, 2, 3, 4, 5), weight=1)

    def run(self):  # Function to run the Smart Home System
        self.createMainWidgets()
        self.createDeviceWidgets()
        # Allows the other windows to be on top
        self.win.after(100, self.disableTopMost)
        self.win.mainloop()

    def createMainWidgets(self):  # Function to create the main widgets
        self.delAllSmartHomeWidgets()
        lblTitle = Label(
            self.mainFrame,
            text="Smart Home System",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblTitle.grid(column=0, row=0, columnspan=3, sticky="nwse")

        lblClock = Label(
            self.mainFrame,
            textvariable=self.clock,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblClock.grid(column=3, row=0, columnspan=2, sticky="nwse")
        # Updates the clock every 3 seconds
        self.win.after(3000, self.updateClock)

        btnTurnAllOn = Button(
            self.mainFrame,
            text="Turn all on",
            command=self.turnAllOn,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnTurnAllOn.grid(column=0, row=1, columnspan=2,
                          sticky="nwse", pady=5)
        self.smartHomeWidgets.append(btnTurnAllOn)

        btnTurnAllOff = Button(
            self.mainFrame,
            text="Turn all off",
            command=self.turnAllOff,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnTurnAllOff.grid(column=2, row=1, columnspan=2,
                           sticky="nwse", pady=5, padx=5)
        self.smartHomeWidgets.append(btnTurnAllOff)

        btnClose = Button(
            self.mainFrame,
            text="Close",
            command=self.close,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnClose.grid(column=4, row=1, columnspan=2,
                      sticky="nwse", pady=5, padx=5)

        btnAdd = Button(
            self.mainFrame,
            text="Add Device",
            command=self.addDevice,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnAdd.grid(column=0, row=3, columnspan=2,
                    sticky="nwse", pady=5)
        self.smartHomeWidgets.append(btnAdd)

        btnAccessibility = Button(
            self.mainFrame,
            text="Interface & Accessibility",
            command=self.Accessibility,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnAccessibility.grid(
            column=3, row=3, columnspan=2, sticky="nwse", pady=5)
        self.smartHomeWidgets.append(btnAccessibility)

    def createDeviceWidgets(self):  # Function to create the device widgets
        self.delAllDeviceWidgets()  # Clears all device widgets
        numDevices = len(self.smartHome.getDevices())
        # Images for the devices
        img1FileName = "images/image1.png"
        img2FileName = "images/image2.png"
        # Gets the full path of the images (fixes issues if another directory is used)
        scriptDir = os.path.dirname(__file__)
        img1FullPath = os.path.join(scriptDir, img1FileName)
        img2FullPath = os.path.join(scriptDir, img2FileName)
        # Subsamples the images to make them smaller
        img1 = PhotoImage(file=img1FullPath).subsample(10, 10)
        img2 = PhotoImage(file=img2FullPath).subsample(13, 13)
        self.optionVars = []  # Clears the optionVars list

        for i in range(numDevices):
            # Dynamically adds rows and increases the height of the window
            self.deviceFrame.rowconfigure(i, weight=1)
            self.height += 30
            device = self.smartHome.getDeviceAt(i)
            # Returns a string with the device's information
            deviceText = self.deviceText(device)
            # Creates a new entry in the optionVars list for the device extra option
            # (consumption rate or brightness)
            self.optionVars.append(IntVar())

            if isinstance(device, SmartPlug):  # Sets the initial values of the device
                self.optionVars[i].set(device.getConsumptionRate())
                img = img2
                limit = 150
            else:
                self.optionVars[i].set(device.getBrightness())
                img = img1
                limit = 100

            lblDevice = Label(
                self.deviceFrame,
                text=deviceText,
                anchor="w",
                width=9,
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            lblDevice.grid(row=i, column=0, columnspan=2,
                           sticky="nwse", padx=(30, 0))
            self.deviceWidgets.append(lblDevice)

            lblDeviceImg = Label(
                self.deviceFrame,
                bg=self.bgColour,
                image=img,
                width=28
            )
            lblDeviceImg.image = img
            lblDeviceImg.grid(row=i, column=0, sticky="w")
            self.deviceWidgets.append(lblDeviceImg)

            lblToggle = Label(
                self.deviceFrame,
                text="Toggle:",
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            lblToggle.grid(row=i, column=2, sticky="w")
            self.deviceWidgets.append(lblToggle)

            checkToggle = Checkbutton(
                self.deviceFrame,
                command=lambda index=i: self.toggleDevice(index),
                bg=self.bgColour,
            )
            if device.getSwitchedOn():
                checkToggle.toggle()  # Toggles the checkbutton if the device is on
            checkToggle.grid(row=i, column=2, sticky="e")
            self.deviceWidgets.append(checkToggle)

            spinOption = Spinbox(
                self.deviceFrame,
                from_=0,
                to=limit,
                textvariable=self.optionVars[i],
                command=lambda index=i: self.setOption(index),
                width=4,
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            spinOption.grid(row=i, column=3)
            self.deviceWidgets.append(spinOption)

            btnEdit = Button(
                self.deviceFrame,
                text="Edit",
                command=lambda index=i: self.editDevice(index),
                width=1,
                bg=self.btnBGColour,
                fg=self.textColour,
                font=self.font
            )
            btnEdit.grid(row=i, column=4, sticky="nwse", pady=5, padx=5)
            self.deviceWidgets.append(btnEdit)

            btnDelete = Button(
                self.deviceFrame,
                text="Delete",
                command=lambda index=i: self.removeDevice(index),
                width=4,
                bg=self.btnBGColour,
                fg=self.textColour,
                font=self.font
            )
            btnDelete.grid(row=i, column=5, sticky="nwse", pady=5, padx=5)
            self.deviceWidgets.append(btnDelete)
        # Resizes the window to fit the new widgets, centers it and makes it unresizable
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))
        self.win.minsize(self.width, self.height)
        self.win.maxsize(self.width, self.height)
        self.height = 175

    def addDevice(self):
        win = Toplevel()
        win.title("Add Device")
        height = 150
        width = 250
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        win.minsize(width, height)
        win.maxsize(width, height)
        win.configure(bg=self.bgColour, padx=5, pady=5)
        win.columnconfigure((0, 1), weight=1)
        win.rowconfigure((0, 1, 2, 3), weight=1)

        # Variables for the add device window
        # Sets initial value to Smart Plug for the radio buttons
        device = IntVar(value=1)
        consumptionStr = StringVar()
        errorMsg = StringVar()

        lblMsg = Label(
            win,
            text="Add a Device",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblMsg.grid(column=0, row=0, columnspan=2, sticky="nwse")

        radioPlug = Radiobutton(
            win,
            text="Smart Plug",
            variable=device,
            value=1,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        radioPlug.grid(column=0, row=1, sticky="w")

        spinPlug = Spinbox(
            win,
            from_=0, to=150,
            textvariable=consumptionStr,
            bg=self.bgColour, fg=self.textColour,
            font=self.font,
            width=4
        )
        spinPlug.grid(column=1, row=1)

        radioLight = Radiobutton(
            win,
            text="Smart Light",
            variable=device,
            value=2,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        radioLight.grid(column=0, row=2, sticky="w")

        def addDevice():  # Adds the device to the Smart Home
            def error():
                msgError.destroy()
            msgError = Message(
                win,
                textvariable=errorMsg,
                bg="red",
                justify="center",
                width=210,
                font=self.font
            )
            if device.get() == 1:  # checks if the device is a Smart Plug (1 is Smart Plug)
                if consumptionStr.get().isdigit():
                    consumption = int(consumptionStr.get())
                    if 0 <= consumption <= 150:
                        self.smartHome.addDevice(SmartPlug(consumption))
                        win.destroy()
                        self.createDeviceWidgets()
                    else:
                        errorMsg.set(
                            "Error Consumption Rate must be between 0 to 150")
                        msgError.grid(column=0, row=0, sticky="nwse",
                                      padx=20, pady=50)
                        lblMsg.after(2000, error)
                else:
                    errorMsg.set("Error Consumption Rate must be an integer")
                    msgError.grid(column=0, row=0, sticky="nwse",
                                  padx=20, pady=50)
                    lblMsg.after(2000, error)
            else:
                self.smartHome.addDevice(SmartLight())
                win.destroy()
                self.createDeviceWidgets()

        btnAddDevice = Button(
            win,
            text="Add",
            command=addDevice,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnAddDevice.grid(column=0, row=3, columnspan=2,
                          sticky="nwse", padx=30, pady=5)

    def editDevice(self, index):  # Function to edit a device
        win = Toplevel()
        win.title("Edit Device")
        height = 225
        width = 250
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        win.minsize(width, height)
        win.maxsize(width, height)
        win.configure(bg=self.bgColour, padx=5, pady=5)
        win.columnconfigure((0, 1, 2, 3), weight=1)
        win.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        # Variables for the edit device window
        device = self.smartHome.getDeviceAt(index)
        errorMsg = StringVar()
        optionVar = StringVar()

        if isinstance(device, SmartPlug):  # Sets the initial value of the optionVar
            optionVar.set(device.getConsumptionRate())
            deviceName = "Smart Plug"
            option = "Consumption:"
            limit = 150
        else:
            optionVar.set(device.getBrightness())
            deviceName = "Smart Light"
            option = "Brightness:"
            limit = 100

        switchedOn = BooleanVar(value=device.getSwitchedOn())

        lblSmartDevice = Label(
            win,
            text=deviceName,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblSmartDevice.grid(column=0, row=0, columnspan=4, sticky="nwse")

        lblProperty = Label(
            win,
            text="Property",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblProperty.grid(column=0, row=1, columnspan=2)

        lblValue = Label(
            win,
            text="Value",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblValue.grid(column=2, row=1, columnspan=2)

        lblSwitchedOn = Label(
            win,
            text="Switched On:",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblSwitchedOn.grid(column=0, row=2, columnspan=2)

        def switchText():  # Changes the text of the switchedOnText
            if switchedOn.get():
                text = "On"
            else:
                text = "Off"
            switchedOnText.set(text)

        checkSwitchedOn = Checkbutton(
            win,
            variable=switchedOn,
            onvalue=True,
            offvalue=False,
            bg=self.bgColour,
            command=switchText
        )
        checkSwitchedOn.grid(column=2, row=2, sticky="e")

        switchedOnText = StringVar()
        switchText()  # Sets the initial value of the switchedOnText

        lblSwitchedOnValue = Label(
            win,
            textvariable=switchedOnText,
            width=2,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblSwitchedOnValue.grid(column=3, row=2, sticky="w")

        lblOption = Label(
            win,
            text=option,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblOption.grid(column=0, row=3, columnspan=2)

        spinOption = Spinbox(
            win,
            from_=0,
            to=limit,
            textvariable=optionVar,
            width=1,
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        spinOption.grid(column=2, row=3, columnspan=2, sticky="nwse")

        lblScheldule = Label(
            win,
            text="Schedule this device:",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblScheldule.grid(column=0, row=4, columnspan=3, sticky="nwse")

        # Variables for schedule
        scheduleWidgets = []
        onTime = IntVar()
        offTime = IntVar()
        scheduleOn = BooleanVar()

        def scheduleDevice(scheduleWidgets):
            lblOn = Label(
                win,
                text="On:",
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            scheduleWidgets.append(lblOn)

            lblOff = Label(
                win,
                text="Off:",
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            scheduleWidgets.append(lblOff)

            spinOn = Spinbox(
                win,
                textvariable=onTime,
                from_=0,
                to=24,
                increment=3,
                width=3,
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            scheduleWidgets.append(spinOn)

            spinOff = Spinbox(
                win,
                textvariable=offTime,
                from_=0,
                to=24,
                increment=3,
                width=3,
                bg=self.bgColour,
                fg=self.textColour,
                font=self.font
            )
            scheduleWidgets.append(spinOff)

            if scheduleOn.get():  # If the schedule is on it will display the schedule widgets
                lblOn.grid(column=0, row=5, columnspan=2, sticky="nwse")
                spinOn.grid(column=0, row=6, columnspan=2)
                lblOff.grid(column=2, row=5, columnspan=2, sticky="nwse")
                spinOff.grid(column=2, row=6, columnspan=2)
            else:
                for widget in scheduleWidgets:
                    widget.destroy()
                for time in self.onTimes:
                    if index in time:
                        self.onTimes.remove(time)
                for time in self.offTimes:
                    if index in time:
                        self.offTimes.remove(time)
                scheduleWidgets = []

        for time in self.onTimes:  # Checks if the device has a schedule and sets the times
            if index in time:
                onTime.set(time[index])
                for i in self.offTimes:
                    if index in i:
                        offTime.set(i[index])
                scheduleOn.set(True)
                scheduleDevice(scheduleWidgets)

        checkSchedule = Checkbutton(
            win,
            bg=self.bgColour,
            onvalue=True,
            offvalue=False,
            variable=scheduleOn,
            command=lambda: scheduleDevice(scheduleWidgets)
        )
        checkSchedule.grid(column=3, row=4, sticky="w")

        def confirm():  # Confirms the changes and updates the main window
            def error():
                msgError.destroy()
            msgError = Message(
                win,
                textvariable=errorMsg,
                bg="red",
                justify="center",
                width=210,
                font=self.font
            )
            if scheduleOn.get():  # If the schedule is on it will add the times to the list
                for time in self.onTimes:  # Removes the old times if they exist
                    if index in time:
                        self.onTimes.remove(time)
                for time in self.offTimes:
                    if index in time:
                        self.offTimes.remove(time)
                self.onTimes.append({index: int(onTime.get())})
                self.offTimes.append({index: int(offTime.get())})
            if optionVar.get().isdigit():  # Checks if the option is an integer
                intOptionVar = int(optionVar.get())
                if switchedOn.get() != device.getSwitchedOn():
                    device.toggleSwitch()
                if isinstance(device, SmartPlug):
                    if 0 <= intOptionVar <= 150:
                        device.setConsumptionRate(intOptionVar)
                        win.destroy()
                        self.createDeviceWidgets()
                    else:
                        errorMsg.set(
                            "Error Consumption Rate should be between 0 and 150")
                        msgError.grid(column=0, row=0,
                                      sticky="nwse", padx=20, pady=50)
                        msgError.after(2000, error)
                else:
                    if 0 <= intOptionVar <= 100:
                        device.setBrightness(intOptionVar)
                        win.destroy()
                        self.createDeviceWidgets()
                    else:
                        errorMsg.set(
                            "Error Brightness should be between 0 and 100")
                        msgError.grid(column=0, row=0,
                                      sticky="nwse", padx=20, pady=50)
                        msgError.after(2000, error)
            else:
                errorMsg.set("Error value should be an integer")
                msgError.grid(column=0, row=0, sticky="nwse", padx=20, pady=50)
                msgError.after(2000, error)

        btnConfirm = Button(
            win,
            text="Confirm",
            command=confirm,
            width=1,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnConfirm.grid(column=0, row=7, columnspan=4,
                        sticky="nwse", padx=10, pady=10)

    def Accessibility(self):
        win = Toplevel()
        win.title("Interface & Accessibility settings")
        win.configure(bg=self.bgColour, padx=5, pady=5)
        height = 200
        width = 250
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        win.minsize(width, height)
        win.maxsize(width, height)
        win.columnconfigure((0, 1, 2, 3), weight=1)
        win.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # Variables for Accessibility settings
        customWidgets = []
        selectedText = StringVar()
        selectedTheme = StringVar()

        # Sets the initial values of the option menus
        if self.font[1] == 9:
            selectedText.set("Small")
        elif self.font[1] == 13:
            selectedText.set("Large")
        else:
            selectedText.set("Regular")

        if self.theme == "Light":
            selectedTheme.set("Light")
        elif self.theme == "Dark":
            selectedTheme.set("Dark")
        else:
            selectedTheme.set("Custom")

        lblTitle = Label(
            win,
            text="Accessibility",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblTitle.grid(column=0, row=0, columnspan=4, sticky="nwse")

        lblTextSize = Label(
            win,
            text="Text Size:",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblTextSize.grid(column=0, row=1, columnspan=2, sticky="nwse")

        def changeTextSize(event):  # Changes the text size of the window and window width
            if event == "Small":
                self.font = ("TkDefaultFont", 9)
                self.width = 500
            elif event == "Regular":
                self.font = ("TkDefaultFont", 11)
                self.width = 550
            else:
                self.font = ("TkDefaultFont", 13)
                self.width = 600

        textOptions = ["Small", "Regular", "Large"]
        optMenTextOptions = OptionMenu(
            win,
            selectedText,
            *(textOptions),
            command=changeTextSize
        )
        optMenTextOptions.grid(column=2, row=1, columnspan=2, sticky="nwse")

        lblTheme = Label(
            win,
            text="Theme:",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblTheme.grid(column=0, row=2, columnspan=2, sticky="nwse")

        def delCustomWidgets(customWidgets):  # Deletes the custom widgets
            for widget in customWidgets:
                widget.destroy()
            customWidgets = []

        def changeTheme(event):  # Changes the theme of the window
            if event == "Light":
                delCustomWidgets(customWidgets)
                self.bgColour = "white"
                self.btnBGColour = "SystemButtonFace"
                self.textColour = "black"
                self.theme = "Light"
            elif event == "Dark":
                delCustomWidgets(customWidgets)
                self.bgColour = "black"
                self.btnBGColour = "#262626"
                self.textColour = "white"
                self.theme = "Dark"
            else:
                def selectBGColor():
                    colour = tkColorChooser.askcolor()
                    win.lift()
                    self.bgColour = colour[1]
                    btnBGColourPicker.configure(bg=self.bgColour or "white")

                def selectBtnBGColor():
                    colour = tkColorChooser.askcolor()
                    win.lift()
                    self.btnBGColour = colour[1]
                    btnBGbtnColourPicker.configure(
                        bg=self.btnBGColour or "SystemButtonFace")

                def selectFGColor():
                    colour = tkColorChooser.askcolor()
                    win.lift()
                    self.textColour = colour[1]
                    btnFGColourPicker.configure(bg=self.textColour or "black")

                lblBGColor = Label(
                    win,
                    text="Background Colour:",
                    bg=self.bgColour,
                    fg=self.textColour,
                    font=self.font
                )
                lblBGColor.grid(column=0, row=3, columnspan=2, sticky="nwse")
                customWidgets.append(lblBGColor)

                btnBGColourPicker = Button(
                    win,
                    text="Select",
                    command=selectBGColor,
                    bg=self.btnBGColour,
                    fg=self.textColour,
                    font=self.font
                )
                btnBGColourPicker.grid(
                    column=2, row=3, columnspan=2, sticky="nwse", padx=5, pady=1)
                customWidgets.append(btnBGColourPicker)

                lblBtnBGColor = Label(
                    win,
                    text="Button Colour:",
                    bg=self.bgColour,
                    fg=self.textColour,
                    font=self.font
                )
                lblBtnBGColor.grid(
                    column=0, row=4, columnspan=2, sticky="nwse")
                customWidgets.append(lblBtnBGColor)

                btnBGbtnColourPicker = Button(
                    win,
                    text="Select",
                    command=selectBtnBGColor,
                    bg=self.btnBGColour,
                    fg=self.textColour,
                    font=self.font
                )
                btnBGbtnColourPicker.grid(
                    column=2, row=4, columnspan=2, sticky="nwse", padx=5, pady=1)
                customWidgets.append(btnBGbtnColourPicker)

                lblFGColor = Label(
                    win,
                    text="Text Colour:",
                    bg=self.bgColour,
                    fg=self.textColour,
                    font=self.font
                )
                lblFGColor.grid(column=0, row=5, columnspan=2, sticky="nwse")
                customWidgets.append(lblFGColor)

                btnFGColourPicker = Button(
                    win,
                    text="Select",
                    command=selectFGColor,
                    bg=self.btnBGColour,
                    fg=self.textColour,
                    font=self.font
                )
                btnFGColourPicker.grid(
                    column=2, row=5, columnspan=2, sticky="nwse", padx=5, pady=1)
                customWidgets.append(btnFGColourPicker)
                self.theme = "Custom"

        # If the theme is custom it will display the custom widgets
        changeTheme(self.theme)

        themeOptions = ["Light", "Dark", "Custom"]
        optMenTheme = OptionMenu(
            win,
            selectedTheme,
            *(themeOptions),
            command=changeTheme
        )
        optMenTheme.grid(column=2, row=2, sticky="nwse", columnspan=2)

        def confirm():  # Confirms the changes and updates the main window
            self.createMainWidgets()
            self.createDeviceWidgets()
            self.win.configure(bg=self.bgColour)
            self.mainFrame.configure(bg=self.bgColour)
            self.deviceFrame.configure(bg=self.bgColour)
            win.destroy()

        btnConfirm = Button(
            win,
            text="Confirm",
            command=confirm,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font)
        btnConfirm.grid(column=0, row=6, columnspan=4, sticky="nwse", pady=10)

    def close(self):  # Closes the window and asks to save
        win = Toplevel()
        win.title("Save and Close")
        win.configure(bg=self.bgColour)
        height = 100
        width = 200
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        win.minsize(width, height)
        win.maxsize(width, height)
        win.columnconfigure((0, 1), weight=1)
        win.rowconfigure((0, 1), weight=1)

        lblMsg = Label(
            win,
            text="Save and Close?",
            bg=self.bgColour,
            fg=self.textColour,
            font=self.font
        )
        lblMsg.grid(column=0, row=0, columnspan=2, sticky="nwse")

        def saveAndClose():  # Saves the file and closes the window
            types = [("CSV Files", "*.csv"), ("Text Files", "*.txt")]
            file = tkFileDialog.asksaveasfile(
                title="Save File",
                filetypes=types,
                defaultextension=types[0][1]
            )
            data = ""
            for device in self.smartHome.getDevices():
                if isinstance(device, SmartPlug):
                    data += f"Plug,{device.getSwitchedOn()},{device.getConsumptionRate()}\n"
                else:
                    data += f"Light,{device.getSwitchedOn()},{device.getBrightness()}\n"

            if file is not None:
                file.write(data)
                file.close()
            win.destroy()
            self.win.destroy()

        btnYes = Button(
            win,
            text="Yes",
            command=saveAndClose,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnYes.grid(column=0, row=1, sticky="nwse", padx=5, pady=5)

        btnNo = Button(
            win,
            text="No",
            command=self.win.destroy,
            bg=self.btnBGColour,
            fg=self.textColour,
            font=self.font
        )
        btnNo.grid(column=1, row=1, sticky="nwse", padx=5, pady=5)

    def updateClock(self):  # Updates the clock and checks for on and off times
        """Error sometimes the time is not updated every 3 seconds, the error is hard to
          replicate"""
        time = self.time.get() + 3
        self.time.set(time)  # Updates the time
        # Retrieves each on time in the format {index: time}
        for onTime in self.onTimes:
            for index in onTime:
                # Gets the value from the key and compares to the time
                if time == onTime[index]:
                    device = self.smartHome.getDeviceAt(index)
                    if not device.getSwitchedOn():  # Checks if the device is off
                        device.toggleSwitch()  # If so turns on the device
                        self.createDeviceWidgets()
        for offTime in self.offTimes:
            for index in offTime:
                if time == offTime[index]:
                    device = self.smartHome.getDeviceAt(index)
                    if device.getSwitchedOn():
                        device.toggleSwitch()
                        self.createDeviceWidgets()
        if time < 10:  # Updates the clock displayed to the user
            self.clock.set(f"Clock: 0{time:}:00")
        elif time < 24:
            self.clock.set(f"Clock: {time}:00")
        else:
            self.time.set(0)
            self.clock.set("Clock: 00:00")
        # Updates the clock every 3 seconds
        self.mainFrame.after(3000, self.updateClock)

    def deviceText(self, device):  # Sets the text for the device
        if device.getSwitchedOn():  # Checks if the device is switched on
            switchedOn = "On"
        else:
            switchedOn = "Off"
        if isinstance(device, SmartPlug):
            text = f"Plug: {switchedOn}, Consumption: {device.getConsumptionRate()}"
        else:
            text = f"Light: {switchedOn}, Brightness: {device.getBrightness()}%"
        return text

    def toggleDevice(self, index):  # Toggles the device and updates the text
        self.smartHome.toggleSwitch(index)
        device = self.smartHome.getDeviceAt(index)
        deviceText = self.deviceText(device)
        self.deviceWidgets[index*7].configure(text=deviceText)

    def setOption(self, index):  # Sets the option for the device and updates the text
        device = self.smartHome.getDeviceAt(index)
        if isinstance(device, SmartPlug):
            device.setConsumptionRate(self.optionVars[index].get())
        else:
            device.setBrightness(self.optionVars[index].get())
        deviceText = self.deviceText(device)
        self.deviceWidgets[index*7].configure(text=deviceText)

    def removeDevice(self, index):  # Removes a device, device widgets and times
        self.smartHome.removeDevice(index)
        for time in self.onTimes:
            if index in time:
                self.onTimes.remove(time)
        for time in self.offTimes:
            if index in time:
                self.offTimes.remove(time)
        self.createDeviceWidgets()

    def turnAllOn(self):  # Turns all devices on and creates device widgets
        self.smartHome.turnAllOn()
        self.createDeviceWidgets()

    def turnAllOff(self):  # Turns all devices off and creates device widgets
        self.smartHome.turnAllOff()
        self.createDeviceWidgets()

    def delAllSmartHomeWidgets(self):  # Deletes all smart home widgets
        for widget in self.smartHomeWidgets:
            widget.destroy()
        self.smartHomeWidgets = []

    def delAllDeviceWidgets(self):  # Deletes all device widgets
        for widget in self.deviceWidgets:
            widget.destroy()
        self.deviceWidgets = []

    def disableTopMost(self):  # Disables the topmost attribute of the window
        self.win.attributes('-topmost', False)


def main():  # Main function
    smartHome = setUpHome()
    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()


main()
