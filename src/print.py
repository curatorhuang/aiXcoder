# main.py 文件内容
from classroom import Classroom
from student import Student

# 创建班级实例
my_class = Classroom("九年级三班")

# 创建一些学生实例
student1 = Student("张三", "男", 15, "九年级三班")
student2 = Student("李四", "女", 14, "九年级三班")

# 将学生添加到班级
my_class.add_student(student1)
my_class.add_student(student2)

# 打印班级信息和学生列表
print(my_class)
my_class.list_students()
