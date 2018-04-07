#!/usr/bin/python3
from sys import argv
from os  import path

def split_file(filename, parts = 10):
    def chunks(ids, parts):
        for i in range(0, len(ids), parts):
            yield ids[i:i + parts]

    with open(filename, 'r') as f:
        ids = [x.strip() for x in f.readlines() if x]
        nos = len(ids) // parts
        val = chunks(ids, nos)
        for i, v in enumerate(val):
            with open('{}_{}'.format(filename.split('.')[0], i), 'w') as f:
                f.write('\n'.join(x for x in v))

if __name__ == '__main__':
    if len(argv) < 2: raise RuntimeError('\nUSAGE : ./split.py <filename> <parts:default 10>\n')
    split_file(argv[1], int(argv[2])) if len(argv) == 3 else split_file(argv[1])

