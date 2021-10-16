### Lesson 5
import cv2
import numpy as np

cap= cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    #frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    #cv2.line(frame,(130,130),(325,333),(0,0,225),5)
    #cv2.rectangle(frame,(200,200),(80,80),(),5)
    pts = np.array([[100,50],[50,100],[200,100],[100,200],[400,200],[200,400]])
    cv2.polylines(frame,[pts],True,(50,150,250),6)
    cv2.circle(frame,(484,135),120,(10,20,15),4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Hello World!",(200,450),font,1,(50,50,150),2)
    cv2.imshow("Web Cap",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
