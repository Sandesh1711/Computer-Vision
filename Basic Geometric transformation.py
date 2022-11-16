import cv2
import numpy as np

img = cv2.imread('Data/board.jpg')
scaled_image = cv2.resize(img,None,fx=1/2,fy=1/2)

cv2.imshow('Frame',img)
cv2.imshow('Resize',scaled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()