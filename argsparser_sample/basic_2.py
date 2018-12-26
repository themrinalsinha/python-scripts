import argparse

parser = argparse.ArgumentParser()
parser.add_argument('square', type=int, help='Dispaly square of a given number')
# by default type of an argument is string, so for other cases you have to define 'type'
args = parser.parse_args()
print(args.square ** 2)
