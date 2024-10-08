import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("Face Detection\haarcascade_face.xml")
# features = np.load("features.npy", allow_pickle = True)
# labels = np.load("labels.npy")

people = ["Katrina Kaif","Wahaj Ali","Virat Kohli"]

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

test_face = cv.imread(r"Face Detection\imgs\test faces\WhatsApp Image 2022-12-13 at 3.31.03 PM.jpeg")     
test_gray = cv.cvtColor(test_face, cv.COLOR_BGR2GRAY)
cv.imshow("Person", test_gray)

faces_rect = haar_cascade.detectMultiScale(test_gray, 1.01, 3)
for (x,y,w,h) in faces_rect:
    faces_roi = test_gray[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label : {people[label]} with a confidence of {confidence}")

    cv.putText(test_face, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (100,160,220), 1)
    cv.rectangle(test_face,(x,y),(x+w,y+h), (0,255,0), 2)

cv.imshow("Detected Face", test_face)
cv.waitKey(0)