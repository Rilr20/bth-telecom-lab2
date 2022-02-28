# Rikard Larsson Rilr20 BTH

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

#destinations porten
serverName = '192.168.1.31'
serverPort = 12000
#changes the speed of messages is sent
time_to_end = 10
waittime = 0.05

waittime = input("Put in your waittime default is 0.05 seconds: ")
if waittime == ""  or waittime.isalpha():
    print("using default")
    waittime = 0.05

time_to_end = input("how many seconds should program run: ")
if time_to_end == "" or time_to_end.isalpha():
    print("using default 10 seconds")
    time_to_end = 10

# waittime = 0.05
#converts to integer
# waittime = int(waittime)
#skapar ett meddelande som är 1400 byteslångt
packet_size = 1400
message = ""
for i in range(0, int(packet_size)):
    message += "a"
# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# Input sentence from keyboard
# sentence = input('Input lowercase sentence: ')

# ska köra i 10 sekunder sedan sluta
i = 0
# this_list = [1,2,3,4,5,6,7,8,9,10,11,13,12,14,15,16,17,18,17,19]
start_time = datetime.now()
# while i < len(this_list):
while True:
    i += 1
    # package = f'{this_list[i]};{message}####'
    package = f'{i};{message}####'
    clientSocket.send(package.encode())
    print(f'package {i}')
    time_delta = datetime.now() - start_time
    time.sleep(float(waittime))
    if time_delta.total_seconds() >= float(time_to_end):
        break

# close the TCP connection
clientSocket.close()
