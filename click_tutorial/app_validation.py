# validating parameter that we pass in our CLI
# we need to install a third party tool: click-params

import click
from click_params import EMAIL, DOMAIN, PUBLIC_URL

@click.group()
def main():
    pass

@main.command()
@click.option("--name", '-n')
@click.option("--email", '-e', type=EMAIL)
@click.option("--domain", '-d', type=DOMAIN)
@click.option("--website", '-w', type=PUBLIC_URL)
def add_user(name, email, domain, website):
    """
    command to add user
    """
    click.echo(f"Your name is: {name}")
    click.echo(f"Your email is: {email}")
    click.echo(f"Your domain is: {domain}")
    click.echo(f"Your website is: {website}")

if __name__ == "__main__":
    main()
