from Cryptodome.Cipher import DES
import binascii

# DES加密

def main():

    key = b'abcdefgh'
    des = DES.new(key, DES.MODE_ECB)
    text = 'haha123 nihao'
    text = text + (8 - (len(text) % 8)) * '='
    print(text)
    encrypt_text = des.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)

    pass


if __name__ == '__main__':
    main()