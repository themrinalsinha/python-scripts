from yaml    import load, dump
from os.path import exists

data = {'apiVersion': 'v1'}
data.setdefault('clusters', [])
data.setdefault('contexts', [])

def write_data(data):
    with open('config.yaml', 'w') as f:
        dump(data, f, default_flow_style=False)

if not exists('config.yaml'):
    write_data(data)
config_data = load(open('config.yaml'))

if not config_data:
    raise RuntimeError("Invalid config file - (NOTE: if it is blank delete it!)")

cluster = {
    'name': input('CLUSTER - Name: '),
    'cluster': {
        'certificate-authority-data': input('CLUSTER - CA data: '),
        'server': input('CLUSTER - Server name: ')
    }
}

context = {
    'name': input('\nCONTEXT - Name: '),
    'context': {
        'cluster': input('CONTEXT - Cluster: '),
        'namespace': input('CONTEXT - Namespace: '),
        'user': input('CONTEXT - User: ')
    }
}

if cluster not in config_data.get('clusters'):
    config_data.get('clusters').append(cluster)
config_data.get('contexts').append(context)
write_data(config_data)
