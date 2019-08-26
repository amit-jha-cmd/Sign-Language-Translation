#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:23:27 2019

@author: amit
"""

import pandas as pd
import numpy as np
import random
temp = None


file1 = pd.read_csv("1.csv")  
file1 = file1.drop("Unnamed: 0", axis=1)

len(file1.columns)

p = pd.DataFrame(file1.iloc[:, sorted(random.sample(range(len(file1.columns)), 15))].values.flat[:]).T
np.concatenate((file1.iloc[:, sorted(random.sample(range(len(file1.columns)), 15))].values.flat[:],
                           file1.iloc[:, sorted(random.sample(range(len(file1.columns)), 15))].values.flat[:]))