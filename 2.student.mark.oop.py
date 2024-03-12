class Student:
    def __init__(self, studentID, name, dob):
        self.__studentID = studentID
        self.__name = name
        self.__dob = dob
    
    def setStudentID(self, studentID):
        self.__studentID = studentID

    def setName(self, name):
        self.__name = name

    def setDOB(self, dob):
        self.__dob = dob
    
    def getstudentid(self) -> str:
        return self.__studentid
    
    def getname(self) -> str:
        return self.__name
    
    def getdob(self) -> str:
        return self.__dob

    def __str__(self) -> str:
        return f"StudentID: {self.__studentID}, Name: {self.__name}, DOB: {self.__dob}."

class Course:
    def __init__(self, courseID, courseName):
        self.__courseID = courseID
        self.__name = courseName

    def setCourseID (self, courseID):
        self.__courseID = courseID

    def setCourseName(self, courseName):
        self.__name = courseName

    def getCourseID(self) -> str:
        return self.__courseID
    
    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"CourseID: {self.__courseID}, Course name: {self.__name}."

class ManagementProgram:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_num_of_students(self):
        return int(input("Enter the number of students: "))

    def input_one_student(self):
        studentID = input("Enter the student ID: ")
        name = input("Enter student name:")
        dob = input("Enter student DOB: ")
        return Student(studentID, name, dob)

    def input_num_of_courses(self):
        return int(input("Enter the number of courses"))

    def input_one_course(self):
        courseID = input("Enter course ID: ")
        courseName = input("Enter course name: ")
        return Course(courseID, courseName)

    def input_student_mark(self):
        marks = {}
        print(f"Enter student's mark for {selected_course.name}: ") 
        for student in students:
            mark = float(input(f"Enter mark for {student.name} ({student.id}): "))
            marks[student.id] = mark
        return marks

    
