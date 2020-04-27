from .get_digits import get_blocks
from tensorflow.keras.models import model_from_json
import tensorflow as tf
import numpy as np
import cv2
from .solve_sudoku import solve_sudoku
from webapp.settings import BASE_DIR,PROCESSING_FILES

json_file = open(PROCESSING_FILES+"/NN/model.json",'r')
loaded_json_model = json_file.read()
json_file.close()
model = model_from_json(loaded_json_model)
graph = tf.get_default_graph()
model.load_weights(PROCESSING_FILES+"/NN/model.h5")

print("loaded model from disk")
model.compile(loss=tf.keras.losses.categorical_crossentropy,optimizer='adam',metrics=['accuracy'])

def convert_sud_to_string(listoflist):
	listf =[]
	for item1 in listoflist:
		s=""
		for item2 in item1:
			s=s+str(item2)+' '
		listf.append(s)
	return listf

def make_sudoku(filename):
	imgs_list,labels_for_blank = get_blocks(filename)

	test_imgs = imgs_list

	test_imgs = np.asarray(test_imgs)
	test_imgs = test_imgs.astype('float32')
	non_empty_blocks = []
	for i in range(test_imgs.shape[0]):
		if labels_for_blank[i]=="no":
			non_empty_blocks.append(test_imgs[i])
			
	non_empty_blocks = np.asarray(non_empty_blocks)
	non_empty_blocks = non_empty_blocks.astype('float32')
	global graph
	with graph.as_default():
		predictions = model.predict(non_empty_blocks)
	
	y_classes = [np.argmax(y) for y in predictions]


	k=0
	list_temp =[]
	final_sudoku =[]
	for i in range(test_imgs.shape[0]):

		if labels_for_blank[i]=="yes":
			list_temp.append(0)
		else:
			list_temp.append(y_classes[k])
			k+=1
		if (i+1)%9==0:
			final_sudoku.append(list_temp)
			list_temp=[]


	initial_sudoku,solved = solve_sudoku(final_sudoku)
	initial_sudoku = convert_sud_to_string(initial_sudoku)
	return initial_sudoku,solved




