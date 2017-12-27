#!/usr/bin/python3
# Author : Mrinal Sinha

"""
Script to fetch all saved wifi passwords from debian or ubuntu systems.
"""

from configparser import ConfigParser
from subprocess   import check_output

def get_ssids():
    ssids = check_output(['sudo', 'ls', '/etc/NetworkManager/system-connections'])
    return [ssid for ssid in ssids.decode('utf-8').split('\n') if ssid]

def get_userpass():
    connections = []
    config      = ConfigParser()
    for ssid in get_ssids():
        data = check_output(['sudo', 'cat', '/etc/NetworkManager/system-connections/{}'.format(ssid)])
        config.read_string(data.decode('utf-8'))
        connections.append((config['connection']['id'], config['wifi-security']['psk']))
    return connections

if __name__ == '__main__':
    print('{0:<25}{1}'.format('Username', 'Password'))
    for ssid in get_userpass():
        print('{0:<25}{1}'.format(ssid[0], ssid[1]))
