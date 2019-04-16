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
