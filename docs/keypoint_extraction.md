# Extracting keypoints from video sequences

>This document is the description of the script developed to extract keypoints from videos

>:warning: We use OpenPose which is state-of-the-art pose detecting model for keypoint extraction. Please make sure it is properly configured in your system with the python API. :warning:

<b><i>datum</i></b> is an object returned by <i>pyopenpose.Datum()</i> method which contains <i>keypoints</i>, <i>heatmaps</i> for *body*, *hand*, *face* and a whole lot of other attributes and associated methods
