# 1) Create a parent class named `Bird`.

class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# 2) Define the constructor `__init__(self)` in `Bird`:

# a) Print "Bird is ready" when a Bird object (or child object) is created.

# 3) Define a method `whoisThis(self)` in `Bird`:

# a) Print "Bird".

# 4) Define a method `swim(self)` in `Bird`:

# a) Print "Swim faster".

# 5) Create a child class named `Penguin` that inherits from `Bird`.

# 6) Define the constructor `__init__(self)` in `Penguin`:

# a) Use `super().__init__()` to call the parent class constructor.

# (This runs the Bird initialization first.)

# b) Print "Penguin is ready" after the parent constructor runs.

# 7) Override the method `whoisThis(self)` in `Penguin`:

# a) Print "Penguin".

# (This replaces the parent version for Penguin objects.)

# 8) Define a new method `run(self)` in `Penguin`:

# a) Print "Run faster".

# (This method exists only in the child class.)

# 9) Create an object `peggy` of the `Penguin` class.

# (This will call Penguin’s constructor, which also calls Bird’s constructor.)

# 10) Call methods using the object:

# a) `peggy.whoisThis()` prints "Penguin" (overridden method).

# b) `peggy.swim()` prints "Swim faster" (inherited from Bird).

# c) `peggy.run()` prints "Run faster" (child class method).