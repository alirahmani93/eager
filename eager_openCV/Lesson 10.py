### Lesson 10:

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    a,b,c,d=10,10,20,30
    #a,b,c,d=0,0,0,0
    lower_red = np.array([a+b,a+c,a+d])
    uper_red = np.array([255,255,255])
    
    mask = cv2.inRange(hsv,lower_red , uper_red)
    result = cv2.bitwise_not(frame,frame,mask=mask)

    #cv2.imshow("frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result",result)

 
