#!/usr/bin/python3
# Author : Mrinal Sinha

from tqdm       import tqdm
from subprocess import check_output

packages = check_output(['pip3', 'list', '--outdated']).decode("utf-8")
packages = tqdm([pkg.split(' ')[0] for pkg in packages.split('\n') if pkg])

for pkg in packages:
    packages.set_description('Updating: {}'.format(pkg))
    check_output(['sudo', '-H', 'pip3', 'install', '-Uq', '{}'.format(pkg)])