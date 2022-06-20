from layers.frame import frame_header
from layers.inet import ip_header
from modules.icmp import icmp_header
from libs.utils import send_data
from consts.uchar import *
import random

def send_ping(
    interface, source_mac, destination_mac, 
    source_ip, destination_ip, 
    type_of_message, ip_time_to_live=64, logs_on=True
    ):
    ether_type = 'IPv4'

    ip_identification = random.randint(0, U_CHAR_2)
    ip_protocol = 'ICMP'
    ip_length = 20

    icmp_identifier = random.randint(0, U_CHAR_2)
    icmp_sequence_number = random.randint(0, U_CHAR_2)

    icmp_pkt = icmp_header(icmp_identifier, icmp_sequence_number, type_of_message, logs_on)
    ip_pkt = ip_header(
        ip_identification, ip_time_to_live, ip_protocol, len(icmp_pkt) + ip_length, 
        source_ip, destination_ip, logs_on
        )
    frame_pkt = frame_header(destination_mac, source_mac, ether_type)

    send_data(interface, frame_pkt + ip_pkt + icmp_pkt, None, 1)

if __name__ == "__main__":
    send_ping(
        'TP-Link Wireless USB Adapter',
        '12:34:56:78:9a:9b',
        'a1:a2:a3:a4:a5:a6',
        '192.168.1.12',
        '192.168.1.1',
        'request'
    )