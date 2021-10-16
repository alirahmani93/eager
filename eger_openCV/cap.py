import cv2


capR = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
adress = 'D:\\Ali\\Faradars\\python\\python desktop file\\Image Processing\\my code\\capW.avi'
capW = cv2.VideoWriter(adress,fourcc,60.0,(640,480))
while True:
    _,frame = capR.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    

    
    ## SHOW ##
    
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    ## Exit ##
    if cv2.waitKey(1) & 0XFF == ord('q'): break

        
capR.release()
capW.release()
cv2.destroyAllWindows()
