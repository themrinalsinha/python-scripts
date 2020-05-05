import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument("text")
def say(text):
    click.echo(f"You said: {text}")

@cli.command()
@click.argument("name")
def greet(name):
    click.echo(f"Hello, {name}")

if __name__ == "__main__":
    cli()
