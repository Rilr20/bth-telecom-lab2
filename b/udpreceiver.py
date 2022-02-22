# Rikard Larsson Rilr20 BTH
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

connectionSocket, addr = serverSocket.accept()
prev_package = 0

while True:
    # server waits for incoming requests; new socket created on return
    # read sentence of bytes from socket sent by the client
    sentence = connectionSocket.recv(2048).decode()
    split_sentence = sentence.split(";")
    # print package number and sentence
    if not sentence:
        print("now i close")
        connectionSocket.close()
        break
    # print (f'paketnummer {split_sentence[0]} {split_sentence[1][:-4]}')
    if prev_package+1 == int(split_sentence[0]):
        print(f'correct package arrived: {split_sentence[0]}')
    elif prev_package < int(split_sentence[0]):
        print(f'wrong package arrived too large expected {prev_package+1} got {split_sentence[0]}')
    elif prev_package > int(split_sentence[0]):
        # print(split_sentence[0])
        # print(prev_package)
        print(f'wrong package arrived too small expected {prev_package+1} got {split_sentence[0]}')

    prev_package += 1