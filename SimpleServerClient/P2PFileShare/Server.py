from socket import *
from os import listdir
from os.path import isfile, join

import requests as requests
mypath = "c:/temp"
myip = "127.0.0.1"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
serverPort = 12

api_url = "http://localhost:5273/api/files"
for filename in onlyfiles:
    filenamejson = {"ip": myip, "port": serverPort}
    response = requests.post(api_url + "/" + filename, json=filenamejson)  # samme med delete
    print(response)
    print('response json:')
    print(response.json())
# serverSocket is the welcoming socket:
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))  # ''normalt en ip adresse, nå den er tom betyder det alle ip adresser på min pc det har ikke noget med kliemt
serverSocket.listen(5)  # listens for request from client, 5 hvor mange kan være i kø af gangen
print('The TCP server is ready to receive')
response = requests.get(api_url)
data = response.json()



while True:
    # when client knocks on door:
    connectionSocket, addr = serverSocket.accept()
    # accept() creates new socket called connectionSocket
    fileName = connectionSocket.recv(1024).decode()  # 1024 op til så mange bytes vi læser af gangen ind 1024 karrektere
    file = open('C:/temp/' + fileName, 'rb')  # rb read byte man kan også skrive i dem med en anden end rb
    file_data = file.read(1024)
    while (file_data):  # mens vi har data i filen
        print('Sending...')
        connectionSocket.send(file_data)
        file_data = file.read(1024)  # her ser vi om der er data
    file.close()
    print("Done Sending")
    connectionSocket.close()
