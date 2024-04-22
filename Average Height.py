# You are going to write a program that calculates the average student height from a List of heights.
# student_heights = [180, 124, 165, 173, 189, 169, 146]

# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer.
# You should try to replicate their functionality using what you have learnt about for loops.
#
# Example Input 1
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
#
# Example Output 1
# total height = 857
# number of students = 5
# average height = 171

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
Total_height = 0
for height in student_heights:
    Total_height += height
print(f"total height = {Total_height}")

Number_students = 0
for student in student_heights:
    Number_students += 1
print(f"number of students = {Number_students}")

Average_height = round(Total_height / Number_students)
print(f"average height = {Average_height}")

# Create a variable for total height
# Create a for loop for each height in the student_heights list
# Define the for loop to add each height in the list of student heights to the new variable, total_height
# Print the total height variable
# Create another variable for Number of students
# Create a for loop for each student in the student_heights list
# Define the for loop to add 1 student to the new variable called Number_of_students
# Print the total number of students variable
# Define another variable called Average_height and
# set it equal to the total height / number of students, rounding it with round()
# Print the Average height variable
