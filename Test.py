# Add function and subtract function
def add(a, b):
    try:
        return a + b
    except ValueError:
        print("Value Error Occured!")
    except ZeroDivisionError:
        print("You can't add with Zero.")

def subtract(a, b):
    try:
        return a - b
    except ValueError:
        print("Value Error Occured!")
    except ZeroDivisionError:
        print("You can't subtract with Zero.")

def multiply(a, b):
    try:
        return a * b
    except ValueError:
        print("Value Error Occured!")
    except ZeroDivisionError:
        print("You can't subtract with Zero.")

def divide(a, b):
    try:
        return a / b
    except ValueError:
        print("Value Error Occured!")
    except ZeroDivisionError:
        print("You can't subtract with Zero.")

# Write a menu

input_one = input(("Enter the operation you want to choose: ")).lower()
input_two = float(input("Enter the first number:"))
input_three = float(input("Enter the second number: "))

if input_one == "add":
    print(add(input_two, input_three))

if input_one == "subtract":
    print(subtract(input_two, input_three))

if input_one == "multiply":
    print(multiply(input_two, input_three))

if input_one == "divide":
    print(divide(input_two, input_three))