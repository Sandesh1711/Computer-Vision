import cv2
import numpy as np

image = cv2.imread('Data/aero1.jpg')

cv2.line(image,(0,0),(100,100),(0,255,0),2)
cv2.circle(image,(240,205),23,(255,0,0),-1)
cv2.rectangle(image, (50,60),(450,95),(0,255,0),-1)
cv2.ellipse(image,(250,150),(80,20),5,0,360,(0,180,180),-1)
yellow = (180,0,180)
points = np.array([[[120,230],[400,230],[320,250]]],np.int32)
cv2.polylines(image,[points],True,yellow,10)

cv2.putText(image,'Sandesh',(20,100),fontFace=4,fontScale=4,color=(255,255,255))
cv2.imshow("Frame", image)
cv2.waitKey(0)

cv2.destroyAllWindows()