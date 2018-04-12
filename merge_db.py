#!/usr/bin/python3

from os      import path
from glob    import glob
from tqdm    import tqdm
from sqlite3 import connect

if __name__ == '__main__':
    curr_path = path.abspath(path.dirname('__file__'))
    db_files  = glob(curr_path + '/*.sqlite3')
    print('\nDATABASES\n---------')
    for db in db_files:
        print(path.basename(db))
    if len(db_files) > 1:
        conn   = connect(db_files[0])
        curs   = conn.cursor()
        tables = curs.execute('SELECT name FROM sqlite_master WHERE type = "table";').fetchall()
        tables = [x[0] for x in tables]
        print('\nTABLES\n------')
        for table in tables:
            print(table)
        tablename = input('\nEnter table name to merge : ')
        if tablename not in tables:
            raise RuntimeError('Wrong table name choose from - {}'.format(tables))
        headers = [x[0] for x in (curs.execute('select * from %s' % tablename)).description]
        conn.close()

        for db in tqdm(db_files[1:], 'MERGING DB into -> {}'.format(path.basename(db_files[0]))):
            conn  = connect(db)
            curs  = conn.cursor()
            title = ','.join(x for x in headers)
            curs.execute('ATTACH DATABASE ? as main_db', (db_files[0],))
            curs.execute("INSERT OR IGNORE INTO {} SELECT {} FROM {}".format('main_db.'+tablename, title, tablename))
            conn.commit()
        conn.close()
    else:
        print('There is no or only one database file.')