from click import STRING, INT, FLOAT, BOOL, UUID
from click import command, option, echo

@command()
@option('--string', nargs=2, type=STRING)
def justtesting(string):
    echo(string)

justtesting()
