from Cryptodome.Cipher import AES
import binascii

# AES加密

def main():
    key = b'abcdefghabcdefgh'
    text = 'haha123 nihao'
    text = text + (16 - (len(text) % 16)) * '='
    print(text)
    aes = AES.new(key, AES.MODE_ECB)
    encrypt_text = aes.encrypt(text.encode())
    encrypt_res = binascii.b2a_hex(encrypt_text)
    print(encrypt_res)

    pass

if __name__ == '__main__':
    main()