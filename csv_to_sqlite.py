#!/usr/bin/python3
# Author : Mrinal Sinha
# Script to load/create data from csv to sqlite database.

from sys     import argv
from csv     import reader
from os.path import basename 
from sqlite3 import connect

def create_db(file_name, data):
    conn = connect(file_name.split('.')[0] + '.db')
    curs = conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS {} ({})".format(file_name.\
                            split('.')[0], ', '.join(x for x in next(data))))

    iter_data = iter(data); next(iter_data)
    for row in iter_data:
        try:
            # TODO: Handle fields containing '' or ""
            curs.execute("INSERT INTO {} VALUES ({})".format(file_name.split('.')[0], \
                            ', '.join('"' + x + '"' for x in list(row))))
        except: pass
    conn.commit()

if __name__ == '__main__':
    if len(argv) > 1:
        file_name = basename(argv[1])
        with open(argv[1], 'r') as csvfile:
            file_reader = reader(csvfile)
            create_db(file_name, file_reader)
    else:
        raise RuntimeError('Please, give csv file...')