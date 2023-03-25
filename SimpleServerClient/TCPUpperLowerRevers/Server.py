from socket import *
import threading

def handleClient(connectionSocket, address):
    while True:
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        sentence = sentence.lower()
        errorMessage = "Don't understand"

        try:
            message = sentence.split(": ")[1][:-1]
            print(message)
        except:
            print("What????")
        if sentence[- 1] != ';':
            connectionSocket.send(errorMessage.encode())
        if sentence.startswith("upper"):
            returnMessage = message.upper()
            connectionSocket.send(returnMessage.encode())
        elif sentence.startswith("lower"):
            returnMessage = message.lower()
            connectionSocket.send(returnMessage.encode())
        elif sentence.startswith("reverse"):
            returnMessage = message[::-1]
            connectionSocket.send(returnMessage.encode())
        elif sentence.lower() == 'close;':
            endMessage = "Closing now"
            connectionSocket.send(endMessage.encode())
            connectionSocket.close()
            break
        else:
            connectionSocket.send(errorMessage.encode())
serverPort = 12
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
# brug client fra TCPMoreClient



