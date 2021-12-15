import socket 
HEADER_LENGTH = 12 # Allows you to have messages of length 10^12 - 1
DECODE_TO = 'utf-8'
HOST = socket.gethostname()
PORT = 8000


def modify(s):
	if isinstance(s, str):
		s = s.strip()
		return f"{len(s):<{HEADER_LENGTH}}" + s
	else: 
		return None