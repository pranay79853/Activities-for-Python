# Write a Python program to create a class named Point. The class should contain:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
p1 = Point(2, 3)
print(p1)
# A constructor (__init__) to initialize the coordinates x and y.

# A function that returns the coordinates in Point format (x, y).

# Create an object of the Point class by passing values for x and y, and print the point coordinates.