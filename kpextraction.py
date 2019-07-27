"""
Developer: Amit Jha
Date: July 21st, 2019
Purpose: To automatically download and process the videos for a paper

DEPENDENCIES:
    1. pandas
    2. moviepy
    3. wget
    4. os
    5. numpy
"""
import os
import pandas as pd
import numpy as np
import sys
import cv2
from sys import platform
import argparse

sys.path.insert(0, "/usr/local/python/openpose")
import pyopenpose as op
# Flags
parser = argparse.ArgumentParser()
#parser.add_argument("--image_dir", default="./openpose/examples/media", help="Process a directory of images. Read all standard formats (jpg, png, bmp, etc.).")
parser.add_argument("--no_display", default=False, help="Enable to disable the visual display.")
parser.add_argument("--hand", default=True)
args = parser.parse_known_args()

if(len(sys.argv) < 4):
    print("Pass following details as command line arguments >>")
    print("BatchNum : To download data in batches. 0 means all at once. options: 1 to 7")
    print("Dir1: folder for raw videos")
    print("Dir2: folder for processed videos")
    print("example: python download_prep.py BatchNum ./unprocessed/ ./processed/")
    exit(1)


# Custom Params (refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "./openpose/models"
params["hand"] = True
params["hand_detector"] = 0


unprocDir = sys.argv[2] #ADJUST THIS DIR ONLY
procDir = sys.argv[3] #ADJUST THIS DIR ONLY
batch = sys.argv[1]
unprocessedLoc = unprocDir +"/{}/{}.mp4" #where the unprocessed videos are saved
processedLoc = procDir+ "/{}/{}/" #where the videos are saved after processing
words = []   #words that the model will be able to understand. There are over 500 words. we chose only these for simplicity

file =pd.ExcelFile('./dataDetail.xlsx') #excel file that contains the frame data and links for the videos
frame = file.parse('Sheet1')
dt = frame.loc[:, ['Main New Gloss', 'Session', 'Scene', 'Start', 'End']] #convert the file into a dataframe
#prepossing
dt = dt[dt["Main New Gloss"] != " "] 
dt = dt.set_index('Main New Gloss')
ind = dt.index
ind = pd.DataFrame(ind)
ind2 = ind.dropna()
ind2 = ind2[ind2["Main New Gloss"] != " "]
ind2 = ind2.drop(0, axis=0)

#counting the number of videos for each word
forDif = ind2["Main New Gloss"].index
forDif = pd.DataFrame(forDif[1:] - forDif[:-1])
ind2 = ind2.reset_index()
final = pd.concat([ind2, forDif], axis=1)
final.columns = ["Position", "Word", "Num. of videos"]
final["Num. of videos"] = final["Num. of videos"] - 1
dt = dt.reset_index()

videoNum = 1
words = np.ndarray.tolist(final[final["Num. of videos"] >= 4]["Word"].values) #which ever word has 4 or more videos
wordList = words
totalV = 200
#download and processing
if(batch == "1"):
    wordList = words[:200]
elif(batch == "2"):
    wordList = words[200:400]
elif(batch == "3"):
    wordList = words[400:600]
elif(batch == "4"):
    wordList = words[600:800]
elif(batch == "5"):
    wordList = words[800:1000]
elif(batch == "6"):
    wordList = words[1000:]
elif(batch == '0'):
    totalV = int(final[final["Num. of videos"] >= 4]["Num. of videos"].sum())
    wordList = words
else:
    print("Specify batch number")
    exit(1)
    
clear = lambda: os.system('clear')
  

try:
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

except Exception as e:
     print(e)
     sys.exit(-1)
    

def FrameCapture(src, dest): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(src) 
  
    
    count = 1
    # checks whether frames were extracted 
    success = 1
  
    while success: 
  
        
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        if(success):
            datum = op.Datum()
            imageToProcess = image
            datum.cvInputData = imageToProcess
            opWrapper.emplaceAndPop([datum])
        # Saves the frames with frame-count 
#        cv2.imwrite(dest + "temp%d.jpg" % count, image) 
            poseVal = datum.poseKeypoints
            
            x = poseVal[0]
            impKeypnts = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18]
            y = x[impKeypnts]
            rightVal = datum.handKeypoints[1]
            leftVal = datum.handKeypoints[0]
            body = pd.DataFrame(y, columns=["Bx", "By", "Bconfidence"])
            right = pd.DataFrame(rightVal[0], columns=["Rx", "Ry", "Rconfidence"])
            left = pd.DataFrame(leftVal[0], columns=["Lx", "Ly", "Lconfidence"])
            keypoints = pd.concat([body, right, left], axis=1, sort=True)
            keypoints.to_csv(dest + "/{}.csv".format(count))
            count += 1

for i in wordList:
    pos = int(final[final["Word"] == i]["Position"].values[0]) #extract the position of the video in the dataframe
    count = int(final[final["Word"] == i]["Num. of videos"].values[0]) #number of videos for i world
    try:
        os.makedirs(procDir + "/" +i.lower(), exist_ok=True)
    except OSError:
        print ("Failed to create directory: {}".format(i.lower()))
        exit()
    for j in range(count):
        
        try:
            os.makedirs(procDir + "/" +i.lower() + "/" + str(j+1), exist_ok=True)
        except OSError:
            print ("Failed to create directory: {}".format(i.lower()))
            exit()
        else:
            print ("Extracting Keypoints of Video {}/{} Detail: {}:{}/{}".format(videoNum, totalV, i.lower(), j + 1, count))
        FrameCapture(unprocessedLoc.format(i.lower(), j+1), processedLoc.format(i.lower(), j+1))
    videoNum += 1
#print("Download sequence complete!")