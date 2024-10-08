import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("imgs\cat.jpg")
cv.imshow('Cat', img)

#AVERAGING BLUR
average = cv.blur(img,(3,3)) #kernel size(odd no) window slide and average of surr value for each centrsl pixel
cv.imshow("AVG",average)

#Gaussian blur
normal = cv.GaussianBlur(img,(3,3),0)
cv.imshow("Normal", normal) 

#Median blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

#Bilateral blur
bilateral = cv.bilateralFilter(img,34,55,45)
cv.imshow("Bilateral", bilateral)

plt.show()
cv.waitKey(0)