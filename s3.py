#!/usr/bin/python3
from os    import path, listdir, makedirs, getcwd
from sys   import argv
from glob  import glob
from json  import load
from tqdm  import tqdm
from boto3 import client

ACCESS_KEY = ''
SECRET_KEY = ''

class Corpdata(object):
    def __init__(self, basedir):
        self.basedir   = basedir
        self.currdir   = getcwd()
        self.connect   = client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
        self.zipfile   = ([x for x in glob(path.join(basedir, '*.zip')) if 'failed' not in x] or [None])[0]
        self.receipts  = [x for x in glob(path.join(basedir, '*')) if '.zip' not in x]
        self.json_file = (glob(path.join(basedir, '*.json')) or [None])[0]

    def __str__(self):
        return path.basename(self.basedir)

    def _upload(self, filepath, bucket_name, filename=None):
        filename = filename if filename else path.basename(filepath)
        self.connect.upload_file(filepath, bucket_name, filename)

    def _list_bucket_content(self, bucket, keyword=''):
        content  = self.connect.list_objects(Bucket=bucket).get('Contents')
        return [x.get('Key') for x in content if keyword in x.get('Key')]

    def _download(self, bucket_name, filekey, download_dir=''):
        self.connect.download_file(bucket_name, filekey, path.join\
        (self.currdir, download_dir, path.basename(filekey)))

    def upload_files(self):
        order_no = path.basename(self.basedir)
        self._upload(self.zipfile, 'corpdata-backup')
        for _ in self.receipts:
            filename = '{}/{}'.format(order_no, path.basename(_))
            self._upload(_, 'corpdata-orders', filename=filename)

    def get_jsons(self):
        if not path.exists(path.join(self.currdir, 'JSON_FILES')):
            makedirs(path.join(self.currdir, 'JSON_FILES'))
        for _ in tqdm(self._list_bucket_content('corpdata-orders', keyword='json')):
            self._download('corpdata-orders', _, 'JSON_FILES')

if __name__ == '__main__':
    if len(argv) < 2:
        raise RuntimeError('Please pass path to base directory.')
    orders_path = tqdm([Corpdata(path.abspath(path.join(argv[1], x))) for x in listdir(argv[1])])

    for order in orders_path:
        orders_path.set_description('Processing: {}'.format(order))
        order.upload_files()
