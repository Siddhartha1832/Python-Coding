
# OpenCV - Image and video processing library with bindings in C++, C, Python, and Java. 
# OpenCV is used for all sorts of image and video analysis, like facial recognition and detection,
# license plate reading, photo editing, advanced robotic vision, optical character recognition, and a whole lot more.

# Install OpenCV module in CMD Prompt
# > pip install opencv-python numpy matplotlib --upgrade

import cv2
import numpy as np
import matplotlib.pyplot as plt
# computer form is measured in frames/sed (fps), each fps is image
img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) # imread - image read. i filtered image by grayscale (optional)
# IMREAD_COLOR - 1 for color, 0 for grayscale
# IMREAD_UNCHANGED = -1

## method1 - show image using opencv
## OpenCV does BGR, matplotlib does RGB
cv2.imshow('imageviewer', img) # show image. imageviewer represent title of image.
cv2.waitKey(0) # close the window if any key pressed
cv2.destroyAllWindows()

## method2 - show image using matplotlib
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.plot([50,100], [80,100], 'c', linewidth=5) # optional. Draw line with coordinates x1,y1,x2,y2 with color c as cyan.
# plt.show()