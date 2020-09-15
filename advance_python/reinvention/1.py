
class Container:
    def __getitem__(self, index):
        print("GETTING: ", index)

    def __setitem__(self, index, value):
        print("SETTING: ", index, value)

c = Container()
c[12]
c['name'] = 'Mrinal'
c['name']
c[1:3]
# ------------------------------------------

x = {
    'a': 1,
    'c': 2,
    'b': 3,
    'd': 4,
}

# order is maintained
print(x)
print(x.keys())
# ------------------------------------------

