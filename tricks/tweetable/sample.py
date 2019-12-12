# Generating random password
from random import choice
from string import ascii_letters, digits
print(''.join([choice(ascii_letters + digits) for _ in range(8)]))

# -----------------------------------------------------------------
# Gererating a column chart for any integer series, visible on terminals
from random import randint

ch = '█'
def col(sz):
    mn, mx = min(sz), max(sz)
    df  = (mx-mn) // 8
    bkt = [(el-mn) // df for el in sz]
    hrz = [f"{b}{c}" for b, c in [(ch*(el+1), " "*(8-el)) for el in bkt]]
    return "\n".join([" ".join(el) for el in list(map(list, zip(*hrz)))[::-1]])
series = [randint(10, 99) for _ in range(25)]
print(col(series))
