import socket
import os
import WLAN_INFO

host = '192.168.1.86'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall(b'client1-snr30-10.0.0.1\n')
data = s.recv(1024)
#s.close()
print('Received', repr(data))

