import  socket

'''

1.slide window
2.heartbeat
3.keepalive

'''

so=socket.socket()

so.connect(("172.16.103.125",30000))
buffer=""

so.sendall("xxxx".encode())
#so.recv(buffer,1024)




