# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5
# e.g. 15 then instead of the number it should print "FizzBuzz"

# Write your code here 👇
target = 100

for number in range(1, target+1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Define a variable called target and set it equal to 100
# Create a for loop for every number in the range from 1 to our target which is 100
# but to include the target we must do target +1 since our list starts at 0
# Set our for loop with an if statement that first tests if the number is divisible by BOTH 3 and 5
# Set that if statement to print "FizzBuzz"
# Create an elif statement that tests if the number is divisible by 3 but NOT by 5
# Set that elif statement to print "Fizz"
# Create another elif statement that tests if the number is divisible by 5 but NOT by 3
# Set that elif statement to print "Buzz"
