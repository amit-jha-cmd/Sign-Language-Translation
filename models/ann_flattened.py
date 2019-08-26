from keras.models import Sequential
from keras.layers import Dense



model = Sequential()
model.add(Dense(2000,input_dim=1710,activation='relu'))
model.add(Dense(2000,activation='relu'))
model.add(Dense(106,activation='softmax'))

model.compile(loss='categorical-crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X_train, Y_train,epochs=150,batch_size=10)