#import sys
import binascii

#For future refrence: consider the usage of spaces in ETAOIN function

def bruteforce_XOR(enc):
    '''XOR bruteforce function'''
    #print(binascii.unhexlify(enc))
    enc = binascii.unhexlify(enc)#conv from hex to bin
    dec = [[] for _ in range(256)]#init list for all possible combinations
    #print(dec)
    for i in range(256):#all possible combinations        
        for x in enc:#each value in enc
           dec[i].append(chr(x^i))#XOR
        dec[i] = ''.join(dec[i])#join list to make list of strings rather than list of lists
    return dec

def ETAOIN(input_list):
    '''function to score each brute force output for likelihood that it is readable using ETAOIN'''
    strings ={}
    points = {#SHRDLU
        'E':12,
        'T':11,
        'A':10,
        'O':9,
        'I':8,
        'N':7,
        'S':6,
        'H':5,
        'R':4,
        'D':3,
        'L':2,
        'U':1
    }
    
    for input in input_list:
        strings[input] = 0
        
        for x in points.items():
            
            if x[0] in input or x[0].lower() in input:
                strings[input] += x[1] 

    #del keys with value 0 to clean up output
    for value in list(strings.items()):
        if value[1] == 0:
            del strings[value[0]]

    #sort from highest to lowest score
    strings = dict(reversed(sorted(strings.items(), key=lambda x:x[1])))#note: reseach lambda function
    
    return strings

def printOutputs(inp):#input is a sorted dictionary
    '''Prints decrypted strings in a readable format'''
    inp = list(inp.items())
    
        #lst=[]
        #for i in range(6):
        #    lst.append(inp[i])
        
    print('Here is a list of the potential outputs:\n')
    for items in inp:
        print('-'*50)
        print('Score: ', items[1], '\n\t', items[0],)
    print('\n','*'*100,'\n')
    
#printOutputs(ETAOIN(bruteforce_XOR('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')))
    


