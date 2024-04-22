from random import randint
from art import logo_3

EASY_MODE_TURNS = 10
HARD_MODE_TURNS = 5


# Define a function to check the user's guess against the actual answer

# Track the number of turns remaining.

def check_answer(guess, answer, turns):
    """Checks answer against guess and returns numbers of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You've guessed the number! The answer was {answer}")


# Make a function set to difficulty
def set_difficulty():
    """Sets difficulty level based on user choice and determines number of guesses"""
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard':\n")
    if difficulty_level == "easy":
        return EASY_MODE_TURNS
    else:
        return HARD_MODE_TURNS


def game():
    print(logo_3)
    # Choose a random number between 1 and 100
    print("Welcome to my number guessing game!")
    print("I'm thinking of a number between and 1000")
    answer = randint(1, 1000)
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()


# Repeat the guessing functionality if the guess does not equal the random number selected
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Allow the player to submit a guess for a number between 1 and 100.
        guess = int(input("Make a guess.\n"))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()

# If they run out of turns, provide feedback to the player.


# play_again = input("Would you like to play again? Type 'Y' or 'N'\n")
