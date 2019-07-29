import numpy as np
import pandas as pd
import random


class Frame_Sampling:

    def __init__(self,src=None,sample_frames=15):
        self.sample_frames = sample_frames
        self.source = src
        self.samples = []
        self.num_samples = 0
        self.frames_list = []
        

    def read(self,source):
        try:
            
            self.source = pd.read_csv(source)
            
            self.frames_list = [int(x) for x in list(self.source.columns.values)[1:]]
            #print(self.frames_list)
            #self.num_samples = self.file_df.columns.values//self.sample_frames
            

        except:
            print('Enter valid source!')

    def sampling(self):
        used_values = self.frames_list
        # for i in range(len(self.frames_list)):
        #     sampled_values = sorted([int(x) for x in (random.sample(self.frames_list,self.sample_frames))])
        #     used_values += sampled_values
        #     self.samples.append(sampled_values)
            #self.frames_list -= sampled_values
        for i in range(len(self.frames_list)//self.sample_frames):
            sampled_values = []
            for j in range(self.sample_frames):
                current_frame = random.choice(used_values)
                sampled_values.append(current_frame)
                used_values.remove(current_frame)
            self.samples.append(sorted(sampled_values))

    def display(self):
        print("sampled values:")
        print(self.samples)


if __name__ == '__main__' :

    sample1 = Frame_Sampling()
    sample1.read('1.csv')
    sample1.sampling()
    sample1.display()


