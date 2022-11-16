import  cv2

img= cv2.imread('F:\Placement\Computer Vision\Data\messi5.jpg')

resized_image = cv2.resize(img,None,fx=0.5,fy=0.5)

cv2.imshow("Frame",img)
cv2.imshow("Resized image",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()