import json
import socket
import threading

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def __init__(self):
        self.setServerConfig()
        self.sock.connect((self.host, self.port))

        inputThread = threading.Thread(target=self.sendMessage)
        inputThread.daemon = True
        inputThread.start()

        while True:
            data = self.sock.recv(1024)

            if not data:
                break
            print(str(data, "utf-8"))

    def setServerConfig(self):
        with open("ServerConfig.json") as jsonFile:
            data = json.load(jsonFile)
            self.host = data["host"]
            self.port = int(data["port"])

    def sendMessage(self):
        while True:
            self.sock.send(bytes(input(""), "utf-8"))


if __name__ == "__main__":
    Client()
