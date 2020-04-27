import csv
import numpy as np
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import backend as K
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


rows=[]
rows_test=[]
with open('mnist_train.csv') as csvfile:
	readCSV = csv.reader(csvfile,delimiter=",")
	for row in readCSV:
		rows.append(row)

with open('mnist_test.csv') as csvfile_test:
	readCSV = csv.reader(csvfile_test,delimiter=",")
	for row in readCSV:
		rows_test.append(row)

num_classes=10

rows_test = rows_test[1:]
rows = rows[1:]
array = np.asarray(rows,np.uint8)
array_test = np.asarray(rows_test,np.uint8)
# print(type(array[0]))
y_train = array[:,0]
x_train = array[:,1:]
y_test = array_test[:,0]
x_test = array_test[:,1:]
x_train = x_train.reshape(x_train.shape[0],28,28,1)
x_test = x_test.reshape(x_test.shape[0],28,28,1)
input_shape = (28,28,1)

y_train = tf.keras.utils.to_categorical(y_train,num_classes)
y_test = tf.keras.utils.to_categorical(y_test,num_classes)

temp_train_list=[]
temp_test_list=[]
for i in range(60000):
  temp_train_list.append(cv2.adaptiveThreshold(x_train[i],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,27,2))

for i in range(10000):
  temp_test_list.append(cv2.adaptiveThreshold(x_test[i],255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,27,2))

temp_train_array = np.asarray(temp_train_list,np.uint8)
temp_test_array = np.asarray(temp_test_list,np.uint8)

x_train = temp_train_array
x_test = temp_test_array
x_train = x_train[...,None]
x_test = x_test[...,None]
print("yess")

# x_train = x_train.astype('float32')
# x_test = x_test.astype('float32')
# x_train/=255
# x_test/=255

batch_size = 128
epochs =8

def getModel():
	model = Sequential()
	model.add(Conv2D(32,kernel_size=(3,3),activation='relu',input_shape=input_shape))
	model.add(Conv2D(64,(3,3),activation='relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))
	model.add(Flatten())
	model.add(Dense(256,activation='relu'))
	model.add(Dropout(0.5)) 
	model.add(Dense(num_classes,activation='softmax'))

	model.compile(loss=tf.keras.losses.categorical_crossentropy,optimizer='adam',metrics=['accuracy'])

	return model

def train():
	model = getModel()
	hist = model.fit(x_train,y_train,batch_size=batch_size, epochs = epochs, verbose =1, validation_data = (x_test,y_test))
	score = model.evaluate(x_test,y_test,verbose=0)
	print("Test loss:",score[0])
	print("Test accuracy:",score[1])
	# serialize model to JSON
	model_json = model.to_json()
	with open("model.json", "w") as json_file:
	    json_file.write(model_json)
	# serialize weights to HDF5
	model.save_weights("model.h5")
	print("Saved model to disk")


if __name__=="__main__":
	train()
# i=0
# for img in x_test:
# 	cv2_imshow(img)