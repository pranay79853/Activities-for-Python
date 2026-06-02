# Write a program to understand how value error exception is working

try:
    number = int(input("Enter a number: "))
    print("Entered number is: ", number)

except ValueError as ex:
    print("Entered number is ", ex)