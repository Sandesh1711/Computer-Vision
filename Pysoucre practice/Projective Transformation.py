import cv2
import  numpy as np
img = cv2.imread("F:\Placement\Computer Vision\Data\ml.png")
rows,cols=img.shape[:2]

src_point=np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
dst_point = np.float32([[0,0],[cols-1,0],[int(0.33*(cols)),rows-1],[int(0.66*(cols)),rows-1]])

M = cv2.getPerspectiveTransform(src_point,dst_point)
Projective = cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
cv2.imshow("Projective Transform",Projective)
cv2.imshow("Frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()