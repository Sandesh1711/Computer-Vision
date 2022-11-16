import cv2
import numpy as np

img1 = cv2.imread('Data/road.jpg')
img2 = cv2.imread('Data/car.jpg')
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
print(img2.shape)
img1 = cv2.resize(img1,(500,375))

road = cv2.bitwise_and(img1,img1,mask=mask)
cv2.imshow('Road',img1)
cv2.imshow('car',img2)
cv2.imshow('mask',road)

cv2.waitKey(0)
cv2.destroyAllWindows()