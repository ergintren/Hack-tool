import subprocess as sb
import re

def Sbp(interface,mac):
    sb.call(["ifconfig",interface,"down"])
    sb.call(["ifconfig",interface,"hw","ether",mac])
    sb.call(["ifconfig",interface,"up"])

def control(interface):
    ifconfig = sb.check_output(["ifconfig",interface])
    new_mac = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if new_mac:
        return new_mac.group(0)

def change_mac(interface,mac):
    Sbp(interface,mac)
    temp = control(interface)
    if temp == mac:
        print("mac adresi değişti")
    else:
        print("mac adresi değştirlemdi")