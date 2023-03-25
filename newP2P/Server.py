from os import listdir
from os.path import isfile, join
import requests
import socket

myip = "10.200.130.82"
myport = 12
mypath = "c:/temp"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

api_url = "https://p2papi2.azurewebsites.net/api/files"


s = socket.socket()
s.bind(('', myport))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
    connectionSocket, addr = s.accept()     # Establish connection with client.

    print('Got connection from ', addr)
    fileName = connectionSocket.recv(1024).decode()
    print("Opening file... ", fileName)
    file = open('C:/temp/' + fileName, 'rb')
    file_data = file.read(1024)
    while (file_data):
        print('Sending...')
        connectionSocket.send(file_data)
        file_data = file.read(1024)
    file.close()
    print("Done Sending")
    connectionSocket.shutdown(socket.SHUT_WR)
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()