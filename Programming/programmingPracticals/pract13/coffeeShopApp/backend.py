class CoffeeShop:

    def __init__(self, limit):
        self.customers = []
        self.limit = limit

    def addCustomer(self, name):
        if len(self.customers) < self.limit:
            self.customers.append(name)

    def removeCustomerAt(self, index):
        del self.customers[index]

    def getLimit(self):
        return self.limit

    def getCustomerAt(self, index):
        return self.customers[index]

    def getNumCustomers(self):
        return len(self.customers)
