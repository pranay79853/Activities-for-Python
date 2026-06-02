# 1) Create a class named `pair_elements`.

class pair_elements:
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i
value = int(input("Enter the target sum: "))
result = pair_elements().twoSum((10, 20, 30, 40, 50, 60, 70), value)
if result:
    print(f"index1={result[0]}, index2={result[1]}")
else:
    print("No two numbers found whose sum equals the target.")

# 3) Create an empty dictionary `lookup = {}`.

# (This will store numbers as keys and their indexes as values for quick searching.)

# 4) Use a loop with `enumerate(nums)` to iterate through `nums`:

# a) `i` gives the index of the current element.

# b) `num` gives the value at that index.

# 5) For each number, check if the required pair exists:

# a) Compute `target - num`.

# b) If `target - num` is already present in `lookup`,

# return a tuple containing:

# - the index of the matching number from `lookup`

# - the current index `i`

# 6) If the pair is not found yet, store the current number and its index:

# a) `lookup[num] = i`

# 7) Take an integer input from the user and store it in `value`.

# (This is the target sum to search for.)

# 8) Call the method `twoSum()` using:

# a) the tuple `(10, 20, 30, 40, 50, 60, 70)` as `nums`

# b) `value` as the `target`

# 9) Print the two indexes returned by `twoSum()` in the format:

# "index1=..., index2=..."