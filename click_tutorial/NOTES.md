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
