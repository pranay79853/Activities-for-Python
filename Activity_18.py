# Grading system
print("Enter Marks Obtained in 5 Subjects: ")
markOne = int(input())

markTwo = int(input())

markThree = int(input())

markFour = int(input())

markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive

avg = int(tot / 5)

validRange = range(0,101)

if avg not in validRange:
    print("Invalid Input!")

elif avg in range(91, 101):
    print("Your grade is A1.")

elif avg in range(81, 91):
    print("Your grade is A2.")

elif avg in range(71, 81):
    print("Your grade is B1.")

elif avg in range(61, 71):
    print("Your grade is B2.")

elif avg in range(51, 61):
    print("Your grade is C1.")

elif avg in range(41, 51):
    print("Your grade is C2.")

elif avg in range(33, 41):
    print("Your grade is D.")

elif avg in range(0, 33):
    print("Your grade is E.")