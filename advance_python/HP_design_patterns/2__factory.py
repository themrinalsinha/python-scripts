

# SIMPLE FACTORY PATTERN METHOD
"""
Learn how to create simple factory which
helps to hide logic of creating objects.
"""

from abc import ABCMeta, abstractmethod

from multiprocessing.util import info

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


# designation = input("Enter designatin : ")
# name        = input("Person name      : ")
designation = 'HR'
name        = 'Mrinal Sinha'
PersonFactory.createPerson(designation, name)

# =======================================================
print('=' * 75)

# FACTORY METHOD PATTERN
# this design pattern allows to create object but differs the decision
# to the subclass, to determine class for object creation.

class AbstractDegree(metaclass=ABCMeta):
    @abstractmethod
    def info(self):
        pass

class BE(AbstractDegree):
    def info(self):
        print("Bachelor of engineering...")

    def __str__(self) -> str:
        return "( Bachelor of engineering )"

class ME(AbstractDegree):
    def info(self):
        print("Masters of engineering...")

    def __str__(self) -> str:
        return "( Masters of engineering )"

class MBA(AbstractDegree):
    def info(self):
        print("Masters of business administration...")

    def __str__(self) -> str:
        return "( Masters of business administration )"


class ProfileAbstractFactory(object):
    def __init__(self) -> None:
        self._degrees = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def addDegree(self, degree):
        self._degrees.append(degree)

    def getDegrees(self):
        return self._degrees

class ManagerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(MBA())

class EngineerFactory(ProfileAbstractFactory):
    def createProfile(self):
        self.addDegree(BE())
        self.addDegree(ME())

# another factory which desides which factory i need to call
class ProfileCreator(object):
    @classmethod
    def create_profile(self, name):
        return eval(f"{name}Factory")()

profile_type = input("Which profile would you like to create ? Manager/Engineer: ")
profile      = ProfileCreator.create_profile(profile_type)
print(f"Creating profile of {profile_type}")
print("Profile has following degrees")
for deg in profile.getDegrees():
    print(deg)

# =======================================================
print('=' * 75)
