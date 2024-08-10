# In Python,
# Abstract methods are defined within abstract base classes (ABCs). An abstract method is a method that is declared, but contains no implementation. Abstract methods are used to enforce that certain methods must be created within any subclass derived from the abstract base class.
#
# Here's how you can define and use abstract methods and classes in Python:
#
# Importing Abstract Base Classes and Abstract Methods: Use the abc module.
# Defining an Abstract Base Class: Inherit from ABC (which stands for Abstract Base Class).
# Declaring Abstract Methods: Use the @abstractmethod decorator.
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Run"


class Cat(Animal):
    def sound(self):
        return "Meow"

    def move(self):
        return "Jump"


# Creating instances of concrete classes
dog = Dog()
cat = Cat()

print(dog.sound())  # Output: Bark
print(dog.move())  # Output: Run
print(cat.sound())  # Output: Meow
print(cat.move())
