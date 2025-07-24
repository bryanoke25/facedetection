import cv2
import os
import numpy as np


haar_file = "haarcascade_frontalface_default.xml"
dataset = "dataset"
sub_data = "oke"

#create directory for storing images
path = os.path.join(dataset, sub_data)
if not os.path.isdir(path):
    os.makedirs(path)

(width, height) = (130, 100)

webcam = cv2.VideoCapture(0)
face_cascade =cv2.CascadeClassifier(haar_file)
count = 1
while count <= 30:
    read, img = webcam.read()
    if not read:
        print("could not capture image")
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)

    if len(faces)> 0:
        for x,y, w,h in faces:
            cv2.rectangle(img, (x,y ), (x+w, y+h), (255, 200, 255), 2)
            face= gray[y:y+h, x:x+w]
            face_resize = cv2.resize(face, (width, height)) 
            cv2.imwrite(os.path.join (path, f"{count}.png"), face_resize)
            count += 1
    cv2.imshow("opencv", img)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()




