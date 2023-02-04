from base64 import b64decode
from Challenge3 import *

def parse(f) -> str:
    with open(f, 'r') as file:
        string=''.join(file.read().split('\n'))
    return string

def base64(enc) -> bytes:
    return b64decode(enc)

def binary(text):
    return ''.join(format(i, '08b') for i in text)

def hamming(a='',b='')-> int:
    if a == '' and b == '':
        test=[b'this is a test', b'wokka wokka!!!']
        a,b = test[0],test[1]
    if len(a)!=len(b):
        raise ValueError("Strings must be equal in length")
    #print(f"{a}\n\n{b}")
    a,b=str(binary(a)),str(binary(b))
    length=len(a)
    count=0
    for i in range(length):    
        if a[i]!=b[i]:
            count+=1
    return count
    
def get_key_size(ct):
    #print(len(ct[-30:]+ct[:-30]),len(ct))
    dist = [(hamming(ct[-i:]+ct[:-i],ct)) for i in range(2,41)]
    key_size = dist.index(min(dist))
    return key_size+2 #+2 since the index is being pushed up by two in the range function in the list comprehension

def get_key(ct,size):
    key=b''
    for i in range(size):
        block=ct[i:-1:size]
        key += single_byte(block)
    return key

def main():
    ct = base64(parse('Set 1/Challenge6.txt'))
    keysize = get_key_size(ct)
    print(f'Key: {get_key(ct,keysize).decode()}')
    key = get_key(ct,keysize)
    pt = xor(ct,key)
    print(pt.decode())

if __name__=="__main__":
    main()