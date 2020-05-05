import click
from random import sample
from string import ascii_letters

@click.group()
def main():
    """
    this function is the main parent head, so everything
    is going to be grouped under this. It is going to be
    the main command & others are going to be its sub-commands.
    """
    pass

# generally we use @click.command() but here since we are grouping
# all the below mention command under main() so use @main.command()

@main.command()
@click.argument("text")
def reverse(text):
    """
    Reverse given string
    """
    click.echo(f"{text[::-1]}")

@main.command()
@click.argument("text")
def leet(text):
    """
    Leet given string
    """
    chars   = dict([(k, str(v)) for v, k in enumerate(ascii_letters)])
    getchar = lambda x: chars[x] if x in chars else x
    click.echo(''.join(getchar(c) for c in text))

@main.command()
@click.argument("text")
def shuffle(text):
    """
    shuffle given string
    """
    click.echo("".join(sample(text, len(text))))

if __name__ == "__main__":
    main()
