# DOMAIN NAME SYSTEM

from sys import path
path.append('..')

from libs.tools import logger

def dns_arg_conv(arg_to_convert):
    u_char_2 = [
        int(str('%04x' % arg_to_convert)[:2], 16),
        int(str('%04x' % arg_to_convert)[2:4], 16)
    ]

    return u_char_2

def packet_int_error(pckts, console_log):
    packet_error = [i for i in pckts if i > 255]

    if packet_error:
        int_error = 'DNS packet greater than one byte'
        logger(int_error, 'warning', console_log)

def dns_header(transaction_id, name, console_log):
    flags = [0x1, 0x0]
    questions = [0x0, 0x1]
    answer_rrs = [0x0, 0x0]
    authority_rrs = [0x0, 0x0]
    additional_rrs = [0x0, 0x0]
    type = [0x0, 0x1]
    class_in = [0x0, 0x1]
    padding_1 = [0x0]

    transaction_id = dns_arg_conv(transaction_id)

    group_size = [len(i) for i in name.split('.')]
    name_split = [i for i in name.split('.')]
    name = []

    for i in range(len(name_split)):
        name.append(group_size[i])
        for j in name_split[i]:
            name.append(ord(j))

    header = []
    queries = []

    header += transaction_id
    header += flags
    header += questions
    header += answer_rrs
    header += authority_rrs
    header += additional_rrs

    queries += name
    queries += padding_1
    queries += type
    queries += class_in

    packet_int_error(header + queries, console_log)

    raw = [i.to_bytes(1, byteorder='big') for i in header + queries]
    raw = b''.join(raw)

    return raw
