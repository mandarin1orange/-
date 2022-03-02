from scapy.all import *

def main():
    ans,vans = sr(IP(dst='192.168.3.40')/TCP(dport=80,flags='S'))
    for snd,rcv in ans:
        print(rcv.sprintf('%IP.src% 80 is up'))
    pass

if __name__ == '__main__':
    main()