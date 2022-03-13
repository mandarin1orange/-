import base64

def main():

    s = 'haha123'
    bs = base64.b64encode(s.encode('utf-8'))
    print(bs.decode('utf-8'))

    s1 = 'aGFoYTEyMw=='
    bs1 = str(base64.b64decode(s1),'utf-8')
    print(bs1)

    pass

if __name__ == '__main__':
    main()