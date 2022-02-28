from scapy.all import *

def main():
    ans,uans = sr(IP(dst='192.168.3.41')/ICMP())
    for snd,rcv in ans:
        print(rcv.sprintf('%IP.src% is alive now'))
    pass

if __name__ == '__main__':
    main()