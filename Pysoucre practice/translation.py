import cv2
import  numpy as np
img = cv2.imread("F:\Placement\Computer Vision\Data\ml.png")
M = np.float32([[1,0,100],[0,1,100]])
translate = cv2.warpAffine(img,M,(img.shape[1]+100,img.shape[0]+100))
cv2.imshow("Translate",translate)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()