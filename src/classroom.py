# classroom.py 文件内容（如果放在同一个文件中，请确保在 Student 类之后）

from student import Student  # 如果在不同文件中，需要导入 Student 类

class Classroom:
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
        else:
            print("添加的不是学生对象")

    def list_students(self):
        for student in self.students:
            print(student)

    def __str__(self):
        return f"班级名称: {self.class_name}, 学生数量: {len(self.students)}"
