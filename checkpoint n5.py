import  numpy as np
from tabulate import tabulate
num_students = int(input("Enter the number of students: ")) #   takes number of students 
num_subjects = int(input("Enter the number of subjects: "))# takes number of subjects
marks = np.zeros((num_students, num_subjects), dtype=int) # uses the numpy zeros function 
#to store number of students and number of subjects
for i in range(num_students):
    print(f"Enter marks for Student {i + 1}:") # we did i plus one because i starts with 0
    for j in range(num_subjects):
        marks[i][j] = int(input(f"Enter marks for Subject {j + 1}: ")) # iterate over the student marks and couple it with the subject 
total_marks = np.sum(marks) # does the sum of all marks 
percentage = (total_marks / (num_subjects * 100)) * 100 # Calculates the  percentage of the grades
print(percentage)

grades = []
if percentage >= 90:
    grades.append('A+') 
if percentage >= 80:
    grades.append('A') 
if percentage >= 70:
    grades.append('B+')
if percentage >= 60:
    grades.append('B')   
if percentage >= 50:
    grades.append('C')
if percentage  <= 50:
    grades.append('F')
data = []    
for i in range(num_students):
    data.append([f"Student {i + 1}", total_marks, f"{percentage:.2f}%", grades[0]])
headers = ["Student", "Total Marks", "Percentage", "Grade"]
table = tabulate(data,headers,tablefmt='grid')
print(table)