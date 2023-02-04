from Challenge6 import parse, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


key = b'YELLOW SUBMARINE'
def decrypt(ct ,ky):
    cipher = AES.new(ky, AES.MODE_ECB)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    print(pt.decode())

def main():
    ct = base64(parse('Set 1/Challenge7.txt'))
    decrypt(ct, key)


if __name__ == '__main__':
    main()