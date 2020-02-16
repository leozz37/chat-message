import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 5000))
sock.listen(1)

connections = []

def handler(cnx, address):
    while True:
        global connections
        data = cnx.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connection.remove(cnx)
            cnx.close()
            break

while True:
    cnx, address = sock.accept()
    cnxThread = threading.Thread(target=handler, args=(cnx, address))
    cnxThread.daemon = True
    cnxThread.start()
    connections.append(cnx)
    print(connections)
