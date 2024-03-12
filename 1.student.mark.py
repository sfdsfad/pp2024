def input_num_of_students():
    num_of_student = input("Enter number of students: ")
    return int(num_of_student)

def input_one_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student DOB: ")
    student = {
        'id': student_id,
        'name': name,
        'dob': dob
    }
    return student

def input_num_of_courses():
    num_of_course = input("Enter number of courses: ")
    return int(num_of_course)

def inputOneCourse(): 
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    course = {
        'id': course_id,
        'name': course_name
    }
    return course

def selectCourseAndInputStudentMarks(course, students):
    print(f"Enter marks for student in course {course,['name']}")
    marks = {}
    marks[course['id']] = []
    for student in students:
        mark = float(input(f"Enter marks for student {student['name']}"))
        marks[course['id']] = {}
        studentMark = {
            'studentid': student['id'],
            'mark': mark
        }
        marks[course['id']] += [studentMark]

def list_courses(courses):
    print("\nList of courses:")
    for course in courses:
        print(f"{course['id']}: {course['name']}")

def list_students(students):
    print("\nList of students:")
    for student in students:
        print(f"{student['id']}: {student['name']}")

def show_student_marks(students, selected_course, marks):
    print(f"\nStudent marks for course {selected_course['name']}:")
    for student in students:
        print(f"{student['name']} ({student['id']}): {marks.get(student['id'], 'N/A')}")