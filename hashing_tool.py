# cli tool to has file in python

from os.path  import basename
from hashlib  import md5, sha1
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

md5_hasher = md5()
sha1_hasher = sha1()

try:
    with open(args.file, 'rb') as f:
        buffer = f.read()
        md5_hasher.update(buffer)
        sha1_hasher.update(buffer)
    print('\n{}\n{}\n{}\n'.format(basename(args.file), md5_hasher.hexdigest(), sha1_hasher.hexdigest()))
except FileNotFoundError as e:
    print(e)
