#!/usr/bin/python3
# Author : Mrinal Sinha

from tqdm       import tqdm
from subprocess import check_output

# TODO: Supress working in some cases
packages = check_output(['pip3', 'list', '--outdated']).decode("utf-8")
packages = tqdm([pkg.split(' ')[0] for pkg in packages.split('\n') if pkg][2:])

for pkg in packages:
    packages.set_description('Updating: {}'.format(pkg))
    try:
        check_output(['python3', '-m', 'pip', 'install', '-Uq', '{}'.format(pkg)])
    except:
        print('{} - failed to update !'.format(pkg))
