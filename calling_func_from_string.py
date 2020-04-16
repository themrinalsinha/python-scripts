# when dealing with class based function

class MyClass(object):
    def install(self):
        print("Hello from class")

class_name        = MyClass()
class_method_name = 'install'

my_method         = None
try:
    my_method = getattr(class_name, class_method_name)
except AttributeError:
    raise NotImplementedError(f"class {class_name.__class__.__name__} does not implement {class_method_name}")

my_method()
# ======================================================================================

# if it is a function
def install():
    print("Yo install function called")

method_name = 'install'
possibles   = globals().copy()
possibles.update(locals())

method = possibles.get(method_name)
if not method:
    raise NotImplementedError(f"Method {method_name} not implemented.")
method()
