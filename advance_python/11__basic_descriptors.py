from unicodedata import name




"""
METHOD 1: using descriptors to set the value to a variable
"""
class Foo(object):
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

if __name__ == "__main__":
    o = Foo('Mrinal Sinha')
    print(o)


"""
METHOD 2: writing a better version of descriptors in order to handle multiple variables
"""
class Descriptor(object):
    def __init__(self, name=None) -> None:
        self.name = name

    def __get__(self, instance, owner):
        print(f"GET => INSTANCE: {instance} | OWNER: {owner}")
        return instance

    def __set__(self, instance, value):
        print(f"SET => INSTANCE: {instance} | VALUE: {value}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"DELETE => {instance}")
        del instance.__dict__[self.name]


class Foo(Descriptor):
    name = Descriptor()

if __name__ == "__main__":
    o = Foo(name="Mrinal Sinha")
    print(o.name)
    o.name = "Mayank"
    print(o.name)
