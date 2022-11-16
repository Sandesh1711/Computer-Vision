import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('F:\Placement\Computer Vision\Data\messi5.jpg')
b,g,r = cv2.split(image)

cv2.imshow("Frame",image)

plt.hist(image.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.show()