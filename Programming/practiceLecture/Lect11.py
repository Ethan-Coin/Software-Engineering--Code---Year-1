# Task 1
class Shopping():

    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount

    def checkout(self):
        discount = 0
        if self.total >= 100:
            discount = 0.25 * self.total
        elif self.total >= 50:
            discount = 0.1 * self.total
        new_total = self.total - discount
        print(f"The discount is £{discount}, new total is £{new_total}")


def testShopping():
    shopping = Shopping()
    shopping.spend(50)
    shopping.spend(60)
    shopping.checkout()


# testShopping()

# Task2

# Task 1
class Shopping2():

    def __init__(self):
        self.total = 0

    def spend(self, amount):
        self.total += amount

    def checkout(self):
        if self.total >= 100:
            discount = 0.25 * self.total
        elif self.total >= 50:
            discount = 0.1 * self.total
        else:
            discount = 0
        new_total = self.total - discount
        print(
            f"The discount is £{discount:.2f}, new total is £{new_total:.2f}")
        self.total = 0


def testShopping2():
    shopping = Shopping2()
    shopping.spend(50)
    shopping.spend(60)
    shopping.checkout()
    shopping.spend(20)
    shopping.checkout()
    shopping.spend(75)
    shopping.checkout()


testShopping2()
