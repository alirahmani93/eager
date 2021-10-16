### detect face parts for VIDEO
import cv2 ; #import numpy as np ; #import matplotlib.pyplot as plt
faceXML     = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_face_frontal_default.xml")
face_altXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_frontalface_alt.xml")
face_alt2XML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_frontalface_alt2.xml")
face_profileXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_face_profile.xml")
eyeXML      = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye.xml")
eye_leftXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye_left_2splits.xml")
eye_rightXML= cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye_right_2splits.xml")
glassesXML   = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye_tree_eyeglasses.xml")
smileXML    = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_smile.xml")
#   Error    # body_lowerXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_body_lower.xml")
#   Error    # body_fullXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_body_full.xml")
#   Error    # body_upperXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_body_upper.xml")

cap= cv2.VideoCapture(0)

while True :
    _,frame =   cap.read()
    gray    =   cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   
        
    faces   =   faceXML.detectMultiScale(gray)
    for x,y,w,h in faces:
        cv2.rectangle(frame , (x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h , x:x+w] # for detecting
        roi_color = frame[y:y+h , x:x+w] # for showing

        eyes = eyeXML.detectMultiScale(roi_gray)
        for ex,ey,ew,eh in eyes:
            cv2.rectangle(roi_color, (ex,ey),(ex+ew , ey+eh),(0,255,0),1)

##        leftEye = eye_leftXML.detectMultiScale(roi_gray)
##        for  lex,ley,lew,leh in leftEye:
##            cv2.rectangle(roi_color , (lex,ley),(lex+lew,ley+leh),(255,255,0),3)

##        rightEye = eye_rightXML.detectMultiScale(roi_gray)
###                        # answer : right better than left #
##        for  lex,ley,lew,leh in rightEye:
##            cv2.rectangle(roi_color , (lex,ley),(lex+lew,ley+leh),(255,0,255),3)

##        glassEye = glassesXML.detectMultiScale(roi_gray)
###                        # answer: not good # 
##        for  lex,ley,lew,leh in glassEye:
##            cv2.rectangle(roi_color , (lex,ley),(lex+lew,ley+leh),(255,255,0),3)

        smiles = smileXML.detectMultiScale(roi_gray)
        for sx,sy,sw,sh in smiles:
            cv2.rectangle(roi_color,(sx,sy),(sx+sw , sy+sh),(0,0,255),1)
            smile_rect = roi_gray[sy:sy+sh , sx:sx+sw ]

##    faces_alt   =   face_altXML.detectMultiScale(gray)
##    for x,y,w,h in faces_alt:
##        cv2.rectangle(frame , (x,y),(x+w,y+h),(255,0,0),2)            

##    faces_alt2   =   face_alt2XML.detectMultiScale(gray)
##    for x,y,w,h in faces_alt2:
##        cv2.rectangle(frame , (x,y),(x+w,y+h),(255,0,0),2)

##    faces_profile   =   face_profileXML.detectMultiScale(gray)
##    for x,y,w,h in faces_profile:
##        cv2.rectangle(frame , (x,y),(x+w,y+h),(0,255,0),2)

            
##    body_full = body_fullXML.detectMultiScale(gray)
##    for a,b,c,d in bodies:
##        cv2.rectangle(frame , (a,b),(a+c,b+d),(255,255,0),3)

##    body_lower = body_lowerXML.detectMultiScale(gray)
##    for a,b,c,d in bodies:
##        cv2.rectangle(frame , (a,b),(a+c,b+d),(255,255,0),3)

##    body_upper = body_upperXML.detectMultiScale(gray)
##    for a,b,c,d in body_upper:
##        cv2.rectangle(frame , (a,b),(a+c,b+d),(255,255,0),3)

    canny = cv2.Canny(smile_rect,100,180)
    cv2.imshow('smile_rect',smile_rect)
    cv2.imshow('Frame',frame)
    #cv2.imshow('CANNY',canny)
    k = cv2.waitKey(27) & 0xFF
    if k == 27 : break
        

cap.release()    
cv2.destroyAllWindows()
