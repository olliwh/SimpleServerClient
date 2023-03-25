from socket import *
import threading

serverPort = 12
# serverSocket is the welcoming socket:
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # listens for request from client
print('The TCP server is ready to receive')

#method does the client handeling
def handleClient(connectionSocket, addr):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence.encode())
        if sentence.lower() == 'close;':
            connectionSocket.close()
            break

while True:
    # when client knocks on door:
    connectionSocket, addr = serverSocket.accept()
    # handleClient(connectionSocket, addr) replaced by:
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
    # threading allows server to handle client at the same time

