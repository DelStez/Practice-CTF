#2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904 --flag CHTB{
from string import ascii_lowercase
from itertools import product

def func_xor(precombo):
    return bytes([a ^ b for a, b in zip(bytes(precombo, 'utf-8'), bytes.fromhex(t))])

def xorf(t, k):
    encoded = []
    for i in range(0, len(t)):
        encoded.append(t[i] ^ k[i*len(k)])

#BruteForce
f = open('Input.txt', 'r')
while (True):
    t = f.readline()
    t_c = (t[0:2], 16)
    t_h = (t[2:4], 16)
    t_t = (t[4:6], 16)
    t_c = (t[6:8], 16)

    for y in product(ascii_lowercase):
        if():
            print("Yes")
        #precombo = ''.join(y)
        #temp = func_xor(precombo, t)
        #if(temp == b'CHTB'):
         #   k = ''.join(y)
          #  try:
           #     g = func_xor(precombo*2, t).decode('utf-8')
            #    #if(g == b'CHTB'):
             #   print('Flag: ', g)
              #  #print('Key: ', k)
            #except: pass
    if(not t):
        exit()
