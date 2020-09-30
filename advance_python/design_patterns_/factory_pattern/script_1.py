import json
import xml.etree.ElementTree as etree

"""
The JSONConnector class parses the JSON file and has a parsed_data() method, that
returns all data as a dictionary (dict). The property decorator is used to make
parsed_data() appear as a normal variable instead of a method as follows.
"""
class JSONConnector:

    def __init__(self, filepath) -> None:
        self.data = dict()
        with open(filepath, encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

"""
The XMLConnector class parse the XML file and has a parsed_data() method that returns
all data as a list of xml.etree.Element as follows
"""
class XMLConnector:

    def __init__(self, filepath) -> None:
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

"""
The connection_factory() function is a Factory Method. It returns as instance of
JSONConnector or XMLConnector depending on the extension of the input file path
as follows
"""
def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError(f'Cannot connect to - {filepath}')
    return connector(filepath)

"""
The connect_to() function is a wrapper of connection_factory(). It adds exception
handling as follows
"""
def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(f'ValueError: {ve}')
    return factory

"""
The main() function demonstrate how the factory method design pattern can be used. The
first part makes sure that exception handling is effective as follows
"""
def main():
    sqlite_factory = connect_to('person.sq3')

    # let's connect to to XML factory
    print(f"\n{'xml data':-^50}")
    xml_factory = connect_to('person.xml')
    xml_data    = xml_factory.parsed_data
    liars       = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    for liar in liars:
        print(f'first name: {liar.find("firstName").text}')
        print(f'last name: {liar.find("lastName").text}')

    # let's connect to to JSON factory
    print(f"\n{'json data':-^50}")
    json_factory = connect_to('donut.json')
    json_data = json_factory.parsed_data
    for donut in json_data:
        print("Name: ", donut['name'])
        print("Price: ", donut['ppu'])

"""
Notice that although JSONConnector and XMLConnector have the same interfaces, what is
returned by parsed_data() is not handled in a uniform way. Different python code must
be used to work with each connector.
"""

if __name__ == '__main__':
    main()
