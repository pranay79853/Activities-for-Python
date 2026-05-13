# 1) Ask the user to enter a word or sentence and store it in `string`.
string1 = input("Enter a word or sentence: ")
# 2) Create an empty string called `string2`.
string2 = ""
# (This will store the reversed version.)

# 3) Loop through each character `i` in `string`:
for i in string1:
    string2 = i + string2
# - Add the character `i` in front of `string2`
print(string2)
# - This builds the reversed string step by step.

# 4) Print the original string (`string`).
print("Original string:", string1)
# 5) Print the reversed string (`string2`).
print("Reversed string:", string2)