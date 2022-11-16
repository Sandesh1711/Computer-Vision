import cv2

#cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('Data/Megamind.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Data/flipped Megamind.avi', fourcc, 25,(640,360))
while True:
    _, img = cap.read()
    img = cv2.flip(img,0)
    cv2.imshow("Video",img)
    out.write(img)
    k = cv2.waitKey(25)
    if k==27:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
