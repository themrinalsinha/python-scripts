from click import command, option, echo

@command()
@option('--verbose', is_flag=True, help='Will print verbose')
@option('--name', default='', help='Who are you ??')
def cli(verbose, name):
    if verbose:
        echo('verbose enabled.')
    echo('Hello world...')
    echo('Bye {}'.format(name))

# if __name__ == '__main__':
#     cli()
cli()
