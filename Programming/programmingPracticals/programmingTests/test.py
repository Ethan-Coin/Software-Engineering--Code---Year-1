class FitnessTracker:
    def __init__(self):
        self.totalSteps = 0

    def logSteps(self, steps):
        self.totalSteps += steps

    def viewStats(self):
        if self.totalSteps >= 1000:
            print("Fitness Discount Voucher Earned: 50%")
        else:
            print("Total steps:", self.totalSteps)


def testFitnessTracker():
    fitnessTracker = FitnessTracker()
    fitnessTracker.logSteps(500)
    fitnessTracker.viewStats()
    fitnessTracker.logSteps(600)
    fitnessTracker.viewStats()


# testFitnessTracker()


class FitnessTracker2:
    def __init__(self):
        self.totalSteps = 0

    def logSteps(self, steps):
        self.totalSteps += steps

    def viewStats(self):
        if self.totalSteps >= 1000:
            discount = 50
            self.totalSteps = 0
        elif self.totalSteps >= 500:
            discount = 25
            self.totalSteps = 0
        elif self.totalSteps >= 100:
            discount = 10
            self.totalSteps = 0
        if discount >= 10:
            print(f"Fitness Discount Voucher Earned: {discount}%")
        else:
            print("Total steps:", self.totalSteps)


def testFitnessTracker2():
    fitnessTracker = FitnessTracker2()
    fitnessTracker.logSteps(20)
    fitnessTracker.viewStats()
    fitnessTracker.logSteps(200)
    fitnessTracker.viewStats()
    fitnessTracker.logSteps(600)
    fitnessTracker.viewStats()
    fitnessTracker.logSteps(1000)
    fitnessTracker.viewStats()


testFitnessTracker2()
