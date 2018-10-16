import socket,threading

ip = '127.0.0.1';
port = 9390

def _recv(name, sock):
	while 1:
		try:
			data = sock.recv(1024)
			udata = data.decode('utf-8')
			print(udata)
		except:
			pass

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.connect((ip,port))
sock.settimeout(1)

name = input('Name: ')
name = name.encode('utf-8')
sock.sendto(name, (ip,port))
rT = threading.Thread(target = _recv, args = ("RecvThread",sock))
rT.start()
while 1:
	w = input()
	if w:
		sock.sendto(w.encode('utf-8'), (ip,port))
rT.join()
sock.close()
