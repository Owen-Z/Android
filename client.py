import socket
import time 
ip_port = ("192.168.100.144", 9999)
data = "0123456789\n" * 100
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	c.connect(ip_port)
	print("Connected.")
	time.sleep(1)
	i=0
	while i < 10:
		print("Send:" + data)
		c.send(data.enconde())
		i = i + 1
finally:
	print("SEnt. Waiting ")
while True:
	time.sleep(0.001)
