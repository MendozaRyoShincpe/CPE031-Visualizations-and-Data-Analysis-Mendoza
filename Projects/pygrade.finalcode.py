# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 00:54:40 2026

@author: Shin
"""

import os

# This class acts as a key information about the students to be entered.
class StudentInfo:

    def __init__(self):
        self.name = ""
        self.gender = ""
        self.id = 0
        self.quiz = 0.0
        self.recitation = 0.0
        self.exam = 0.0
        self.finalGrade = 0.0
        self.occupancy = False

# Student can be stored up to 100
studentSize = 100
students = [StudentInfo() for _ in range(studentSize)]
# It tracks the number of student records on the list. Initialized to 0 because no student are added at the beginning of the program.
counter = 0

#Acts to clear the terminal output
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# This function acts as the confirmation for the user.
def confirm_enter():
    while True:
        choice = input("Are you sure you want to enter? (Yes/No): ").strip().lower() #Make sure that the entered letter is it lowercase

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Please enter ONLY 'Yes' or 'No'.")

# This is the log in for the user, no password or pin code added to the instructor.
def userType():
    while True:
        user = input("Log in as Instructor or Student or Quit? (I/S/Q): ").upper()

        if user == 'I':
            if confirm_enter():
                professorMenu()
            else:
                print("Cancelled.\n")

        elif user == 'S':
            entry = studentUser()
            # Verify that the student ID is on the list
            verify = any(s.id == entry for s in students)

            if verify:
                studentMenu(entry)
            else:
                print("Student ID not found.")

        elif user == 'Q':
            print("Thank you for using the program.")
            break

        else:
            print("Invalid Input.")
            
# This is the professor manu which acts as the main interface of the program.
def professorMenu():
    while True:
        print("\nProfessor Menu")
        print("(1) - Add student")
        print("(2) - Edit student's Grade")
        print("(3) - Delete student Info")
        print("(4) - View student")
        print("(5) - Log-out")

        choice = int(input("Choose action: "))

        if choice == 1:
            add()
        elif choice == 2:
            edit()
        elif choice == 3:
            delete()
        elif choice == 4:
            view()
        elif choice == 5:
            return
        else:
            print("Invalid Action.")
            
# (1) Add Student
def add():
    global counter
    if counter >= studentSize:
        print("Cannot add more students. Maximum capacity reached.") # The maximum of students to enter is 100.
        return

    # Find the first available slot
    index = -1
    for i, s in enumerate(students):
        if not s.occupancy:
            index = i
            break

    if index == -1: # Should not happen if counter < studentSize, but good for safety
        print("No available slots found.")
        return

    new_student = students[index]

    # This are the information the the instructor needed to input in the program.

    new_student.name = input("Enter Student Name: ")


    while True:
        gender_input = input("Enter Student Gender (M/F): ").upper()
        if gender_input in ['M', 'F']:
            new_student.gender = gender_input
            break
        else:
            print("Invalid gender. Please enter 'M' or 'F'.")

    while True:
        try:
            student_id = int(input("Enter Student ID: "))
            # Check for uniqueness, so that student ID cannot be repeated
            if any(s.id == student_id and s.occupancy for s in students):
                print("Student ID already exists. Please enter a unique ID.")
            else:
                new_student.id = student_id
                break
        except ValueError:
            print("Invalid ID. Please enter a number.") # Error handling if the user enter a letter or any symbol.

    while True:
        try:
            quiz_grade = float(input("Enter Quiz Grade (0-100): "))
            if 0 <= quiz_grade <= 100:
                new_student.quiz = quiz_grade
                break
            else:
                print("Grade must be between 0 and 100.") # Error handling it entered less than 0 or greater than 100
        except ValueError:
            print("Invalid input. Please enter a number.") # Error handling if the user enter a letter or any symbol.

    while True:
        try:
            recitation_grade = float(input("Enter Recitation Grade (0-100): "))
            if 0 <= recitation_grade <= 100:
                new_student.recitation = recitation_grade
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.") # Error handling if the user enter a letter or any symbol.

    while True:
        try:
            exam_grade = float(input("Enter Exam Grade (0-100): "))
            if 0 <= exam_grade <= 100:
                new_student.exam = exam_grade
                break
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.") # Error hanling if the user enter a letter or any symbol.

    new_student.finalGrade = (new_student.quiz * 0.40) + (new_student.recitation * 0.10) + (new_student.exam * 0.50) # 40% Quiz, 10% Recitation, 50% Exam
    new_student.occupancy = True
    counter += 1
    print("Student added successfully!")

# (2) Edit Student Grades
def edit():
    student_id = int(input("Enter Student ID to edit: "))
    # Checks if the student ID is on the list
    index = next((i for i, s in enumerate(students) if s.id == student_id), -1)

    if index == -1:
        print("Student not found.") # If the student ID is not on the list
        return

    s = students[index]
    
    # User will enter a number if the user will edit the grade, user should type '-1' if the grade will be keep.
    new = float(input(f"Quiz ({s.quiz}) new or -1 to keep: "))
    if new != -1:
        s.quiz = new

    new = float(input(f"Recitation ({s.recitation}) new or -1 to keep: "))
    if new != -1:
        s.recitation = new

    new = float(input(f"Exam ({s.exam}) new or -1 to keep: "))
    if new != -1:
        s.exam = new

    s.finalGrade = s.quiz * 0.40 + s.recitation * 0.10 + s.exam * 0.50 

    print("Updated successfully!")
    
# (3) Delete Student Info
def delete():
    global counter

    student_id = int(input("Enter Student ID to delete: ")) #User should know the student ID per student

    index = next((i for i, s in enumerate(students) if s.id == student_id), -1)

    if index == -1:
        print("Student not found.")
        return

    confirm = input("Are you sure? (Y/N): ").upper()

    if confirm == 'Y':
        students[index] = StudentInfo()
        counter -= 1
        print("Deleted successfully.")
    else:
        print("Cancelled.")

# (4) View Students
def view():
    print("(1) View by Names (Alphabetical)")
    print("(2) View by Grades (Highest to Lowest)")

    choice = int(input("Choose: "))

    if choice == 1:
        sorted_list = sorted([s for s in students if s.occupancy], key=lambda x: x.name) # Will arranged the names Alphabetically.
    elif choice == 2:
        sorted_list = sorted([s for s in students if s.occupancy], key=lambda x: x.finalGrade, reverse=True) # Highest to lowest Grade
    else:
        print("Invalid.")
        return

    display(sorted_list)
    
def display(data):
    # Adjusted widths for consistent alignment
    print(f"\n{'Name':<15}{'Gender':<8}{'ID':<12}{'Quiz':<10}{'Recitation':<12}{'Exam':<10}{'Final':<10}")
    print("*" * 77)  # Adjusted separator length to match total width

    for s in data:
        # Format grades to two decimal places
        print(f"{s.name:<15}{s.gender:<8}{s.id:<12}{s.quiz:<10.2f}{s.recitation:<12.2f}{s.exam:<10.2f}{s.finalGrade:<10.2f}")

    print("*" * 77)  # Closing separator

# Student Section
def studentUser():
    return int(input("Enter Student ID: "))

# Student Menu
def studentMenu(student_id):
    index = next((i for i, s in enumerate(students) if s.id == student_id), -1)

    if index == -1:
        print("Student not found.") # Incorrect Student Number or not in the list
        return

    while True:
        print("\nStudent Menu")
        print("(1) View Grades")
        print("(2) Log-out")

        choice = int(input("Choose: "))

        if choice == 1:
            studentView(index)
        elif choice == 2:
            return
        else:
            print("Invalid.")

# Student can view their own grade

def studentView(index):
    s = students[index]
    1
    # Using f-string formatting with fixed widths for proper alignment
    print(f"\n{'Name':<20}{'Gender':<6} {'ID':<5}{'Quiz':<7}{'Recitation':<10}{'Exam':<7}{'Final':<7}")
    print("-" * 63) # Adjust separator length to match column widths
    # Ensure grades are formatted to two decimal places for consistency
    print(f"{s.name:<20}{s.gender:<6} {s.id:<5}{s.quiz:<7.2f}{s.recitation:<10.2f}{s.exam:<7.2f}{s.finalGrade:<7.2f}")
    print("-" * 63)

# Will go back the program to the Login Interface
if __name__ == "__main__":
    userType()