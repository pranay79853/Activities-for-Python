# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).

def add(P, Q):
    return P + Q

# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).

def subtract(P, Q):
    return P - Q

# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).

def multiply(P, Q):
    return P * Q

# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).

def divide(P, Q):
    if Q != 0:
        return P / Q
    else:
        return "Error: Division by zero is not allowed."
    
# 5) Display a menu to the user showing the available operations:

# a) Add

# b) Subtract

# c) Multiply

# d) Divide

# 6) Take the user's choice as input and store it in `choice`.

choice = input("Choose an operation:\na) Addition\nb) Subtraction\nc) Multiplication\nd) Division\nEnter your choice (a/b/c/d): ")
# 7) Take two integer inputs from the user:
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))

# a) Store the first number in `num_1`

num_1 = input_1

# b) Store the second number in `num_2`

num_2 = input_2

# 8) Use conditional statements to perform the chosen operation:

# a) If `choice` is 'a', call `add(num_1, num_2)` and print the result.

if choice == 'a':
    result = add(num_1, num_2)
    print(f"The result of addition is: {result}")

# b) Else if `choice` is 'b', call `subtract(num_1, num_2)` and print the result.

elif choice == 'b':
    result = subtract(num_1, num_2)
    print(f"The result of subtraction is: {result}")

# c) Else if `choice` is 'c', call `multiply(num_1, num_2)` and print the result.

elif choice == 'c':
    result = multiply(num_1, num_2)
    print(f"The result of multiplication is: {result}")

# d) Else if `choice` is 'd', call `divide(num_1, num_2)` and print the result.

elif choice == 'd':
    result = divide(num_1, num_2)
    print(f"The result of division is: {result}")

# 9) If the user enters anything other than a/b/c/d, print an invalid input message.

else:
    print("Invalid input. Please enter a valid operation (a/b/c/d).")