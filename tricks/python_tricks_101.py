# swapping values
a, b = 10, 5
print(a, b)
a, b = b, a
print(a, b)


# create a single string from all the elements in list
a = ['Hello', 'world', 'this', 'is', 'mrinal']
print(' '.join(a))


# Finding most frequest value in list
# ---- most frequest element in a list -----
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print('Set gives all unique element from list: ', set(a))
print('Max (without key) given max value in that list: ', max(set(a)))
print('Finding max base on number of repetation: ', max(set(a), key=a.count))
# ---- using counter from collection -----
from collections import Counter
cnt = Counter(a)
print('counter output: ',  cnt)
print('most frequest in counter: ', cnt.most_common(3))


# checking if two words are anagrams
# anagram = a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
from collections import Counter
print(Counter('mrinal'))
print(Counter('mrinal') == Counter('rnaiml'))


# reverse a string
a = 'abcdefghijklmnopqrstuvwxyz'
print('reverse is :', a[::-1])
print(reversed(a))
for char in reversed(a):
    print(char)
num = 123345567688
print(int(str(num)[::-1]))


# Transpose 2d array
original = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*original)
print(list(transposed))


# Chained comparison with all kind of operators
b = 6
print(4 < b < 7)
print(1 == b < 20)


# chained function call
# calling different functions with same arguments based on conditions
def product(a, b):
    return a * b
def add(a, b):
    return a + b
b = True
print((product if b else add)(5, 6))


# Copying list
# --- a fast way to make a shallow copy of a list ---
a = [1, 2, 3, 4, 5]
print('regular list: ', a)
b = a
print('assigning b=a: ', b)
b[0] = 11
print('b[0]=11 then A = ', a)
print('b[0]=11 then B = ', b)
# --- another way but it will noot affect the main list ---
b = a[:]
print('B: ', b)
print('A: ', a)
b[0] = 111
print('B: ', b)
print('A: ', a)
# --- copy list by typecasting method ---
a = [1, 2, 3, 4, 5]
print(list(a))
# --- using the list.copy() method ---
print('copy method ', a.copy())
# --- copy nested lists using copy.deepcopy ---
l = [[1, 2, 3], [4, 5, 6]]
from copy import deepcopy
l2 = deepcopy(l)
print(l2)


# Sort dictonary by value
d = {'apple': 1000, 'banana': 201, 'orange': 45, 'tomato': 123}
# ---- sorting based on value ---- x[1] for value x[0] for key
print(sorted(d.items(), key=lambda x: x[1]))
# ---- Sorting using operator.itemgetter as the sort key instead of a lambda ----
from operator import itemgetter
# 0 for key and 1 for value
print(sorted(d.items(), key=itemgetter(1)))
# ---- sort dict keys by value ----
print(sorted(d, key=d.get))
