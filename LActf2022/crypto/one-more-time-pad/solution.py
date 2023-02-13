'''Original Challenge Code for Reference
from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

key = cycle(b"lactf{??????????????}")

ct = ""

for i in range(len(pt)):
    b = (pt[i] ^ next(key))
    ct += f'{b:02x}'
print("ct =", ct)

#ct = 200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e
'''

ct = bytes.fromhex("200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e")
# bytes.fromhex() converts a hex string into a byte string
def find_unknown(ct):
    key=''
    crib=b'Long ago, the four nations lived together in harmony ...'
    '''
        The repeating key was used to encrypt the plaintext (crib), and the output was ct = 200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e
        I repurposed ct and xor'ed it with the crib (or known plaintext) to find the key
        
    Theory:
            "plaintext" ^ "key" = "ciphertext"
            "apple" ^ "AAAAA" = " 11-$"
        XOR is commutative, so the key can be found by xor'ing the known plaintext with the ciphertext
            " 11-$" ^ "apple" = "AAAAA"
        Likewise
            " 11-$" ^ "AAAAA" = "apple"
    '''
    for i in range(len(ct)):
        key += chr(crib[i] ^ ct[i]) #xor each value with eachother and append its output to the key
                                    #in this case crib and pt are the same length, so there is no need to pad anything
    return key

print(find_unknown(ct))
#The output is the padded key, i.e. it is repeated until it matched the length of the plaintext(or text to be encrypted). In XOR the key is generally shorter that the plaintext, so it is usually padded
# output:
#   lactf{b4by_h1t_m3_0ne_m0r3_t1m3}lactf{b4by_h1t_m3_0ne_m0

