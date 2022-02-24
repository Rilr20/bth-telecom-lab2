# Rikard Larsson Rilr20 BTH
# Mottagare

#kolla paketnummret
#är det för högt? 10005 => 10007
#kommer de i rätt ordning? 10006 => 10005
#det ska loggas för att se om det är i ordning eller inte

from socket import *
serverPort = 12000

# create UDP socket and bind to specified port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")
prev_package = 10000
while True:
    # read client's message and remember client's address (IP and port)
    sentence, clientAddress = serverSocket.recvfrom(2048)
    decoded = sentence.decode()
    split_sentence = decoded.split(";")
    # Print message and client address
    # print (sentence.decode())
    # print (clientAddress)

    # if not sentence:
    #     print("now i close")
    #     connectionSocket.close()
    #     break
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
