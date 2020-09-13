from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names
    )

# avoiding writing constructor
class Base(object):
    # _fields = []

    __signature__ = make_signature([])


    def __init__(self, *args, **kwargs) -> None:
        bound = self.__signature__.bind(*args, **kwargs)
        for name, value in bound.arguments.items():
            print(name, value)
            setattr(self, name, value)
        # for name, value in zip(self._fields, args):
        #     print(name, value)
        #     setattr(self, name, value)


class Person(Base):
    # _fields = ['name', 'age']
    __signature__ = make_signature(['name', 'age'])

    def method(self):
        print(f"NAME --> {self.name}\nAGE --> {self.age}\n")
        return

if __name__ == "__main__":
    o = Person(name="mrinal sinha", age=123)
    print(o)
    o.method()
