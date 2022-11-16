import cv2
import numpy as np
image1 = cv2.imread('Data/aero1.jpg')
image2 = cv2.imread('Data/ml.png')
image1 = cv2.resize(image1,(400,400))
image2 = cv2.resize(image2,(400,400))
#cv2.imshow('image1',image1)
#cv2.imshow('image2',image2)

gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(gray,170,255,cv2.THRESH_BINARY)
sum1 = cv2.add(image2,image1)

weighted = cv2.addWeighted(image1,1, image2,0.3,0)
#cv2.imshow("weighted",weighted)
cv2.imshow('Threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()