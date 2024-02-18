class SmartDevice:
    def __init__(self):
        self.switchedOn = False

    def getSwitchedOn(self):
        return self.switchedOn

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def __str__(self):
        return f"Switched On: {self.switchedOn}"


class SmartPlug(SmartDevice):
    def __init__(self, consumption):
        super().__init__()
        self.consumption = consumption

    def getConsumptionRate(self):
        return self.consumption

    def setConsumptionRate(self, consumption):
        self.consumption = consumption

    def __str__(self):
        return f"Switched On: {self.switchedOn}\nConsumption Rate: {self.consumption}"


def testSmartPlug():
    smartPlug = SmartPlug(45)
    smartPlug.toggleSwitch()
    print(smartPlug.getSwitchedOn())
    print(smartPlug.getConsumptionRate())
    smartPlug.setConsumptionRate(150)
    print(smartPlug.getConsumptionRate())

    print(smartPlug)


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__()
        self.brightness = 0

    def getBrightness(self):
        return self.brightness

    def setBrightness(self, brightness):
        self.brightness = brightness

    def __str__(self):
        return f"Switched On: {self.switchedOn}\nBrightness: {self.brightness}%"


def testSmartLight():
    smartLight = SmartLight()
    smartLight.toggleSwitch()
    print(smartLight.getSwitchedOn())
    print(smartLight.getBrightness())
    smartLight.setBrightness(50)
    print(smartLight.getBrightness())
    print(smartLight)


class SmartHome:
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self, index):
        return self.devices[index]

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
                output += f"Smart Plug:\n - Switched On: {device.switchedOn}\n - Consumption: {device.consumption}"
            else:
                output += f"Smart Light:\n - Switched On: {device.switchedOn}\n - Brightness: {device.brightness}%"
        return output
