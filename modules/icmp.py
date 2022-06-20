# INTERNET CONTROL MESSAGE PROTOCOL

from sys import path
path.append('..')

from libs.assemble import assemble_packets

def icmp_arg_convert(arg_):
    u_char_2 = [
        int(str('%04x' % arg_)[:2], 16),
        int(str('%04x' % arg_)[2:4], 16)
    ]

    return u_char_2

def icmp_header(identifier, sequence_number, type_of_message, console_log):
    global console_logging
    console_logging = console_log

    if type_of_message == 'request':
        type_of_message = [0x08]
    elif type_of_message == 'reply':
        type_of_message = [0x0]

    code = [0x0]
    init_checksum = [0x0, 0x0]

    identifier = icmp_arg_convert(identifier)
    sequence_number = icmp_arg_convert(sequence_number)

    header = []

    header += type_of_message
    header += code
    header += identifier
    header += sequence_number

    raw_bytes = assemble_packets(header, init_checksum, False, 'icmp', console_log)

    return raw_bytes