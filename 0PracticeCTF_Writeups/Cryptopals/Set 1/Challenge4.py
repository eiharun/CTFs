#Refrence:https://www.youtube.com/watch?v=zTq4iwpAGM8
from Challenge3 import *
def openfile():
    with open('Set 1/Challenge4File.txt', 'r') as file:
        file_list = file.readlines()
        for n,i in enumerate(file_list):
            file_list[n]=i.strip()
    return file_list

def find_pt(pt_list):
    filtered=[]
    for i in pt_list:
        score = get_score(i)
        max_score = max(score)
        filtered.append((max_score, i))
    maxz=0
    pt=''
    for i in filtered:
        if maxz<i[0]:
            maxz = i[0]
            pt = i[1]
    return pt


def filtered(pt):
    filters=[]
    for i in pt:
        for k in ETAOIN.keys():
            if ord(k) not in i:
                break
            else:
                filters.append(i)
                break
    return filters

def main():
    encoded_list = openfile()
    filter=[]
    for encoded in encoded_list:    
        ct=bytes.fromhex(encoded)
        key = single_byte(ct)
        pt = xor(ct,key)
        filter.append(pt)
    print(find_pt(filtered(filter)))

if __name__=='__main__':
    main()
    
