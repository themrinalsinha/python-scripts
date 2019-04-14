from os.path import abspath, dirname, join, exists
from os      import mkdir
from glob    import glob
from tqdm    import tqdm
from json    import load, dumps
from shutil  import rmtree

from pydrive.auth  import GoogleAuth
from pydrive.drive import GoogleDrive

class MergeJSONfromGDrive(object):
    def __init__(self, folder_id):
        self.BASE_PATH = abspath(dirname(__name__))
        self.folder_id = folder_id
        self.auth      = GoogleAuth()
        self.auth.LocalWebserverAuth()
        self.drive     = GoogleDrive(self.auth)

        if not exists(join(self.BASE_PATH, 'json_dump')):
            mkdir(join(self.BASE_PATH, 'json_dump'))

    def get_data(self):
        meta_data = self.drive.ListFile({'q': "'{}' in parents and trashed=false".format(self.folder_id)}).GetList()
        return dict([(x.get('id'), x.get('title')) for x in meta_data if x.get('fileExtension') == 'json'])

    def download_and_merge(self, delete=None):
        meta_info = self.get_data()

        for file_key, file_name in tqdm(meta_info.items(), 'Downloading'):
            f = self.drive.CreateFile({'id': file_key})
            f.GetContentFile(join(self.BASE_PATH, 'json_dump', file_name))

        json_files = glob(join(self.BASE_PATH, 'json_dump', '*.json'))
        json_data  = []
        for j_file in json_files:
            _data = None
            try:
                _data = load(open(j_file, encoding='utf-16'))
            except:
                _data = load(open(j_file, encoding='utf-8'))
            if isinstance(_data, list):
                [json_data.append(x) for x in _data]
            elif isinstance(_data, dict):
                json_data.append(_data)

        open(join(self.BASE_PATH, 'output.json'), 'w').write(dumps(json_data))

        if delete:
            rmtree(join(self.BASE_PATH, 'json_dump'))

MergeJSONfromGDrive('<folder id>').download_and_merge()
