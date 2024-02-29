from tkinter import *
from backend import SmartHome, SmartLight, SmartPlug


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
            command=self.turnAllOff
        )
        btnTurnAllOff.grid(column=2, row=0, columnspan=2,
                           sticky="nwse", pady=5, padx=5)

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

        for i in range(numDevices):
            self.deviceFrame.rowconfigure(i, weight=1)
            self.height += 30
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)

            lblDevice = Label(
                self.deviceFrame,
                text=deviceText,
                anchor="w",
                width=9
            )
            lblDevice.grid(row=i, column=0, columnspan=2,
                           sticky="nwse")
            self.smartHomeWidgets.append(lblDevice)

            btnToggle = Button(
                self.deviceFrame,
                text="Toggle",
                command=lambda index=i: self.toggleDevice(index)
            )
            btnToggle.grid(row=i, column=2, sticky="nwse",
                           pady=5, padx=(0, 0))
            self.smartHomeWidgets.append(btnToggle)

            btnEdit = Button(
                self.deviceFrame,
                text="Edit",
                command=lambda index=i: self.editDevice(index),
                width=1
            )
            btnEdit.grid(row=i, column=3, sticky="nwse", pady=5, padx=5)
            self.smartHomeWidgets.append(btnEdit)

            btnDelete = Button(
                self.deviceFrame,
                text="Delete",
                command=lambda index=i: self.removeDevice(index),
                width=4
            )
            btnDelete.grid(row=i, column=4, sticky="nwse", pady=5, padx=5)
            self.smartHomeWidgets.append(btnDelete)
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))
        self.height = 175

    def addDevice(self):
        win = Toplevel()
        win.title("Add Device")
        height = 175
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
        mainFrame.rowconfigure((0, 1, 2, 3, 4), weight=1)
        entry = []
        device = StringVar()
        consumptionStr = StringVar()
        errorMsg = StringVar(value="")

        lblMsg = Label(mainFrame, text="Add a Device")
        lblMsg.grid(column=0, row=0, columnspan=2, sticky="nwse")

        lblDevice = Label(mainFrame, text="Device:")
        lblDevice.grid(column=0, row=1, columnspan=2, sticky="nwse")

        def plug():
            if device.get() != "Smart Plug":
                entryPlug = Entry(
                    mainFrame, textvariable=consumptionStr)
                entryPlug.grid(column=0, row=3, columnspan=2, sticky="nwse")
                entry.append(entryPlug)
            device.set("Smart Plug")
            lblDevice.configure(text="Device: Smart Plug")

        btnPlug = Button(mainFrame, text="Smart Plug",
                         command=plug)
        btnPlug.grid(column=0, row=2, sticky="nwse", padx=5, pady=5)

        def light():
            if device.get() == "Smart Plug":
                entry[0].destroy()
                entry.pop(0)
            device.set("Smart Light")
            lblDevice.configure(text="Device: Smart Light")

        btnLight = Button(
            mainFrame, text="Smart Light", command=light)
        btnLight.grid(column=1, row=2, sticky="nwse", padx=5, pady=5)

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
            if device.get() == "Smart Plug":
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
            elif device.get() == "Smart Light":
                self.smartHome.addDevice(SmartLight())
                win.destroy()
                self.createDeviceWidgets()
            else:
                errorMsg.set("Error Device not selected")
                msgError.grid(column=0, row=0, sticky="nwse",
                              padx=20, pady=50)
                lblMsg.after(2000, error)

        btnAddDevice = Button(
            mainFrame,
            text="Add",
            command=addDevice
        )
        btnAddDevice.grid(column=0, row=4, columnspan=2,
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

        def toggle():
            device.toggleSwitch()
            if device.getSwitchedOn():
                text = "On"
            else:
                text = "Off"
            switchedOnText.set(text)

        btnToggle = Button(
            mainFrame,
            text="Toggle",
            command=toggle
        )
        btnToggle.grid(column=2, row=2, sticky="nwse", padx=5, pady=5)

        switchedOnText = StringVar()
        if device.getSwitchedOn():
            switchedOnText.set("On")
        else:
            switchedOnText.set("Off")

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

        entryOption = Entry(
            mainFrame,
            textvariable=optionVar,
            width=1
        )
        entryOption.grid(column=2, row=3, columnspan=2, sticky="nwse")

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

    def removeDevice(self, index):
        self.smartHome.removeDevice(index)
        self.createDeviceWidgets()

    def turnAllOn(self):
        self.smartHome.turnAllOn()
        numDevices = len(self.smartHome.getDevices())
        for i in range(numDevices):
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)
            self.smartHomeWidgets[i*4].configure(text=deviceText)

    def turnAllOff(self):
        self.smartHome.turnAllOff()
        numDevices = len(self.smartHome.getDevices())
        for i in range(numDevices):
            device = self.smartHome.getDeviceAt(i)
            deviceText = self.deviceText(device)
            self.smartHomeWidgets[i*4].configure(text=deviceText)

    def delAllDeviceWidgets(self):
        for widget in self.smartHomeWidgets:
            widget.destroy()
        self.smartHomeWidgets = []


def main():
    smartHome = setUpHome()
    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()


main()
