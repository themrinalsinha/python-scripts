#!/usr/bin/python3

######## PROBLEM STATEMENT ##########
# Neo has a complex matrix script. The matrix script is a X grid of strings. It consists of
# alphanumeric characters, spaces and symbols (!,@,#,$,%,&).

# To decode the script, Neo needs to read each column and select only the alphanumeric
# characters and connect them. Neo reads the column from top to bottom and starts
# reading from the leftmost column.
# If there are symbols or spaces between two alphanumeric characters of the decoded
# script, then Neo replaces them with a single space '' for better readability.
# Neo feels that there is no need to use 'if' conditions for decoding.
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
# Input​ ​Format
# The first line contains space-separated integers (rows) and (columns) respectively.
# The next lines contain the row elements of the matrix script.
# Constraints
# Note​: A score will be awarded for using 'if' conditions in your code.
# Output​ ​Format
# Print the decoded matrix script.
# Sample​ ​Input​
# 7 3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ir!
# Sample​ ​Output
# This is Matrix# %!
#####################################

user_input = [int(i) for i in input().split()]
line, char = user_input
inp_string = []

def parse_string(text):
    spcl   = ',@#$%&'
    trns   = str.maketrans(spcl, ' '*len(spcl))
    text   = text.translate(trns)
    return ' '.join(text.split())

for i in range(line): inp_string.append(input())
out_string = [inp_string[y][x] for x in range(char) for y in range(len(inp_string))]
out_string = ''.join([x for x in out_string])

print(parse_string(out_string))

# ==============================
"""
INPUT
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!

OUTPUT
This is Matrix !
"""
# ==============================