from layers.frame import frame_header
from modules.arp import arp_header
from libs.utils import send_data

def send_arp(interface, sender_mac, target_mac, sender_ip, target_ip, arp_message_type, logs_on=True):
    if arp_message_type == 'request':
        target_mac = 'ff:ff:ff:ff:ff:ff'
        arp_mac_target = '00:00:00:00:00:00'
    elif arp_message_type == 'reply':
        arp_mac_target = target_mac
    
    frame_pkt = frame_header(target_mac, sender_mac, 'ARP')
    arp_pkt = arp_header(sender_ip, target_ip, sender_mac, arp_mac_target, arp_message_type, logs_on)
    send_data(interface, frame_pkt + arp_pkt, None, 1)

if __name__ == "__main__":
    # INTERFACE
    # SOURCE MAC ADDRESS
    # DESTINATION MAC ADDRESS
    # SOURCE IP ADDRESS
    # DESTINATION IP ADDRESS
    # ARP MESSAGE TYPE

    send_arp(
        'TP-Link Wireless USB Adapter',
        '12:34:56:78:9a:9b',
        None,
        '192.168.1.12',
        '192.168.1.1',
        'request'
    )
