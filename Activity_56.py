# 1) Import the `random` module to generate random numbers.

import random

# 2) Create a variable `playing = True` to control the game loop.

playing = True

# 3) Generate a random number between 0 and 9 using `random.randint(0, 9)`

integer_one = random.randint(0, 9)

# and convert it to a string, then store it in `number`.

number = str(integer_one)

# (This is the secret number the user must guess.)

# 4) Print instructions explaining the guessing game.

print("Welcome to the Number Guessing Game!")
print("Guess a number between 0 and 9.")

# 5) Start a `while` loop that runs as long as `playing` is True:

while playing == True:
    guess = input(("Enter a number: "))
    if number == guess:
        print("Congratulations! You guessed correctly.")
        print("The secret number was:", number)
        break
    else:
        print("Wrong guess! Good Luck next time")
        
# a) Take a guess from the user and store it in `guess`.

# 6) Check if the user's guess matches the secret number:

# a) If `number == guess`:

# i) Print a winning message.

# ii) Display the secret number.

# iii) Stop the loop using `break` (game ends).

# 7) Otherwise (if the guess is incorrect):

# a) Print a message telling the user to try again.

# b) The loop continues and asks for another guess.