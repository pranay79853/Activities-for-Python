# 1) Create a dictionary `test_dict` with words as keys and numbers as values.
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print(test_dict)
K = int(input("Enter the number whose frequency you want to check: "))
result = 0
for key in test_dict:
    if test_dict[key] == K:
        result = result + 1
print(f"Frequency of {K}: {result}")
# 2) Print the original dictionary.

# 3) Store the target value to search for in `K`.

# (Here, K = 2.)

# 4) Initialize a counter `res = 0` to count how many keys have the value `K`.

# 5) Use a `for` loop to iterate through each `key` in the dictionary:

# a) Check if the value of the current key `test_dict[key]` is equal to `K`.

# b) If yes, increase the counter `res` by 1.

# 6) After the loop finishes, print the final count `res`

# which represents the frequency of value `K` in the dictionary.