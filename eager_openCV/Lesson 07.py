### Lesson 07:
import cv2
import numpy as np

image1 = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\sky1.JPG")
image2 = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\cycle.JPG")

add1 = image1 + image2
add2 = cv2.add(image1,image2)
add3 = cv2.addWeighted(image1,0.2 , image2,0.8,0)
#cv2.imshow('1' , image1)
#cv2.imshow('2' , image2)
#cv2.imshow('add1' , add1)
cv2.imshow('add2' , add2)
cv2.imshow('add3' , add3)

cv2.waitKey(0)
cv2.destroyAllWindows()
