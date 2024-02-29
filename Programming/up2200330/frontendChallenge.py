from tkinter import *
from backendChallenge import SmartHome, SmartLight, SmartPlug


def setUpHome():
    smartHome = SmartHome()
    for _ in range(5):
        error = "\nInvalid Option please enter a valid option\n"
        while True:
            device = input(
                "Enter a device to add (Smart Plug [1] or Smart Light [2]): ").lower().replace(" ", "")
            if device in ["smartplug", "1", "smartlight", "2"]:
                if device in ["smartplug", "1"]:
                    while True:
                        consumption = input("Enter consumption rate (0-150): ")
                        if consumption.isdigit():
                            consumption = int(consumption)
                            if 0 <= consumption <= 150:
                                break
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
    return smartHome


class SmartHomeSystem:

    def __init__(self, smartHome):
        self.smartHome = smartHome

        # Main Window Configuration
        self.win = Tk()
        self.win.title("Smart Home System")
        self.width = 500
        self.height = 175
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))
        self.win.minsize(500, 175)
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)

        # Main Frame for widgets
        self.mainFrame = Frame(self.win)
        self.mainFrame.grid(column=0, row=0, sticky="nwse", padx=5, pady=5)
        self.mainFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.mainFrame.rowconfigure((0, 3), weight=2)
        self.mainFrame.rowconfigure(2, weight=1)
        self.mainFrame.rowconfigure(1, weight=20)

        self.smartHomeWidgets = []

        # Frame for devices
        self.deviceFrame = Frame(self.mainFrame)
        self.deviceFrame.grid(column=0, row=1, columnspan=5, sticky="nwse")
        self.deviceFrame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.deviceFrame.rowconfigure(
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)

        # Page Number variables
        self.pageNumber = 1
        self.maxPageNumber = 1
        self.page = StringVar()

    def run(self):
        self.createMainWidgets()
        self.createDeviceWidgets()
        self.win.mainloop()

    def createMainWidgets(self):
        btnTurnAllOn = Button(
            self.mainFrame,
            text="Turn all on",
            command=self.turnAllOn
        )
        btnTurnAllOn.grid(column=0, row=0, columnspan=2,
                          sticky="nwse", pady=5)

        btnTurnAllOff = Button(
            self.mainFrame,
            text="Turn all off",
            command=self.turnAllOff,
            width=10
        )
        btnTurnAllOff.grid(column=2, row=0, columnspan=2,
                           sticky="nwse", pady=5, padx=5)

        btnClose = Button(
            self.mainFrame,
            text="Close",
            command=self.win.destroy
        )
        btnClose.grid(column=4, row=0, sticky="nwse", pady=5, padx=5)

        lblPage = Label(
            self.mainFrame,
            textvariable=self.page,

        )
        lblPage.grid(column=2, row=2, sticky="nwse")

        btnBack = Button(
            self.mainFrame,
            text="Back",

            command=self.backPage
        )
        btnBack.grid(column=1, row=2, sticky="nwse", pady=5, padx=5)

        btnNext = Button(
            self.mainFrame,
            text="Next",
            command=self.nextPage
        )
        btnNext.grid(column=3, row=2, sticky="nwse", pady=5, padx=5)

        btnAdd = Button(
            self.mainFrame,
            text="Add Device",
            command=self.addDevice
        )
        btnAdd.grid(column=0, row=3, columnspan=2,
                    sticky="nwse", pady=5)

    def createDeviceWidgets(self):
        self.delAllDeviceWidgets()
        numDevices = len(self.smartHome.getDevices())
        if numDevices % 10 > 0 or numDevices == 0:
            self.maxPageNumber = numDevices//10 + 1
        else:
            self.maxPageNumber = numDevices//10
        if self.pageNumber > self.maxPageNumber:
            self.pageNumber = self.maxPageNumber
        self.page.set(f"Page {self.pageNumber}/{(self.maxPageNumber)}")

        startIndex = (self.pageNumber - 1) * 10
        if numDevices-startIndex > 10:
            EndIndex = startIndex + 10
        else:
            EndIndex = numDevices

        for i in range(startIndex, EndIndex):
            self.height += 30
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)

            lblDevice = Label(
                self.deviceFrame,
                text=deviceText,
                anchor="w",
                width=9
            )
            lblDevice.grid(row=i % 10, column=0, columnspan=2,
                           sticky="nwse")
            self.smartHomeWidgets.append(lblDevice)

            btnToggle = Button(
                self.deviceFrame,
                text="Toggle",
                command=lambda index=i: self.toggleDevice(index)
            )
            btnToggle.grid(row=i % 10, column=2, sticky="nwse",
                           pady=5, padx=(0, 0))
            self.smartHomeWidgets.append(btnToggle)

            btnEdit = Button(
                self.deviceFrame,
                text="Edit",
                command=lambda index=i: self.editDevice(index),
                width=1
            )
            btnEdit.grid(row=i % 10, column=3, sticky="nwse", pady=5, padx=5)
            self.smartHomeWidgets.append(btnEdit)

            btnDelete = Button(
                self.deviceFrame,
                text="Delete",
                command=lambda index=i: self.removeDevice(index),
                width=4
            )
            btnDelete.grid(row=i % 10, column=4, sticky="nwse", pady=5, padx=5)
            self.smartHomeWidgets.append(btnDelete)
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))
        self.height = 175

    def addDevice(self):
        win = Toplevel()
        win.title("Add Device")
        height = 150
        width = 250
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width,
                                          height, x, y))
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

        mainFrame = Frame(win)
        mainFrame.grid(column=0, row=0, padx=5, pady=5, sticky="nwse")
        mainFrame.columnconfigure((0, 1), weight=1)
        mainFrame.rowconfigure((0, 1, 2, 3), weight=1)

        device = IntVar(value=1)
        consumptionStr = StringVar()
        errorMsg = StringVar(value="")

        lblMsg = Label(mainFrame, text="Add a Device")
        lblMsg.grid(column=0, row=0, columnspan=2, sticky="nwse")

        radioPlug = Radiobutton(mainFrame, text="Smart Plug",
                                variable=device, value=1)
        radioPlug.grid(column=0, row=1, sticky="w")

        spinPlug = Spinbox(mainFrame, from_=0, to=150,
                           textvariable=consumptionStr)
        spinPlug.grid(column=1, row=1)

        radioLight = Radiobutton(
            mainFrame, text="Smart Light", variable=device, value=2)
        radioLight.grid(column=0, row=2, sticky="w")

        def addDevice():
            def error():
                msgError.destroy()
            msgError = Message(
                win,
                textvariable=errorMsg,
                bg="red",
                justify="center",
                width=210
            )
            if device.get() == 1:
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
            mainFrame,
            text="Add",
            command=addDevice
        )
        btnAddDevice.grid(column=0, row=3, columnspan=2,
                          sticky="nwse", padx=30, pady=5)

    def editDevice(self, index):
        win = Toplevel()
        win.title("Edit Device")
        height = 150
        width = 250
        y = (win.winfo_screenheight() // 2) - (height // 2)
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        win.geometry("{}x{}+{}+{}".format(width,
                                          height, x, y))
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

        mainFrame = Frame(win)
        mainFrame.grid(column=0, row=0, padx=5, pady=5, sticky="nwse")
        mainFrame.columnconfigure((0, 1, 2, 3), weight=1)
        mainFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)

        device = self.smartHome.getDeviceAt(index)
        errorMsg = StringVar()
        optionVar = StringVar()
        if isinstance(device, SmartPlug):
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
            mainFrame,
            text=deviceName
        )
        lblSmartDevice.grid(column=0, row=0, columnspan=4, sticky="nwse")

        lblProperty = Label(
            mainFrame,
            text="Property"
        )
        lblProperty.grid(column=0, row=1, columnspan=2)

        lblValue = Label(
            mainFrame,
            text="Value"
        )
        lblValue.grid(column=2, row=1, columnspan=2)

        lblSwitchedOn = Label(
            mainFrame,
            text="Switched On:"
        )
        lblSwitchedOn.grid(column=0, row=2, columnspan=2)

        def switchText():
            if switchedOn.get():
                text = "On"
            else:
                text = "Off"
            switchedOnText.set(text)

        checkSwitchedOn = Checkbutton(
            mainFrame,
            variable=switchedOn,
            onvalue=True,
            offvalue=False,
            command=switchText
        )
        checkSwitchedOn.grid(column=2, row=2, sticky="e")

        switchedOnText = StringVar()
        switchText()

        lblSwitchedOnValue = Label(
            mainFrame,
            textvariable=switchedOnText,
            width=2
        )
        lblSwitchedOnValue.grid(column=3, row=2, sticky="w")

        lblOption = Label(
            mainFrame,
            text=option
        )
        lblOption.grid(column=0, row=3, columnspan=2)

        spinOption = Spinbox(
            mainFrame,
            from_=0,
            to=limit,
            textvariable=optionVar,
            width=1
        )
        spinOption.grid(column=2, row=3, columnspan=2, sticky="nwse")

        def confirm():
            def error():
                msgError.destroy()
            msgError = Message(
                win,
                textvariable=errorMsg,
                bg="red",
                justify="center",
                width=210
            )
            if optionVar.get().isdigit():
                intOptionVar = int(optionVar.get())
                if switchedOn.get() != device.getSwitchedOn():
                    device.toggleSwitch()
                if deviceName == "Smart Plug":
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
            mainFrame,
            text="Confirm",
            command=confirm,
            width=1
        )
        btnConfirm.grid(column=0, row=4, columnspan=4,
                        sticky="nwse", padx=10, pady=10)

    def deviceText(self, device):
        if device.getSwitchedOn():
            switchedOn = "On"
        else:
            switchedOn = "Off"
        if isinstance(device, SmartPlug):
            text = f"Plug: {switchedOn}, Consumption: {device.getConsumptionRate()}"
        else:
            text = f"Light: {switchedOn}, Brightness: {device.getBrightness()}%"
        return text

    def toggleDevice(self, index):
        self.smartHome.toggleSwitch(index)
        device = self.smartHome.getDeviceAt(index)
        deviceText = self.deviceText(device)
        self.smartHomeWidgets[index*4].configure(text=deviceText)

    def nextPage(self):
        if self.pageNumber < self.maxPageNumber:
            self.pageNumber += 1
            self.createDeviceWidgets()

    def backPage(self):
        if self.pageNumber > 1:
            self.pageNumber -= 1
            self.createDeviceWidgets()

    def removeDevice(self, index):
        self.smartHome.removeDevice(index)
        self.createDeviceWidgets()

    def turnAllOn(self):
        self.smartHome.turnAllOn()
        numDevices = len(self.smartHome.getDevices())
        if numDevices - (self.pageNumber-1) * 10 >= 10:
            forRange = 10
        else:
            forRange = numDevices - (self.pageNumber-1) * 10
        for i in range(forRange):
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)
            self.smartHomeWidgets[i*4].configure(text=deviceText)

    def turnAllOff(self):
        self.smartHome.turnAllOff()
        numDevices = len(self.smartHome.getDevices())
        if numDevices - (self.pageNumber-1) * 10 >= 10:
            forRange = 10
        else:
            forRange = numDevices - (self.pageNumber-1) * 10
        for i in range(forRange):
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)
            self.smartHomeWidgets[i*4].configure(text=deviceText)

    def delAllDeviceWidgets(self):
        for widget in self.smartHomeWidgets:
            widget.destroy()
        self.smartHomeWidgets = []


def testSmartHomeSystem():
    smartHome = SmartHome()
    for i in range(35):
        if i % 2 != 0:
            smartHome.addDevice(SmartPlug(i))
        else:
            smartHome.addDevice(SmartLight())

    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()


testSmartHomeSystem()


def main():
    smartHome = setUpHome()
    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()

# Do the challenges afterwards

# put spin boxes in the main gui
# Photoimages of devices
# Device Scheduler
# Interface & Accessibility setting
# chatgpt comment code
# font size 3 options small medium large 3 other font families

# more than
