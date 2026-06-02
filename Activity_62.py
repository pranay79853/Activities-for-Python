# 1) Define a function `palind(r)` to check whether a tuple is a palindrome

def palind(r):
    if r == tuple(reversed(r)):
        print("This number is a palindrome.")
    else:
        print("This number is not a palindrome.")
        palind(r)
t = tuple(map(int, input("Enter elements separated by space: ").split()))
palind((1, 2, 3, 3, 2, 1))

# (meaning it reads the same forward and backward).

# 2) Inside the function:

# a) Set `e = len(r) - 1` to point to the last index of the tuple.

# b) Set `s = 0` to point to the first index of the tuple.

# 3) Use a `while` loop to compare elements from both ends:

# a) Repeat while `s < e`.

# b) If the element at the start `r[s]` is not equal to the element at the end `r[e]`,

# return False immediately (not a palindrome).

# c) Move the start pointer forward using `s += 1`.

# d) Move the end pointer backward using `e -= 1`.

# 4) If the loop finishes without mismatches, return True.

# (This means the tuple is a palindrome.)

# 5) Create a tuple `r = (1, 2, 3, 3, 2, 1)`.

# 6) Call the function `palind(r)`:

# a) If it returns True, print "The Tuple is Flip-Flop".

# b) Otherwise, print "The Tuple is not Flip-Flop".