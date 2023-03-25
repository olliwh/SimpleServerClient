from socket import *
serverPort = 12
# serverSocket is the welcoming socket:
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)  # listens for request from client
print('The TCP server is ready to receive')


while True:
    # when client knocks on door:
    connectionSocket, addr = serverSocket.accept()
    # accept() creates new socket called connectionSocket
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
