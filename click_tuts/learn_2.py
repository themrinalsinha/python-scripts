# Nesing commands

# Commads can be attached to other commands of type Group.
# This allows arbitrary nesting of scripts. As an example here is script
# that implements two commands for managing databases.


# As you can see, the group() decorator works like a command() decorator,
# but creates a Group object instead which can be given multiple subcommands
# that can be attached with Group.add_command()

import click

@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

cli()
