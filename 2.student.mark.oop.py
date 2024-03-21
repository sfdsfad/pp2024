class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def __str__(self):
        return f"{self.student_id}: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"{self.course_id}: {self.name}"


class StudentMarkSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def input_number_of_students(self):
        return int(input("Enter the number of students in the class: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth: ")
        return Student(student_id, name, dob)

    def input_number_of_courses(self):
        return int(input("Enter the number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        return Course(course_id, name)

    def input_student_marks(self):
        student_id = input("Enter student ID for marking: ")
        course_id = input("Enter course ID for marking: ")

        if student_id in self.students and course_id in self.courses:
            marks = float(input(f"Enter marks for {self.students[student_id].name}: "))
            self.students[student_id].input_marks(course_id, marks)
            print("Marks added successfully.")
        else:
            print("Invalid student or course ID.")

    def list_courses(self):
        print("\nList of Courses:")
        for course_id, course in self.courses.items():
            print(course)

    def list_students(self):
        print("\nList of Students:")
        for student_id, student in self.students.items():
            print(student)

    def show_student_marks(self):
        student_id = input("Enter student ID to show marks: ")

        if student_id in self.students:
            student = self.students[student_id]
            print(f"\nMarks for {student.name}:")
            
            for course_id, marks in student.marks.items():
                if course_id in self.courses:
                    course_name = self.courses[course_id].name
                    print(f"{course_id} ({course_name}): {marks}")
                else:
                    print(f"{course_id}: {marks} (Course information not found)")
        else:
            print("Invalid student ID.")

    def main(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            student = self.input_student_information()
            self.students[student.student_id] = student

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            course = self.input_course_information()
            self.courses[course.course_id] = course

        while True:
            print("\nStudent Mark Management System:")
            print("1. Input Student Marks")
            print("2. List Courses")
            print("3. List Students")
            print("4. Show Student Marks for a Course")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.input_student_marks()
            elif choice == "2":
                self.list_courses()
            elif choice == "3":
                self.list_students()
            elif choice == "4":
                self.show_student_marks()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    student_mark_system = StudentMarkSystem()
    student_mark_system.main()
