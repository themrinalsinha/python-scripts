# A command line argument based calculator

import argparse
parser = argparse.ArgumentParser()
# parser.add_argument('echo')
# # If you add any parser argument without '--' it will be acted
# # as positional argument. Otherwise with -- it becomes optional argumnet.
# parser.parse_args()
# print(args.echo)
# ----------------------------------------------

parser.add_argument('hello', help='Use it to say anyting..')
args = parser.parse_args()

