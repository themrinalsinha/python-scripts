## CLICK (Command line application development)

Installation: `$ pip install click`

#### Working with "option"
`option` is an optional parameter for any command
- @click.option(large_name, small_name, default_value, help_text)
```python
import click
@click.command()
@click.option('--name', '-n', default="Sinha", help='your name please')
def main(name):
    print(f"Hello, {name}")
```
```shell
$ python app.py
$ Hello, Sinha
-----------------------------
$ python app.py --name Mrinal
$ Hello, Mrinal
-----------------------------
NOTE: if default value is not
given then when you run:
$ python app.py
$ Hello, None
```
- if you want to pass certain no of arguments use "nargs"
```python
@click.option('--coordinates', '-c', nargs=2)
# if the option --coordinates is passed it will be
$ python app.py --coordinates 101 201
# if it is less than or greater than 2 it will throw error
```
- passing multiple values for any particular option
```python
@click.option('--places', '-p', multiple=True)
# then you can pass -p multiple times eg:
$ python app.py -p India -p USA -p Peru
```
- specifying type of input explicitly
```python
@click.option('--salary', '-s', type=int)
$ python app.py -s "102" -> 102
$ python app.py -s 102 -> 102
$ python app.py -s "abc" -> throw error
```
----------------------------------------------------
#### Working with "argument"
`argument` are mandatory parameter unless you are not passing default value
- argument(input_name, default=None)
```python
@click.command()
@click.argument('name')
@click.argument('age', type=int)
@click.argument('pan', default="ABCD1234E")
def main(name, pan, age):
    click.echo(f"Hello, {name} ({age} - yrs young!)")
    click.echo(f"Your PAN number is: {pan}")
    click.echo(f"VALID PAN HOLDER") \
        if age >= 18 else click.echo(f"INVALID PAN HOLDER")
```
working with `nargs`
- If you pass `nargs = -1` (it will take any number of arguments in)
- If you pass anything else, it will take that amount fixed (as seen above)
```python
@click.argument('places', nargs=-1)
@click.argument('birth_places', nargs=1)
def main(places, birth_places):
    click.echo(f"places: {places}")
    click.echo(f"birth place: {birth_places}")

$ python app.py a b c d e
$ places: (a, b, c, d)
$ birth place: e
```
------------------------
#### Working with "prompt & user input"
`prompt` is used when you want to take user input
```python
@click.command()
@click.option('--name', '-n', prompt=True, help="Please, your name?")
@click.option('--age', '-a', type=int, prompt="What is your age?")
def main(name, age):
    click.echo(f"Hello, {name} >|< Age: {age}")
```
```shell
$ python app.py
$ Name: Mrinal           ## will prompt for name
$ What is your age?: 25  ## will ask for age with custom message
Hello, Mrinal >|< Age: 25
----------------------------------------------------------------
Other way if you pass values as options it will not prompt eg:
$ python app.py --name Mrinal --age 25 ## it will not prompt
Hello, Mrinal >|< Age: 25
```
- taking input in hidden manner, eg for `passwords`
```python
@click.option('--password', '-p', prompt=True, hide_input=True)

$ python app.py
$ Password: <take input in hidden manner>
```
- taking password and also confirming (re-prompt for confirmation)
```python
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)

$ python app.py
$ Password: <take input in hidden manner>
$ Repeat for confirmation: <takes input in hidden manner>
# if both do not match it will throw an error and ask again to enter.
```
