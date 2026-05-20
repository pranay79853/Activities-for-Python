# 1) Take a word input from the user and store it in `a`.
a = input("Enter a word: ")
b = input("Enter a character to search for: ")
# 2) Use a `for` loop to iterate through each character `i` in the word `a`.
for i in a:
    if i == b.lower() or i == b.upper():
        print(f'"{b}" is found')
        break
    else:
        print(f'"{b}" not found')
# 3) For each character, check if it is equal to 'A':

# a) If `i == 'A'`, print "A is found".

# b) Use `break` to stop the loop immediately after finding 'A'.

# 4) If the current character is not 'A', print "A not found".

# (This message prints for each character until 'A' is found or the loop ends.)