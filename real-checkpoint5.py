import numpy as np

# Ask the user for the number of students and the number of subjects
num_students = int(input("Enter the number of students: "))
num_subjects = int(input("Enter the number of subjects: "))

# Create an empty NumPy array to store the marks
marks = np.empty((num_students, num_subjects), dtype=int)

# Ask the user to enter marks for each student in each subject
for i in range(num_students):
    marks[i] = np.array([int(x) for x in input(f"Enter marks for student {i + 1} in {num_subjects} subjects, separated by spaces: ").split()])

# Calculate total marks for each student using sum() function
total_marks = np.sum(marks, axis=1)

# Calculate the percentage for each student
percentage = (total_marks / (num_subjects * 100)) * 100

# Calculate the grade for each student
grades = np.select([percentage >= 90, percentage >= 80, percentage >= 70, percentage >= 60, percentage >= 50],
                   ["A+", "A", "B+", "B", "C"], default="F")

# Display the result in a tabular format
print("\nStudent\tTotal Marks\tPercentage\tGrade")
for i in range(num_students):
    print(f"Student {i + 1}\t{total_marks[i]}\t\t{percentage[i]:.2f}%\t\t{grades[i]}")


