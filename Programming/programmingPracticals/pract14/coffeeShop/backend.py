class CoffeeShop:

    def __init__(self):
        self.customers = []

    def addCustomer(self, name):
        self.customers.append(name)

    def removeCustomerAt(self, index=0):
        del self.customers[index]

    def getCustomerAt(self, index):
        try:
            return self.customers[index]
        except IndexError:
            return None

    def getNumCustomers(self):
        return len(self.customers)
