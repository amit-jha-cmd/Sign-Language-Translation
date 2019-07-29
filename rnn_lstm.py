from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout, Masking
from keras.callbacks import EarlyStopping, ModelCheckpoint


model = Sequential()

class Model:



    def __init__(self):
        self.model = Sequential()
        #self.input_dimention = input_dim

    def add_Embedding(self,input_dim,training_length,output_length,weights=None,trainable=False,mask_zero=True):
        
        self.model.add(
            Embedding(input_dim=input_dim,
                input_length = training_length,
                output_dim=100,
                weights=[embedding_matrix],
                trainable=False,
                mask_zero=True))

    def add_LSTM(self,input_size,dropout=0.1, reccurent_dropout=0.1):
        self.model.add(
            LSTM(input_size,dropout=dropout,return_sequences=False,reccurent_dropout=reccurent_dropout))

    def add_Masking(self,mask_value=0.0):
        self.model.add(Masking(mask_value=mask_value))

    def add_Dense(self,input_size,activation_func):
        self.model.add(Dense(input_size,activation=activation_func))

    def model_compile(self,optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy']):
        self.model.compile(optimizer=optimizer,loss=loss,metrics=metrics)

    def model_fit(self,X_train,y_train,callbacks,validation_data,batch_size=100,epochs=150):
        istory = model.fit(X_train,  y_train, 
                    batch_size=batch_size, epochs=epochs,
                    callbacks=callbacks,
                    validation_data=validation_data) # (X_valid, y_valid)

        # Facing synatax error
    #def add_callbacks(self):
    #    callbacks = [(EarlyStopping(monitor='val_loss', patience=5),ModelCheckpoint('../models/model_rnn.h5'),save_best_only=True, save_weights_only=False)]


    
