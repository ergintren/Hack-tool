import scapy.all as sc
from scapy_http import http
import optparse as op

class NetScan():

    def user_input():
        parse = op.OptionParser()
        parse.add_option("-i","--iface",dest="iface")
        (user_inputs,arguments) = parse.parse_args()
        return user_inputs

    def listen_packet(self,interface):
        sc.sniff(iface=interface,store=False,prn=self.packet_analyz)

    def packet_analyz(self,packet):
        #packet.show()
        if packet.haslayer(http.HTTPRequest):
            if packet.haslayer(sc.Raw):
                print(packet[sc.Raw].load)

    def sniff(self,iface):
        self.listen_packet(iface)

