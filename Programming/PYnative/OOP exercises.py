'''Exersise 1
class Vehicle:
    def __init__(self, maxSpeed, mileage):
        self.max_speed = maxSpeed
        self.mileage = mileage

#polo = Vehicle(93,26000)
#print("The max speed of this car is",polo.max_speed,"and the amount of miles it has is",polo.mileage)
'''

'''Exercise 2 
class Vehicle:
    pass
'''
    
'''Exercise 3
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

volvo = Bus("School Volvo", 180, 12)
print("Vehicle Name:",volvo.name,"Speed:",volvo.max_speed,"Mileage:",volvo.mileage)

'''

'''Exercise 4
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus(Vehicle):
    pass

bus=Bus("bus",20,20)
print(bus.seating_capacity(50))
'''

#Exercise 5
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "white"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass