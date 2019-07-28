# Download and extract video sequences 

This script makes use of wget library together with some inbuilt libraries to automatically download video sequences and extract certain sub-video sequences based upon the metadata provided by the [dataset source].

## Explanation

### Original excel file
The dataset contains lot of columns each representing a import parameter and pertaining to certain explanation.<br>
If you wish to read the original file please refer to this link.

Out of all the columns provided we explain only the ones we need.
    
    Index | Main New Gloss | Scene | Session | Start | End | Separate
    ------|---------------|---------|-------|-----|---------|--------
      1    |TWENTY | 2 |ASL_2008_01_11| 2635 | 2661 | [LINK]

<b>Start</b> : Frame from which the sign begins <br>
<b>End </b>: Frame at which the sign ends <br>
The dataset website provides a link that can be used to download the video:

``` 
URL:
http://csr.bu.edu/ftp/asl/asllvd/asl-data2/quicktime/sessionId/sceneId-camera1.mov 

sessionId replaced by Session
SceneId replaced by Scene    
 ```
The dataset have been prepared using 3 cameras recording from different angles. However, not all video files from camera2 and 3 are available. So, we decided to stick with only camera1.


    
### "final" Dataframe 
    index | Position |  Word |  Num. of Videos
    ------|----------|-------|----------------
       0  |     1    |TWENTY |      4
       1  |     6    |ALONE  |      8
       2  |     15   |LONLY  |      4
       3  |     20   |BACHELOR|     7

This dataframe is used to download the files in a structured manner.Only first 4/9000+ entries are shown.
```
Description:
Position: Index of the word in the original dataframe
Word: Word that the sign represents
Num. of Videos: Number of videos for that word
```

```python 
pos = int(final[final["Word"] == i]["Position"].values[0]) #position at which the word occurs
count = int(final[final["Word"] == i]["Num. of videos"].values[0]) #number of videos of that word
```
The above variables are self explanatory. Inside for loop they are used to iterate over all the videos for the words in wordList array.


```python
start = dt.iat[pos+ 1 + j, 3] #starting frame where the word occurs
end = dt.iat[pos + 1 + j, 4] #ending frame where the word ends
session = dt.at[pos + 1 + j, "Session"] #session id for the url
scene = dt.at[pos + 1 + j, "Scene"] #scene id for the url
```
These variables are used to download and trim down videos.
> Here, start represents the frame at which the sign begins and end represents the frame where the sign ends.

```python
wget.download(url.format(session, scene), unprocessedLoc.format(j+1)) #download the video
```
<i>wget</i> library is used to download the video file from the provided link and saved in a directory

```python
ffmpeg_extract_subclip(unprocessedLoc.format(j+1), (start/60), #frame rate: 60
    (end/60), targetname=processedLoc.format(i.lower(), j+1))  #convert the video
```
The <i>framerate</i> of all the videos made available is 60. In order to trim the videos we divide the frames by 60
to get the time(in sec) at which the sign beings/ends. <br> 
> <i>These values are iteratively updated to process each video automatically.</i>

## How to execute 
General syntax for downloading the videos are provided below with examples

```shell
python Download_extract.py greaterthan ./unprocessed ./processed
```
<b>graterthan</b> represents the number of videos each word should have, for example if you wish to have more than 5 videos for each sign you would run the follow command in the terminal
```shell
python Download_extract.py 6 ./unprocessed ./processed
```

<b>./unprocessed</b> represents the folder where each raw(untrimmed) video is saved.

> :warning: unprocessed video is deleted after each iteration :warning:

<b>./processed</b> is the folder where the trimmed video files are saved in a structured manner.


### Example scripts
```shell
python Download_extract.py 10 ./temp/data ./Documents/data/processed
```

```shell
python Download_extract.py 4 /home/user_name/video/unproc /home/user_name/video/processed
```

```shell
python Download_extract.py 0 ./tmp ./dataset
```