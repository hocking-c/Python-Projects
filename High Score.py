# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example.
# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
#
# Example Output
# The highest score in the class is: 91
# Input a list of student scores

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
print(f"The highest score in the class is: {highest_score}")

# Create a variable called highest_score and set it equal to 0
# Create a for loop for each score in the student_scores list
# Define the for loop with an IF statement ( if score > highest score )
# then the highest_score will therefore equal that score
# Print the highest score variable
