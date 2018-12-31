# Options

# Adding options to commands can be accomplished by the option() decorator.
# Since options can come in various different versions, there are a ton of
# parameters to configure their behavior. Options in click are distinct from
# positional arguments.

# Name your options.
import click

@click.command()
@click.option('-s', '--string-to-echo', help='It does something')
def echo(string_to_echo):
    click.echo(string_to_echo)
# Or, explicitly, by giving one non-dash-prefixed argument:

# @click.command()
# @click.option('-t', '--text-to-echo', click.STRING)
# def echo(string):
#     click.echo(string)

echo()
