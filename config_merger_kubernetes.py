from json    import load as json_load
from yaml    import load, dump, SafeLoader
from os.path import exists, join

# Checking if input.json exists or not
if not exists('input.json'):
    raise RuntimeError('JSON file missing!')

# Checking if output.yaml exists or not
if not exists('output.yaml'):
    open('output.yaml', 'w').close()

# Helper function to write data
def write_data(data):
    with open('output.yaml', 'w') as outfile:
        dump(data, outfile, default_flow_style=False)

# Loading input and output data
input_data  = json_load(open('input.json'))
output_data = load(open('output.yaml'), Loader=SafeLoader)
final_data  = []

# Mandatory checking if input data is present or not
if not input_data:
    raise RuntimeError('Input file does not contain any configuration')

# Removing repetation from input.json
_temp_list = []
for data in input_data:
    if data not in _temp_list:
        _temp_list.append(data)

# Comparing if any of the data from input.json is already present in output.yaml
if output_data:
    for _data in _temp_list:
        if _data not in output_data:
            output_data.append(_data)
    write_data(output_data)
else:
    write_data(_temp_list)
