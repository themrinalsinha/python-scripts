# equation = 'SEND + MORE = MONEY'
# 1. substitute M = 2
# 2. check:
#    max = 9, min = 0
#    compare max on left side with min on right side
#    compare min on left side with max on right side
#    if max_left < min_right or min_left > max_right
#        the current chosen substitutions (M = 2 in this example) can not lead to a valid solution.


import itertools


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s


def crypt_arithmatic(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

if __name__ == '__main__':
    crypt_arithmatic("SEND + MORE = MONEY")


# Other puzzles to try:
# query = "THREE + THREE + ONE = SEVEN"
# query = "SEND + MORE = MONEY"
# query = "I + BB = ILL"
# query = "WHOSE + TEETH + ARE + AS = SWORDS"
# query = "BILL + WILLIAM + MONICA = CLINTON"
# query = "GREEN + ORANGE = COLORS"
# query = "PACIFIC + PACIFIC + PACIFIC = ATLANTIC"
# query = "CASSATT + RENOIR = PICASSO"
# query = "MANET + MATISSE + MIRO + MONET + RENOIR = ARTISTS"
# query = "COMPLEX + LAPLACE = CALCULUS"
