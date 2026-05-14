# 1) Ask the user to enter the number of terms and store it in `n`.
n = int(input("Enter the number of terms: "))
# 2) Initialize `sum` to 0.
sum = 0
# (This will store the running total.)

# 3) Initialize `i` to 1.
i = 1
# (This is the first number we will add.)

# 4) Repeat while `i` is less than or equal to `n`:
while i <= n:
    sum += i
    i += 1
# a) Add `i` to `sum`.

# b) Increase `i` by 1 to move to the next number.

# 5) After the loop ends, print the final value of `sum`.
print("The sum of the first", n, "terms is:", sum)