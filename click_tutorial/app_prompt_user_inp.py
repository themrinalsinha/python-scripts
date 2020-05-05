import click

@click.command()
@click.option('--name', '-n', prompt=True, help="Please, your name?")
@click.option('--age', '-a', prompt="What is your age?")
# NOTE: taking password as input in a hidden manner
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
def main(name, age, password):
    click.echo(f"Hello, {name} >|< Age: {age}")
    click.echo(f"Your password is: {password}")
    _fname = click.prompt("First name: ")
    _lname = click.prompt("Last name: ")
    click.echo(f"First name: {_fname} and Last name: {_lname}")

if __name__ == '__main__':
    main()
