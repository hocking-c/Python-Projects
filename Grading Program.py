# You have access to a database of student_scores in the format of a dictionary.
# The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program;
# You should have a new dictionary called student_grades
# that should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.
# DO NOT modify lines 1-7 to change the existing student_scores dictionary.
# DO NOT write any print statements.

# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

# Create an empty dictionary called student_grades {} - this is what we will fill up using our program
# Create a for loop that loops through the dictionary of student_scores so we can get a hold of each key in that dictionary 1 by 1
# In order to access that student's score, we have to use the corresponding key on the student scores dictionary
# We set the for loop with a new variable that is equal to the student_scores dictionary where we pass in each student name as the 'key'
# Now when our For loop runs, the first time our score will equal the first key of the dictionary [Harry] = 81, and so on...
# We then write our IF ELIF ELSE statements where we use the criteria in the decription pane to determine how each score will be interpreted
# Each statement will account for a score i.e if score > 90 , take our empty dictionary student_grades, and take square brackets []
# to assign the student 'key' from the student_scores dictionary and set it equal to a value which will equal their grade