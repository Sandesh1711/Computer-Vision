import cv2
import numpy as np
# white image
#frame = np.ones([100,100,3],dtype = np.uint8)*255
# black image
#frame = np.ones([100,100,3],dtype = np.uint8)
def nothing(x):
    pass
cv2.namedWindow('Frame')
cv2.createTrackbar('test','Frame',0,255,nothing)

while True:
    frame = cv2.imread('Data/gradient.png')
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(200,200))
    value_threshold = cv2.getTrackbarPos('test','Frame')
    _,threshold_binary = cv2.threshold(frame,value_threshold,255,cv2.THRESH_BINARY)
    _,threshold_binary1 = cv2.threshold(frame,value_threshold,255,cv2.THRESH_BINARY_INV)
    _,threshold_binary2 = cv2.threshold(frame,value_threshold,255,cv2.THRESH_TRUNC)
    _,threshold_binary3 = cv2.threshold(frame,value_threshold,255,cv2.THRESH_TOZERO)
    _,threshold_binary4 = cv2.threshold(frame,value_threshold,255,cv2.THRESH_TOZERO_INV)
    cv2.imshow('Frame',frame)
    cv2.imshow('frame',threshold_binary)
    cv2.imshow('frame1',threshold_binary1)
    cv2.imshow('frame2',threshold_binary2)
    cv2.imshow('frame3',threshold_binary3)
    cv2.imshow('frame4',threshold_binary4)
    k = cv2.waitKey(100)
    if  k ==100:
        break

cv2.destroyAllWindows()

