import socket

HOST='127.0.0.1'
PORT=30

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as soc:
    soc.connect((HOST,PORT))
    message=input("Enter the Message:").encode()
    soc.sendall(message)
    data=soc.recv(256)
    print('Received',repr(data))
