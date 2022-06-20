from sys import path
path.append('..')

from libs import winpcapy as wcap

def capture_packets(device, callback):
    wcap.WinPcapUtils.capture_on(device, callback)

def list_devices():
    with wcap.WinPcapDevices() as devices:
        for device in devices:
            name = device.name
            description = device.description
            print(name.decode(),description.decode())

def find_device(dev):
    name, description = wcap.WinPcapDevices.get_matching_device(dev)
    if dev == description:
        return True
    return False

def send_data(dev, data_to_send, callback, limit):
    wcap.WinPcapUtils.send_packet(
        dev, data_to_send, callback=callback, limit=limit
        )