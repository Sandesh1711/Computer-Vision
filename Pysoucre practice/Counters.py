import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame=cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,168],dtype=np.uint8)
    upper = np.array([172,1111,255],dtype=np.uint8)
    mask = cv2.inRange(img,lower,upper)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    ret3,contours,ret1 =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(contours)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow("frame",frame)
    cv2.imshow('mask',res)
    k=cv2.waitKey(25)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()