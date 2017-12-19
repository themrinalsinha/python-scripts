#!/usr/bin/python3

from tsv     import format_fields
from csv     import reader
from sys     import argv
from os.path import splitext

with open(argv[1], 'r') as csvfile:
    with open(splitext(argv[1])[0] + '.tsv', 'w') as tsvfile:
        for record in reader(csvfile):
            tsvfile.write(format_fields(record) + '\n')
