#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 14:13:46 2019

@author: amit
"""

import os
import sys
import pandas as pd
import numpy as np
import cv2
import time
import argparse
sys.path.insert(0, "/usr/local/python/openpose")
import pyopenpose as op
temp = None
batch= sys.argv[1].split(":")
label_src = sys.argv[2]
src = sys.argv[3]
dest = sys.argv[4]

labels = pd.DataFrame(pd.read_csv(label_src))
sLabels = []
#print(labels)
#exit(1)
#print(labels)
p = labels.iloc[eval(batch[0]) : eval(batch[1]), 0]
for i in range(len(p)):
    sLabels.append(p.values[i].split(";"))

# Flags
parser = argparse.ArgumentParser()
#parser.add_argument("--image_dir", default="./openpose/examples/media", help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
parser.add_argument("--hand", default=True)
args = parser.parse_known_args()


# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "./openpose/models"
params["hand"] = True
params["hand_detector"] = 0

try:
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

except Exception as e:
     print(e)
     sys.exit(-1)



def FrameCapture(src, temp): 
    img = cv2.imread(src)    
    datum = op.Datum()
    imageToProcess = img
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop([datum]) 
    poseVal = datum.poseKeypoints 
    try:
        x = poseVal[0]
        impKeypnts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18]
        y = x[impKeypnts]
        rightVal = datum.handKeypoints[1]
        leftVal = datum.handKeypoints[0]
        body = pd.DataFrame(y, columns=["Bx", "By", "Bconfidence"])
        right = pd.DataFrame(rightVal[0], columns=["Rx", "Ry", "Rconfidence"])
        left = pd.DataFrame(leftVal[0], columns=["Lx", "Ly", "Lconfidence"])
        keypoints = pd.concat([body, right, left], axis=1, sort=False)
        body = keypoints.loc[:14, ["Bx", "By"]]
        rhand = keypoints.loc[:, ["Rx", "Ry"]]
        lhand = keypoints.loc[:, ["Lx", "Ly"]]
        final = np.concatenate((body.values.flat[:]
                                , lhand.values.flat[:]
                                , rhand.values.flat[:])
                                , axis=0)
    except IndexError as e:
        final = np.zeros((114, 1))
#            print(final)
    final = final.reshape((114, 1))
    return final
#    if temp is None:
#        temp = final
#    else:
#        temp = np.concatenate([temp, final], axis=1)
#    count += 1

cont = 0

for i in sLabels:
    imgSeq = os.listdir(src + "/" + i[0])
    cont += 1
    print("Extracting keypoints {}/{} | {}".format(cont, len(sLabels), (float)(cont/len(sLabels))))
    start = time.time()
    for j in imgSeq:
        ltemp = FrameCapture(src + "/" + i[0] + "/" + j, temp)
        if temp is None:
            temp = ltemp
        else:
            temp = np.concatenate([temp, ltemp], axis=1)
    try:
        os.makedirs(dest + "/" + i[0])
        pd.DataFrame(temp).to_csv(dest + "/" + i[0] + "/video.csv")
        temp = None        
    except:
        print("error saving sequence for: {} >> skipping".formate(i[1]))
        continue
    end = time.time()
    dur = (end - start)
    print("time remaining: {} mins".format((dur * (len(sLabels) - cont))/60))