Instructions
You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".
Generate a random number, either 0 or 1.
Then use that number to print out "Heads" or "Tails".

e.g. 1 means Heads 0 means Tails

Example Output
Heads
or
Tails
----------------------------------------------------------------------------------------------------------------
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

random_pick = random.randint(0,1)
if random_pick == 0:
    print("Tails")
else:
    print("Heads")