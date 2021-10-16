### Lesson 11:
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (1):
    _,frame= cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_8U)
    sobelx  =  cv2.Sobel(frame,cv2.CV_8U ,1,0 , ksize=5)
    sobely  =  cv2.Sobel(frame,cv2.CV_8U ,0,1 , ksize=5)
    sobelxy =  cv2.Sobel(frame,cv2.CV_8U ,2,1 , ksize=5)
    canny   =  cv2.Canny(frame,150,255)
    canny2  =  cv2.Canny(frame,150,255,edges=4,apertureSize=5)
    
    cv2.imshow('Laplacian',laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('sobelxy',sobelxy)
    cv2.imshow('canny',canny)
    cv2.imshow('canny2',canny2) 
    if (cv2.waitKey(1) & 0xFF) ==ord('q'): break
    
cap.release()
cv2.destroyAllWindows()
