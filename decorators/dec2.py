# Decorator to handle DivisionByZero Error.

def validate_division(func):
    def inner_function(a, b):
        # Here inner_function (a, b) will take it's value from go_divide funcation a, b
        print("I'm dividing {} and {}".format(a, b))
        if b == 0:
            print('Oops! Division by zero is illegal...!')
            return
        return func(a, b)
    return inner_function

@validate_division
def go_divide(a, b):
    return a/b

print(go_divide(4356, 12))
print(go_divide(4356, 0))
