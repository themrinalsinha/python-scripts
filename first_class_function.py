def square(x):
    return x ** 2

def cube(x):
    return x ** 3

# f = square(5)
# # Assigning function and value to a variable.
# g = square

# print(f)
# print(g)
# print(g(5))

def my_map(func, args):
    return [func(x) for x in args]

print(my_map(square, (1, 2, 3, 4, 5)))


# =======================================
# eg: of first class function
def logger(msg):
    def log_message():
        print('Log : ', msg)
    return log_message

log_hi = logger('Hi!')
print(log_hi())

# ======================================

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text

print_tag = html_tag('H1')
print(print_tag)
print_tag('Hello there...')













