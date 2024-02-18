class Worker:

    def __init__(self, id, name, jobTitle):
        self.id = id
        self.name = name
        self.jobTitle = jobTitle

    def getID(self):
        return self.id

    def getname(self):
        return self.name

    def getJob(self):
        return self.jobTitle

    def setJobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def setname(self, name):
        self.forename = name

    def __str__(self):
        output = f"\nUnique Identifier: {self.id}\nForename: {self.name}\n"
        output += f"Job Title: {self.jobTitle}\n"
        return output


class Employee(Worker):

    promotionAmount = (500, 1000, 2000)

    def __init__(self, id, name, jobTitle, salary):
        super().__init__(id, name, jobTitle)
        self.salary = salary
        self.promotion = 0

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def promote(self):
        self.salary += self.promotionAmount[self.promotion]
        if self.promotion != 2:
            self.promotion += 1

    def __str__(self):
        output = f"\nUnique Identifier: {self.id}\nForename: {self.name}\n"
        output += f"Job Title: {self.jobTitle}\n"
        output += f"Salary: £{self.salary} p/m\nPromotions: {self.promotion}\n"
        return output


class Contractor(Worker):

    def __init__(self, id, name, jobTitle, hourlyWage, contractHours):
        super().__init__(id, name, jobTitle)
        self.hourlyWage = hourlyWage
        self.contractHours = contractHours
        self.extraHours = 0

    def setHourlyWage(self, wage):
        self.hourlyWage = wage

    def setContractHours(self, hours):
        self.contractHours = hours

    def setExtraHours(self, hours):
        self.extraHours = hours

    def updateExtraHours(self, hours):
        self.extraHours += hours

    def getHourlyWage(self):
        return self.hourlyWage

    def getContactHours(self):
        return self.contractHours

    def getExtraHours(self):
        return self.extraHours

    def getSalary(self):
        return (self.contractHours + self.extraHours) * self.hourlyWage

    def __str__(self):
        output = f"\nUnique Identifier: {self.id}\nForename: {self.name}\n"
        output += f"Job Title: {self.jobTitle}\n"
        output += f"Hourly Wage £{self.hourlyWage}\nContract Hours: {self.contractHours}\n"
        output += f"Extra Hours: {self.extraHours}\n"
        return output


class Company:

    def __init__(self, title):
        self.title = title
        self.employees = {}
        self.contractors = {}

    def addWorker(self, worker):
        if isinstance(worker, Employee):
            self.employees[worker.id] = worker
        else:
            self.contractors[worker.id] = worker

    def removeWorker(self, id):
        if id in self.employees:
            del self.employees[id]
        else:
            del self.contractors[id]

    def totalSalaries(self):
        total = sum(employee.getSalary()
                    for employee in self.employees.values())
        total += sum(contractor.getSalary()
                     for contractor in self.contractors.values())
        return total

    def totalWorkers(self):
        return len(self.employees), len(self.contractors)

    def __str__(self):
        totalWorkers = self.totalWorkers()
        output = f"\nCompany Title: {self.title}\nEmployees: {totalWorkers[0]}\n"
        output += f"Contractors: {totalWorkers[1]}\n"
        return output


def test_employee():
    employee = Employee("1", "John", "Developer", 5000)
    print(employee.getSalary())  # 5000
    employee.promote()
    print(employee.getSalary())  # 5500
    print(employee)
    """
    Unique Identifier: 1
    Forename: John
    Job Title: Developer
    Salary: £5500 p/m
    Promotions: 1
    """


def test_contractor():
    contractor = Contractor("2", "Jane", "Designer", 20, 40)
    print(contractor.getSalary())  # 800
    contractor.updateExtraHours(24)
    print(contractor.getSalary())  # 1280
    print(contractor)
    """
    Unique Identifier: 2
    Forename: Jane
    Job Title: Designer
    Hourly Wage £20
    Contract Hours: 40
    Extra Hours: 24
    """


def test_company():
    company = Company("My Company")
    employee = Employee("1", "John", "Developer", 5000)
    employee2 = Employee("3", "Alice", "Manager", 6000)
    contractor = Contractor("2", "Jane", "Designer", 20, 40)
    contractor2 = Contractor("4", "Bob", "Freelancer", 25, 30)

    company.addWorker(employee)
    company.addWorker(contractor)
    company.addWorker(employee2)
    company.addWorker(contractor2)
    print(company.totalSalaries())  # 12550
    print(company.totalWorkers())  # (2,2)
    print(company)
    """
    Company Title: My Company
    Employees: 2
    Contractors: 2
    """

    company.removeWorker("1")
    print(company)
    """
    Company Title: My Company
    Employees: 1
    Contractors: 2
    """


if __name__ == "__main__":
    # test_employee()
    # test_contractor()
    test_company()
