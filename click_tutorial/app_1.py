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

@click.command()
@click.option('--name', '-n', nargs=2) # if passed --name/-n then 2 values are required
def main(name):
    print(f"Hello, {name}")

if __name__ == '__main__':
    main()
