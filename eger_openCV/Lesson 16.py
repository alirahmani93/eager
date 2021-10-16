### Lesson 16:
import cv2
import numpy as np

faceXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_frontalface_default.xml")
eyeXML  = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while True :
    _,frame =   cap.read()
    gray    =   cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces   =   faceXML.detectMultiScale(gray)

    for x,y,w,h in faces:
        cv2.rectangle(frame , (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w]
        roi_color = frame[y:y+h , x:x+w]

        eyes = eyeXML.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew , ey+eh),(0,0,255),1)

    cv2.imshow('frame',frame)        
    k = cv2.waitKey(27) & 0xFF
    if k == 27 : break

cap.release()
cv2.destroyAllWindows()
