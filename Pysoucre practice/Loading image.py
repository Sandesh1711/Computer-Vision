import cv2

image = cv2.imread('F:\Placement\Computer Vision\Data\ml.png')
#img1 = cv2.resize(image,fx=.5,fy=.5)
shape=image.shape
#cv2.imwrite("Resized_ML_image",img1)
#cv2.imshow("img1",img1)
print(shape)
cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()