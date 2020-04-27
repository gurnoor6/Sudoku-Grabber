import cv2
import numpy as np

def crop_img(src):
	image = cv2.imread(src,0)
	blur = cv2.GaussianBlur(image, (11,11),0)
	thresholded = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,5)
	kernel = np.asarray([[0,1,0],[1,1,1],[0,1,0]],np.uint8)
	eroded = cv2.erode(thresholded,kernel)
	contours, hierarchy = cv2.findContours(eroded,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

	maxA = cv2.contourArea(contours[0],True)
	max_index= 0
	for i in range(1,len(contours)):
		area = cv2.contourArea(contours[i],True)
		if area>maxA:
			maxA = area
			max_index = i

	mask = np.zeros(image.shape,np.uint8)
	cv2.drawContours(mask,contours,max_index,255,-1)
	whitePixels = np.nonzero(mask)
	X = whitePixels[1]
	Y = whitePixels[0]

	add = X+Y
	diff = X-Y

	a1 = np.argmax(add)
	a2 = np.argmin(add)
	a3 = np.argmax(diff)
	a4 = np.argmin(diff)

	tl_x = X[a2]+5
	tl_y = Y[a2]+5
	tr_x = X[a3]-5
	tr_y = Y[a3]+5
	bl_x = X[a4]+5
	bl_y = Y[a4]-5
	br_x = X[a1]-5
	br_y = Y[a1]-5

	l_sudoku = int((tr_x-tl_x+br_x-bl_x+br_y-tr_y+bl_y-tl_y-40)/2)
	l_smallsquare = l_sudoku//9
	l_sudoku = l_smallsquare*9

	src = np.asarray([[tl_x,tl_y],[tr_x,tr_y],[br_x,br_y],[bl_x,bl_y]],np.float32)
	dst = np.asarray([[0,0],[l_sudoku,0],[l_sudoku,l_sudoku],[0,l_sudoku]],np.float32)

	transformMatrix = cv2.getPerspectiveTransform(src,dst)
	cropped_img = cv2.warpPerspective(image,transformMatrix,(l_sudoku,l_sudoku))
	equalized = cv2.equalizeHist(cropped_img)
	t_value = np.sum(equalized)/(equalized.size*4)			
	_,thresh = cv2.threshold(equalized,t_value,255,cv2.THRESH_BINARY_INV)
	image_final = cv2.resize(thresh,(720,720))
	return image_final

def get_blocks(src):
	cropped_img  = crop_img(src)
	points = []
	i=0
	while i<=640:
		points.append(i)
		i+=80

	label =[]
	imgs = []
	for j in points:
		for k in points:
			temp = cropped_img[j+15:j+65,k+15:k+65]
			temp = cv2.resize(temp,(28,28))
			temp = temp[:,:,None]
			trueval = (temp<=127)
			sum = np.sum(trueval)
			if(sum>=770):
				label.append("yes")
			else:
				label.append("no")
			imgs.append(temp)
	return imgs,label



if __name__=='__main__':
	imgs_list = get_blocks("images/sud.jpg")
	test_imgs = imgs_list
	i=0
	for img in test_imgs:
		cv2.imshow("image",img)
		i+=1
		cv2.waitKey(0)
		cv2.destroyAllWindows()























