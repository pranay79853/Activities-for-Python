# 1) Import the `random` module to let the computer make a random choice.

import random

# 2) Start an infinite loop using `while True` so the game can repeat for multiple rounds.

while True:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ").lower()
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chosed {user_action}, Computer chosed {computer_action}.\n")
    if user_action == computer_action:
        print("You and Computer have come to a draw.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You won! Paper defeats Rock.")
        if computer_action == "scissors":
            print("Computer won! Scissor defeats Paper.")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You won! Rock defeats Scissors.")
        if computer_action == "paper":
            print("Computer won! Paper defeats Rock.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You won! Scissors defeats Paper.")
        if computer_action == "rock":
            print("Computer won! Rock defeats Scissors.")
    else:
        print("Invalid Input! Enter the correct options.")
        
# 3) Take the user's choice as input and store it in `user_action`.

# (Expected inputs: "rock", "paper", or "scissors".)

# 4) Create a list `possible_actions` containing the three valid moves.

# 5) Use `random.choice(possible_actions)` to randomly select the computer’s move

# and store it in `computer_action`.

# 6) Display both choices (user and computer) using an f-string.

# 7) Compare `user_action` and `computer_action` to decide the result:

# a) If both are the same, print that it’s a tie.

# b) Else if the user chose "rock":

# i) If computer chose "scissors", user wins.

# ii) Otherwise, user loses (computer chose "paper").

# c) Else if the user chose "paper":

# i) If computer chose "rock", user wins.

# ii) Otherwise, user loses (computer chose "scissors").

# d) Else if the user chose "scissors":

# i) If computer chose "paper", user wins.

# ii) Otherwise, user loses (computer chose "rock").

# 8) After showing the result, ask the user if they want to play again

# and store the input in `play_again`.

# 9) If `play_again` is not "y", stop the game using `break`.

# Otherwise, the loop continues and a new round starts.