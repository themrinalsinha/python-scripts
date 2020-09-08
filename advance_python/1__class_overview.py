
class Test(object):
    def __init__(self, num=1) -> None:
        self.num = num ## class variable
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
