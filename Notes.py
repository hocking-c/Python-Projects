# # Print Statements
#  print("Day - 1 Python Print Function")
#  print("The function is declared like this:")
#  print("print('what to print')")
#
# # Debugging Practice
# print('Day 1 - String Manipulation')
# print('String Concatenation is done with the "+" sign.')
# print('e.g print("Hello " + "world")')
# print("New lines can be created with a  backslash and n.")
#
# # Input Statements
# # input() will get user input in console
#
# # Print() will then print the word within the () followed by the user input()
# print("Hello " + input("What is your name? ") + "!")
#
# # Test Input statements
# input("What is your favorite car? ") + input("Why is it your favorite car? \n")
# print('Thanks, just one more question if you dont mind.\n')
# input("Do you happen to enjoy fishing at all? \n")
# print("Thanks for sharing your thoughts!")
#
# print("Hello " + input("What is your name? "))
# print("Don't worry!") + input("What is your ultimate goal here? \n")
# print("Thanks" + input("What is your favorite color? "))
#
# # Clean print inputs
# Name1 = input("What is your name? ")
# print(Name1) # This line will print the text and line 1 of the input and output
# Name2 = input()
# def vars():" "
# print(Name1 +" " + Name2) # This line will print the text and line 2 of input into output
#
# # When changing a variable the new value will replace the old value
#
# # There are two variables, a and b from input[a = 29 b = 41]
# a = input()
# b = input()
# # Write some code that will switch inputs of variable a and variable b in the input console
# c = a
# a = b
# b = c
# # Don't write below this code (statements for reference)
# print("a" + a)
# print("b" + b)
#
# #We must define a third variable 'c' to store the value of 'a' while we redefine 'a' and 'b'
#
# # Data Types ( Type Checking and character placement)
# print(type(input())) # Type checking will print type of variable
# #Important to use type checking when using concatenation as different variables cannot be concatenated
#
# # 1st method
# two_digit_number = input()
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# two_digit_number = int(first_digit) + int(second_digit)
# print(two_digit_number)
#
# #2nd Method
# two_digit_number = input()
# first_digit = input(two_digit_number[0])
# second_digit = input(two_digit_number[1])
# two_digit_number = first_digit + second_digit
# print(two_digit_number)
#
# # Band Name Generator
# #1. Create a greeting for your program
# print("Welcome to the band name generator!")
# #2. Ask the user for the city that they grew up in.
# city = input("What city did you grow up in?\n")
# #3. Ask the user for the name of a pet.
# pet = input("What is the name of a pet?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print("Your band name could be " + city + " " + pet)
# #5 Make sure the input cursor shows on a new line, see the example at:
# # http://band-name-generator-end.appbrewery.repl.run/
#
# # Data Types (Strings are expressed with "double quotes")
# #(Integers are expressed as whole numbers)
# #(Floats are numbers expressed as decimals)
# #(Boolean is a true false argument)
# # converting an integer into a string
# num_char = len(input("What is your name?\n"))
# new_num_char = str(num_char)
# print("Your name contains " + new_num_char + "characters.")
# a = float(123)
# print(type(a))
# print(70 + float("100.5"))
# print(str(70) + str(100))
#
# # Mathematical Operations
# 3 + 5
# 7 - 4
# 3 * 2
# 6 / 3
# 2 ** 3
#
# PEMDAS
# #Calculation furthest to the left takes priority between multiplication and division
# ()
# **
# * /
# + -
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -
#
# print(3 * 3 + 3 / 3 - 3) << How can you change this line of code to get it to result, 3 instead of 7
# print(3 * (3 + 3) / 3 - 3)
#
# # BMI Calculator Activity 1.0
# # 1st input: enter height in meters e.g: 1.65
# height = input()
# # 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# heightBMI = float(height)
# weightBMI = float(weight)
# print(int(weightBMI/(heightBMI*heightBMI)))
#
#         OR
# heightBMI = float(height)
# weightBMI = int(weight)
# print(weightBMI/(heightBMI**2))
#
# # Using the exponent
#
#
# # Life in Weeks Exercise
# Instructions
# Create a program using maths and f-Strings that tells
# us how many weeks we have left, if we live until 90 years old.
# It will take your current age as the input and output a message
# with our time left in this format:
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks
# the input age has left until age 90.
#
# Warning your output should match the Example Output format
# exactly, even the positions of the commas and full stops.
#
# Example Input
# 56
#
# Example Output
# You have 1768 weeks left.
#
# age = input()
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# # My solution which passed
# Ending_Age = 90
# Current_Age = int(age)
# Time_Left_Years = Ending_Age - Current_Age
# X = int(Time_Left_Years*52)
# print(f"You have {X} weeks left.")
#
# # Auditorium Solution
# age = input()
# # Your code below this line 👇
# years = 90 - int(age)
# weeks = years * 52
#
# print(f"You have {weeks} weeks left.")
#
#
#
# #If the bill was $150.00, split between 5 people, with 12% tip
# print("Welcome to the tip calculator!")
#
# B = float(input("What is the total bill? "))
# P = int(input("How many people are splitting the bill? "))
# T = int(input("What percentage tip would you like to give: 10, 12, 15, 20? "))
#
# #Each person should pay ( 150.00 / 5) * 1.12 = 33.6
#
# Split_dues = (B/P) * (1 + (T/100))
#
# #Format the result to 2 decimal places = 33.60
# Split_dues = round(Split_dues, 2)
# #Tip: There are 2 ways to round a number {variable: .2f} would mean the floating variable (f) gets rounded (2) places
#
# print(f"Each person should pay: ${Split_dues:.2f}")
#
# #The function uses a variable that was created to represent how much each person owes on a bill after tip
# #I needed to define my variables first:
# # as the total bill includes a decimal it will be a float
# # as the total number of people the bill is split between a whole number it will be an integer
# # as the total % tip being paid is going to be represented by a whole number, we use an integer here
# # Define a new variable to represent a functional equation with our newly created variables
# # We must format our new variable to reflect rounding to 2 decimal places
# # Our final print function uses an f string to allow for concatenating different variables [ string and float ]
#
# B = float(input("What is the total bill? "))
# P = int(input("How many people are splitting the bill? "))
# T = int(input("What percentage tip would you like to give: 10, 12, 15, 20? "))
# tip_as_percent = T / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = B + total_tip_amount
# bill_per_person = total_bill / P
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")
#
# # If Else and Conditional Operators
# if condition:
#     do this
# else:
#     show this
# # Bathtub example
# water_level = 50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")
#
# # Roller Coaster Height Requirements
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
#
# if height > 120:
#     print("You can ride the roller coaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")
#
# # Nested if / else statements
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this
#
# # Roller Coaster Height Requirement and Ticket pricing nested if and elif functions
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the roller coaster!")
#     age = input("What is your age? ")
#     if age <= 12:
#         print("Your ticket will be $5.00")
#     elif age <= 18:
#         print("Your ticket will be $7.00")
#     else:
#         print("Your ticket will be $12.00")
# else:
#     print("Sorry you need to grow taller before you can ride.")
#
#
# # BMI Exercise Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# BMI Formula = weight / (height * height)
#
# Important: you do not need to round the result to the nearest whole number.
# It('s fine to print out a floating point number for this exercise.
#
# Example Input 1
# 1.50
# 63
# Example Output 1
# Your BMI is 28.0, you are slightly overweight.
# since 63 ÷ (1.50 x 1.50) = 28
#
# The testing code will check for print output that is formatted like one of the lines below:
#
# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."
#
# # My Solution below:
# # Enter your height in meters e.g., 1.55
# height = float(input())
# # Enter your weight in kilograms e.g., 72
# weight = int(input())
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# bmi = weight / (height * height)
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight.")
# elif bmi < 25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi < 30:
#   print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif bmi < 35:
#   print(f"Your BMI is {bmi}, you are obese.")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese.")
#
#
# # Leap Year Exercise
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.
# This is how you work out whether if a particular year is a leap year:
# *on every year that is divisible by 4 with no remainder*
# * except every year that is evenly divisible by 100 with no remainder*
# * unless the year is also divisible by 400 with no remainder*
# # Which year do you want to check?
# # Instructor's solution
# year = int(input())
#
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year")
#     else:
#       print("Not leap year")
#   else:
#     print("Leap year")
# else:
#   print("Not leap year")
#
# # My solution
# year = int(input())
#
# if year % 4 == 0:
#   if year % 100 > 0:
#     print("Leap year")
#   elif year % 400 > 0:
#     print("Not leap year")
# else:
#     print("Not leap year")
#
#
#
# # Pizza Order Practice Exercise
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# *Small pizza (S): $15
# *Medium pizza (M): $20
# *Large pizza (L): $25
# *Add pepperoni for *small pizza (Y or N): +$2
# *Add pepperoni for *medium or *large pizza (Y or N): +$3
# *Add extra cheese for *any size pizza (Y or N): +$1
#
# Example Input
#     L
#     Y
#     N
#
# Example Output
# Thank you for choosing Python Pizza Deliveries!
# Your final bill is: $28.
#
# # My solution
# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25
#
# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3
#
# if extra_cheese == "Y":
#   bill += 1
#
# print(f"Your final bill is: ${bill}.")
#
#
#
# # Roller Coaster Exercise
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the roller coaster")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#     wants_photo = input("Do you want a photo taken? Y or No. ")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is {bill}.")
# else:
#     print("Sorry but you need to grow taller before you can ride the roller coaster.")
#
#
# # True Love exercise
#
# print("The Love Calculator is calculating your score...")
# name1 = input() # What is your name?
# name2 = input() # What is their name?
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# combined_names = name1 + name2
# lower_names  = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and  (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")
#
#
# # Banker Roulette Exercise
#
# names = names_string.split(", ")
# # The code above converts the input into an array separating
# # each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
#
# # Always import random module first
# import random
#
# # Define variable & calculate number of items in list w/ len()
# num_items = len(names)
#
# # Define second variable between 0 and last index
# # random module using random integer first position 0
# # and num_items set to -1 because len() calculates total length
# # and therefore starts at 0, whereas all lists start at 0
# random_pick = random.randint(0, num_items - 1)
#
# # Pick out payer name from list of names using the random pick
# payer_name = names[random_pick]
#
# # Final print statement
# print(payer_name + " is going to buy the meal today!")
#
# # Pycharm Solution
#
# import random
# import string
# names_string = str(input())
# names = names_string.split(", ")
#
# num_items = len(names)
#
# random_pick = random.randint(0, num_items - 1)
#
# payer_name = names[random_pick]
#
# print(payer_name + " is going to buy the meal today!")
#
#
# # Treasure map exercise
#
# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?
# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) - 1
# map[number_index][letter_index] = "X"
#
# print(f"{line1}\n{line2}\n{line3}")
#
#
#
#  # Rock Paper Scissors Exercise
# import random
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# # Write your code below this line
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# if user_choice > 2 or user_choice < 0:
#     print("You have typed an invalid number,")
# else:
#     print("You chose:")
#     if user_choice == 0:
#         print(rock)
#     elif user_choice == 1:
#         print(paper)
#     elif user_choice == 2:
#         print(scissors)
#
# print("Computer Chose:")
# computer_choice = random.randint(0, 2)
# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# elif computer_choice == 2:
#     print(scissors)
#
# if user_choice == 0 and computer_choice == 0:
#     print("Wow, it's a draw!")
# elif user_choice == 0 and computer_choice == 1:
#     print("Oh no, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("Congratulations, you win!")
#
# if user_choice == 1 and computer_choice == 1:
#     print("Wow, it's a draw!")
# elif user_choice == 1 and computer_choice == 0:
#     print("Congratulations, you win!")
# elif user_choice == 1 and computer_choice == 2:
#     print("Oh no, you lose!")
#
# if user_choice == 2 and computer_choice == 2:
#     print("Wow, it's a draw!")
# elif user_choice == 2 and computer_choice == 1:
#     print("Congratulations, you win!")
# elif user_choice == 2 and computer_choice == 0:
#     print("Oh no, you lose!")
#
#
# # Adding Even Numbers
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to X.
# If X is 100 then the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.
#
# # Given input variable
# target = int(input())                   # Enter a number between 0 and 1000
# even_sum = 0                            # Starting variable that will act as our cumulator - we will add to it as the input works through the range to get the final sum
# for number in range(2, target + 1, 2):  # For loop to loop through each number in the range starting with 2, which is the first even number
#     even_sum += number                  # the end of our range will be our target variable + 1, so the input itself is included
# print(even_sum)                         # As default, the end of a range will stop at the input and not include it
#                                         # Next we redefine our variable to equal itself + the new number our for loop catches ( += )
#                                         # Make sure that the print statement is not indented and aligns with our first line of code
#
# #An alternative solution would be as presented below
# target = int(input())                   # Enter a number between 0 and 1000
# alternative_sum = 0                     # Starting variable that will act as our cumulator - we will add to it as the input works through the range to get the final sum
# for number in range(2, target + 1):     # For loop to loop through each number in the range starting with 2, which is the first even number
#     if number % 2 == 0:                 # the end of our range will be our target variable + 1, so the input itself is included (we will not include an increment in this iteration)
#         alternative_sum += number       # As default, the end of a range will stop at the input and not include it
# print(alternative_sum)                  # Next we redefine our variable to equal itself + the new number our for loop catches ( += )
#                                         # Make sure that the print statement is not indented and aligns with our first line of code
#
# # FizzBuzz Game Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz":
# e.g. it might start off like this:
#
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
#
# # Write your code here 👇
# # My Solution
# target = 100
# for number in range(1, target + 1):
#   if number % 3 == 0 and number % 5 > 0:
#     print("Fizz")
#   elif number % 5 == 0 and number % 3 > 0:
#     print("Buzz")
#   elif number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   else:
#     print(number)
#
#     # Teacher Solution
#     target = 100
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)
#
# # 2 Flavors of For Loops
#
#     for item in list_of_items:
#        Do something to each item in the list
#
#     for number in range(a, b):
#         print(number)
#
# # Password Generator Exercise
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like in your password?\n"))
# nr_numbers = int(input("How many numbers would you like in your password?\n"))
#
#
#
#
# # Reeborg's World
# # Hurdle 3 Solutions
#
# # My Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while not at_goal() == True:
#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         jump()
#
# # Course Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
# while wall_in_front():
#     jump()
# else:
#     move()
#
# # Hurdle 4 Solutions
#
# # My Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while not at_goal():
#     if wall_on_right() != True:
#         turn_right()
#         move()
#     elif wall_in_front():
#         turn_left()
#     elif wall_on_right():
#         move()
#     else:
#         move()
#
# # Course Solution
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear ():
#         move()
#     turn_left()
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# # Functions and Outputs
#
# def format_name(f_name, l_name):
#     """Take a first and last name and format it to return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"
#
# print(format_name(input("What is your first name? "), input("What is your last name? ")))

