# 1) Ask the user to enter height in centimeters

height = float(input("Enter your height in cm: "))

# 2) Ask the user to enter weight in kilograms

weight = float(input("Enter your weight in kg: "))

# 3) Convert height into meters

height_in_meter = height / 100

# Calculate BMI

# Formula: weight / (height in meters)^2

BMI = weight / (height_in_meter ** 2)

# 4) Print BMI value

print("Your BMI is:", BMI)

# 5) Check BMI category

if BMI <= 18.4:
    print("underweight")

elif BMI <= 24.9:
    print("healthy")

elif BMI <= 29.9:
    print("over weight")

elif BMI <= 34.9:
    print("severely over weight")

elif BMI <= 39.9:
    print("obese")

else:
    print("severely obese")