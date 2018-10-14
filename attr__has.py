# the hasattr() method returns true if an object has the given named attribute and false if it does not.

class Person(object):
    age  = 23
    name = 'Mrinal'

person = Person()

print('Person has age ? : ', hasattr(person, 'age'))
print('Person has age ? : ', hasattr(person, 'salary'))

