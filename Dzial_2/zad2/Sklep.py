import random

class Student:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.promoted = False

class School:
    def __init__(self,name,students):
        self.name = name
        self.students = students


def print_student(student):
    print(f"Student: {student.first_name} {student.last_name}, promoted: {student.promoted}")

def promote_student(student):
    student.promoted = True

def stworz_szkole(nazwa_szkoly):
    liczba_studentow = random.randint(1,20)
    studenci = []
    for students_number in range (liczba_studentow):
        first_name = f"Student nr. {students_number}"
        last_name = "Smith"
        studenci.append(Student(first_name,last_name,liczba_studentow))
    szkola = School(nazwa_szkoly, studenci)
    return szkola

def run_example():
    school = stworz_szkole("Harvard")
    print(school)
    for student in school.students:
        print_student(student)

if __name__ == '__main__':
    # student_1 = Student("James","Smith",18)
    # print_student(student_1)
    #
    # student_2 = Student("Dorota","Marge",32)
    # print_student(student_2)
    # promote_student(student_2)
    # print_student(student_2)
    run_example()


