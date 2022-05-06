import nmap3
import nmap
import sys
import os
import subprocess
from NopeBanner import *
import random
from colorama import init
from colorama import Fore
import center
import argparse
from datetime import datetime
import time
from tqdm import tqdm



header = '''




▌─────▐█▓░░░░░░█▓░░▓█░░░░▓█▌─────▐
▌─────▓█▌░▓█▓▓██▓░█▓▓▓▓▓░▓█▌─────▐
▌─────▓▓░▓██████▓░▓███▓▓▌░█▓─────▐
▌────▐▓▓░█▄▐▓▌█▓░░▓█▐▓▌▄▓░██─────▐
▌────▓█▓░▓█▄▄▄█▓░░▓█▄▄▄█▓░██▌────▐
▌────▓█▌░▓█████▓░░░▓███▓▀░▓█▓────▐
██████████████████████████████████
█░▀░░░░▀█▀░░░░░░▀█░░░░░░▀█▀░░░░░▀█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░██░░░█░░░██░░█
█░░▐█▌░░█░░░██░░░█░░░░░░▄█░░▄▄▄▄▄█
█░░▐█▌░░█░░░██░░░█░░░░████░░░░░░░█
█░░░█░░░█▄░░░░░░▄█░░░░████▄░░░░░▄█
██████████████████████████████████

[ * ] Title : NopePy Network Enumeartion [ * ]
[ * ] Code Written By : KrdSploit        [ * ]
[ * ] Version : 0.0.1                    [ * ]
[ * ] Support : Windows - Mac - Linux    [ * ]
[ * ] Language : Bash - Python - HTML    [ * ]
[ * ] Modules : Nmap3 - Nmap - Requests  [ * ]

																		'''

print(header)


init()

txt = (Fore.RED + "Enter The --help command to get the guide ")
x = txt.center(30)
print(x)


command_input = input("Enter your command : ")


prog_list = [1,2,3,4]

for i in tqdm(prog_list):
	time.sleep(1)

if command_input == "--help":
	usg = """



[*] Host Scanning          [*]
[*] OS Scanning            [*]
[*] Port Scanning          [*]
[*] Up Server Scanning     [*]
[*] DNS Brute Script       [*]
[*] TCP Scanning           [*]
[*] UDP Scanning           [*]
[*] SYN Scanning           [*]
[*] Ping Server Scanning   [*]
[*] Subnet Scanning        [*]
[*] Version Detection      [*]
[*] Top Port Scanning      [*]
[*] List Scanning          [*]
[*] Scanning Technique     [*]
[*] Version Scanning Nmap  [*]


								"""

print(usg)



def main():

	print(Fore.RED + "[*] Wait till 3 second [*]")
	time.sleep(3)

	init()

	print(Fore.BLUE + "[*] Host Scanning :   [*]")
	print(Fore.RED + "[*] OS Scanning :      [*]")
	print(Fore.YELLOW + "[*] Port Scanning : [*]")
	print(Fore.GREEN + "[*] Up Server Scanning : [*]")
	print(Fore.BLACK + "[*] DNS Brute Script : [*]")
	print(Fore.BLUE + "[*] TCP Scanning : [*]")
	print(Fore.RED + "[*] UDP Scanning: [*]")
	print(Fore.YELLOW + "[*] SYN Scanning : [*]")
	print(Fore.GREEN + "[*] Ping Server Scanning : [*]")
	print(Fore.BLACK + "[*] Subnet Scanning : [*]")
	print(Fore.BLACK + "[*] Version Detection : [*]")
	print(Fore.BLUE + "[*] Top Port Scanning : [*]")
	print(Fore.RED + "[*] List Scanning : [*]")
	print(Fore.YELLOW + "[*] Scanning Technique : [*]")
	print(Fore.BLACK + "[*] Version Scanning Nmap : [*]")



	cmd_input = int(input(Fore.GREEN + "Enter Your Fav Choice To Pwn : "))

	if cmd_input==1:
		hst()
	elif cmd_input==2:
		os()
	elif cmd_input==3:
		prt()
	elif cmd_input==4:
		up()
	elif cmd_input==5:
		dns()
	elif cmd_input==6:
		tcp()
	elif cmd_input==7:
		udp()
	elif cmd_input==8:
		syn()
	elif cmd_input==9:
		ping()
	elif cmd_input==10:
		subnet()
	elif cmd_input==11:
		version()
	elif cmd_input==12:
		top()
	elif cmd_input==13:
		listsc()
	elif cmd_input==14:
		technique()
	elif cmd_input==15:
		nmvers()
	else:
		print(Fore.GREEN + "Sorry After 3 Second This Script Will Shuting Down !")



def hst():

	nm = nmap.PortScanner()

	host_trg = input("Host===> : ")

	scan_range = nm.scan(hosts=host_trg)
	print(scan_range['scan'])

	return()

	scan_range = nm.scan(hosts=host_trg)
	print(scan_range['scan'])
	nm.all_hosts()
	for host in nm.all_hosts():
		print("Host: %s (%s" % (host, nm[host].hostname()))
		print("Open TCP Ports : ")
		print("%s" % (nm[host].all_tcp()))
		return()




def os():
	host_trget = input("===> Target : ")
	nmap = nmap3.Nmap()
	os_result = nmap.nmap_os_detection(host_trget)
	print(os_result)
	


def prt():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.scan_top_ports(target)
	print(res)


def up():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_ping_scan(target)
	print(res)

def dns():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_dns_brute_script(target)
	print(res)

def tcp():

	target = input("===> Target : ")
	nmap = nmap3.Nmap()

	res = nmap.nmap_top_scan(target)

	print(res)


def udp():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_udp_scan(target)
	print(res)

def subnet():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_subnet_scan(target)
	print(res)


def syn():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_syn_scan(target)
	print(res)


def ping():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_ping_scan(target)
	print(res)


def version():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_version_detection(target)
	print(res)


def listsc():

	target = input("===> Target : ")
	nmap = nmap3.Nmap()


def nmvers():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.nmap_version()
	print(res)


def top():
	target = input("===> Target : ")
	nmap = nmap3.Nmap()
	res = nmap.scan_top_ports(target)
	
	for results in res:
		print("\n Host : ", [res])
		print(results)






if __name__ == '__main__':
	main()
