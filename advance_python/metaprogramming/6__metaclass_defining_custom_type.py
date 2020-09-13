
# a simple example of custom type
class mytype(type):
    def __new__(cls, name, bases, cls_dict):
        print(f"\nNAME: {name}\nBASES: {bases}\nCLASS DICT: {cls_dict}")
        if len(bases) > 1:
            raise TypeError("NO!!")
        return super().__new__(cls, name, bases, cls_dict)

class Base(metaclass=mytype):
    pass

class A(Base):
    pass

class B(Base):
    pass

# class C(A, B): # it will throw error, because it is inheriting from 2 base class
#     pass
