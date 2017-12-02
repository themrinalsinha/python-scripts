#!/usr/bin/python3
# Author : Mrinal Sinha

"""
Find Excel column name from a given column number. (or)
Find Excel column number from a given column name.

eg: MS Excel columns has a pattern like A, B, C, … ,Z, AA, 
AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, 
column 1 is named as “A”, column 2 as “B”, column 27 as “AA”.
"""

from string import ascii_uppercase

def _get_value(val, num_val=False):
    """
    returns mapping for corresponding character or number
    set 'num_val = True' when passing number (range 1-26)
    """
    mapping = {}
    for num, char in enumerate(ascii_uppercase):
        mapping[char] = num + 1
    if num_val == True:
        for k, v in mapping.items():
            if v == int(val):
                return k
    else:
        return mapping[val]

temp = []
def _calculate(num):
    q = num % 26; r = num // 26
    temp.append(q)
    if r > 26: _calculate(r)
    else: temp.append(r)
    return ''.join(_get_value(x, num_val=True) for x in temp)

def num_to_str(num):
    """
    Function to convert given number to corresponding
    column number. (eg: 1 -> A, 27 -> AA etc.)
    """
    if num <= 26: 
        return _get_value(num, num_val=True)
    else:
        return _calculate(num)[::-1]

def str_to_num(text):
    """
    Function to convert given string to corresponding
    column name. (eg: A -> 1, AA -> 27 etc.)
    """
    sum    = 0
    strlen = len(text) - 1
    for x in text:
        value = 26 ** strlen * _get_value(x)
        sum += value; strlen -= 1
    return sum

if __name__ == '__main__':
    in_value = input('Enter column name/number : ')
    if in_value.isdigit():
        in_value = int(in_value)
        print('Column name : {}'.format(num_to_str(in_value)))
    else:
        print('Numeric value : {}'.format(str_to_num(in_value.upper())))