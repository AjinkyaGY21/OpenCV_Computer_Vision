import cv2 as cv
import numpy as np

img = cv.imread("imgs\group.jpg")
cv.imshow("Person", img)
def rescale_image(img,scale):
    ht = int(img.shape[0] * scale)
    wd = int(img.shape[1] * scale)
    dim = (ht,wd)
    return cv.resize(img,dim,interpolation=cv.INTER_CUBIC)

#haarcascades look at the img using edges(detect if it is face or not)
resc = rescale_image(img,3)
cv.imshow("Resc",resc)
sharpen_kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
final_img = cv.filter2D(resc,-1,sharpen_kernel)
cv.imshow("Final",final_img)

gray = cv.cvtColor(final_img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#using pretrained classifiers of OpenCV to detect face
#error can be min by min sensitivity to noise(decrese minNeighbours and scaleFactor) making OpenCV more prone to noise
haar_casc = cv.CascadeClassifier("Face Detection\haarcascade_face.xml")
faces_rect = haar_casc.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=2)
print(f"Number of faces found : {len(faces_rect)}")
#print(faces_rect)
# [[332 232  40  40]
#  [ 11 538  60  60]]

for(x,y,w,h) in faces_rect:
    cv.rectangle(final_img, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow("Detected", final_img)
cv.waitKey(0)