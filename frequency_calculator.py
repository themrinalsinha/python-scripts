#!/usr/bin/python3
# Author : Mrinal Sinha

"""
Script to calculate frequency of the characters 
in a given string and plot it as bar chart.
"""

from string import ascii_lowercase
import matplotlib.pyplot as plt

def frequency_graph(char_dict):
    # Plots graph. :)
    f = []; c = []
    for x, y in char_dict.items():
        c.append(x); f.append(y)
    plt.bar(range(26), f)
    plt.xticks(range(26), c)
    plt.show()

def character_frequency(string):
    """
    Initialize all the characters (a-z) to 0 in a dictonary.
    Get the input string iterate over it and update the dictonary.
    """
    char_dict = dict([(x, 0) for x in ascii_lowercase])
    for x in string:
        if x in char_dict.keys():
            char_dict[x] += 1
    frequency_graph(char_dict)

if __name__ == '__main__':
    # Enter either string or give path to file.txt as input
    in_string = input('Enter string or [path to .txt file] : ')
    if in_string.split('.')[-1] == 'txt':
        string = ' '.join(open(in_string, 'r').read().split('\n')).lower()
    else:
        string = in_string.lower()
    character_frequency(string)