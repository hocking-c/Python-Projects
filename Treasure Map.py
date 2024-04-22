line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
letter_choice = position[0].upper()
abc = ("A", "B", "C")
letter_index = abc.index(letter_choice)

number_choice = position[1]
number_index = int(number_choice) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")
