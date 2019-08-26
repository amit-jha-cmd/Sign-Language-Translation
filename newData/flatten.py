#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:13:46 2019

@author: amit
"""

import sys
import pandas as pd
import numpy as np
import random
temp = None
batch= sys.argv[1].split(":")
label_src = sys.argv[2]
src = sys.argv[3]
dest = sys.argv[4]

labels = pd.DataFrame(pd.read_csv(label_src))
sLabels = []
p = labels.iloc[eval(batch[0]) : eval(batch[1]), 0]
for i in range(len(p)):
    sLabels.append(p.values[i].split(";"))



cont = 0
lst = []
temp = None
for i in sLabels:
    cont += 1
    try:
        file = pd.read_csv(src + "/{}/video.csv".format(i[0]))
        arr = file.iloc[:, sorted(random.sample(range(len(file.columns)), 15))].values.flat[:].reshape(1, 1710)
        if(temp is None):
            temp = arr
        else:
            temp = np.concatenate((temp, arr), axis=0)
            lst.append(i)
            print("{}/{} | {}".format(cont, batch[1], (float)(cont/eval(batch[1]))*100))
    except:
        continue
    
pd.DataFrame(temp).to_csv("xtrain.csv")
pd.dataFrame(lst).to_csv("ytrain.csv")