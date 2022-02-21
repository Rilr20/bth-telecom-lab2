# TCP Client
# Anders Nelsson BTH
# Example code from course book

from socket import *
from datetime import datetime
import time
# serverName = 'hostname'
serverName = '192.168.1.112'
serverPort = 12000

#skapar ett meddelande som är 1400 byteslångt
packet_size = 1400
message = ""
for i in range(0, int(packet_size/2)):
    message += "ä"

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# Input sentence from keyboard
# sentence = input('Input lowercase sentence: ')

# ska köra i 10 sekunder sedan sluta
i = 0
start_time = datetime.now()
while True:
    i += 1
    package = f'{i};{message}####'
    clientSocket.send(package.encode())
    print(f'package {i}')
    time_delta = datetime.now() - start_time
    time.sleep(0.05)
    if time_delta.total_seconds() >= 10:
        break

# send text over the TCP connection
# there's no need to specify server name & port
# sentence converted to bytes

# get modified sentence back from server
# modifiedSentence = clientSocket.recv(1024)
# print ('From Server:', modifiedSentence.decode())

# close the TCP connection
clientSocket.close()


#50ms asvstånd
#kunna skjustera tiden mellan utskicken
#skicka paket i 10sekunder
#mindre än 1500bytes stora
#inkludera ett meddelande nummer
#10001;
#10002;
#avsluta med fyra ####
