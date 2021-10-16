### Lesson 2:
import numpy as np
import cv2
import matplotlib as plt

image = cv2.imread("C:\\Users\\my\\Desktop\\python desktop file\\Machine Learning\\thumbnail_large.JPG")

plt.imshow(image , camp= gray , interpolation = ' bicubibc')
plt.plot([600,200],[256,512],'b',linewidth=5)
plt.show()
cv2.imwrite('image_out.JPG',image)
