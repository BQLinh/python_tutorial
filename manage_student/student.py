class Student:
    def __init__(self, id, name, age, student_class):
        self.id = id
        self.name = name
        self.age = age
        self.student_class = student_class

    def __str__(self) -> str:
        return f'{self.id},{self.name},{self.age},{self.student_class} \n'


linh = Student(1, 'linh', 18, 12)
print(str(linh))