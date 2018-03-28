# Closures: A closure is a record storing a function together with an environment:
# A mapping associating each free variable of the function with the value or storage location
# to which the name was bound when the closure was created. etc..

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func

x = outer_func()
x()
x()

# ==============================
import logging
logging.basicConfig(filename = 'example.log', level = logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
sub_logger(5, 2)
