class Person:
    def __init__(self, name, age):
        """构造方法，初始化实例属性"""
        self.name = name
        self.age = age

    def __str__(self):
        """返回对象的字符串表示，用于 print() 或 str()"""
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        """返回对象的正式表示，用于调试"""
        return f"Person({self.name!r}, {self.age!r})"

    def __eq__(self, other):
        """比较方法，用于判断两个对象是否相等"""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __iter__(self):
        """迭代方法，使得对象可以被迭代"""
        self.index = 0
        self.data = [self.name, self.age]
        return self

    def __next__(self):
        """定义如何返回下一项"""
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __enter__(self):
        """上下文管理方法，在进入上下文时调用"""
        print(f"Entering context for {self}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """上下文管理方法，在退出上下文时调用"""
        print(f"Exiting context for {self}")

# 创建一个 Person 对象
person1 = Person("Alice", 25)

# 使用 __str__ 和 __repr__ 方法
print(person1)
print(repr(person1))

# 创建另一个 Person 对象
person2 = Person("Alice", 25)

# 使用 __eq__ 方法比较两个对象
print(person1 == person2)

# 使用迭代方法
for attr in person1:
    print(attr)

# 使用上下文管理方法
with person1 as p:
    print(f"Using person {p}")
