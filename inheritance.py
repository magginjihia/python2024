class Animal:  #parent class
    def speak(self):
        print("Animal is speaking")


class Dog(Animal):#inherited from parent class
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is Meowing")

class Cow(Animal):
    def moo(self):
        print("Cow is mooing")

#Object
d = Dog()
d.bark()
c = Cat()
c.meow()
m = Cow()
m.moo()
# d.speak()
