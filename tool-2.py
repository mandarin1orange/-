import socket

def main():
    ip = socket.gethostbyname('www.baidu.com')
    print(ip)
    pass

if __name__ == '__main__':
    main()