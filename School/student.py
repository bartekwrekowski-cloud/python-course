class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = int(age)
        self.score = int(score)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Score: {self.score}"

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Score: {self.score}"

    def __int__(self):
        return self.score

    def __float__(self):
        return self.score

    def __len__(self):
        return len(self.name)

    def __bool__(self):
        return bool(self.score)