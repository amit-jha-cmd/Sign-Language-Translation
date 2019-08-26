# Sign-language recognition

> :warning: Please make sure OpenPose is properly configured in your environment with it's python API enabled :warning:

> The dataset for this paper was collected from this link["#"]
- [Sign-language recognition](#sign-language-recognition)
  - [Introduction](#introduction)
  - [Steps Involved](#steps-involved)
  - [Documentation](#documentation)

## Introduction

## Steps Involved
1. The dataset used in this project has over 140K video sequences broken down into 22 batches. Each batch contains around 6k folders each containing all the frames for the given class. Each folder in nameed according to the jester-v1-train(.csv) file. Due to the shear volume of the dataset the videos sequences are downloaded in the cloud and all the processing takes place in google colab. Each batch in the dataset in orderes in the falling sequence.
    ```
    -> : Folder
    -- : files

    Video Dataset
        |->3122
        |   |-- 1.jpg
        |   |-- 2.jpg
        |   |-- 3.jpg
        |   |-- 4.jpg
        |
        |->1212
        |   |-- 1.jpg
        |   |-- 2.jpg
        |   |-- 3.jpg
        |   |-- 4.jpg
        |   |-- 5.jpg
        |
        .
        .
        .
    
    ```
    >Each jpg file represents a frame in the respective video.

2. We extract keypoints from  the videos using the pre-trained openpose model for each frame in the video and save it in a folder as csv files in a manner similar to how we save the video sequences after extraction. We only need the keypoints for upper body and hands to detect signs hence other keypoints are removed from the file before saving.

    | Bx  | By  | Bconfidence | Rx  | Ry  | Rconfidence | Lx  | Ly  | Lconfidence |
    | --- | --- | ----------- | --- | --- | ----------- | --- | --- | ----------- |
    | 329 | 133 | 0.89        | 296 | 232 | 0.78        | 364 | 385 | 0.65        |
    | 245 | 157 | 0.39        | 522 | 311 | 0.89        | 231 | 512 | 0.53        |

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
        |->3122
        |   |-- video.csv
        |
        |->1212
        |   |-- video.csv
        .
        .
        .
    ```

3. A total of 1200 ASL words are used out of 2700 words in the dataset. Total number of video sequences used are 6700.

4. We propose using a Many-to-One RNN(Recurrent Neural Network)

## Documentation
- Download and extract videos
- Extract keypoints
- Feature augmentation
- Normalization technique
- Colab implementation