#Object Oriented Programming

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        #method
    def display(self):
        print(self.first_name, self.last_name)

    #object
my_student = Student("Maggie", "Njihia")
my_student.display()