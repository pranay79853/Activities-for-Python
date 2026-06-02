# Define a function to find a cube

def cube(num):
    return num ** 3

# Define another function which lets execute the cube function if the number is divisible by 3.

def check_divisible(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return "The number is not divisible by 3."
input_num = int(input("Enter a number: "))
print(check_divisible(input_num))