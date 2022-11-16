import cv2
image = cv2.imread('Data/apple.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image',image)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()