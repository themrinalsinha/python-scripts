# the setattr() method setss the value of given attribute of an object.
# Syntax : setattr(object, name, value)
# object - object whose attribute has to be set.
# name   - string which contains the name of the attribute to be set.
# value  - value of the attribute to be set.

# Eg1 ---------------------------------------
class Person:
    name = 'Mrinal'

p = Person()
print('Before modification : ', p.name)
setattr(p, 'name', 'Lucky')
print('After modification : ', p.name)

# Eg2 ---------------------------------------
class Person_1(object):
    name = 'Mrinal'

p = Person_1()

setattr(p, 'lname', 'Sinha')
setattr(p, 'age', 24)

print('Name : ', p.name +' '+ p.lname)
print('Age : ', p.age)
