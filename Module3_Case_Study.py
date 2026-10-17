# Name: Tyree Callahan
# File Name: Module3_Case_Study.py
# Description: This program uses classes to store
# and display information about a car.

class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter roof type (solid or sun roof): ")

car = Automobile(year, make, model, doors, roof)

print()
print("Vehicle type:", car.vehicle_type)
print("Year:", car.year)
print("Make:", car.make)
print("Model:", car.model)
print("Number of doors:", car.doors)
print("Type of roof:", car.roof)
