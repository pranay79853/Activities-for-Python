# 1) Create variables to store different types of values:

# - `name` as text (string)
Name = "Pranay"
# - `age` as a whole number (integer)
Age = 11
# - `is_student` as True/False (boolean)
is_student = True
# - `weight` as a decimal number (float)
Weight = 37.0
# 2) Print each variable’s value.
print(Name)
print(Age)
# 3) Print the datatype of each variable using `type()`.
print(type(Name))
print(type(Age))
print(type(is_student))
print(type(Weight))
# 4) Show a message that type casting will happen next.
print("Typecasting")
# 5) Convert `age` from an integer to a string and store it back in `age`.

age = str(Age)
# 6) Print `age` and print its datatype again to confirm it changed.
print(age)
print(type(age))
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
weight =int(Weight) 
# 8) Print `weight` and print its datatype again to confirm it changed.
print(type(weight))