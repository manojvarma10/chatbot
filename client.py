import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8090))

while True:
    nb = raw_input('send a message: ')
    print(nb)
    clientsocket.send(nb)
    print clientsocket.recv(1024)
