# 1) Store values in `a`, `b`, and `c`.
a = 45
b = 18
c = 7
# 2) Check if `a` is not equal to `b` using `!=` and print the result (True/False).
if a != b:
    print("A and B are not equal.")
else:
    print("A and B are equal.")
# 3) Check if `b` is not equal to `c` using `!=` and print the result (True/False).
if b != c:
    print("True")
else:
    print("False")
# 4) Store two strings in `a` and `b`.
a = "I live on Earth."
b = "I live on Earth."
# 5) If `a` is not equal to `b`, print a message saying they are different.
if a != b:
    print("A and B are different.")
else:
    print("A and B are the same.")
# 6) Store new numeric values in `a` and `b`.
a = 15
b = 25
# 7) Check this condition: (a equals 1) is not the same as (b equals 5).
if (a == 1) != (b == 5):
    print("A and B are not equal")
else:
    print("A and B are equal")
# - If exactly one of these comparisons is True, the condition becomes True.

# - If the condition is True, print "Hello".

# 8) Take an integer input from the user and store it in `a`.
a = int(input("Enter a number: "))
# 9) Check if `a` is not divisible by 2 (remainder is not 0).
if a % 2 == 0:
    print("The given number is a even number.")
else:
    print("The given number is a odd number.")
# - If true, print that `a` is not an even number (it is odd).