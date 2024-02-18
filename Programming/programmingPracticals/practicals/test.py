class Battery:

    def __init__(self, capacity, power):
        self.capacity = capacity
        self.power = power

    def drain(self, amount):
        self.power = max(0, self.power - amount)

    def isEmpty(self):
        return self.power == 0


class Torch:

    def __init__(self, battery):
        self.battery = battery
        self.isOn = False

    def showPower(self):
        output = f"Battery capacity: {self.battery.capacity}mAh, "
        output += f"power: {self.battery.power}"
        return output

    def switch(self):
        if self.battery.isEmpty():
            self.isOn = False
        else:
            self.isOn = not self.isOn
            if self.isOn:
                self.battery.drain(100)

    def status(self):
        output = "The Torch is"
        if self.isOn:
            output += " on"
        else:
            output += " off"
        return output


def testClasses():
    myBattery = Battery(3000, 1000)
    myTorch = Torch(myBattery)
    print(myTorch.showPower())
    myTorch.switch()
    print(myTorch.status())
    print(myTorch.showPower())


testClasses()
