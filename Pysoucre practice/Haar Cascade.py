import cv2

def nothing():
    pass

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
face = cv2.CascadeClassifier('F:\Placement\Computer Vision\haarcascades\haarcascade_frontalface_default.xml')
cv2.namedWindow('Frame')
cv2.createTrackbar("scale",'Frame',11,20,nothing)
cv2.createTrackbar("Neighbours",'Frame',0,20,nothing)


while (cap.isOpened):
    ret, image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    scale = cv2.getTrackbarPos("scale",'Frame')
    neighbour = cv2.getTrackbarPos('Neighbours','Frame')

    faces = face.detectMultiScale(gray,scale,5)
    print(faces)
    for f in faces:
        (x,y,w,h)=f
        frame = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),4)
    cv2.imshow("Face",image)
    k=cv2.waitKey(25)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()