from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import numpy as np
import statistics

class Model:

    def __init__(self,n_estimators=1000,max_depth=100,random_state=0):
        self.model = RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth,random_state=random_state)
        #self.X, self.Y = make_classification(n_samples=1000, n_features=6,n_classes=3,n_informative=4, n_redundant=2,
         #               random_state=0, shuffle=False)
       # self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X,self.Y,test_size = 0.25,random_state = 0)

    def train_trial(self):
        self.model.fit(self.X_train,self.Y_train)

    def train(self,X_train,Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        self.model.fit(self.X_train,self.Y_train)


    def create_dataset(self,n_samples=1000,n_features=6,n_classes=3,n_informative=4,n_redundant=2,random_state=0,shuffle=False):
        self.X, self.Y = make_classification(n_samples=n_samples, n_features=n_features,n_classes=n_classes,
                        n_informative=n_informative, n_redundant=n_redundant,random_state=random_state, shuffle=shuffle)
        # split the data
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.X,self.Y,test_size = 0.25,random_state = random_state)


    def prediction_trial(self):
        self.predictions = self.model.predict(self.X_test)

    def prediction(self,X_test):
        self.X_test = X_test

        self.predictions = self.model.predict(self.X_test)


    def accuracy_trail(self):
        
        #self.Y_test = Y_test
        #acc = 100 - np.mean(np.ndarray(abs(self.predictions - self.Y_test)))
        acc = 100 - statistics.mean(abs(self.predictions - self.Y_test))
        #print(sum(abs(self.predictions - self.Y_test))/len(self.Y_test))
        return acc


    def accuracy(self,Y_test):
        
        self.Y_test = Y_test
        acc = 100 - np.mean(abs(self.predictions - self.Y_test))
        
        return acc



# if __name__ == '__main__' :

#     rf1 = Model()
#     rf1.create_dataset()
#     rf1.train_trial()
#     rf1.prediction_trial()
#     val = rf1.accuracy_trail()
#     print(val)
#     #print(rf1.predictions)
    

