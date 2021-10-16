### Lesson 06:
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\my\\Desktop\\python desktop file\\Image Processing\\c1.JPG",cv2.IMREAD_COLOR) ## wolf , lamp , ali is anothor JPG in this address 
px = img[100:250,150:230]
img[350:450 , 150: 250] = [0,0,0]

pts = np.array([[100,50],[50,100],[200,100],[100,200],[400,200],[200,400]])
cv2.polylines(img,[pts],True,(50,150,250),6)

part1 = img[300:400,300:400]
img[400:500 , 200: 300] = part1

print(px)
cv2.imshow('Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
