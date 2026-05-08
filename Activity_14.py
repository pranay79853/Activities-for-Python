# 1) Store values in `a`, `b`, and `c`.
a = True
b = False
c = False
# 2) Check an AND condition using `a and b and c`:

# - This becomes True only if all three values are treated as True.

# - If the condition is True, print the “all true” message.

# - Otherwise, print the “at least one false” message.
if a and b and c:
    print("All are true.")
else:
    print("All are not true.")
# 3) Re-assign (change) new values to `a`, `b`, and `c` for the next checks.
a = -15
b = -90
c = 1
# 4) Check an OR condition: `a > 0 or b > 0`
if a > 0 or b > 0:
    print("Either is greater than 0.")
else:
    print("Neither of them is greater than 0.")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.

# 5) Check another OR condition: `b > 0 or c > 0`
if b > 0 or c > 0:
    print("Either is greater than 0.")
else:
    print("Neither of them is greater than 0.")
# - If at least one of them is greater than 0, print the “either is greater than 0” message.

# - Otherwise, print the “no number is greater than 0” message.