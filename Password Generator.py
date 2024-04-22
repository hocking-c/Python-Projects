# Password Generator Project
import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Night Hawk's Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
amount_numbers = int(input(f"How many numbers would you like?\n"))

# My first solution

rand_let = random.sample(letters, num_letters)
rand_num = random.sample(numbers, amount_numbers)
rand_sym = random.sample(symbols, num_symbols)
combined_list = rand_let + rand_num + rand_sym
random.shuffle(combined_list)
password = ""
for char in combined_list:
  password += char
print(f"Your password is: {password}")


# My Alt Solution
password = ""
for letter in range(0,num_letters):
    password += random.choice(letters)
for symbol in range(0, num_symbols):
    password += random.choice(symbols)
for number in range(0, amount_numbers):
    password += random.choice(numbers)
print(f"Your password could be: {password}")


# GigaChad Solution
random_letters = random.choices(letters, k=num_letters)
random_numbers = random.choices(numbers, k=amount_numbers)
random_symbols = random.choices(symbols, k=num_symbols)
random_list = random_letters + random_numbers + random_symbols
random.shuffle(random_list)
password = ''.join(random_list)
print(f"Your password could be: {password}")




# Parameter	Description
# random.choices(sequence, weights=None, cum_weights=None, k=1)
# sequence	Required. A sequence like a list, a tuple, a range of numbers etc.
# weights	Optional. A list were you can weigh the possibility for each value.
# cum_weights	Optional. A list were you can weigh the possibility for each value, only this time the possibility is accumulated.
# Example: normal weights list: [2, 1, 1] is the same as this cum_weights list; [2, 3, 4].
# Default None
# k	Optional. An integer defining the length of the returned list
# random.choice(list)	Choose a random item from a sequence. Here seq can be a list, tuple, string, or any iterable like range.
# random.choices(list, k=3)	Choose multiple random items from a list, set, or any data structure.
# random.choice(range(1, 100))	Pick a single random number from range 1 to 100
# random.getrandbits(1)	Returns a random boolean
# random.choice(list(dict1))	Choose a random key from a dictionary
# np.random.choice()	Return random choice from a multidimensional array
# secrets.choice(list1)	Choose a random item from the list securely
# Common String Methods - Syntax
# string.digits - Returns the string '0123456789'
# string.ascii_lowercase- Returns the string 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase- Returns the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters - Returns a string containing all of the uppercase and lowercase letters.
# string.punctuation - Returns the string '!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'.