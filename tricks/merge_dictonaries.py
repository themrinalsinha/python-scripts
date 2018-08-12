# How to merge two dictionaries
a = {'a' : 1, 'b' : 2}
b = {'aa' : 11, 'bb' : 22}
c = {'aaa' : 111, 'bbb' : 222}

# In python3
md = {**a, **b, **c}
print(md)

# In python2
mdd  = dict(a, **b)
mddd = dict(mdd, **c)
