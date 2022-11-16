import cv2

img = cv2.imread("F:\Placement\Computer Vision\Data\home.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img= cv2.GaussianBlur(img,(5,5),0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)


laplacian = cv2.Laplacian(img,cv2.CV_64F,ksize=5)

canny = cv2.Canny(img,90,150)
cv2.imshow("Canny",canny)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("Frame",img)
cv2.imshow("SobelX",sobelx)
cv2.imshow("Sobely",sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()