from os   import getcwd
from csv  import writer, reader
from glob import glob

files = glob(getcwd() + '/*.csv', recursive = True)
with open('combined_files.csv', 'w') as outcsv:
    w = writer(outcsv)
    for file in files:
        with open(file) as csvfile:
            r = reader(csvfile)
            for row in r:
                w.writerow(row)
