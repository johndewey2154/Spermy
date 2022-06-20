# TRANSMISSION CONTROL PROTOCOL

from sys import path
path.append('..')

from consts.stream_flags import *
from consts.stream_consts import *
from libs.assemble import assemble_packets
from libs.tools import ip_convert

def tcp_arg_convert(byte, size):
	if size == 2:
		u_char_2 = [
			int(str('%04x' % byte)[:2], 16),
			int(str('%04x' % byte)[2:4], 16)
		]

		return u_char_2

	elif size == 4:
		u_char_4 = [
			int(str('%08x' % byte)[:2], 16),
			int(str('%08x' % byte)[2:4], 16),
			int(str('%08x' % byte)[4:6], 16),
			int(str('%08x' % byte)[6:8], 16)
		]

		return u_char_4

def tcp_header(
	source_ip, destination_ip, total_length,
	source_port, destination_port, sequence_number,
	acknowledgement_number, flags, console_log):

	protocol = [0x0, 0x6]
	source_ip = ip_convert(source_ip)
	destination_ip = ip_convert(destination_ip)
	total_length = tcp_arg_convert(total_length, 2)

	source_port = tcp_arg_convert(source_port, 2)
	destination_port = tcp_arg_convert(destination_port, 2)
	sequence_number = tcp_arg_convert(sequence_number, 4)
	acknowledgement_number = tcp_arg_convert(acknowledgement_number, 4)
	flags = TCP_FLAGS[flags]

	pseudo = []
	header = []

	pseudo += protocol
	pseudo += source_ip
	pseudo += destination_ip
	pseudo += total_length

	header += source_port
	header += destination_port
	header += sequence_number
	header += acknowledgement_number
	header += OFFSET_RESERVED
	header += flags
	header += WINDOW_SIZE
	header += URGENT_POINTER

	raw_bytes = assemble_packets(pseudo + header, INIT_CHECKSUM, False, 'tcp', console_log)

	return raw_bytes