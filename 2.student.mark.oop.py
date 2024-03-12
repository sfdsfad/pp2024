class Student:
    def __init__(self, student_name, student_id, dob):
        self.__student_name = student_name
        self.__student_id = student_id
        self.__dob = dob

    def get_student_name(self) -> str:
        return self.__student_name
    
    def get_student_id(self) -> str:
        return self.__student_id
    
    def get_dob(self) -> str:
        return self.__dob
    
    def __str__(self) -> str:
        return f"Student name: {self.__student_name}\nStudent ID: {self.__student_id}\nDate of birth: {self.__dob}"
    