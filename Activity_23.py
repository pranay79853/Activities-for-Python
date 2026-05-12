# 1) Ask the student if they had a medical cause and store the answer in `medical_cause`.
medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper()
# (Also clean the input so it becomes either 'Y' or 'N'.)

# 2) If `medical_cause` is 'Y':
if medical_cause == 'Y':
    print("You are allowed to attend the exam.\n Good Luck!")
# - Print that the student is allowed to attend the exam.

# 3) Otherwise (medical_cause is 'N'):
else:
    print("Please inform us about your attendance percentage.")
    atten  = float(input("Enter your attendance percentage:"))
    if atten >= 75:
        print("You are qualified to attend the exam.\n Good Luck!")
    else:
        print("You are not allowed to attend the exam. \nPlease try to improve your attendance for the next exam.")
# a) Ask for the student’s attendance percentage and store it in `atten`.

# b) If `atten` is 75 or more:

# - Print "Allowed"

# c) Else:

# - Print "Not allowed"