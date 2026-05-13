# 1) Ask the user to enter a number (greater than 1) and store it in `n`.
n = int(input("Enter a number greater than 1: "))
print("Numbers from", n, "to 1:")
# 2) Print a message saying you will display numbers from `n` down to 1.

# 3) Use a `for` loop that starts from `n`, goes down to 1, and decreases by 1 each time.
for i in range(n, 0, -1):
    print(i)
# 4) Inside the loop, print the current value of `i` (so numbers appear in reverse order).