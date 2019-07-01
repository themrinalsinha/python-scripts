from click import command, option, echo

@command()
@option('--count', default=1, help='Number of greetings')
@option('--name',  prompt='Your name: ', help='The person name to greet')
def hello(count, name):
    for x in range(count):
        echo('Hello, {}!'.format(name))

if __name__ == '__main__':
    hello()
