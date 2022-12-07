import random
lst=[]
with open('out.txt', 'r') as f:
    flag = f.read() #reads the out.txt

flag = int(flag, 16)#converts from hex to decimal
seed = random.randint(0,999)
random.seed(seed)

#flag=str(flag)
#length = len(flag)
#print(length)#the exponent couldn't have been more than 84

for i in range(0,999):
    random.seed(i)
    for x in range(1):
        flag = int(flag ** (1/random.randint(84,255)))
        print(chr(flag))
#decrypted = ''.join(f'{(chr(int(c)) ^ 1/(random.randint(0,255)))}' for c in flag)

#print(lst)