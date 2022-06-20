TCP_FLAGS_CODE = {
    '0x1': 'FIN',
    '0x2': 'SYN',
    '0x4': 'RST',
    '0x8': 'PSH',
    '0x10': 'ACK',
    '0x20': 'URG',
    '0x11': 'FIN ACK',
    '0x12': 'SYN ACK',
    '0x14': 'RST ACK',
    '0x18': 'PSH ACK'
}

TCP_FLAGS = {
    'FIN': [0x1],
    'SYN': [0x2],
    'RST': [0x4],
    'PSH': [0x8],
    'ACK': [0x10],
    'URG': [0x20],
    'FIN ACK': [0x11],
    'SYN ACK': [0x12],
    'RST ACK': [0x14],
    'PSH ACK': [0x18]
}