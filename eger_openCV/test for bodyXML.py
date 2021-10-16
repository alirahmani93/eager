import cv2
body_lowerXML = cv2.CascadeClassifier("D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\haarcascade_body_lower.xml")
cap= cv2.VideoCapture(0)

while True :
    _,frame =   cap.read()
    gray    =   cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 


    body_lower = body_lowerXML.detectMultiScale(gray)
    for a,b,c,d in body_lower:
        cv2.rectangle(frame , (a,b),(a+c,b+d),(255,255,0),3)

    cv2.imshow('Frame',frame)
    k = cv2.waitKey(27) & 0xFF
    if k == 27 : break
        

cap.release()    
cv2.destroyAllWindows()
