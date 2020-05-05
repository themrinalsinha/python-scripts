# working with click configuration file

import click
import click_config_file

@click.command()
@click.option('--name', '-n', default="Sinha", help="specify name")
@click.option('--salary', '-s', type=int)
@click_config_file.configuration_option()
def main(name, salary):
    click.echo(f"Hello, {name}. Your salary is: {salary}")

if __name__ == "__main__":
    main()
