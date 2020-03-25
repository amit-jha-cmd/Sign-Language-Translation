
> :warning: The model and the code will be published when our paper is accepted in a journal. :warning:


# Sign Language Recognition
This repo contains the codebase for the paper: <i>Sign Language recognition on video dataset using transfer learning</i>
<hr>


><b>This Paper attempts to do sign language recognition on video dataset using transfer learning</b>

Sign language recognition on video dataset is a difficult task due to following reason:

1. Video dataset are sparse

2. It is difficult to train on videos as the sequences can vary in length.

<hr>

# Feature Extraction

### Method 1: CNN + LSTM
In this approach we extract features from the videos by treating each individual frame as a picture and then extracting features from these images using Inception V3.
The extraction process is rather simple as we simply remove the last few layers of Inception and save the features from the existing layer into a folder is a structured manner.
The feature map collected from the aforementioned process is used to train the LSTM based model.
<hr>

### Method 2: ConvLSTM

This is another approach to train our model. We combine convolution with LSTM and then perform the training on our video dataset. For the purpose of this method we used ConvLSTM2D which is an implementation is keras.
<hr> 


# Transfer Learning
The model obtained by traning on (CNN + LSTM ) model and ConvLSTM is now retrained on sign language video dataset to achieve high accuracy.
<hr>

## Dataset
For this implementation we used transfer learning on UCF101 dataset using InceptionV3 as the base model. 

<hr>

## Documentation
1. [How to run](./docs/run.md)
2. [Extract Features](./docs/extract.md)
3. [Transfer Learning](./docs/tf.md)
<hr>

## Contributors
1. Amit Jha [Github](github.com/devbihari) | [LinkedIn](linkedin.com/devbihari)
2. Yash Bharathdwaj [Github](github.com/mario) | [LinkedIn](linkedin.com/mario)

<i>This repo is the implementation for a paper. Entire code base is not being made publicly available until the paper is accepted in a journal.</i>



















