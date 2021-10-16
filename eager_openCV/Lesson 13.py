### Lesson 13:
import cv2
import numpy as np

img = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\messi.JPG")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1=np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray1,100,.1,10)
corners = np.int0(corners)

for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,(0,100,255),1)
cv2.imshow('MESSI' , img)
cv2.imshow('MESSI' , gray)
## split Image's Channels
##b,g,r,a=cv2.split(gray)
##cv2.imshow('img',img)
##cv2.imshow('b',b)
##cv2.imshow('g',g)
##cv2.imshow('r',r)
##cv2.imshow('a',a)

cv2.waitKey(0)

cv2.destroyAllWindows()
