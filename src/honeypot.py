import socket

ip = "127.0.0.1"
port = 2222
msg = "Connection Successful" 

Socket1 = socket.socket(socket.AF_INET)
Socket1.bind((ip,port))
Socket1.listen(1)
Socket1.accept()
print(msg)
