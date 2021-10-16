### Lesson 08:
import cv2
import numpy as np

img1 = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\sky1.JPG")
logo = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\pythonlogo.PNG")

rows,cols,channel= logo.shape
roi = img1[0:rows , 0:cols]

logogray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

ret , mask = cv2.threshold(logogray,220,225,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask)
logo_fg = cv2.bitwise_and(logo,logo,mask=mask_inv)

dst = cv2.add( logo_fg , img1_bg )
#det = cv2.addWeighted(img1_bg,.35, logo_fg,.65,0)
add= cv2.add( logo_fg, img1_bg )
img1[0:rows,0:cols]=dst

#cv2.imshow('fram',logogray)
cv2.imshow("mask",mask)
cv2.imshow("mask_inv",mask_inv)
#cv2.imshow('backGround',img1_bg)
#cv2.imshow('frontGround',logo_fg)
cv2.imshow('destenation',dst)
cv2.imshow('img1',img1)
cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
