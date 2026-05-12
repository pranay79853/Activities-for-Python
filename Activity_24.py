# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.
unit = float(input("Enter the number of electricity units consumed: "))
# 2) Use if–elif–else to decide the cost based on `units`:
surcharge = 0
amount = 0
# - If `units` is less than 50:
if unit < 50:
    amount = unit * 2.60
    surcharge = 25
# - Else if `units` is 100 or less:
elif unit <= 100:
    amount = (50 * 2.60) + ((unit - 50) * 3.25)
    surcharge = 35
# - Else if `units` is 200 or less:
elif unit <= 200:
    amount = (50 * 2.60) + (50 * 3.25) + ((unit - 100) * 5.26)
    surcharge = 45
# - Else (units more than 200):
else:
    amount = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + ((unit - 200) * 8.45)
    surcharge = 75

# 3) Calculate the final bill:
total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places.
print(f"Your electricity bill is: ${total:.2f}")
# Set `amount` as units × 2.60 and set `surcharge` as 25.

# - Else if `units` is 100 or less:

# Set `amount` as (cost for first 50 units) + (remaining units × 3.25)

# Set `surcharge` as 35.

# - Else if `units` is 200 or less:

# Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)

# Set `surcharge` as 45.

# - Else (units more than 200):

# Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)

# Set `surcharge` as 75.

# 3) Calculate the final bill:

# total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places.