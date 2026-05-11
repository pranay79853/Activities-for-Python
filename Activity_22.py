# 1) Take three integer inputs from the user and store them in `a`, `b`, and `c`.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
# 2) Calculate the average of `a`, `b`, and `c`:
average = (a + b + c) / 3
# - Add them and divide by 3

# - Store the result in `avg`

# - Print `avg`
print(average)
# 3) Compare `avg` with `a`, `b`, and `c` using if–elif:
if average > a and average > b and average > c:
    print(f"{average} is higher than {a}, {b}, and {c}")
# - If `avg` is greater than all three numbers, print that it is higher than `a`, `b`, and `c`.
elif average > a and average > b:
    print(f"{average} is higher than {a} and {b}")
# - Else if `avg` is greater than `a` and `b`, print that it is higher than `a` and `b`.
elif average > a and average > c:
    print(f"{average} is higher than {a} and {c}")
# - Else if `avg` is greater than `a` and `c`, print that it is higher than `a` and `c`.
elif average > b and average > c:
    print(f"{average} is higher than {b} and {c}")
# - Else if `avg` is greater than `b` and `c`, print that it is higher than `b` and `c`.
elif average > a:
    print(f"{average} is just higher than {a}")
# - Else if `avg` is greater than only `a`, print that it is just higher than `a`.
elif average > b:
    print(f"{average} is just higher than {b}")
# - Else if `avg` is greater than only `b`, print that it is just higher than `b`.
elif average > c:
    print(f"{average} is just higher than {c}")
# - Else if `avg` is greater than only `c`, print that it is just higher than `c`.
else:
    print("invalid input")
# 4) If none of the above conditions match, print "invalid input".