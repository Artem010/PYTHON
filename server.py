import socket, time

ip = '';
port = 9390
cl=[]
users =[]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))
# sock.listen(3)

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
# try:
while 1:
	try:
		data, addr = sock.recvfrom(1024)
	except:
		for n in users:
			if n['_addr'] == addr:
				print(n['_name'] + 'disconnected...')
		# print ('Disconnected' + c['_name'])
	udata = data.decode('utf-8')
	if not addr in cl:
		cl.append(addr)
		# clients.append(dict.fromkeys(['_name'], udata))
		users.append({'_name':udata, '_addr': addr})
		# clients.append(dict(_name=data, _addr=addr))
		print(udata + ' join from: ' + str(addr[0].replace(' ', '')) + ':' + str(addr[1]).replace(' ', '') + ' [' + time.strftime('%X') + ']')
		sendALL(addr, 'join from chat', True)
	else:
		if not data: break
		if udata == '/online':
			sock.sendto(str(len(users)).encode('utf-8'), addr)
		else:
			udata = udata.upper()
			# udata = udata.encode('utf-8')
			sendALL(addr, udata)
# except socket.error as err:
# 	print(err)
sock.close()

# [

# 			{'Name': 'bob',
# 			 'addr': [123.4324.4324, 888]},
# 			{'Name': 'bob',
# 			 'addr': [123.4324.4324, 888]},
# 			{'Name': 'bob',
# 			 'addr': [123.4324.4324, 888]}

# 			]