# Rikard Larsson Rilr20 BTH
# Sändare

#50ms asvstånd
#kunna skjustera tiden mellan utskicken
#skicka paket i 10sekunder
#mindre än 1500bytes stora
#inkludera ett meddelande nummer
#10001;
#10002;
#avsluta med fyra ####

from socket import *
from datetime import datetime
import time

serverName = '192.168.1.112'
serverPort = 12000
waittime = 0.05

#skapar paketet
packet_size = 1400
message = ""
for i in range(0, int(packet_size/2)):
    message += "ä"


# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get input from keyboard
# message = input('Input lowercase sentence:')

# send sentence to socket; server and port number required

i = 0
start_time = datetime.now()
while True:
    i += 1
    # package = f'{this_list[i]};{message}####'
    package = f'{i};{message}####'
    # clientSocket.send(package.encode())
    clientSocket.sendto(package.encode(),(serverName, serverPort))
    print(f'package {i}')
    time_delta = datetime.now() - start_time
    time.sleep(waittime)
    if time_delta.total_seconds() >= 10:
        break

# need to convert message from string to bytes for Python 3

# receive the modified sentence in upper case letters from server
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# output modified sentence and close the socket, cast message to string
# print ("Received from server: ", modifiedMessage.decode())

# close UDP socket
clientSocket.close()
