#kolla paketnummret
#är det för högt? 10005 => 10007
#kommer de i rätt ordning? 10006 => 10005
#det ska loggas för att se om det är i ordning eller inte

from socket import *
serverPort = 12000

# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

# server starts listening for incoming TCP requests
serverSocket.listen(1)

print ('The TCP server is ready to receive')

while True:
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()

    # read sentence of bytes from socket sent by the client
    sentence = connectionSocket.recv(1024).decode()
    split_sentence = sentence.split(";")

    # print package number and sentence
    print (f'paketnummer {split_sentence[0]} {split_sentence[1][:-4]}')

    # convert sentence to upper case
    capitalizedSentence = sentence.upper()

    # send back modified sentence over the TCP connection
    connectionSocket.send(capitalizedSentence.encode())
 
    # close the TCP connection; the welcoming socket continues
    if int(split_sentence[0]) >= 100:
        connectionSocket.close()
