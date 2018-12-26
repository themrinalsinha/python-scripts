# Introducing Optional arguments

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--verbosity', help='Increase output verbosity')
args = parser.parse_args()
print(args)
if args.verbosity:
    print('verbosity turned on')
