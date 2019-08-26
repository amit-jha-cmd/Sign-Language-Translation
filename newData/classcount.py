#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 21:14:16 2019

@author: amit
"""

import pandas as pd
import numpy as np
import sys


label = pd.read_csv("~/Downloads/junk/jester-v1-labels.csv")
train = pd.read_csv("~/Downloads/junk/jester-v1-train.csv")

batch= sys.argv[1].split(":")
train_src = sys.argv[2]
label_src = sys.argv[3]


#train = pd.DataFrame(pd.read_csv(train_src))
#label = pd.DataFrame(pd.read_csv(label_src))
strain = []
#print(train)
#exit(1)
#print(train)
p = train.iloc[eval(batch[0]) : eval(batch[1]), 0]
for i in range(len(p)):
    strain.append(p.values[i].split(";")[1])

#print(strain)
dic = {}
lst = []
for i in list(label.values):
    dic[i[0]] = 0
    lst.append(i[0])

#print(lst) 
for i in strain:
    for j in lst:
        if(i == j):
            dic[i] += 1
        
for key, val in dic.items():
    print("{} : {}".format(key, val))