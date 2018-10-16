import socket, time

ip = '';
port = 9390
cl=[]
users =[]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))

def sendALL(addr, udata, add=False):
	for c in users:
			if c['_addr'] != addr:
				for _nm in users:
					if _nm['_addr'] == addr:
						nm = _nm['_name']
				nm = nm + ': ' + udata
				if not add:
					print('[', nm, ']', time.strftime('%X'))
				nm = nm.encode('utf-8')
				sock.sendto(nm, c['_addr'])
while 1:
	try:
		data, addr = sock.recvfrom(1024)
		udata = data.decode('utf-8')
		if not addr in cl:
			cl.append(addr)
			users.append({'_name':udata, '_addr': addr})
			print(udata + ' join from: ' + str(addr[0].replace(' ', '')) + ':' + str(addr[1]).replace(' ', '') + ' [' + time.strftime('%X') + ']')
			sendALL(addr, 'join from chat', True)
		else:
			if not data: break
			if udata == '/online':
				sock.sendto(str(len(users)).encode('utf-8'), addr)
			else:
				udata = udata.upper()
				sendALL(addr, udata)
	except:
		for n in users:
			if n['_addr'] == addr:
				print(n['_name'] + ' disconnected...')
				users.remove(n)
				break
sock.close()
