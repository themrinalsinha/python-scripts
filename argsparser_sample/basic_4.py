from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--verbose', help='Increase output verbosity', action='store_true')
args = parser.parse_args()
if args.verbose:
    print('verbosity turned on')

# When 'store_true' is set as action in add_argument.
# Then set or assign the value True to args.verbose.
# Not specifying it implies False.


