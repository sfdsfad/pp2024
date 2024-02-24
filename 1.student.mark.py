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
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    course = {
        'id': id,
        'name': name
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

