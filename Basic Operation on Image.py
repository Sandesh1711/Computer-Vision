import cv2
import numpy as np

image = cv2.imread('Data/butterfly.jpg')
# image = np.array([[
#     [255,0,0],[255,0,0],[255,0,0],[255,255,255]],
#     [[0,255,0],[0,255,0],[0,255,0],[255,255,255]],
#     [[0,0,255],[0,0,255],[0,0,255],[255,255,255]]],np.uint8)
#

#image = cv2.resize(image,(300,300))
image[100,100] =(0,0,0)
row, col, ch = image.shape
print(row,col,ch)

roi = image[100:col,100:row]
cv2.imshow("ROI", roi)
cv2.imshow('frame',image)

cv2.waitKey(0)

cv2.destroyAllWindows()