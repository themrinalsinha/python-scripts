from itertools import permutations

def validate_name(ORIGINAL_NAME, PROVIDED_NAME):
    ORIGINAL_NAME       = ORIGINAL_NAME.lower()
    PROVIDED_NAME       = PROVIDED_NAME.lower()

    # Check if both the names are equal
    if ORIGINAL_NAME == PROVIDED_NAME:
        return True

    ORIGINAL_NAME       = ORIGINAL_NAME.lower().split(' ')
    FAMILY_NAME         = ORIGINAL_NAME[-1]
    OTHER_NAME          = ORIGINAL_NAME[:-1]
    NAME_COMBINATIONS   = []

    # Validating name based of permutations
    for i in range(1, len(ORIGINAL_NAME) + 1):
        combi = list(permutations(ORIGINAL_NAME, i))
        for _ in combi:
            if PROVIDED_NAME == ' '.join(_):
                return True

    # Validating based on initials
    for i in range(1, len(OTHER_NAME) + 1):
        combi = list(permutations(OTHER_NAME, i))
        for _ in combi:
            initials = [x[0] for x in _]
            _w = ''.join(initials) +' '+ FAMILY_NAME
            _x = ' '.join(initials) +' '+ FAMILY_NAME
            _y = '. '.join(initials) +' '+ FAMILY_NAME
            _z = '. '.join(initials) +'. '+ FAMILY_NAME
            if PROVIDED_NAME in (_w, _x, _y, _z):
                return True
    return False

while True:
    original_name = input('ORIGINAL NAME: ').strip()
    provided_name = input('PROVIDED NAME: ').strip()
    print('Match: ', validate_name(original_name, provided_name), end='\n--------------\n')

# print(validate_name('mrinal vinay sinha', 'mrinal sinha'))
