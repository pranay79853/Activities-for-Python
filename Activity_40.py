# 1) Take an integer input from the user and store it in `rowSize`.
#    (This represents the total height of the diamond pattern.)

rowSize = int(input("Enter the row size: "))

# 2) Decide how many rows the top half of the diamond should have:
#    a) If `rowSize` is even, set `halfDiamRow = rowSize/2`
#    b) If `rowSize` is odd, set `halfDiamRow = rowSize/2 + 1`
#    (This ensures the middle row is included in the upper half.)

if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = rowSize // 2 + 1

# 3) Initialize `space = halfDiamRow - 1`.
#    (This controls leading spaces before printing numbers in the upper half.)

space = halfDiamRow - 1

# 4) Print the upper half of the diamond:
#    a) Use an outer loop `i` from 1 to `halfDiamRow` (inclusive) for rows.

for i in range(1, halfDiamRow + 1):

    #    b) For each row:
    #       i) Print `space` number of blank spaces using an inner loop.

    for j in range(space):
        print(" ", end="")

    #       ii) Decrease `space` by 1 after printing spaces.

    space -= 1

    #       iii) Set `num = 1` to start printing numbers from 1 in that row.

    num = 1

    #       iv) Print `(2*i - 1)` numbers in the row using another inner loop:
    #           - Print the current `num` without moving to the next line.
    #           - Increase `num` by 1 after each print.

    for j in range(1, 2 * i):
        print(num, end="")
        num += 1

    #       v) Print a newline to move to the next row.

    print()

# 5) Reset `space = 1` for the lower half of the diamond.
#    (Now spaces increase as we go downward.)

space = 1

# 6) Print the lower half of the diamond:
#    a) Use an outer loop `i` from 1 to `halfDiamRow - 1` for rows.

for i in range(1, halfDiamRow):

    #    b) For each row:
    #       i) Print `space` number of blank spaces using an inner loop.

    for j in range(space):
        print(" ", end="")

    #       ii) Increase `space` by 1 after printing spaces.

    space += 1

    #       iii) Set `num = 1` to start printing numbers from 1 in that row.

    num = 1

    #       iv) Print `2*(halfDiamRow - i) - 1` numbers using an inner loop:
    #           - Print the current `num` without moving to the next line.
    #           - Increase `num` by 1 after each print.

    for j in range(1, 2 * (halfDiamRow - i)):
        print(num, end="")
        num += 1

    #       v) Print a newline to move to the next row.

    print()