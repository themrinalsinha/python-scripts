#!/usr/bin/python3

"""
    input  : apple | balloon
    output : a2ple | ba2l2on
"""

def char_counter(text):
    count  = 1
    string = []
    for i in range(1, len(text)):
        if text[i-1] == text[i]:
            count += 1
        else:
            string.append([str(count),text[i-1]])
            count  = 1
    string.append([str(count),text[i]])
    return string

if __name__ == '__main__':
    text   = input()
    result = char_counter(text)
    string = ''
    for x in result:
        if x[0] == '1':
            string += x[1]
        else:
            string += x[0]+x[1]
    print(string)