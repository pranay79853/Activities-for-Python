# 1) Create two lists `Number_1` and `Number_2` containing integer values.

Number_1 = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(Number_1)
Number_2 = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(Number_2)
result = map(lambda x, y: x + y, Number_1, Number_2)
print(result)
print(list(result))
Numbers = [2, 4, 6, 8]
def Square(n):
    return n * n
Square_1 = list(map(Square, Numbers))
print(Square_1)
print("Square of numbers in list")

# 2) Use `map()` with a `lambda` function to add corresponding elements:

# a) The lambda takes two inputs `x` and `y`.

# b) It returns `x + y`.

# c) `map()` applies this to each pair from `numbers1` and `numbers2`

# and stores the mapped result in `result`.

# 3) Print a heading message: "Addition of two lists".

# 4) Convert the `map` object into a list using `list(result)` and print the final added list.

# 5) Create a list `nums` containing numbers to demonstrate `map()` again.

# 6) Define a function `sq(n)` that returns the square of a number (`n * n`).

# 7) Use `map(sq, nums)` to apply the `sq` function to every element in `nums`:

# a) Convert the result into a list and store it in `square`.

# 8) Print a heading message: "Square of numbers in list"

# and print the list `square`.