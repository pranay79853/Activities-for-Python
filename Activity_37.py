# -------------------------------

# Square Pattern Boilerplate

# -------------------------------

# Step 1: Take input from the user
size = int(input("Enter the size of the square pattern: "))
# Step 2: Use an outer loop for rows
for i in range(size):
# Step 3: Use an inner loop for columns
    for j in range(size):
         print("*", end="")
# Step 4: Print stars on the same line
    print()
# Step 5: Move to the next line after one row is complete