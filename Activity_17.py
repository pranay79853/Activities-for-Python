# Python program to illustrate the use
x = 5
# of 'is' identity operator
if (type(x) is int):
    print("This number is a integer.")

else:
    print("This number is not a integer.")

x = 5.5
if (type(x) is float):
    print("This number is a decimal.")

else:
    print("This number is not a decimal.")

x = 20
y = 20
if (x is y):
    print("X and Y are the same identity.")

else:
    print("X and Y are not the same identity.")