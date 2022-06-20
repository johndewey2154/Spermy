# INTERNET PROTOCOL VERSION 4

from sys import path
path.append("..")

from consts.inet_protocols import *
from consts.inet_consts import *
from libs.tools import ip_convert
from libs.assemble import assemble_packets

def ip_arg_convert(arg, size):
	if size == 1:
		u_char_1 = [int(str('%02x' % arg), 16)]

		return u_char_1

	elif size == 2:
		u_char_2 = [
			int(str('%04x' % arg)[:2], 16),
			int(str('%04x' % arg)[2:4], 16)
		]

		return u_char_2

def ip_header(
	identification, time_to_live, protocol,
	total_length, source_ip, destination_ip, console_log):

	identification = ip_arg_convert(identification, 2)
	time_to_live = ip_arg_convert(time_to_live, 1)
	protocol = IP_PROTOCOLS[protocol]
	total_length = ip_arg_convert(total_length, 2)
	source_ip = ip_convert(source_ip)
	destination_ip = ip_convert(destination_ip)

	header = []

	header += VERSION_IHL
	header += TYPE_OF_SERVICE
	header += total_length
	header += identification
	header += FRAGMENT_SET
	header += OFFSET
	header += time_to_live
	header += protocol
	header += source_ip
	header += destination_ip

	raw_bytes = assemble_packets(header, INIT_CHECKSUM, False, 'ip', console_log)

	return raw_bytes