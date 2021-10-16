### detect face parts for IMAGE

import cv2 ; import numpy as np ; #import matplotlib.pyplot as plt
faceXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_frontalface_default.xml")
eyeXML= cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye.xml")
smileXML= cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_smile.xml")
eye_leftXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_eye_left_2splits.xml")
##bodyXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_body_lower.xml")

img = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\Messi9.jpg")
##temp = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\barca team2.JPG")
   
gray    =   cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces   =   faceXML.detectMultiScale(gray)

for x,y,w,h in faces:
    cv2.rectangle(img , (x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h , x:x+w]
    roi_color = img[y:y+h , x:x+w]

##        eyes = eyeXML.detectMultiScale(roi_gray)
##        for ex,ey,ew,eh in eyes:
##            cv2.rectangle(roi_color, (ex,ey),(ex+ew , ey+eh),(0,255,0),1)

    smiles = smileXML.detectMultiScale(gray)
    for sx,sy,sw,sh in smiles:
        cv2.rectangle(roi_color,(sx,sy),(sx+sw , sy+sh),(0,0,255),1)

    leftEye = eye_leftXML.detectMultiScale(gray)
    for a,b,c,d in leftEye:
        cv2.rectangle(img , (a,b),(a+c,b+d),(255,255,0),3)

##body = bodyXML.detectMultiScale(gray)
##for a,b,c,d in lefEye:
##    cv2.rectangle(img , (a,b),(a+c,b+d),(255,255,0),3)

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#############################
"""
def findFace():
    pass
def findSmile():
    pass



def findPattern():
    pass
    orb = cv2.ORB_create()
    kp1 , dst1 = orb.detectAndCompute(img,None)
    kp2 , dst2 = orb.detectAndCompute(temp,None)

    bf =  cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck = True)

    matches = bf.match(dst1 , dst2)

    matches = sorted(matches, key=lambda x:x.distance)

    img_out = cv2.drawMatches(img,kp1,temp , kp2 , matches[:20],None , flags=2)

    plt.imshow(img_out)
    plt.show
def canny():
    canny   =  cv2.Canny(img,150,255)
    cv2.imshow('canny',canny)
"""
