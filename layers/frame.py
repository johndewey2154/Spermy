from sys import path
path.append('..')

from consts.ether_types import *
from libs.tools import mac_convert

def frame_header(destination_mac, source_mac, ether_type):
	src_mac = mac_convert(source_mac)
	dst_mac = mac_convert(destination_mac)

	if ether_type in ETHER_TYPES:
		ether_type = ETHER_TYPES[ether_type]
	else:
		raise Exception('Ethernet type is not in support types.')

	frame = []

	frame += dst_mac
	frame += src_mac
	frame += ether_type

	raw_bytes = [i.to_bytes(1, byteorder='big') for i in frame]
	raw_bytes = b''.join(raw_bytes)

	return raw_bytes