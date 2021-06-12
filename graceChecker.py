student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇

for i in student_scores:
    for j in student_scores.values():
        student_grades[i] = student_scores[i]
        if student_scores[i] < 71:
            student_grades[i] = "Fail"
        elif 71 <= student_scores[i] <= 80:
            student_grades[i] = "Acceptable"
        elif 81 <= student_scores[i] <= 90:
            student_grades[i] = "Exceeds Expectations"
        elif 91 <= student_scores[i] <= 100:
            student_grades[i] = "Outstanding"
# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)

# Write your code above this line 👆
# 🚨 Do NOT modify the code below this line 👇
