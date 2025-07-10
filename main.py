import cv2
import os


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