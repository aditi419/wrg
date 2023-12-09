import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        prunt(client.addr)

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()