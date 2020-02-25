# https://dev.to/apcelent/python-decorator-tutorial-with-example-529f
# https://realpython.com/primer-on-python-decorators/

def command(name, **cmd_args):
    def wrapper(func):
        print(cmd_args)
        return func
    return wrapper

@command('mrinal', help="this is help")
def temp():
    print('hello main fun..')

temp()
