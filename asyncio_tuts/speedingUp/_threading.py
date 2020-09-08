import json
from urllib.request import urlopen, Request

def write_genre(file_name):
    """
    Uses genrenator from binaryjazz.us to write a random genre to the
    name of the given file
    """

    req = Request("https://binaryjazz.us/wp-json/genrenator/v1/genre/", headers={'User-Agent': 'Mozilla/5.0'})
    genre = json.load(urlopen(req))

    with open(file_name, "w") as new_file:
        print(f'Writing "{genre}" to "{file_name}"...')
        new_file.write(genre)
