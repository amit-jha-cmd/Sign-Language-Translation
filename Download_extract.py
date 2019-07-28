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
import wget
import pandas as pd
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip #for cropping the video sequence
import sys

if(len(sys.argv) < 4):
    print("Pass following details as command line arguments >>")
    print("BatchNum : To download data in batches. 0 means all at once. options: 1 to 7")
    print("Dir1: folder for raw videos")
    print("Dir2: folder for processed videos")
    print("example: python download_prep.py BatchNum ./unprocessed/ ./processed/")
    exit(1)


url = 'http://csr.bu.edu/ftp/asl/asllvd/asl-data2/quicktime/{}/scene{}-camera1.mov'#url to download the unprocessed videos
unprocDir = sys.argv[2] #ADJUST THIS DIR ONLY
procDir = sys.argv[3] #ADJUST THIS DIR ONLY
unprocessedLoc = unprocDir +"{}.mp4" #where the unprocessed videos are saved
processedLoc = procDir + "{}/{}.mp4" #where the videos are saved after processing
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
greaterThan = sys.argv[1]
words = np.ndarray.tolist(final[final["Num. of videos"] >= int(greaterThan)]["Word"].values) #which ever word has 4 or more videos
wordList = words
    
clear = lambda: os.system('clear')
    


for i in wordList:
    i = str(i)
    pos = int(final[final["Word"] == i]["Position"].values[0]) #extract the position of the video in the dataframe
    count = int(final[final["Word"] == i]["Num. of videos"].values[0]) #number of videos for i world
    try:
        os.makedirs(unprocDir, exist_ok=True) #create the required dir
        os.makedirs(procDir + i.lower(), exist_ok=True)
    except OSError:
        print ("Failed to create directory: {}".format(i.lower()))
        exit()
    else:
        print ("Successfully created the directory: ".format(i.lower()))
    for j in range(count):
        start = dt.iat[pos+ 1 + j, 3] #starting frame where the word occures
        end = dt.iat[pos + 1 + j, 4] #ending frame where the word ends
        session = dt.at[pos + 1 + j, "Session"] #session id for the url
        scene = dt.at[pos + 1 + j, "Scene"] #scene id for the url
        print("Downloading: Word: "  + i + " | Word Number: " + str(wordList.index(i)+1) + " => " + str(j+1) + "/" + str(count))
        wget.download(url.format(session, scene), unprocessedLoc.format(j+1)) #download the video
        print(" Download complete...")
        print("extracting video sequences from video " + str(videoNum))
        videoNum += 1
        ffmpeg_extract_subclip(unprocessedLoc.format(j+1), (start/60),           #frame rate: 60
                               (end/60), targetname=processedLoc.format(i.lower(), j+1)) #convert the video
        os.remove(unprocessedLoc.format(j+1))
        clear()

print("Download sequence complete!")