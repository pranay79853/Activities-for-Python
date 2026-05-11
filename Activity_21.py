# 1) Store the given values:

# `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.
mean1 = 5
wrong_number = 10
correct_number = 15
total_number = 20
# 2) Calculate the total sum using the wrong mean:
wrong_sum = mean1 * total_number
# - Multiply `mean1` by `total_number`
mean1 * total_number
# - Store it in `sum`
sum = mean1 * total_number
# - Print the sum.
print(sum)
# 3) Fix the sum to get the correct total:
sum2 = sum - wrong_number + correct_number
# - Remove the wrong number (subtract `wrong_number`)
subtract_wrong = sum - wrong_number
# - Store the result in `num1`
num1 = sum - wrong_number
# - Add the correct number (add `correct_number`)
add_correct = num1 + correct_number
# - Store the corrected total in `num2`
num2 = num1 + correct_number
# - Print the corrected sum.
print(num2)
# 4) Find the correct mean:
mean2 = num2 / total_number
# - Divide `num2` by `total_number`
num2 / total_number
# - Store it in `mean2`
mean2 = num2 / total_number
# - Print `mean2`.
print(mean2)