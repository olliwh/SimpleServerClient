from socket import *
import requests
api_url = "http://localhost:5273/api/files"
responce = requests.get(api_url)
data = responce.json()

fileName = data[0]
print(fileName)

response = requests.get(api_url + "/" + fileName)
data = response.json()

# serverIP = data[0]["ipAddress"]
# serverPort = data[0]["port"]

# server adress:
serverName = '127.0.0.1'
serverPort = 12
# Make client Socket:
clientSocket = socket(AF_INET, SOCK_STREAM)
# SOCK_STREAM says its TCP
# Here we establish Connection with server adress:
clientSocket.connect((serverName, serverPort))
filename = input('Search For filename:')
clientSocket.send(filename.encode())  # no address needed

file = open('c:/temp/output/' + filename, 'wb')  # wr wirte byte
file_data = clientSocket.recv(1024)
while (file_data):  # samme loop som server
    print("Receiving...")
    file.write(file_data)
    file_data = clientSocket.recv(1024)
file.close()

print("Done Sending")
clientSocket.close()

