# Rikard Larsson Rilr20 BTH

#20 paket per sekund 0.05ms delay
#under 20 sekunder
#50 paket per sekund 0.02ms delay

from socket import *
from datetime import datetime
import time

serverName = '192.168.1.112'
serverPort = 12000
#changes the speed of messages is sent
# waittime = input("Put in your waittime default is 0.5 seconds: ")
waittime = 0.05
# if waittime == "" or not waittime.isalpha():
#     print("using default")
#     waittime = 0.05
#converts to integer
# waittime = int(waittime)
#skapar ett meddelande som är 1400 byteslångt
packet_size = 1400
message = ""
for i in range(0, int(packet_size/2)):
    message += "ä"

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))

# ska köra i 10 sekunder sedan sluta
i = 0
time_count = 0
# this_list = [1,2,3,4,5,6,7,8,9,10,11,13,12,14,15,16,17,18,17,19]
start_time = datetime.now()
# while i < len(this_list):
while time_count <= 20:
    i += 1
    # package = f'{this_list[i]};{message}####'
    package = f'{i};{message}####'
    clientSocket.send(package.encode())
    print(f'package {i}')
    time_delta = datetime.now() - start_time
    time.sleep(waittime)
    time_count = time_count + waittime
    # print(time_count)
    # if time_delta.total_seconds() >= 22:
    #     break

# close the TCP connection
clientSocket.close()
