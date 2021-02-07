import socket

HOST='127.0.0.1'
PORT=30
sockett=(HOST,PORT)
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind((sockett))
print("Listening for connections")
soc.listen()

connection.addr=soc.accept()
with connection:
    print('connected',addr)
    while True:
        data=connection.recv(1024)
        if not data:
            break
        connection.sendall(data)
        print(data)
