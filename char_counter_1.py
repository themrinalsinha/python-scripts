#!/usr/bin/python3

"""
    // Using lambda function
    input  : apple | balloon
    output : a2ple | ba2l2on
"""

from itertools import groupby

text         = input('Enter text : ')
string       = '' 
char_counter = lambda text : [(c, sum(1 for _ in fn)) for c, fn in groupby(text)]
for x in char_counter(text):
    if x[1] == 1: 
        string += x[0]
    else: 
        string += str(x[1]) + x[0]
print(string)