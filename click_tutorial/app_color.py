import click

@click.command()
@click.option('--name', '-n')
def main(name):
    click.echo(f"My name is {name}") # normal printing
    click.echo(
        click.style(
            f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
        )
    )
    # print with all other options
    click.echo(
        click.style(
            f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
            bold = True,
            dim=False,
            underline=True,
            blink=True,
            reverse=True,
            reset=True,
        )
    )

    # In order to apply style you can directly use secho from click
    click.secho(
        f"My name is {name}", # text to print
            fg = "red",
            bg = "white",
            bold = True,
            dim=False,
            underline=True,
            blink=True,
            reverse=True,
            reset=True,
    )

if __name__ == '__main__':
    main()
