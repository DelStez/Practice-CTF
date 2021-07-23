#2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904 --flag CHTB{
from string import ascii_lowercase
from itertools import product

def func_xor(precombo):
    return bytes([a ^ b for a, b in zip(bytes(precombo, 'utf-8'), bytes.fromhex(t))])

#BruteForce
t = '2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'
for y in product(ascii_lowercase, repeat=5):
     precombo = ''.join(y)
     temp = func_xor(precombo)
     if(temp == b'CHTB{'):
        k = ''.join(y)
        print('Flag: ',func_xor(precombo*6).decode('utf-8'))
        exit()