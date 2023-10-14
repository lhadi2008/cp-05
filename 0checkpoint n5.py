import numpy as np

# Ask the user for the number of students and subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create an empty NumPy array to store marks
marks = np.empty((num_students, num_subjects), dtype=int)

# Ask the user to enter marks for each student in each subject
for i in range(num_students):
    for j in range(num_subjects):
        marks[i, j] = int(input(f"Enter marks for student {i + 1}, subject {j + 1}: "))

# Calculate total marks for each student using sum() function
total_marks = np.sum(marks, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Calculate the grade for each student
grades = []
for p in percentage:
    if p >= 90:
        grades.append("A+")
    elif p >= 80:
        grades.append("A")
    elif p >= 70:
        grades.append("B+")
    elif p >= 60:
        grades.append("B")
    elif p >= 50:
        grades.append("C")
    else:
        grades.append("F")

# Display the result in a tabular format
print("\nStudent\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"Student {i + 1}\t{total_marks[i]}\t\t{percentage[i]:.2f}%\t\t{grades[i]}")
