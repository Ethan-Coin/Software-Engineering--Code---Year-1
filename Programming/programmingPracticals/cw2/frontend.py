from tkinter import *
from tkinter import ttk
from backend import SmartPlug, SmartLight, SmartHome


class SmartHomeSystem:
    def __init__(self, smartHome):
        self.smartHome = smartHome
        self.deviceFrames = []

        self.win = Tk()
        self.width = 400
        self.height = 75
        self.win.title("Smart Home")
        self.y = (self.win.winfo_screenheight() // 2) - (self.height // 2)
        self.x = (self.win.winfo_screenwidth() // 2) - (self.width // 2)
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))

        self.buttonStyle = ttk.Style(self.win)
        self.buttonStyle.configure('TButton',
                                   font=("Tekton Pro", 10))
        self.LabelStyle = ttk.Style(self.win)
        self.LabelStyle.configure('TLabel',
                                  font=("Tekton Pro", 10))

        self.mainFrame = Frame(self.win)
        self.mainFrame.pack(padx=5, pady=10, expand=True, fill="both")
        self.topFrame = Frame(self.mainFrame)
        self.topFrame.pack(fill="both", expand=True)
        self.middleFrame = Frame(self.mainFrame)
        self.middleFrame.pack(fill="both", expand=True)
        self.bottomFrame = Frame(self.mainFrame)
        self.bottomFrame.pack(fill="both", expand=True)

    def run(self):
        self.createWidgets()
        for device in self.smartHome.getDevices():
            self.addDevice(device)
        self.win.mainloop()
        print(self.bottomFrame)

    def createWidgets(self):
        btnTurnOnAll = ttk.Button(
            self.topFrame,
            text="Turn on all",
            width=15
        )
        btnTurnOnAll.pack(side="left", anchor="w")

        btnTurnOffAll = ttk.Button(
            self.topFrame,
            text="Turn off all",
            width=15
        )
        btnTurnOffAll.pack(side="left", anchor="w", padx=(49, 0))

        btnAdd = ttk.Button(
            self.bottomFrame,
            text="Add"
        )
        btnAdd.pack(anchor="w", expand=True)

    def updateWindow(self):
        self.height += 25
        self.win.geometry("{}x{}+{}+{}".format(self.width,
                          self.height, self.x, self.y))

    def addDevice(self, device):
        deviceFrame = Frame(self.middleFrame)
        deviceFrame.pack(anchor="w")

        if device.getSwitchedOn():
            status = "on"
        else:
            status = "off"
        if isinstance(device, SmartPlug):
            lblAttributes = ttk.Label(
                deviceFrame,
                text=f"Plug: {status}, Consumption: {device.getConsumptionRate()}",
                width=23,
                anchor="w"
            )
        else:
            lblAttributes = ttk.Label(
                deviceFrame,
                text=f"Light: {status}, Brightness: {device.getBrightness()}%",
                width=23,
                anchor="w"
            )
        lblAttributes.pack(side="left")

        btnToggle = ttk.Button(
            deviceFrame,
            text="Toggle",
            width=8
        )
        btnToggle.pack(side="left")

        btnEdit = ttk.Button(
            deviceFrame,
            text="Edit",
            width=5
        )
        btnEdit.pack(side="left", padx=(5, 0))

        btnDelete = ttk.Button(
            deviceFrame,
            text="Delete"
        )
        btnDelete.pack(side="left", padx=(10, 0))

        self.deviceFrames.append(deviceFrame)
        self.updateWindow()


# def setUpHome():
#     smartHome = SmartHome()
#     for _ in range(5):
#         while True:
#             device = input(
#                 "Enter the device to add to your smart home (Smart Plug or Smart Light): ")
#             device = device.replace(" ", "").lower()
#             if device in ["smartplug", "1", "smartlight", "2"]:
#                 break
#             else:
#                 print("\nInvalid option please enter a valid option\n")
#         if device in ["smartplug", "1"]:
#             while True:
#                 consumption = input(
#                     "Enter consumption rate of the smart plug (0-150): ")
#                 if not consumption.isdigit():
#                     print("\nInvalid option please enter a valid option (0-150)\n")
#                 else:
#                     consumption = int(consumption)
#                     if 0 <= consumption <= 150:
#                         break
#                     else:
#                         print(
#                             "\nInvalid option please enter a valid option (0-150)\n")
#             smartHome.addDevice(SmartPlug(consumption))
#         else:
#             smartHome.addDevice(SmartLight())

def setUpHome():
    smartHome = SmartHome()
    smartPlug1 = SmartPlug(45)
    smartPlug2 = SmartPlug(45)
    smartLight = SmartLight()

    smartPlug1.toggleSwitch()
    smartPlug1.setConsumptionRate(150)
    smartPlug2.setConsumptionRate(25)
    smartLight.setBrightness(65)

    smartHome.addDevice(smartPlug1)
    smartHome.addDevice(smartPlug2)
    smartHome.addDevice(smartLight)

    smartHome.toggleSwitch(1)

    smartHomeSystem = SmartHomeSystem(smartHome)
    smartHomeSystem.run()


setUpHome()
