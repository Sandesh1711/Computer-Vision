import cv2
import numpy as np
img = cv2.imread("F:\Placement\Computer Vision\Data\ml.png")
height,width=img.shape[:2]
M=cv2.getRotationMatrix2D((width/2,height/2),10,1)
Rotate = cv2.warpAffine(img,M,(img.shape[1]+100,img.shape[0]+100))
cv2.imshow("Rotate",Rotate)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()