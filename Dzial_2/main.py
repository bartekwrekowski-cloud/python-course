class Student:
    pass

class Grade:
    pass

class  School:
    pass

if __name__ == '__main__':
    student_Bartek = Student()

    grade_a = Grade()
    grade_f = Grade()

    moja_szkola = School()

    # print(moja_szkola)
    # print(grade_a, grade_f)
    # print(moja_szkola)

    print("type(student_Bartek): ", type(student_Bartek))
    print("type(grade_a): ", type(grade_a))
    print("type(grade_f): ", type(grade_f))
    print("type(moja_szkola): ", type(moja_szkola))

    all_students = {Student(),Student(),Student(),Student(),Student()}
    print(all_students)

    grades = {
        1: Grade(),
        2: Grade(),
        3: Grade(),
        4: Grade(),
        5: Grade(),
        6: Grade(),
    }
    print(grades)
