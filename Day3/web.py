import numpy as np
import cv2
import datetime as dt

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    date_time=str(dt.datetime.now())
    frame=cv2.putText(frame,date_time,(20,50),cv2.FONT_HERSHEY_TRIPLEX,1,(255,45,78),2,cv2.CV_64F)
    frame = cv2.putText(frame, "Shivam", (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (105, 25, 255), 2)

    cv2.imshow("Video",frame)
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()              # realease the computer resource
cv2.destroyAllWindows()