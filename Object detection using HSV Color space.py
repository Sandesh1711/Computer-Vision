import cv2
import numpy as np
def nothing():
    pass
cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")
cv2.createTrackbar('lower_x','Trackbar',0,255,nothing)
cv2.createTrackbar('lower_y','Trackbar',0,255,nothing)
cv2.createTrackbar('lower_z','Trackbar',0,255,nothing)
cv2.createTrackbar('upper_x','Trackbar',0,255,nothing)
cv2.createTrackbar('upper_y','Trackbar',0,255,nothing)
cv2.createTrackbar('upper_z','Trackbar',0,255,nothing)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_x = cv2.getTrackbarPos('lower_x','Trackbar')
    l_y = cv2.getTrackbarPos('lower_y', 'Trackbar')
    l_z = cv2.getTrackbarPos('lower_z', 'Trackbar')
    u_x = cv2.getTrackbarPos('upper_x', 'Trackbar')
    u_y = cv2.getTrackbarPos('upper_y', 'Trackbar')
    u_z = cv2.getTrackbarPos('upper_z', 'Trackbar')


    lower_blue = np.array([l_x,l_y,l_z])
    upper_blue = np.array([u_x,u_y,u_z])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('result',result)
    cv2.imshow("mask",mask)
    cv2.imshow('Frame',hsv)
    k = cv2.waitKey(25)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()