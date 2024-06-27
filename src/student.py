# student.py

class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}"
