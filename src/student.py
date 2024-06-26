# student.py 文件内容

class Student:
    def __init__(self, name, gender, age, class_name):
        self.name = name
        self.gender = gender
        self.age = age
        self.class_name = class_name

    def __str__(self):
        return f"学生名: {self.name}, 性别: {self.gender}, 年龄: {self.age}, 班级: {self.class_name}"
