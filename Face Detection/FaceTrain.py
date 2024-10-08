import os
import cv2 as cv
import numpy as np

people = ["ABC","XYZ","PQR"]
haar_cascade = cv.CascadeClassifier("Face Detection\haarcascade_face.xml")
# p = []
# for i in os.listdir(r"Face Detection\imgs"):
#     p.append(i)
# print(p)

DIR = r"Face Detection\imgs"
features = []
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+h]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("Training completed ===================== ")

# print(f"No of features are : {len(features)}")
# print(features)
# print(f"No of labels are : {len(labels)}")
# print(labels)

features = np.array(features,dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
#train the recognizer on features and labels list
face_recognizer.train(features, labels)
face_recognizer.save("face_trained.yml")

np.save("features.npy",features)
np.save("labels.npy",labels)
