# Generating random password
from random import choice
from string import ascii_letters, digits
print(''.join([choice(ascii_letters + digits) for _ in range(8)]))

