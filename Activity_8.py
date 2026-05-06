# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
maths = 95
english = 98
science = 91
hindi = 70 
# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum = maths + english + science + hindi
# 3) Print the total marks stored in `sum`.
print("The total marks obtained", sum)
# 4) Calculate the percentage:
sum /= 400
# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)
print("sum", sum*100)
# - Multiply the result by 100
percentage = sum*100
# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.
print("percentage", percentage)