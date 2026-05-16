num = int(input("Enter an integer: "))

# Also copy the same value into `t` for digit counting.
t = num

# 2) Initialize `numLen = 0` to count the number of digits.
numLen = 0

# 3) Count the digits using a loop
while t > 0:
    numLen += 1
    t = int(t / 10)

# 4) Check if the number has at least 4 digits
if numLen >= 4:

    numLen = int(numLen / 2)
    chk = 0

    while num > 0:

        rem = num % 10

        if chk == numLen:
            midOne = rem

        elif chk == (numLen - 1):
            midTwo = rem

        num = int(num / 10)
        chk = chk + 1

    prod = midOne * midTwo

    print("\nProduct of Mid digits (" +
          str(midOne) + "*" + str(midTwo) + ") = ", prod)

else:
    print("\nIt's not a 4 or more than 4-digit number!")