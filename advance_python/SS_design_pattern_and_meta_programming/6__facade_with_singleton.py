from typing import Any

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


class Meta(type):
    """ singleton design patterns """
    _instances = {}
    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Meta, cls).__call__(*args, **kwargs)
            return cls._instances[cls]


class Facade(metaclass=Meta):
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
print("first obj: ", obj)
obj.emergency()
obj.no_emergency()

obj1 = Facade()
print(f"object one : {obj1}")
# obj1.emergency()
