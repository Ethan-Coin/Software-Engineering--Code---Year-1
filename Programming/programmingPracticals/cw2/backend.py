class SmartPlug:
    def __init__(self, consumptionRate):
        self.switchedOn = False
        self.consumptionRate = 0
        self.setConsumptionRate(consumptionRate)

    def toggleSwitch(self):  # Toggles the state of the plug
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):  # Returns the sate of the plug
        return self.switchedOn

    def getConsumptionRate(self):  # Returns the consumption rate of the plug
        return self.consumptionRate

    # Sets the consumption rate of the plug
    def setConsumptionRate(self, consumptionRate):
        self.consumptionRate = consumptionRate

    def __str__(self):
        return f"Switched on: {self.switchedOn}\nConsumption Rate: {self.consumptionRate}"


def testSmartPlug():
    smartPlug = SmartPlug(45)
    smartPlug.toggleSwitch()
    print("The smart plug is on:", smartPlug.getSwitchedOn())  # True
    print("The smart plug consumption rate is",
          smartPlug.getConsumptionRate())  # 45
    print(smartPlug)


class SmartLight:
    def __init__(self):
        self.switchedOn = False
        self.brightness = 0

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def getSwitchedOn(self):
        return self.switchedOn

    def getBrightness(self):
        return self.brightness

    def setBrightness(self, brightness):  # Sets the brightness of the light
        self.brightness = brightness

    def __str__(self):
        return f"Switched on: {self.switchedOn}\nBrightness: {self.brightness}%"


def testSmartLight():
    smartLight = SmartLight()
    smartLight.toggleSwitch()
    print("The smart light is on:", smartLight.getSwitchedOn())  # True
    print(f"The smart light brightness it at:\
 {smartLight.getBrightness()}%")  # 0
    smartLight.setBrightness(65)
    print(f"The smart light brightness it at:\
 {smartLight.getBrightness()}%")  # 65
    print(smartLight)


class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):  # Returns the list of all devices
        return self.devices

    def getDeviceAt(self, index):  # Returns the device at a certain index
        if 0 <= index < len(self.devices):
            return self.devices[index]

    def addDevice(self, device):
        self.devices.append(device)

    def toggleSwitch(self, index):
        if 0 <= index < len(self.devices):
            self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for device in self.devices:
            if device.getSwitchedOn() == False:
                device.toggleSwitch()

    def turnOffAll(self):
        for device in self.devices:
            if device.getSwitchedOn():
                device.toggleSwitch()

    def __str__(self):
        output = "Devices in Smart Home:"
        for device in self.devices:
            if isinstance(device, SmartPlug):
                output += f"\nSmart Plug:\n - Switched On:\
 {device.getSwitchedOn()}\n - Consumption Rate: {device.getConsumptionRate()}"
            else:
                output += f"\nSmart Light:\n - Switched On:\
 {device.getSwitchedOn()}\n - Brightness: {device.getBrightness()}%"
        return output


def testSmartHome():
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

    print(smartHome)
    """
Devices in Smart Home:
Smart Plug:
 - Switched On: True
 - Consumption Rate: 150
Smart Plug:
 - Switched On: True
 - Consumption Rate: 25
Smart Light:
 - Switched On: False
 - Brightness: 65%
    """

    smartHome.turnOnAll()

    print(smartHome)


"""
Devices in Smart Home:
Smart Plug:
 - Switched On: True
 - Consumption Rate: 150
Smart Plug:
 - Switched On: True
 - Consumption Rate: 25
Smart Light:
 - Switched On: True
 - Brightness: 65%
"""