# formatted_string = format_name("cOreY", "HOcKinG")
# # print(formatted_string)
# import random
#
# age = random.randint(1,12)
# name = input("What is your dog's name?\n")
#
# def dog_info(age,name):
#     print(f"Your dog, {name}, is awfully energetic for {age} years old.")
# dog_info(age,name)

#
#
# def caps_string(text):
#     return text.upper()
# print(caps_string("Corey"))
#
# names = ['Nick', 'Jane', 'Sarah']
#
# for name in names:
#     print(caps_string(name))
#
# user_text = input('What is your name?\n')
# print(user_text.upper())
# user_number = input('What do you want to double?')
#
# print(int(user_number) * 2)
# new_user_text = input('Please provide a statement. Type "1" for uppercase or "2" for lowercase')
#
# if new_user_text == "1":
#     print(new_user_text.upper())
# else:
#     print(new_user_text.lower())



















import random
import time

print("I am going to select a number between 1 and 100 - good luck!")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
attempts = 0

while guess != correct_number:
        time.sleep(1)
        attempts += 1
        if guess > correct_number:
                print("Try guessing lower.")
        else:
                print("Try guessing higher.")
        guess = int(input("What is your guess?: "))


print(f"""Well done! It took you {attempts} attempts, but you
managed to guess {guess} and the correct number was {correct_number}.""")
