# 1) Create two sets S1 and S2 with some elements
S1 = ["A", "B", "C", "D"]
S2 = ['1', '2', '3', '4']

# 2) Use Zip (S1, S2) and convert to list

S3 = zip(S1, S2)

# 3) Print the zipped pairs

print(list(S3))

# 4) Create two lists

L1 = [10, 20, 30, 40]

L2 = [1, 2, 3, 4]

# 5) Pair elements with reversed second list
print("Pairing List 1 with reversed List 2:")
for x, y in zip(L1, L2[::-1]):
    print(x, y)