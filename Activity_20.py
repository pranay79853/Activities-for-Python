# 1) Ask the user to enter the numerator and store it in `numn`.
numn = int(input("Enter the numerator: "))
# 2) Ask the user to enter the denominator and store it in `numd`.
numd = int(input("Enter the denominator: "))
# 3) Check if `numn` is divisible by `numd`:
numn % numd == 0
# - Find the remainder when `numn` is divided by `numd`.
if numn % numd == 0:
    print(f"{numn} is divisible by {numd}.")
else:
    print(f"{numn} is not divisible by {numd}.")