

def command(name, **cmd_args):
    def wrapper(func):
        print(cmd_args)
        return func
    return wrapper

@command('mrinal', help="this is help")
def temp():
    print('hello main fun..')

temp()
