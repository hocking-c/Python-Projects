# Instructions
# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill._
# Important: You are not allowed to use the choice() function.
# Line 1 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

names = names_string.split(", ")
# The code above converts the input into an array separating
# each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

# Always import random module first
import random

# Define variable & calculate number of items in list w/ len()
num_items = len(names)

# Define second variable between 0 and last index
# random module using random integer first position 0
# and num_items set to -1 because len() calculates total length
# and therefore starts at 0, whereas we want total items but not to include 0
random_pick = random.randint(0, num_items - 1)

# Pick out payer name from list of names using the random pick
payer_name = names[random_pick]

# Final print statement
print(payer_name + " is going to buy the meal today!")
