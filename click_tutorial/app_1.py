import click

# @click.command()
# @click.option('--name', '-n', default="Sinha", help='Username to print if any') # optional fields
# def main(name):
#     print(f"Hello, {name}")
# # =================================
# # $ python app_1.py --name/-n Mrinal
# # $ Hello, Mrinal
# # $ python app_1.py
# # $ Hello, Sinha
# # If Sinha is not given as default,
# # It will print "Hello, None"
# # =================================

# # working with multiple values
# @click.command()
# @click.option('--name', '-n', nargs=2) # if passed --name/-n then 2 values are required
# def main(name):
#     print(f"Hello, {name}")

@click.command()
@click.option('--name', '-n', default="Sinha", help='Username to print if any')
@click.option('--salary', '-s', nargs=2, type=int) # specifying input type
def main(name, salary):
    # print(f"Hello, {name} !! Salary: {sum(salary)}")
    click.echo(f"Hello, {name} !! Salary: {sum(salary)}")
# ==============================================
# $ python app_1.py -n Mrinal -s 21 21
# $ Hello, Mrinal !! Salary: ('21', '21')
# ==============================================

if __name__ == '__main__':
    main()
