import numpy as np
import cv2

cap=cv2.VideoCapture(0)
while(True):
    ret,img=cap.read()
    cv2.namedWindow('img',cv2.WINDOW_NORMAL)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    path="haarcascade_frontalface_default.xml"
    path1="haarcascade_eye.xml"

    face_cascade = cv2.CascadeClassifier(path)
    eye_cascade=cv2.CascadeClassifier(path1)

    faces=face_cascade.detectMultiScale(gray,1.10,5)
    eyes=eye_cascade.detectMultiScale(gray,1.2,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    for (x,y,w,h) in eyes:
        xc=(x+ x+w)/2
        yc=(y+y+h)/2
        radius=w/2
        cv2.circle(img,(int(xc),int(yc)),int(radius),(255,0,0),2)
    cv2.imshow("img",img)

    ch=cv2.waitKey(1)
    if ch & 0xFF==ord('q'):
        break
    
    
cap.release()

cv2.destroyAllWindows()
    
    
