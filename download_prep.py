"""
Developer: Amit Jha
Date: July 21st, 2019
Purpose: To automatically download and process the videos for a paper
"""

import os
import wget
import pandas as pd
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip #for cropping the video sequence
url = 'http://csr.bu.edu/ftp/asl/asllvd/asl-data2/quicktime/{}/scene{}-camera1.mov'#url to download the unprocessed videos
unprocessedLoc = "/home/amit/Documents/paper/asl/dataset/unprocessed/{}/{}.mp4" #where the unprocessed videos are saved
processedLoc = "/home/amit/Documents/paper/asl/dataset/processed/{}/{}.mp4" #where the videos are saved after processing
numofVideos = 161 #calculated using other script. May change if words list is altered.
words = [   #words that the model will be able to understand. There are over 500 words. we chose only these for simplicity
    'EXAGGERATE',
    'CONTINUE',
    'CARE',
    'GUITAR',
    'CABBAGE',
    'FINALLY',
    'PING-PONG/TENNIS',
    'TEMPERATURE',
    'WHISTLE',
    'GRAB',
    'STORY',
    'STAND-UP',
    'SLEEP',
    'SHAME',
    'SECRET',
    'SAME',
    'RUN',
    'FLOWER',
    'ENGAGEMENT',
    'RESPONSIBILITY'
]

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

#download and processing
for i in words:
    pos = int(final[final["Word"] == i]["Position"].values) #extract the position of the video in the dataframe
    count = int(final[final["Word"] == i]["Num. of videos"].values) #number of videos for i world
    try:
        os.makedirs("/home/amit/Documents/paper/asl/dataset/unprocessed/" + i.lower()) #create the required dir
        os.makedirs("/home/amit/Documents/paper/asl/dataset/processed/" + i.lower())
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
        print("Downloading: Video " + str(videoNum) + "abount" + i)
        wget.download(url.format(session, scene), unprocessedLoc.format(i.lower(), j+1)) #download the video
        wget.bar_adaptive(videoNum, numofVideos)
        print("Download complete...")
        print("extracting video sequences from video " + str(videoNum))
        videoNum += 1
        ffmpeg_extract_subclip(unprocessedLoc.format(i.lower(), j+1), (start/60),
                               (end/60), targetname=processedLoc.format(i.lower(), j+1)) #convert the video
        
        
print("Download sequence complete!")