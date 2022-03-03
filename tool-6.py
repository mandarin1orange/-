from scapy.all import *


def main():
    ip = '192.168.3.40'

    ans, vans = sr(IP(dst=ip) / UDP(dport=80))
    for snd, rcv in ans:
        print(rcv.sprintf('%IP.src% is up'))

    pass


if __name__ == '__main__':
    main()