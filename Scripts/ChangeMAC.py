import subprocess as sb
import optparse
import re


def Parser():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="mac değiştirici")
    parse.add_option("-m","--mac",dest="mac")
    return parse.parse_args()
    
def Sbp(interface,mac):
    sb.call(["ifconfig",interface,"down"])
    sb.call(["ifconfig",interface,"hw","ether",mac])
    sb.call(["ifconfig",interface,"up"])

def control(interface):
    ifconfig = sb.check_output(["ifconfig",interface])
    new_mac = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)
    if new_mac:
        return new_mac.group(0)
    
(user_inputs,arguments) = Parser()
Sbp(user_inputs.interface,user_inputs.mac)
temp = control(user_inputs.interface)
if temp == user_inputs.mac:
    print("mac adresi değişti")
else:
    print("mac adresi değştirlemdi")
    
