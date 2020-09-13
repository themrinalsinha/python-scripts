
class Test(object):

    MYVAR_1 = 1
    MYVAR_2 = 2
    MYVAR_3 = 3
    MYVAR_4 = 4

    def __init__(self, num=1) -> None:
        self.num = num
        self._num = 2  ## Private variable
        self.__num = 3 ## Protected variable

    # NOTE: you cannot access the protected variable
    # from outsite the class, so in order to access it
    # you have to use getter and setter
    def get(self):
        return self.__num

    def set(self, val):
        self.__num = val
        return self.__num

    # working with property decorator
    @property
    def methoda(self):
        print("Hola, desh")

    # working with static methods
    # NOTE: static method doesn't take self as first param
    @staticmethod
    def methodb():
        print("I'am static method...")

    def __str__(self) -> str:
        return "object..."

    @classmethod
    def classvariableaccess(cls):
        print(f"class variable access: {cls.MYVAR_1} {cls.MYVAR_2} {cls.MYVAR_3} {cls.MYVAR_4}")

if __name__ == "__main__":
    obj = Test(123)
    print(obj) # it will just print the memory location of the object

    print(obj.num)
    print(obj._num)
    # print(obj.__num) # can be accessed using obj.get()
    print(obj.get())
    print(obj.set(333))
    print(obj.get())

    # property value of the class can be accessed directly without calling method
    print(obj.methoda)

    # static method
    print(obj.methodb())
    print(Test.methodb())

    # class variable
    print(Test.MYVAR_1)
    print(Test.MYVAR_2)
    print(Test.MYVAR_3)
    print(Test.MYVAR_4)

    # calling a class method
    print(obj.classvariableaccess())
