# Real-time Sign-language translation(ASL to English)

> :warning: Please make sure OpenPose is properly configured in your environment with it's python API enabled :warning:

The dataset for this paper was collected from this link["#"]

## Steps Involved
1. The dataset is available both as pre-processed file and raw files. For our implementation a preprocessed data would not work as OpenPose would not be able to detect keypoints. So, we downloaded the raw(unprocessed) files using an automation script that automatically downloads and extracts the different signs in the videos in the right sequence and stores it in the a directory in the following order
    ```
    -> : Folder
    -- : files

    Dataset
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

2. We extract keypoints from  the videos using the pre-trained openpose model for each frame in the video and save it in a folder as csv files in a manner similar to how we saved the video sequences after extraction. We only needed the keypoints for upper body and hands to detect signs hence other keypoints were removed from the file before saving.

    Bx |  By | Bconfidence |  Rx  |  Ry  | Rconfidence |  Lx  |  Ly  | Lconfidence
    ---- | ---- | ------------- | ------ | ------ | ------------- | ------ | ------ | ------------- |
    329 | 133 | 0.89 | 296 | 232 | 0.78 | 364 | 385 | 0.65
    245 | 157 | 0.39 | 522 | 311 | 0.89 | 231 | 512 | 0.53

    ```
    Keypoints being saved in csv:

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 18]

    index starts from 0

    row i of csv file = arr[i]
    ```


3. A total of 1200 ASL words are used out of 2700 words in the dataset. Total number of video sequences used are 6700.

4. We propose using a Many-to-One RNN(Recurrent Neural Network)

## Table of Content
1. Video extraction
2. Keypoint extraction