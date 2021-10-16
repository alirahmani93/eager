### Lesoon 14: 
import cv2
import numpy as np
import matplotlib.pyplot as plt

img  = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\barca team.JPG",0)
temp = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\barca team2.JPG",0)

orb = cv2.ORB_create()

kp1 , des1 = orb.detectAndCompute(img ,None)
kp2 , des2 = orb.detectAndCompute(temp,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING2 , crossCheck = True)

matches = bf.match(des1,des2)
matches = sorted(matches, key= lambda x:x.distance)

img_out = cv2.drawMatches(img,kp1, temp, kp2, matches[:60], None, flags =2)


plt.imshow(img_out)
plt.show()
##cv2.imshow("Temp", temp)
##cv2.imshow("Img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()

