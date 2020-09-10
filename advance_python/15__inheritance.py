

# avoiding writing constructor
class Base(object):
    _fields = []

    def __init__(self, *args, **kwargs) -> None:
        for name, value in zip(self._fields, args):
            print(name, value)
            setattr(self, name, value)


class Person(Base):
    _fields = ['name', 'age']

    def method(self):
        print(f"NAME --> {self.name}\nAGE --> {self.age}\n")
        return

if __name__ == "__main__":
    o = Person("Mrinal Sinha")
    print(o)
    o.method()
