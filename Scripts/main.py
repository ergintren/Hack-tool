from mitm import arp_posion,netscanner,packet_sniffing
from Change_mac import mac
import os
import subprocess as sb
from Listener import listener


a = """
    Welcome to hacktool

1-)Phishing
2-)Arp_posion
3-)Netscanner
4-)sniff
5-)Keyloger
6-)Backdoor
7-)Hack connection console
8-)Ransomware
9-)Changemac
example: use 1

"""
print(a)
user_input = input("input:")


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


if user_input == 'use 9':
    sb.call(["echo","1",">","/proc/sys/net/ipv4/ip_forward"])
    change_mac()
elif user_input == 'use 3':
    netscan()
elif user_input == 'use 2':
    arp_spoof()
elif user_input == 'use 4':
    sniff()
elif user_input == 'use 7':
    Listen()
