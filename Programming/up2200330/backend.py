# Classes
class SmartDevice:  # Base class containing the switchedOn variable for inheritance
    def __init__(self):
        self.switchedOn = False

    def getSwitchedOn(self):
        return self.switchedOn

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def __str__(self):
        return f"Switched On: {self.switchedOn}"


class SmartPlug(SmartDevice):  # Smart plug inherits from SmartDevice
    def __init__(self, consumption):
        super().__init__()
        self.consumptionRate = consumption

    def getConsumptionRate(self):
        return self.consumptionRate

    def setConsumptionRate(self, consumption):
        if 0 <= consumption <= 150:
            self.consumptionRate = consumption
        else:
            print("Invalid consumption rate, valid options are between 0 and 150.")

    def __str__(self):
        return f"Switched On: {self.switchedOn}\nConsumption Rate: {self.consumptionRate}"


class SmartLight(SmartDevice):  # Smart light inherits from SmartDevice
    def __init__(self):
        super().__init__()
        self.brightness = 0

    def getBrightness(self):
        return self.brightness

    def setBrightness(self, brightness):
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            print("Invalid consumption rate, valid options are between 0 and 100.")

    def __str__(self):
        return f"Switched On: {self.switchedOn}\nBrightness: {self.brightness}%"


class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self, index):
        return self.devices[index]

    def removeDevice(self, index):
        self.devices.pop(index)

    def addDevice(self, device):
        self.devices.append(device)

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnAllOn(self):
        for device in self.devices:
            if not device.switchedOn:
                device.toggleSwitch()

    def turnAllOff(self):
        for device in self.devices:
            if device.switchedOn:
                device.toggleSwitch()

    def __str__(self):
        output = "Devices in Smart Home:"
        for device in self.devices:
            if isinstance(device, SmartPlug):
                output += f"\nSmart Plug:\n - Switched On: {device.getSwitchedOn()}\n\
 - Consumption: {device.getConsumptionRate()}"
            else:
                output += f"\nSmart Light:\n - Switched On: {device.getSwitchedOn()}\n\
 - Brightness: {device.getBrightness()}%"
        return output


# Tests

def testSmartPlug():
    smartPlug = SmartPlug(45)
    smartPlug.toggleSwitch()
    print("Switched On:", smartPlug.getSwitchedOn())  # True
    print("Consumption rate is:", smartPlug.getConsumptionRate())  # 45
    smartPlug.setConsumptionRate(150)
    print("Consumption rate is:", smartPlug.getConsumptionRate())  # 150
    print(smartPlug)


def testSmartLight():
    smartLight = SmartLight()
    smartLight.toggleSwitch()
    print("Switched On:", smartLight.getSwitchedOn())  # True
    print("Brightness is:", smartLight.getBrightness())  # 0
    smartLight.setBrightness(50)
    print("Brightness is:", smartLight.getBrightness())  # 50
    print(smartLight)


def testSmartHome():
    smartHome = SmartHome()
    smartPlug = SmartPlug(45)
    smartPlug1 = SmartPlug(45)
    smartLight = SmartLight()
    smartPlug.toggleSwitch()
    smartPlug.setConsumptionRate(150)
    smartPlug1.setConsumptionRate(25)
    smartLight.setBrightness(50)
    smartHome.addDevice(smartPlug)
    smartHome.addDevice(smartPlug1)
    smartHome.addDevice(smartLight)
    smartHome.toggleSwitch(1)
    print(smartHome)
    """
    Devices in Smart Home:
Smart Plug:
 - Switched On: True
 - Consumption: 150
Smart Plug:
 - Switched On: True
 - Consumption: 25
Smart Light:
 - Switched On: False
 - Brightness: 50%"""
    smartHome.turnAllOn()
    print(smartHome)
    """
Devices in Smart Home:
Smart Plug:
 - Switched On: True
 - Consumption: 150
Smart Plug:
 - Switched On: True
 - Consumption: 25
Smart Light:
 - Switched On: True
 - Brightness: 50%"""
