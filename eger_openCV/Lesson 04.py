### Lesson 04
import cv2
import numpy as np

cap= cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    #frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.line(frame,(130,130),(325,333),(0,0,225),5)
    cv2.rectangle(frame,(200,200),(80,80),(),5)
    cv2.imshow("Web Cap",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
