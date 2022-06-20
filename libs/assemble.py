from sys import path
path.append('..')

from libs.tools import logger, checksum

def checksum_conv(chksum):
    u_char_2 = [
        int(str('%04x' % chksum)[:2], 16),
        int(str('%04x' % chksum)[2:4], 16)
    ]

    return u_char_2

def checksum_error(chksum):
    new_chksum_error = [i for i in chksum if i > 255]

    if new_chksum_error:
        chksum_error = f'Calculated {packet_to_calc} checksum greater than one byte'
        logger(chksum_error, 'warning', log_on=console_logging)

def packet_int_error(pckts):
    packet_error = [i for i in pckts if i > 255]

    if packet_error:
        int_error = f'{packet_to_calc} packet greater than one byte'
        logger(int_error, 'warning', log_on=console_logging)

def assemble_packets(array, chsm, calc, type_packet, console_log):
    packet_format = []

    global packet_to_calc
    packet_to_calc = type_packet

    global console_logging
    console_logging = console_log

    bool_tcp = type_packet == 'tcp'
    bool_udp = type_packet == 'udp'
    bool_ip = type_packet == 'ip'
    bool_icmp = type_packet == 'icmp'

    if calc and bool_tcp:
        del array[:12]
    elif calc and bool_udp:
        del array[:12]
        del array[6:]

    for i, n in enumerate(array):
        if i == 16 and bool_tcp and calc:
            packet_format += chsm
        elif i == 10 and bool_ip and calc:
            packet_format += chsm
        elif i == 2 and bool_icmp and calc:
            packet_format += chsm

        packet_format.append(n)
    
    if bool_udp and calc:
        packet_format += chsm
    
    if not calc:
        cal = checksum(packet_format, len(packet_format))
        cal = checksum_conv(cal)

        checksum_error(cal)

        return assemble_packets(packet_format, cal, True, type_packet, console_log)

    packet_int_error(packet_format)

    raw = [i.to_bytes(1, byteorder='big') for i in packet_format]
    return b''.join(raw)