from hashlib import md5

def md5hs(str1):
    s = str1
    new_md5 = md5()
    new_md5.update(s.encode(encoding='utf-8'))
    return new_md5.hexdigest()

def main():
    a = md5hs('admin')
    print(a)
    pass

if __name__ == '__main__':
    main()