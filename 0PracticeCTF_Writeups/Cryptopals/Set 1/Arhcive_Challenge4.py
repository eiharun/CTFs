#Refrence:https://cypher.codes/writing/cryptopals-challenge-set-1
import Single_byte_XOR_cipher_decoder as XOR

with open('Set 1\Challenge4File.txt', 'r') as file:
    file_list = file.readlines()
    for n,i in enumerate(file_list):
        file_list[n]=i.strip()
    #print(file_list)
all = {}
for i in file_list:
    #print(i)
    all[i] = XOR.bruteforce_XOR(i) #function returns list, creates a dictionary with input as key, and outputs in list as value
#print(all)

for k in all:
    #print(k)
    print(k)
    for i in all[k]:
        if i.isprintable() == True:
            print('\t', i,'\n')
        

'''
    all[k]=XOR.ETAOIN(all[k])
    #print(list(all[k]),all[k])
    for i in list(all[k]):#I is the key of subdict/possible decrypted value
        for x in i:
            if x.isspace() == True:
                break
            else:
                #print(k, i, all[k])
                all[k].pop(i)#remove keys that don't have any spaces
                break'''
#print(all)
'''for k in all:
    print(k,':\n')
    XOR.printOutputs(all[k])
'''
