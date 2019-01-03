import timeit

cy = timeit.timeit('sentdex_tut_2.test(100000)', setup='import sentdex_tut_2', number=100)
py = timeit.timeit('sentdex_tut_2.test(100000)', setup='import sentdex_tut_py', number=100)

print(cy, py)
print('Cython is {} times faster'.format(cy/py))
