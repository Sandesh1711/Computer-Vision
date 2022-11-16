import cv2
import numpy as np
from matplotlib import pyplot as plt
img1 = cv2.imread("Data/messi5.jpg")
b,g,r = cv2.split(img1)

img = np.zeros((100,100),np.uint8)
cv2.rectangle(img,(0,50),(100,100),(255),-1)
cv2.imshow('img',img)

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()
#cv2.waitKey(0)
# cv2.destroyAllWindows()


