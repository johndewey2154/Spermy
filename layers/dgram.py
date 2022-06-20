# USER DATAGRAM PROTOCOL

from sys import path
path.append('..')

from consts.dgram_consts import *
from libs.tools import ip_convert
from libs.assemble import assemble_packets

def udp_arg_convert(byte):
    u_char_2 = [
        int(str('%04x' % byte)[:2], 16),
        int(str('%04x' % byte)[2:4], 16),
    ]

    return u_char_2

def udp_header(
    source_ip, destination_ip, total_length, 
    source_port, destination_port, udp_payload, console_log):

    source_ip = ip_convert(source_ip)
    destination_ip = ip_convert(destination_ip)
    total_length = udp_arg_convert(total_length)
    source_port = udp_arg_convert(source_port)
    destination_port = udp_arg_convert(destination_port)

    pseudo = []
    header = []
    payload = []

    pseudo += source_ip
    pseudo += destination_ip
    pseudo += PADDING_1
    pseudo += UDP_PROTOCOL
    pseudo += total_length

    header += source_port
    header += destination_port
    header += total_length

    payload += [i for i in udp_payload]

    raw_bytes = assemble_packets(pseudo + header + payload, INIT_CHECKSUM, False, 'udp', console_log)

    return raw_bytes