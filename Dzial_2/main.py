class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False
        self.final_grades = []


    def promote(self):
        self.promoted = True

    def print_something(self):
        print(f"Student {self.first_name} {self.last_name} is promoted: {self.promoted}")

    def print_self(self):
        print("What is self?: ", self)
        print("Here is the acces for name: ", self.name)

    def add_final_grade(self, grade):
        self.final_grades.append(grade)
        if grade == 1:
            self.promoted = False


class Grade:
    pass

class  School:
    pass

def run_example():
    student = Student("Bartek")
    student.print_something()


if __name__ == '__main__':
    run_example()