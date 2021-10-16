### Lesson 15:
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fg= cv2.createBackgroundSubtractorKNN()

while True:
    _,frame = cap.read()
    fmask = fg.apply(frame)

    cv2.imshow("ORIGINAL" , frame)
    cv2.imshow('FG',fmask)

   
    if cv2.waitKey(27) & 0xFF==27 :
        break
cap.release()
cv2.destroyAllWindows()
