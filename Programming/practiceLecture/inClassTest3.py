
class Shopping:

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
        newTotal = self.total - discount
        return discount, newTotal


def testShopping():
    shopping = Shopping()
    shopping.spend(50)
    shopping.spend(60)
    totals = shopping.checkout()
    print(
        f"Discounted Amount: {totals[0]}\nNew Total after Discount: {totals[1]}")


# testShopping()


class Shopping2:

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
        newTotal = self.total - discount
        self.total = 0
        return discount, newTotal


def testShopping2():
    shopping = Shopping2()
    shopping.spend(50)
    shopping.spend(60)
    discount, newTotal = shopping.checkout()
    print(
        f"Discount Amount: {discount}\nNew Amount after Discount: {newTotal}")
    shopping.spend(20)
    discount, newTotal = shopping.checkout()
    print(
        f"Discount Amount: {discount}\nNew Amount after Discount: {newTotal}")
    shopping.spend(75)
    discount, newTotal = shopping.checkout()
    print(
        f"Discount Amount: {discount}\nNew Amount after Discount: {newTotal}")


testShopping2()
