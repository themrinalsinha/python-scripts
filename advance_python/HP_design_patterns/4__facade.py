"""
Facade design pattern
"""

class Cook(object):
    """
    Facade class
    Description: Provides easy interface to prepare dish instead of calling three
                 different classes and making difficult for client to use.
    """
    def prepareDish(self):
        self.cutter = Cutter()
        self.cutter.cutVegetables()

        self.boiler = Boiler()
        self.boiler.boilVegetables()

        self.frier = Frier()
        self.frier.fry()

class Cutter(object):
    """
    System class
    Description: Cutter class provide feature of cutting vegetables
    """
    def cutVegetables(self):
        print("All vegetables are cut...")

class Boiler(object):
    """
    System class
    Description: Boiler class provide feature of boiling vegetables
    """
    def boilVegetables(self):
        print("All vegetables are boiled...")

class Frier(object):
    """
    System class
    Description: Frier class provided feature frying vegetables
    """
    def fry(self):
        print("All vegetables are fried...")

cook = Cook()
cook.prepareDish()
