from json    import load
from difflib import get_close_matches

dictionary = load(open('dictionary.json'))
dictionary = dict([(k.lower(), v) for k, v in dictionary.items()])

def definition(word):
    meaning = dictionary.get(word, None)
    if meaning:
        return meaning
    else:
        similar = get_close_matches(word, dictionary.keys(), n=1, cutoff=0.75)
        if similar:
            return 'Did you mean "{}" instead ?'.format(similar[0])
        return 'Word do not exists!'

while True:
    w = input('\nEnter word: ').lower()
    print(definition(w))
