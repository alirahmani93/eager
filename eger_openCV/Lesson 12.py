### Lesson 12:
import cv2
import numpy as np

img=  cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\lamp2.JPG")
temp= cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\temp.JPG",0)
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
w,h = temp.shape[::-1]

res = cv2.matchTemplate(gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = .9

location = np.where(res>=threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
cv2.imshow('orin',img)
cv2.imshow('Temp',img)



cv2.waitKey(0)
cv2.destroyAllWindows()
