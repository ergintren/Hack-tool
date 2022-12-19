import scapy.all as scapy
from scapy_http import http
import optparse


def Scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    brodcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = brodcast/arp_request
    (answered,unanswered) = scapy.srp(combined,timeout=1)
    answered.summary()
