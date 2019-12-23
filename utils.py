import numpy as np

ALPHABET = 'qwertyuiopasdfghjklzxcvbnm1234567890'
N_ALPHABET = len(ALPHABET)
list_char = [c for c in ALPHABET]
dict_char = {list_char[i]:i for i in range(N_ALPHABET)}

def onehot(num):
    r = [0 for i in range(N_ALPHABET)]
    r[num] = 1
    return r 

def str2onehot(string):
    arr = []
    for c in string:
        arr.append(dict_char[c])
    res = []
    for e in arr:
        res.extend(onehot(e))
    return res 

