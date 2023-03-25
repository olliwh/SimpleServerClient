from socket import *
# server adress:
serverName = '127.0.0.1'
serverPort = 12
# Make client Socket:
clientSocket = socket(AF_INET, SOCK_STREAM)
# SOCK_STREAM says its TCP
# Here we establish Connection with server adress:
clientSocket.connect((serverName, serverPort))
while True:
    sentence = input('Input lowercase sentence:')

    clientSocket.send(sentence.encode())  # no address needed
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    if sentence == 'close':
        clientSocket.close()
        break
