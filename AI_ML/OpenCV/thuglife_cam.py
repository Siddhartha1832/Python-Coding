import cv2, time
from PIL import Image
import numpy as np

maskPath = "mask.png" # thug life meme mask image path
cascPath = "haarcascade_frontalface_default.xml" # haarcascade path

faceCascade = cv2.CascadeClassifier(cascPath) # cascade classifier object 
mask = Image.open(maskPath) # Open mask as PIL image

## function to add thug life mask to input image
def thug_mask(image):
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert input image to grayscale
	faces = faceCascade.detectMultiScale(gray, 1.15) # detect faces in grayscale image
	background = Image.fromarray(image) # convert cv2 imageto PIL image
	for (x,y,w,h) in faces:
		resized_mask = mask.resize((w,h), Image.ANTIALIAS) # resize mask
		offset = (x,y) # define offset for mask
		background.paste(resized_mask, offset, mask=resized_mask) # pask mask on background
	return np.asarray(background) # return background as cv2 image

cap = cv2.VideoCapture(cv2.CAP_ANY) # VideoCapture object

while True:
	ret, frame = cap.read() # read return value and frame
	if ret == True:
		# show frame with thug life mask
		cv2.imshow('Live', thug_mask(frame))
		# chck if esc key or letter q is pressed
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

# release cam
cap.release()
# destroy all open opencv windows
cv2.destroyAllWindows()