
def xor(x,y):
    XOR_result=int(x,16)^int(y,16)
    return hex(XOR_result)[2:]

def main():
    string = '1c0111001f010100061a024b53535009181c'
    XOR_value = '686974207468652062756c6c277320657965'
    print(xor(string, XOR_value))

if __name__ == '__main__':
    main()