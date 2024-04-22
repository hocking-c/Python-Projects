# IF the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to Hocking's Tip Calculator!")
bill = float(input("What is the total bill? "))
people = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to give? 15, 20, 25? "))

dues = (bill / people) * (1 + (tip/100))
cleaned = round(dues, 2)

print(f"Each person should pay: ${cleaned}")
