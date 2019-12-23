from __future__ import print_function
import sys, os
import pickle, gzip
import numpy as np
import imageio
from PIL import Image
import matplotlib.pyplot as plt 
from utils import *

N_DATA = int(sys.argv[1])
N_TRAIN = int(N_DATA * 0.9)

dataX = []
dataY = []

for i in range(N_DATA):
    path = "captchagen/captchas/%d.jpg"%(i) 
    img = imageio.imread(path).astype(np.float)
    grayim = np.dot(img[...,:3],[0.299,0.587,0.114])
    dataX.append(grayim) 

passfile = open('captchagen/captchas/pass.txt')
labelY = passfile.read().split(' ')[:N_DATA]

for y in labelY:
    dataY.append(str2onehot(y))

trX = dataX[:N_TRAIN]
teX = dataX[N_TRAIN:]
trY = dataY[:N_TRAIN]
teY = dataY[N_TRAIN:]

pickle.dump((trX, teX, trY, teY), gzip.open("data.pkl.gz", "wb"))
