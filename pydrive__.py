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


# # STEPS TO FOLLOW

# Step 1: download the zip file from attachment and extract it.

# Step 2: download the credentials.json file from https://developers.google.com/drive/api/v3/quickstart/python and download credentials.json then rename credentials.json to 'client_secrets.json' and put it into the extracted folder.

# Step 3: In the extracted folder there is a settings.yaml file open it and replace client_id and client_secret with the one you find in client_secrets.json

# Step 4: Now we have to create a virtual machine and install the required packages.
#     -> Open the extracted folder in cmd or shell.
#     -> run command: virtualenv -p python3 venv
#     -> run command: source venv/bin/activate
#     -> pip install -r requirements.txt
#     Once u r done with the above steps

# Step 5: In app.py you will see that the last line is commented, uncomment it and replace folder-id with your drives folder id, done!

# run the script for the first time it will open browser to authenticate and also downlaod all the json files from that folder and it will create 'output.json' file with all the merged files
