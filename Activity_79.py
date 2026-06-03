# 1) Create a class named `Vehicle`.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name)
print("Max Speed:", School_bus.max_speed)
print("Mileage:", School_bus.mileage)

# 2) Create an `__init__` method inside the `Vehicle` class to initialize instance variables:

# - `self.name = name`

# - `self.max_speed = max_speed`

# - `self.mileage = mileage`

# 3) Create a class named `Bus` that inherits from the `Vehicle` class:

# a) Use `class Bus(Vehicle):`

# b) Use `pass` because no extra properties or methods are added.

# (Bus automatically gets all features of Vehicle through inheritance.)

# 4) Create an object `School_bus` of the `Bus` class by passing:

# a) name = "School Volvo"

# b) max_speed = 180

# c) mileage = 12

# 5) Print the details of `School_bus` by accessing inherited instance variables:

# a) Print the vehicle name.

# b) Print the max speed.

# c) Print the mileage.