# 1) Print a heading message for the pattern.
print("Half Pyramid Pattern of Stars")
# 2) Take an integer input from the user and store it in `n`.
n = int(input("Enter the number of rows for the half pyramid: "))
# (This represents the number of rows in the half pyramid.)

# 3) Use an outer loop to run from 0 to `n-1` (each iteration builds one row):
for i in range(n):
    for j in range(i + 1):
        print("* ", end="")
    print()
# a) For each row `i`, the number of stars to print is `i + 1`.

# 4) Use an inner loop to print stars in the current row:

# a) Run `j` from 0 to `i` (total `i + 1` times)

# b) Print "* " on the same line using `end=""` so it doesn’t go to the next line.

# 5) After finishing the inner loop for a row, print a blank `print()`

# to move the cursor to the next line for the next row.