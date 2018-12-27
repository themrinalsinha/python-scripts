# CLICK!

# Why not Argparse ?
#   -> Click is internally based on optparser instead of argparser. This
# however is an implementation detail that a user does not have to be concerned with.
#       -> argparse has built-in magic behavior to guess if something is an argument or an option.
#       this becomes a problem when dealing with incomplete command line how the parser is going to behave.
#       This goes against click's ambitions of dispatching to subparser.
#
#       -> argparse currently does not support disability of interspersed arguments.
#       without this feature it's not possible to safely implement click's nested parsing nature.

# Basic concepts - creating a command
# click is based on declaring commands through decorators, Internally, there is a non-decorator
# interface for advanced use cases, but it's discouraged for hight level usage.
# A function becomes a Click command line tool by decorating it through click.command().
# At its simplest, just decorating a function with this decorator will make it into a callable script

import click

@click.command()
def hello():
    click.echo('Hello world..!')
# Decorator converts the function into a command which then can be invoked.

if __name__ == '__main__':
    hello()

# Echoing: reason why this program use echo() instead of the regular print() function, coz
# click attempts to support both python2 and python3 the same way and to be very robust even when
# the environment is misconfigured.
