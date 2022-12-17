import sys

def helps():
    print('Enter values in hexadecimal, without the 0x')
    print('Format: python3 XOR_Program.py \'string\' \'XOR with\' ')
    print('Example: python3 XOR_Program.py \'1c0111001f010100061a024b53535009181c\' \'686974207468652062756c6c277320657965\'')
def xor(x,y):
    XOR_result=x^y
    return hex(XOR_result)

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    helps()
else:
    string = int(sys.argv[1],16)
    #print(string)
    XOR_value = int(sys.argv[2],16)
    print(xor(string, XOR_value)[2:])



