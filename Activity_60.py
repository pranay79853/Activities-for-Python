# 1) Create a list `L` with some integer values and print it as the original list.
L = [5, 2, 4, 3, 1]
print("Original List :", L)
count = 0
for i in L:
    count = count + i
average = count / len(L)
print("sum = ", count)
print("average = ", average)
print()
L.sort()
print("Ascending order: ", L)
print("Smallest element is:", L[0])
print("Largest element is:", L[-1])
# 2) Initialize a variable `count = 0` to store the sum of all elements in the list.

# 3) Use a `for` loop to iterate through each element `i` in the list `L`:

# a) Add each element to `count` using `count += i`.

# 4) Calculate the average of the list:

# a) Divide the total sum `count` by the number of elements `len(L)`.

# b) Store the result in `avg`.

# 5) Print the total sum and the average.

# 6) Sort the list `L` in ascending order using `L.sort()`.

# 7) After sorting:

# a) The smallest element will be at index 0 → print `L[0]`.

# b) The largest element will be at the last index → print `L[-1]`.