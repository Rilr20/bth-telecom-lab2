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
time_to_end = 10

waittime = input("Put in your waittime default is 0.05 seconds: ")
if waittime == ""  or waittime.isalpha():
    print("using default")
    waittime = 0.05
time_to_end = input("how many seconds should program run: ")

if time_to_end == "" or time_to_end.isalpha():
    print("using default 10 seconds")
    time_to_end = 10
#skapar paketet
packet_size = 1400
message = ""
# waittime = float(waittime) - 0.003
for i in range(0, int(packet_size/2)):
    message += "ä"


# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

i = 10000
start_time = datetime.now()
time_to_end = int(time_to_end)
waittime = float(waittime)
time_delta = datetime.now() - start_time
print(time_delta.total_seconds() >= time_to_end)
while time_delta.total_seconds() <= time_to_end:
    i += 1
    # package = f'{this_list[i]};{message}####'
    package = f'{i};{message}####'
    # clientSocket.send(package.encode())
    clientSocket.sendto(package.encode(),(serverName, serverPort))
    time_delta = datetime.now() - start_time
    time.sleep(waittime)
    # if time_delta.total_seconds() >= time_to_end:
    #     break
print(f'package {i}')

clientSocket.close()
