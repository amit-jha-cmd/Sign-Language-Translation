
> :warning: The model and the code will be published when our paper is accepted in a journal. :warning:


# Sign Language Recognition
This repo contains the codebase for the paper: <i>Sign Language recognition on video dataset using transfer learning</i>
<hr>

```
This Paper attempts to do sign language recognition on video dataset using transfer learning
```
Sign language recognition on video dataset is a difficult task due to following reason:

1. Video dataset are sparse

2. It is difficult to train on videos as the sequences can vary in length.

<hr>

## CNN and LSTM
In this approach we extract features from the videos by treating each individual frame as a picture and then extracting features from these images using Inception V3.
The extraction process is rather simple as we simply remove the last few layers of reset and saves the features from the last existing layer into a folder is a structured manner.
The feature map collected from the aforementioned process is used to train the LSTM based model.
<hr>

## ConvLSTM

This is another approach to train our model. We combine convolution with LSTM and then perform the training on our video dataset. For the purpose of this method we used ConvLSTM2D which is an implementation is keras. 
<hr>


### Dataset
For this implementation we used transfer learning on UCF101 dataset using InceptionV3 as the base model. 

































