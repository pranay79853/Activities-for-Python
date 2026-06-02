# 1) Create a class named `Vehicle`.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
Car = Vehicle("Koenigsegg", 531, 8)
Bus = Vehicle("Volvo", 180, 12)
print("The max speed of the", Car.name, "is", Car.max_speed, "km/h and its mileage is", Car.mileage, "km/l.")
print("The max speed of the", Bus.name, "is", Bus.max_speed, "km/h and its mileage is", Bus.mileage, "km/l.")

# 2) Inside the class, define the constructor method `__init__(self, max_speed, mileage)`:

# a) This method runs automatically when an object of the class is created.

# b) It takes two inputs: `max_speed` and `mileage`.

# 3) Store the passed values inside the object using instance variables:

# a) Assign `self.max_speed = max_speed`

# b) Assign `self.mileage = mileage`

# 4) Create an object of the `Vehicle` class named `modelX`

# by passing values for max speed and mileage: `Vehicle(240, 18)`.

# 5) Access the object’s instance variables and print them:

# a) Print `modelX.max_speed` as the model’s max speed.

# b) Print `modelX.mileage` as the model’s mileage.