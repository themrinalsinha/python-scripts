

# SIMPLE FACTORY PATTERN METHOD
"""
Learn how to create simple factory which
helps to hide logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass

class HR(Person):
    def create(self, name):
        print(f"HR ({name}) is created !!! :)")

class Engineer(Person):
    def create(self, name):
        print(f"Engineer ({name}) is created !!! :)")

class PersonFactory(object):
    @classmethod
    def createPerson(cls, destination, name):
        eval(destination)().create(name)


designation = input("Enter designatin : ")
name        = input("Person name      : ")
PersonFactory.createPerson(designation, name)
