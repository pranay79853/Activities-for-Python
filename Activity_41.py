# 1) Import the `turtle` library to draw shapes on a screen.
import turtle
# 2) Set up the turtle drawing screen:
turtle.bgcolor("cyan")
turtle.setup(width = 600, height = 600)
# a) Change the background color to "orange".

# b) Set the screen size using `setup(width, height)`.

# 3) Create a Turtle object and store it in `polygon`.
polygon = turtle.Turtle()
polygon.color("orange")
polygon.pencolor("red")
polygon.fillcolor("blue")
# (This turtle will do the drawing.)

# 4) Store polygon details in variables:

# a) `num_sides` = number of sides of the polygon (here, 6).
num_sides = 6
# b) `side_length` = length of each side.
side_length = 100
# c) Calculate the turning angle using `angle = 360.0 / num_sides`.
angle = 360.0 / num_sides
polygon.penup()
polygon.goto(-side_length / 2, side_length * (3 ** 0.5) / 2)
polygon.pendown()
polygon.begin_fill()
# 5) Use a loop to draw the polygon:
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
polygon.end_fill()
# a) Repeat `num_sides` times.

# b) Move the turtle forward by `side_length`.

# c) Turn the turtle right by `angle` degrees after each side.

# 6) Call `turtle.done()` to keep the turtle window open after drawing finishes.
turtle.done()