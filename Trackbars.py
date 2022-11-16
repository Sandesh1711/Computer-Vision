import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass
cv2.namedWindow('frame')

cv2.createTrackbar('test','frame',50,500,nothing)
cv2.createTrackbar('color/gray','frame',0,1,nothing)
while True:
    _, frame = cap.read()

    test = cv2.getTrackbarPos('test','frame')
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, str(test),(50,150),font ,4,(255,0,0))
    s = cv2.getTrackbarPos('color/gray', 'frame')
    if s==1:
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
    else:
        cv2.imshow('frame', frame)
    k = cv2.waitKey(25)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()