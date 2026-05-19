from student import Student

def run_example():
    student = Student("Bartek",21,5)
    student_str = str(student)
    print(student_str)
    student_repr = repr(student)
    print(student_repr)
    student_int = int(student)
    print(student_int)
    student_len = len(student)
    print(student_len)
    student_bool = bool(student)
    print(student_bool)

if __name__ == "__main__":
    run_example()