# classroom.py
from student import Student  # 导入Student类


class Classroom:
    def __init__(self, class_name, teacher_name, students=[]):
        self.class_name = class_name
        self.teacher_name = teacher_name
        self.students = students  # students是一个包含Student对象的列表

    def add_student(self, name, gender, age, city):
        student = Student(name, gender, age, city)
        self.students.append(student)

    def num_students(self):
        return len(self.students)

    def list_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Gender: {student.gender}, Age: {student.age}, City: {student.city}")

