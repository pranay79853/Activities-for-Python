#1 Take a number as input from the user
num = int(input("Enter a number: "))
#2 sum_digits will store the total sum of all digits
sum_digits = 0
# 3 temp is a copy of num, so we don't change the original number
temp = num
#4 Loop runs until temp becomes 0 (means no digits are left)
while temp > 0:
# 4.a Get the last digit of the number
    digit = temp % 10
#4.b Add that digit to the sum
    sum_digits += digit
#4.c Remove the last digit from temp
    temp //= 10
# Print the final result
print(f"The sum of digits in {num} is {sum_digits}.")