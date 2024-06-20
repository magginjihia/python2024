class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def print_name(self):
        print(f"My name is {self.first_name}, {self.last_name} and I am {self.age} years old")


class Student(Person):  #statement in brackets indicates inheritance from person class
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)


my_student = Student("John", "Smith", 25)
my_student.print_name()
student2 = Student("Joyce", "Joy", 25)
student2.print_name()
student3 = Student("Bob", "Ryan", 30)
student3.print_name()