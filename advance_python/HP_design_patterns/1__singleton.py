"""
Pattern name: Singleton (Mono state patter)
Pattern type: Creational Design Pattern
"""

# SOLUTION - 1
from tokenize import Single


print('-' * 50)
class Singleton_1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

s1__1 = Singleton_1()
print("S1__1 (Object 1) ==> ", s1__1)
s1__1.data = 10
print(s1__1.data)

s1__2 = Singleton_1()
print("S1__2 (Object 1) ==> ", s1__2.data)
s1__2.data = 100
print(s1__2.data)

""" OUTPUT (they both have same memory address)
S1__1 (Object 1) ==>  <__main__.Singleton_1 object at 0x7f57a341ae20>
10
S1__2 (Object 1) ==>  <__main__.Singleton_1 object at 0x7f57a341ae20>
100
"""
# =====================================================================

# SOLUTION - 2
print('-' * 50)
class Borg(object):
    _shared = {}

    def __init__(self) -> None:
        self.__dict__ = self._shared

class Singleton_2(Borg):
    def __init__(self, arg) -> None:
        Borg.__init__(self)
        self.val = arg

s2__1 = Singleton_2("Mrinal Sinha")
print(f"S2_1 --> {s2__1}")
print(f"S2_1 --> {s2__1.val}")

s2__2 = Singleton_2("Lucky")
print(f"S2_2 --> {s2__2}")
print(f"S2_2 --> {s2__2.val}")
print(f"S2_1 (val) --> {s2__1.val}")

""" OUTPUT
S2_1 --> <__main__.Singleton_2 object at 0x7f173ffc7070>
S2_1 --> Mrinal Sinha
S2_2 --> <__main__.Singleton_2 object at 0x7f173ffc72e0>
S2_2 --> Lucky
S2_1 (val) --> Lucky
"""

# =====================================================================

# SOLUTION - 3
# using decorator based approach
print('-' * 50)

class SingletonDecorator(object):
    def __init__(self, _class) -> None:
        self._class   = _class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self._class(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Logger(object):
    def __init__(self) -> None:
        self.start = None

    def write(self, message):
        if self.start:
            print(f"{self.start} -- {message}")
        else:
            print(message)

logger_1 = Logger()
logger_1.start = "# >"
print("Logger - 1: ", logger_1)
logger_1.write("Logger 1 object is created...")

logger_2 = Logger()
logger_2.start = "$ >"
print("Logger - 2: ", logger_2)
logger_1.write("Logger 2 object is created...")

""" OUTPUT
Logger - 1:  <__main__.Logger object at 0x7f626101e130>
# > -- Logger 1 object is created...
Logger - 2:  <__main__.Logger object at 0x7f626101e130>
$ > -- Logger 2 object is created...
"""

# =====================================================================

# SOLUTION - 4
# using metaclass
print('-' * 50)

class SingletonMeta(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
        print(cls.__instance)
        return cls.__instance[cls]

class DBConnector(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.status = 'Not connected'

    def disconnected(self):
        self.status = "Disconnected"

    def connected(self):
        self.status = "Connected"


client_1 = DBConnector()
print(f"CLIENT 1: ", client_1)
print(client_1.status)

client_2 = DBConnector()
print(f"CLIENT 2: ", client_2)
client_2.connected()

print("CLIENT 1 (status): ", client_1.status)
client_1.disconnected()

print("CLIENT 2 (status): ", client_2.status)


""" OUTPUT
{<class '__main__.DBConnector'>: <__main__.DBConnector object at 0x7f632f8ca4f0>}
CLIENT 1:  <__main__.DBConnector object at 0x7f632f8ca4f0>
Not connected
{<class '__main__.DBConnector'>: <__main__.DBConnector object at 0x7f632f8ca4f0>}
CLIENT 2:  <__main__.DBConnector object at 0x7f632f8ca4f0>
CLIENT 1 (status):  Connected
CLIENT 2 (status):  Disconnected
"""
