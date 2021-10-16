### Lesson 09:
import cv2
import numpy as np
img = cv2.imread("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\book2.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret , threshold = cv2.threshold(img,150,255,cv2.THRESH_BINARY,1)
adapth= cv2.adaptiveThreshold(gray, 225,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
adapth2= cv2.adaptiveThreshold(gray, 225,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,115,1)

#cv2.imshow("BOOK",img)
cv2.imshow("BOOK_GRAY",gray)
cv2.imshow("BOOK_THRESHOLD",threshold)
cv2.imshow("BOOK_ADAPTIV",adapth)
#cv2.imshow("BOOK_ADAPTIV2",adapth2)
cv2.waitKey(0)
cv2.destroyAllWindows()
