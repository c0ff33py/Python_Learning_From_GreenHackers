# Exercise 4: Inheritance
# Parent class
class Animal:
    def speak(self):
        print("Animal makes sound")

# Child class


class Dog(Animal):
    def bark(self):
        print("Woof Woof!")


class Cat(Animal):
    def sound(self):
        print("Meow!")


dog = Dog()
dog.speak()
dog.bark()

cat = Cat()
cat.speak()
cat.sound()
