students_score = {
  "Thomas" : 57,
  "James": 80,
  "Jane": 95,
  "Lucas": 65
}

# Do not change the code above ☝️
#################################################################

# TODO 1: Create an empty dictionary, students_grade

# TODO 2: Add each student name from students_score dictionary as the key 
#         and the value is the grade of the student



#################################################################
# Do not change the code below ️️
students_grade = {}

for name in students_score:
  score = students_score[name]
  if (score >= 80):
    grade = "A"
  elif (score >= 60 and score <= 79):
    grade = "B"
  elif (score >= 55 and score <= 59):
    grade = "C"
  elif (score >= 50 and score <= 54):
    grade = "D"
  else:
    grade = "F"

  students_grade[name] = grade

print(students_grade)