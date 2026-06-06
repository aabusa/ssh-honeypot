import socket
from datetime import datetime


ip = "127.0.0.1"
port = 2222
msg = "Connection Successful"
file_name = input("pleas enter the file name: ")
path = "data/" + file_name + ".log"


print(path)
Socket1 = socket.socket(socket.AF_INET)
Socket1.bind((ip,port))
Socket1.listen(1)

while True :
    soc,con_adr = Socket1.accept()
    client_ip = con_adr[0]
    con_datetime = datetime.now()
    print(msg)
    with open(path , 'a') as file :
        file.write(f"{con_datetime} Failed connection from {client_ip}\n")
        soc.close()