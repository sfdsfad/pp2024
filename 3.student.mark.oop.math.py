import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course_id, marks):
        self.marks[course_id] = math.floor(marks * 10) / 10  # Round down to 1 decimal place

    def calculate_gpa(self, courses):
        total_marks = 0
        total_credits = 0
        for course_id, marks in self.marks.items():
            if course_id in courses:
                total_marks += marks * courses[course_id].credits
                total_credits += courses[course_id].credits
        if total_credits != 0:
            return total_marks / total_credits
        else:
            return 0

    def __str__(self):
        return f"{self.student_id}: {self.name}, DoB: {self.dob}, GPA: {self.gpa:.2f}"


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"{self.course_id}: {self.name}, Credits: {self.credits}"


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    students = {}
    courses = {}

    def input_number_of_students():
        stdscr.addstr("Enter the number of students in the class: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def input_student_information():
        stdscr.addstr("Enter student ID: ")
        stdscr.refresh()
        student_id = stdscr.getstr().decode()
        stdscr.addstr("Enter student name: ")
        stdscr.refresh()
        name = stdscr.getstr().decode()
        stdscr.addstr("Enter student Date of Birth: ")
        stdscr.refresh()
        dob = stdscr.getstr().decode()
        return Student(student_id, name, dob)

    def input_number_of_courses():
        stdscr.addstr("Enter the number of courses: ")
        stdscr.refresh()
        return int(stdscr.getstr().decode())

    def input_course_information():
        stdscr.addstr("Enter course ID: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()
        stdscr.addstr("Enter course name: ")
        stdscr.refresh()
        name = stdscr.getstr().decode()
        stdscr.addstr("Enter course credits: ")
        stdscr.refresh()
        credits = int(stdscr.getstr().decode())
        return Course(course_id, name, credits)

    def input_student_marks():
        stdscr.addstr("Enter student ID for marking: ")
        stdscr.refresh()
        student_id = stdscr.getstr().decode()
        stdscr.addstr("Enter course ID for marking: ")
        stdscr.refresh()
        course_id = stdscr.getstr().decode()

        if student_id in students and course_id in courses:
            stdscr.addstr(f"Enter marks for {students[student_id].name}: ")
            stdscr.refresh()
            marks = float(stdscr.getstr().decode())
            students[student_id].input_marks(course_id, marks)
            stdscr.addstr("Marks added successfully.\n")
        else:
            stdscr.addstr("Invalid student or course ID.\n")

    def calculate_student_gpas():
        for student_id, student in students.items():
            student.gpa = student.calculate_gpa(courses)

    def list_courses():
        stdscr.addstr("\nList of Courses:\n")
        for course_id, course in courses.items():
            stdscr.addstr(str(course) + "\n")
        stdscr.refresh()

    def list_students():
        stdscr.addstr("\nList of Students:\n")
        for student_id, student in students.items():
            stdscr.addstr(str(student) + "\n")
        stdscr.refresh()

    def show_student_marks():
        stdscr.addstr("Enter student ID to show marks: ")
        stdscr.refresh()
        student_id = stdscr.getstr().decode()

        if student_id in students:
            student = students[student_id]
            stdscr.addstr(f"\nMarks for {student.name}:\n")
            
            for course_id, marks in student.marks.items():
                if course_id in courses:
                    course_name = courses[course_id].name
                    stdscr.addstr(f"{course_id} ({course_name}): {marks}\n")
                else:
                    stdscr.addstr(f"{course_id}: {marks} (Course information not found)\n")
        else:
            stdscr.addstr("Invalid student ID.\n")
        stdscr.refresh()

    def sort_students_by_gpa():
        nonlocal students
        students = {k: v for k, v in sorted(students.items(), key=lambda item: item[1].gpa, reverse=True)}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student = input_student_information()
        students[student.student_id] = student

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course = input_course_information()
        courses[course.course_id] = course

    calculate_student_gpas()
    sort_students_by_gpa()

    while True:
        stdscr.addstr("\nStudent Mark Management System:\n")
        stdscr.addstr("1. Input Student Marks\n")
        stdscr.addstr("2. List Courses\n")
        stdscr.addstr("3. List Students\n")
        stdscr.addstr("4. Show Student Marks for a Course\n")
        stdscr.addstr("5. Exit\n")
        stdscr.addstr("Enter your choice (1-5): ")
        stdscr.refresh()

        choice = stdscr.getstr().decode()

        if choice == "1":
            input_student_marks()
            calculate_student_gpas()
            sort_students_by_gpa()
        elif choice == "2":
            list_courses()
        elif choice == "3":
            list_students()
        elif choice == "4":
            show_student_marks()
        elif choice == "5":
            stdscr.addstr("Exiting the program. Goodbye!\n")
            stdscr.refresh()
            break
        else:
            stdscr.addstr("Invalid choice. Please enter a number between 1 and 5.\n")
            stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(main)
