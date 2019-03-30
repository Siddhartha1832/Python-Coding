# Loading video source

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 represents first webcam in your sys.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outfile = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
	ret, frame = cap.read() # ret returns true/false
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	outfile.write(frame) # write captured video
	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release() # camera will release for capture.
outfile.release() # save captured video and close
cv2.destroyAllWindows()