#Refrence:https://www.youtube.com/watch?v=zTq4iwpAGM8
encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xor(*args, **kwargs):
    strg = [s for s in args]#List of strings in args, i.e. the value to be xor'ed
    length = kwargs.pop('length','max')#get the length value from kwargs, default should be max
    if isinstance(length,int):#if length is an integer  
        length=length
    elif length == 'max':
        length = max(len(s) for s in strg)
    elif length == 'min':
        length = min(len(s) for s in strg)
    else:
        raise ValueError("Length must be an int")
     
    def xor_indices(index):
        b=0
        for s in strg:
            b ^= s[index % len(s)]
        return b
    return bytes([xor_indices(i) for i in range(length)])

ETAOIN = {
        b'a':.0655, b'b':.0127, b'c':.0227, b'd':.0335, b'e':.1021,
        b'f':.0197, b'g':.0164, b'h':.0486, b'i':.0573, b'j':.0011,
        b'k':.0057, b'l':.0336, b'm':.0202, b'n':.0570, b'o':.0620,
        b'p':.1500, b'q':.0009, b'r':.0497, b's':.0533, b't':.0751,
        b'u':.0230, b'v':.0079, b'w':.0169, b'x':.0015, b'y':.0147,
        b'z':.0007, b' ':.1832
    }

def get_freq() -> list:
    
    freq_vector = [[0]*256 for _ in range(256)]#Size of 256 since there are 256 possible values in ascii
    for k,v in ETAOIN.items():
        for row in range(256):
            freq_vector[row][ord(k)^row] = v
    return freq_vector

def get_ct_freq(a:bytes) -> list:
    size = len(a)
    w = [0] * 256
    for b in a:
        w[b] += (1/size)
    return w

def dotproduct(a:list, b:list) -> int:
    return sum([i*j for i, j in zip(a,b)])

def get_score(ct:bytes) -> list:
    freq = get_freq()
    w = get_ct_freq(ct)
    return [dotproduct(w, v) for v in freq]#dot product: a value of 1 means they are identical

def single_byte(ct: bytes) -> bytes:#ct is in bytes, and function returns bytes
    scores = get_score(ct)
    key = scores.index(max(scores))#index where score is highest
    return bytes([key])

def main():
    ct=bytes.fromhex(encoded)
    key = single_byte(ct)
    pt = xor(ct,key)
    print(pt,key)
    
if __name__=='__main__':
    main()

