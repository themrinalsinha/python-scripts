"""
Dependency Inversion
--------------------

The dependency inversion principle (also known as the open-closed principle) or DIP states
that high level modules should not depend on low level modules; both should depend on abstractions.
Abstraction should not depend on details .Details should depend on abstractions.

"""

class LightBulb:
    def turn_on(self):
        print("LightBulb: ON")

    def turn_off(self):
        print("LightBulb: OFF")

class ElectricPowerSwitch:
    def __init__(self, l: LightBulb) -> None:
        self.lightbulb = l
        self.on = False

    def press(self):
        if self.on:
            self.lightbulb.turn_off()
            self.on = False

        else:
            self.lightbulb.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
switch.press()
switch.press()

"""
In the example above, we can clearly see there is a dependency between lightbulb and switch.
electric power switch directly calls ON and OFF method of lightbulb.

We'll see how we can use dependency inversion principle to make this code better and remove
this dependency between lightbulb and the switch.
"""

# =====================================================================================
from abc import ABC, abstractmethod

class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class LightBulb(Switchable):
    def turn_on(self):
        print("LightBulb: ON")

    def turn_off(self):
        print("LightBulb: OFF")

class ElectricPowerSwitch:
    def __init__(self, s: Switchable) -> None:
        self.switchable = s
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False

        else:
            self.switchable.turn_on()
            self.on = True

l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()
switch.press()
switch.press()

"""
In the above example, we can see:
- Now that light bulb in subclass of Switchable class. So there is no direct dependency
    between light bulb and electric power switch. you can change the powerswitch to any other
    switchable class. and it will stilll work
"""
