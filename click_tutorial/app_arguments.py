import click

@click.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('pan', default="ABCD1234E")
@click.argument('places', nargs=-1)
@click.argument('birth_places', nargs=1)
def main(name, pan, age, places, birth_places):
    click.echo(f"Hello, {name} ({age} - yrs young!)")
    click.echo(f"Your PAN number is: {pan}")
    click.echo(f"VALID PAN HOLDER") \
        if age >= 18 else click.echo(f"INVALID PAN HOLDER")
    click.echo(f"places: {places}")
    click.echo(f"birth place: {birth_places}")

# when you want to pass 'n' no of arguments use nargs = -1
# and for fixed no of arguments pass the value eg: nargs = 2 (etc)
# eg:
# $ python app_arguments.py Mrinal 13 a b c d
# $ Hello, Mrinal (13 - yrs young!)
# $ Your PAN number is: a
# $ INVALID PAN HOLDER
# $ places: ('b', 'c')
# $ birth place: d

if __name__ == "__main__":
    main()
