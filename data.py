__author__ = 'moahmed'

def Commands():
    commands = [
        {
            'id': 1,
            'cmd': 'show running-config'
        },
        {
            'id': 2,
            'cmd': 'show mac address-table'
        },
        {
            'id': 3,
            'cmd': 'show ip arp'
        },
        {
            'id': 4,
            'cmd': 'show version | in software'
        }
    ]

    return commands

''' Devices list '''

def Devices():
    devices = [
        {
            'username': '',
            'password': '',
            'device_type': 'cisco_nxos',
            'ip': '192.168.100.106',
        },
        {
            'device_type': 'cisco_nxos',
            'ip': '192.168.100.107',
            'username': '',
            'password': '',
        },
        {
            'device_type': 'cisco_nxos',
            'ip': '192.168.100.114',
            'username': '',
            'password': '',
        },
        {
            'device_type': 'cisco_nxos',
            'ip': '192.168.100.115',
            'username': '',
            'password': '',
        }
    ]

    return devices


def Apps():
    apps = [
        {
            'id': '1',
            'app': 'Nexus_01',
            'ip': '10.10.10.5'
        },
        {
            'id': '2',
            'app': 'Nexus_02',
            'ip': '192.168.10.251'
        },
        {
            'id': '3',
            'app': 'Nexus_011',
            'ip': '192.168.10.251'
        },
        {
            'id': '4',
            'app': 'Nexus_022',
            'ip': '192.168.10.251'
        }
    ]


    return apps