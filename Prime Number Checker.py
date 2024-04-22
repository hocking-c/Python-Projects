# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)

# First we define our function called Prime_checker()
# We then define a variable called is_prime that by default will be set to True
# and set to False if the code detects it's not a prime number
# We must create a range and set the start of the range to 2
# because prime numbers can only be divided by themselves and 1 cleanly
# Setting the start of the range to 2 also means we do not need to increase the number by 1 at the end of our range
# We then create a for loop to loop through each of those numbers in the for loop
# And check our potential prime number, which is stored in the variable 'number' as the input to our function
# We check if we divided that potential prime number by the current number 'i' in our range, does it divide cleanly
# If any of the numbers in our range between 2 and our number,
# can substitute for 'i' and we end up with a remainder of 0 then it is clearly not a prime number
# so we set is_prime to False
# We then create an IF statement that says:
# ( if our is_prime variable is true, we print "Is a prime number", else we print "Is not a prime number"
