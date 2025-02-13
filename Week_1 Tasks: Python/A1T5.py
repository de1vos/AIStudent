# Task 5: Car Dealership Inventory
## Story:
# You manage the inventory for a car dealership. 
# The dealership sells various types of vehicles like cars and trucks. 
# You need to organize vehicle information, including calculating the 
# total inventory value and displaying information about each vehicle in 
# a readable format.

## Tasks:
# - Create a base Vehicle class with attributes for `make`, 
#   `model`, `year`, and `price`.
# - Create a `Car` and a `Truck` subclass, each with a specific feature. 
#   Cars have `num_doors`, and trucks have `payload_capacity`.
# - Implement the `__str__` dunder method to display vehicle information neatly.
# - Using the class attributes, calculate the total value of the inventory 
#   consisting of a 2023 Toyota Camry, worth $24,000, a 2022 Ford F-150, 
#   worth $35,000, and a 2021 Honda Civic, worth $22,000. The Ford F-150 
#   has a payload capacity of 1000 kg and the other two vehicles have 4 doors.

## Starting Point:

# Base class Vehicle
class Vehicle:
    # __init__ = Python's constructor
    def __init__(self, make: str, model: str, year: int, price: int):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    # __str__ = Python's function for defining an object's representation as a string
    def __str__(self):
        return f"{self.year} {self.make} {self.model} - ${self.price}"

class Car(Vehicle):
    # Car subclass constructor that inherits Vehicle and adds num_doors
    def __init__(self, make: str, model: str, year: int, price: int, num_doors: int):
        super().__init__(make, model, year, price)
        self.num_doors = num_doors

    # Car's representation as string
    def __str__(self):
        return f"{super().__str__()} (Car, {self.num_doors} doors)"

class Truck(Vehicle):
    # Truck subclass constructor that inherits Vehicle and adds Payload_capacity
    def __init__(self, make: str, model: str, year: int, price: int, payload_capacity: int):
        super().__init__(make, model, year, price)
        self.payload_capacity = payload_capacity

    # Truck's representation as string
    def __str__(self):
        return f"{super().__str__()} (Truck, Payload capacity: {self.payload_capacity} kg)"

# Inventory list
inventory = [Car("Toyota", "Camry", 2023, 24000, 4),
             Truck("Ford", "F-150", 2022, 35000, 1000),
             Car("Honda", "Civic", 2021, 22000, 4)]

# Display all vehicles and calculate total value
total_value = 0
for vehicle in inventory:
    print(vehicle)
    total_value += vehicle.price

print(f"Total inventory value: ${total_value}")

## Expected Output:

# > 2023 Toyota Camry - $24000 (Car, 4 doors)

# > 2022 Ford F-150 - $35000 (Truck, Payload capacity: 1000 kg)

# > 2021 Honda Civic - $22000 (Car, 4 doors)

# > Total inventory value: $81000