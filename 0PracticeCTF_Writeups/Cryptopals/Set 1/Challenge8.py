
def parse(filename) -> list:
    with open(filename, 'r') as file:
        ct = file.read().split('\n')
    return ct

def dupl(cts, length, blocksize):
    blocks = [[ct[i:i+blocksize*2] for i in range(0,length,blocksize*2)] for ct in cts]#blocksize*2 since block size in in bytes, but the ciphertext is in hex which takes up 2 per byte, essentially when in hex, the string is doubled in lengh
    for i in blocks:
        if len(i)!=len(set(i)):
            return ''.join(blocks[blocks.index(i)])
    


def getinfo(ct):
    length = len(ct)
    block_size=16
    block_num = (length//2)//block_size#(length//2) since it takes 2 hex chars to make a byte
    return length,block_size,block_num

def main():
    cts = parse('Set 1/Challenge8.txt')
    length,block_size,block_num = getinfo(cts[0])
    print(f'The AES Encryption in ECB mode is:\n {dupl(cts, length, block_size)}')
    
    
    
if __name__ == '__main__':
    main()