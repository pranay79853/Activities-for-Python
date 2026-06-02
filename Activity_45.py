# Write a program to display weather condition in Autumn and Spring

def weather_condition(season):
    if season == "Autumn":
        print("The weather condition in Autumn is cool and windy.")
    elif season == "Spring":
        print("The weather condition in Spring is mild and pleasant.")
    elif season == "Summer":
        print("The weather condition in Summer is hot and sunny.")
    elif season == "Winter":
        print("The weather condition in Winter is cold and snowy.")
    elif season == "Pre-Monsoon":
        print("The weather condition in Pre-Monsoon is hot and humid.")
    elif season == "Monsoon":
        print("The weather condition in Monsoon is rainy and humid.")
    elif season == "Post-Monsoon":
        print("The weather condition in Post-Monsoon is cool and dry.")
    elif season == "Pre-Winter":
        print("The weather condition in Pre-Winter is cold and dry.")
    else:
        print("Invalid season. Please enter either 'Autumn' or 'Spring' or 'Summer' or 'Winter' or 'Pre-Monsoon' or 'Monsoon' or 'Post-Monsoon' or 'Pre-Winter'.")

# Call the function

season = input("Enter the season (Autumn/Spring/Summer/Winter/Pre-Monsoon/Monsoon/Post-Monsoon/Pre-Winter): ").title()
weather_condition(season)