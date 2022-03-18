from pexpect import pxssh

def Login(server,username,password):
    try:
        s = pxssh.pxssh()
        s.login(server,username,password)
        print('yes')
    except:
        print('no')

def main():
    Login('','kali','kali')  # 目标IP
    pass

if __name__ == '__main__':
    main()