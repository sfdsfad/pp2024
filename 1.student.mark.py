def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth: ")
    return {"id": student_id, "name": name, "dob": dob}

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_student_marks(students, courses):
    student_id = input("Enter student ID for marking: ")
    course_id = input("Enter course ID for marking: ")

    if student_id not in students or course_id not in courses:
        print("Invalid student or course ID.")
        return

    marks = float(input("Enter marks for {}: ".format(students[student_id]["name"])))
    students[student_id]["marks"][course_id] = marks
    print("Marks added successfully.")

def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course_info in courses.items():
        print(f"{course_id}: {course_info['name']}")

def list_students(students):
    print("\nList of Students:")
    for student_id, student_info in students.items():
        print(f"{student_id}: {student_info['name']}")

def show_student_marks(students):
    student_id = input("Enter student ID to show marks: ")
    if student_id in students:
        student_info = students[student_id]
        print(f"\nMarks for {student_info['name']}:")
        for course_id, marks in student_info["marks"].items():
            print(f"{course_id}: {marks}")
    else:
        print("Invalid student ID.")

def main():
    students = {}
    courses = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student_info = input_student_information()
        students[student_info["id"]] = {"name": student_info["name"], "dob": student_info["dob"], "marks": {}}

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_info = input_course_information()
        courses[course_info["id"]] = {"name": course_info["name"]}

    while True:
        print("\nStudent Mark Management System:")
        print("1. Input Student Marks")
        print("2. List Courses")
        print("3. List Students")
        print("4. Show Student Marks for a Course")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            input_student_marks(students, courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            list_students(students)
        elif choice == "4":
            show_student_marks(students)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
