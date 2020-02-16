import json
import socket
import sys
import threading

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.setServerConfig()
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def setServerConfig(self):
        with open("ServerConfig.json") as jsonFile:
            data = json.load(jsonFile)
            self.host = data["host"]
            self.port = int(data["port"])

    def handler(self, cnx, address):
        while True:
            global connections
            data = cnx.recv(1024)
            for connection in self.connections:
                if connection == cnx:
                    continue

                payload = ("[" + str(address[1]) + "] said: " + str(data, "utf-8")).encode("utf-8")
                connection.send(bytes(payload))
            if not data:
                print(str(address[0]) + ":" + str(address[1]), "disconnected")
                self.connections.remove(cnx)
                cnx.close()
                break

    def run(self):
        while True:
            cnx, address = self.sock.accept()
            cnxThread = threading.Thread(target=self.handler, args=(cnx, address))
            cnxThread.daemon = True
            cnxThread.start()
            self.connections.append(cnx)
            print(str(address[0]) + ":" + str(address[1]), "connected")

if __name__ == "__main__":
    server = Server()
    server.run()