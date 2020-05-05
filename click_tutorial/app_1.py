import click

@click.command()
@click.option('--name', '-n', default="User", help="Enter your name")
@click.option('--marks', '-m', nargs=3, help="PCM marks", type=int)
@click.option('--total', '-t', type=int, help="total marks")
def main(name, marks, total):
    click.echo(f"Hello, {name}")
    if marks and total:
        click.echo(f"PCM total: {sum(marks)}")
        click.echo(f"Total of: {total}")
        click.echo(f"Percentage: {(sum(marks)/total) * 100}")

if __name__ == '__main__':
    main()

# eg:
# $ python app_1.py --name Mrinal -m 48 29 45 --total 150
# $ Hello, Mrinal
# $ PCM total: 122
# $ Total of: 150
# $ Percentage: 81.33333333333333
