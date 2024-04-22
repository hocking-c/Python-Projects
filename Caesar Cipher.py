# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# #
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# # Try not to name arguments and parameters with the same name ( e.g text becomes plain_text and shift becomes shift_amount)
# # When we send the input to this function we will be sending the text to plain_text and the shift to shift_amount
# # Keeping the names of the argument and the parameter different will help us later on to see which one is which
# # We start by creating an empty string variable called Cipher_text which we will build onto with our encryption
# # Then we begin writing a for loop that loops through each of the letters in the plain_text input
# # Position > We then take each of the plain text letters and work out their position in the list we titled alphabet
# # We tap into the list with the variable list name example and then tap into the index of the list
# # Alphabet is the list . index () and inside the parentheses we put our letter
# # New Position > We simply take our current position and add the shift amount to it
# # New Letter > We set our new letter variable = the alphabet list at the [new position]
# # With that empty cipher text variable we will add each new letter via the variable new_letter
# # Finally we print the output with an f string and display the encoded text as 'cipher text'
# #TODO-2: Inside the encr'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text. [We use the ( + ) key]
#

# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text=text, shift_amount=shift)
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# # Because the first text we will be working with is scrambled (cipher text) we will call our text parameter cipher_text and the second parameter will remain the shift_amount
# # We can start by creating a blank string variable which we will name plain_text and add each new letter to it
# # Create a for loop to loop through each letter of cipher_text
# # Inside the loop we want to 1) get a hold of the position of that letter in the alphabet list
# # We then want to 2) get a hold of that new position by taking our current position and subtracting the shift_amount which will shift the letters backwards as requested
# # Once we have a new position we fetch our new letter again by defining a new variable called new letter and setting it to the new_position of the list [alphabet] e.g alphabet[new_position]
# # Finally we can print the output with an f string and using the plan_text variable to express the decoded message
# #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text [We use the ( - ) key]
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The decoded text is {plain_text}")
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z'
            ]

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo_1
print(logo_1)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_continue = False
        print("Goodbye")