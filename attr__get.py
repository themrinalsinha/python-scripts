# The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.

# Eg 1 : -------------------------------------
class Person(object):
    age  = 23
    name = 'Mrinal'

person = Person()
print('The age is :', getattr(person, 'age'))
print('The age is :', person.age)

# Eg 2 : -------------------------------------
class Person_1(object):
    age  = 23
    name = 'Sinha'

person = Person_1()

# When default value is provided.
print('The sex is : ', getattr(person, 'sex', 'Male'))
print('The place is : ', getattr(person, 'addr', 'Mumbai'))

# When no default value is provided.
# print('The sex is : ', getattr(person, 'sex'))
