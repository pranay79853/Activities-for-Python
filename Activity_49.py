# Write a factorial program using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
input_number = int(input("Enter a number to calculate its factorial: "))

print(factorial(input_number))