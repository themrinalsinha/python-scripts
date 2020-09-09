


class Test(object):
    __slots__ = ("name")

    def __init__(self, name) -> None:
        self.name = name

# Normal class instintiate and printing it...
t = Test("Mrinal Sinha")
print(t)

# although there is no name associated with the object...
# we can assign and access it...
t.name = 'Mrinal Sinha'
print(t.name)

# since we've defined slot and we are saying it to use only "name"
# it will not allow any more allocation.
t.age = 123
print(t.age)
"""
__slots__ magic

    In python every class cna have instance attributes. By default python uses a dict to
    store an object's instance attributes. This is really helpful as it allows settings
    arbitrary new attributes at runtime.

    However, for small classes with known attributes it might be a bottleneck. The dict
    wastes a lot of RAM. Python can't just allocate a static amount of memory at object
    creation to store all the attributes. Therefore it sucks a lot of RAM if you create
    a lot of objects (in thousands or millions). Still there is a way to circumvent this
    issue. It involves the usage of __slots__ to tell python not to use a dict, and only
    allocates space to fixed set of attributes.
"""
