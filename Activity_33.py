# Step 1: Take a number from the user
number = int(input("Enter a number: "))
# Step 2: Store the original number
original = number
# We need this later to compare

# Step 3: Create a variable for reversed number
reverse_number = 0
# At start, reverse number is 0

# Step 4: Run loop until temp becomes 0
while number > 0:
# Step 5: Get the last digit of temp
    last_digit = number % 10
# Step 6: Add this digit to rev
    reverse_number = reverse_number * 10 + last_digit
# Example: if rev = 12 and rem = 1

# rev becomes 121

# Step 7: Remove the last digit from temp
    number = number // 10
# Step 8: Compare original number and reversed number
if original == reverse_number:
    print("This number is a palindrome number.")
else:
    print("This number is not a palindrome number.")