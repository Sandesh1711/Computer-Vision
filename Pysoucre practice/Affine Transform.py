import cv2
import  numpy as np
img = cv2.imread("F:\Placement\Computer Vision\Data\ml.png")
rows,cols=img.shape[:2]

src_point=np.float32([[0,0],[cols-1,0],[0,rows-1]])
dst_point = np.float32([[0,0],[int(0.6*(cols-1)),0],[int(0.4*(cols-1)),rows-1]])

M = cv2.getAffineTransform(src_point,dst_point)
Affine = cv2.warpAffine(img,M,(img.shape[1]+100,img.shape[0]+100))
cv2.imshow("Affine Transform",Affine)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()