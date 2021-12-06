import socket 
import time 
def recv_data(sock, length):
	data = b''
	while len(data) < length:
		more= sock.recv(length - len(data))
		if not more:
			pass 
		data += more
	return data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
s.bind(('0.0.0.0', 9999))
s.lisnten(1)
print("Server listening on 9999...")
try:
	sc, addr = as.accept()
	while True:
		rcvdata = recv_data(sc,16)
		time.sleep(0.01)
		pass
finally:
	sc.close()
	s.close()
	
	
