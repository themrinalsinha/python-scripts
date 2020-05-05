# setuptools is a powerful package, that allows
# us to enhance the abilities of the utilities,
# Using setuptools
# - pip install pipenv
# - pipenv install click setuptools
# once it is done insalling you will see, there will be a Pipfile
# now we'll create a calculator app

import click

@click.command()
@click.option('--name', '-n')
def main(number):
    click.echo(f"Your number was {number}")

if __name__ == "__main__":
    main()

# before running we'll initialize our pipenv shell
# $ pipenv shell
# $ python app_setuptools.py

# we'll create setup.py to create entrypoint
# to run it or install it on your virtualenv
# pip install -e|--editable .
