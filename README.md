# Real-time Sign-language translation(ASL to English)

> :warning: Please make sure OpenPose is properly configured in your environment with it's python API enabled :warning:

The dataset for this paper was collected from this link["#"]

## Steps Involved
1. The dataset is available both as pre-processed file and raw files. For our implementation a preprocessed dataset will not work as OpenPose would not be able to detect keypoints. So, we download the raw(unprocessed) files using an automation script that automatically downloads and extracts the different signs in the videos in the right sequence and stores it in a directory
    ```
    -> : Folder
    -- : files

    Video Dataset
        |->Hello
        |   |-- 1.mp4
        |   |-- 2.mp4
        |   |-- 3.mp4
        |   |-- 4.mp4
        |
        |->Bye
        |   |-- 1.mp4
        |   |-- 2.mp4
        |   |-- 3.mp4
        |   |-- 4.mp4
        |   |-- 5.mp4
        |
        .
        .
        .
    ```

2. We extract keypoints from  the videos using the pre-trained openpose model for each frame in the video and save it in a folder as csv files in a manner similar to how we save the video sequences after extraction. We only need the keypoints for upper body and hands to detect signs hence other keypoints are removed from the file before saving.

    Bx |  By | Bconfidence |  Rx  |  Ry  | Rconfidence |  Lx  |  Ly  | Lconfidence
    ---- | ---- | ------------- | ------ | ------ | ------------- | ------ | ------ | ------------- |
    329 | 133 | 0.89 | 296 | 232 | 0.78 | 364 | 385 | 0.65
    245 | 157 | 0.39 | 522 | 311 | 0.89 | 231 | 512 | 0.53

    ```
    COLUMNS:
    Bx: Body x co-ordinate
    By: Body y co-ordinate
    Bconfidence: confidence score of the keypoint

    Rx: Right x co-ordinate
    Ry: Right y co-ordinate
    Rconfidence: confidence score of the keypoint

    Lx: Left x co-ordinate
    Ly: Left y co-ordinate
    Lconfidence: confidence score of the keypoint

    ROWS: 
    row i of csv file = arr[i]

    
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18]

    arr represents the body keypoints being saved. Please refer to openpose/docs/output.md for details
    ```
    Structure of the csv files
    ```
    -> : Folder
    -- : files

    CSV Dataset
        |->Hello
        |   |->1
        |   |   |-- 1.csv
        |   |   |-- 2.csv
        |   |   |-- 3.csv
        .
        .
        .
        |   |->2
        |   |   |-- 1.csv
        |   |   |-- 2.csv
        |   |   |-- 3.csv
        |   |   |-- 4.csv
        .
        .
        .
    ```

3. A total of 1200 ASL words are used out of 2700 words in the dataset. Total number of video sequences used are 6700.

4. We propose using a Many-to-One RNN(Recurrent Neural Network)

## Table of Content
1. Video extraction
2. Keypoint extraction