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
