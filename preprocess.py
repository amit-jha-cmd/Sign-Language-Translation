#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:23:27 2019

@author: amit
"""

import pandas as pd
import numpy as np

file = pd.read_csv("1.csv")
body = file.loc[:14, ["Bx", "By"]]
rhand = file.loc[:, ["Rx", "Ry"]]
lhand = file.loc[:, ["Lx", "Ly"]]
final = np.concatenate((body.values.flat[:]
                        , lhand.values.flat[:]
                        , rhand.values.flat[:])
                        , axis=0)
