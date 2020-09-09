"""
facade design pattern or bridge design pattern

this pattern involves an interface which acts as a bridge which makes the
functionality of concrete classes independent from interface implementer classes.
Both types of classes can be altered structurally without affecting each row.
"""

class Sensor(object):
    def __init__(self):
        pass

    def sensorOn(self):
        print("sensor is on")

    def sensorOff(self):
        print("sensor is off")

class Light(object):
    def __init__(self):
        pass

    def lightOn(self):
        print("light is on")

    def lightOff(self):
        print("light is off")

class Smoke(object):
    def __init__(self):
        pass

    def smokeOn(self):
        print("smoke is on")

    def smokeOff(self):
        print("smoke is off")

# define our fasade class
# we encapsulated all the methods and we'll call the facad when we need it..
class Facade(object):
    def __init__(self) -> None:
        self._smoke  = Smoke()
        self._light  = Light()
        self._sensor = Sensor()

    def emergency(self):
        self._sensor.sensorOn()
        self._light.lightOn()
        self._smoke.smokeOn()

    def no_emergency(self):
        self._sensor.sensorOff()
        self._light.lightOff()
        self._smoke.smokeOff()

obj = Facade()
obj.emergency()
obj.no_emergency()
