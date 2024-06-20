# class name cars, model YOM Type and color
# my dream car is ... manufactured in ..., being a... and color...
class Car:
    def __init__(self, model, yearofmanufacture, type, color):
        self.model = model
        self.yearofmanufacture = yearofmanufacture
        self.type = type
        self.color = color

        #method

    def display(self):
        print(
            f"My dream car is {self.model} manufactured in {self.yearofmanufacture} being a {self.type} in color {self.color}")

        #object


my_type = Car("Mazda", 2009, "Axela", "red")
my_type.display()
my_type = Car("Nissan", 2011, "Juke", "Grey")
my_type.display()
my_type = Car("Toyota", 2015, "Prado", "White")
my_type.display()
my_type = Car("Honda", 2013, "Fit", "Black")
my_type.display()
