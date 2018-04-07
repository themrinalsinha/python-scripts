#!/usr/bin/python3

from sys  import argv
from os   import path

def split_file(filename, parts = 10):
    def _helper(data, n):
        for i in range(0, len(data), n):
            yield data[i:i+n]

    with open(filename, 'r') as f:
        data  = [x.strip() for x in f.readlines() if x]
        chunk = len(data) // parts

        for i, x in enumerate(_helper(data, chunk)):
            with open('{}_{}'.format(i, path.basename(filename).split('.')[0]), 'w') as f:
                f.write('\n'.join(a for a in x))

if __name__ == '__main__':
    if len(argv) < 2: raise RuntimeError('USAGE: .split <filename> <no_of_files:default 10>')
    split_file(argv[1], int(argv[2])) if len(argv) == 3 else split_file(argv[1])