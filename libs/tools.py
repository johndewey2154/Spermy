from time import strftime

def logger(msg, msg_type, log_on=True):
	if log_on:
		if msg_type == 'info':
			print(strftime(f'[%H:%M:%S][INFO]: {msg}'))
		elif msg_type == 'warning':
			print(strftime(f'[%H:%M:%S][WARNING]: {msg}'))
	return

def mac_convert(mac_address):
	if isinstance(mac_address, str):
		mac_address = mac_address.split(':')
		if len(mac_address) != 6:
			raise Exception('Invalid mac address.')
		else:
			return [int(i, 16) for i in mac_address]
	else:
		raise Exception('Mac adress must be of type string.')

def ip_convert(ip_address):
	if isinstance(ip_address, str):
		octets = ip_address.split('.')
		if len(octets) > 4 or len(octets) < 4:
			raise Exception('Invalid ip address.')
		elif [j for j in octets if int(j) > 255]:
			raise Exception('Invalid ip address.')

		return [int(i) for i in octets]
	else:
		raise Exception('IP address must be of type string.')

def checksum(buff, size):
	sum = 0
	pointr = 0

	while size > 1:
		od_buff = '%02x' % buff[pointr]
		ev_buff = '%02x' % buff[pointr + 1]

		sum += int(str(od_buff) + str(ev_buff), 16)
		size -= 2
		pointr += 2

	if size:
		sum += buff[pointr]

	sum = (sum >> 16) + (sum & 0xffff)
	sum += (sum >> 16)

	return (~sum) & 0xffff