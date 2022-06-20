# ADDRESS RESOLUTION PROTOCOL

from sys import path
path.append('..')

from libs.tools import mac_convert, ip_convert, logger

def packet_int_error(pckts):
	packet_error = [i for i in pckts if i > 255]

	if packet_error:
		int_error = 'ARP packet greater than one byte'
		logger(int_error, 'warning', log_on=console_logging)

def arp_header(sender_ip, target_ip, sender_mac, target_mac, opcode, console_log):
	hardware_type = [0x0, 0x1]
	protocol_type = [0x8, 0x0]
	hardware_size = [0x6]
	protocol_size = [0x4]

	global console_logging
	console_logging = console_log

	if opcode == 'request':
		opcode = [0x0, 0x1]
	elif opcode == 'reply':
		opcode = [0x0, 0x2]
	else:
		raise Exception('Invalid opcode argument.')

	sender_mac = mac_convert(sender_mac)
	sender_ip = ip_convert(sender_ip)
	target_mac = mac_convert(target_mac)
	target_ip = ip_convert(target_ip)

	header = []

	header += hardware_type
	header += protocol_type
	header += hardware_size
	header += protocol_size
	header += opcode
	header += sender_mac
	header += sender_ip
	header += target_mac
	header += target_ip

	packet_int_error(header)

	raw_bytes = [i.to_bytes(1, byteorder='big') for i in header]
	raw_bytes = b''.join(raw_bytes)

	return raw_bytes