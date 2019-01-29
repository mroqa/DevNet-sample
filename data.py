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
            'app': 'RY_ELM1_N7KSRV_AGG01',
            'ip': '10.10.10.5'
        },
        {
            'id': '2',
            'app': 'RY_ELM1_N7KSRV_AGG02',
            'ip': '192.168.100.251'
        },
        {
            'id': '3',
            'app': 'RY_ELM1_N9KSRV_ACC01',
            'ip': '192.168.100.251'
        },
        {
            'id': '4',
            'app': 'RY_ELM1_N9KSRV_ACC02',
            'ip': '192.168.100.251'
        }
    ]


    return apps