from Challenge3 import xor
import binascii

pt=b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
key = b'ICE'

def main():
    print(binascii.hexlify(xor(pt,key)).decode())

if __name__ == '__main__':
    main()



