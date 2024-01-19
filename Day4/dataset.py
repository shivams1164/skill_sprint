import cv2
import os
import time

haar_file = "haarcascade_frontalface_default.xml"
datasets = 'C:/Users/shiva/OneDrive/Desktop/Python Bootcamp/Day4/dataset'
name = input()

path = os.path.join(datasets, name)
if not os.path.isdir(path):
    os.mkdir(path)

face_cascade = cv2.CascadeClassifier(haar_file)
cap = cv2.VideoCapture(0)
print("Webcam is open?",cap.isOpened())
time.sleep(2)
count = 1

while count < 101:
    ret, frame = cap.read()
    if ret==True:
        img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (45, 255, 0), 2)
            faces = img_gray[y: y+h, x: x+h]
            face_resize = cv2.resize(faces, (600, 480))
            cv2.imwrite("%s/ %s.png" % (path, count), face_resize)
        count = count + 1
        cv2.imshow("Face capture", frame)
        if cv2.waitKey(1) == ord("q"):
            break


print("Your face has been created")
cap.release()
cv2.destroyAllWindows()
