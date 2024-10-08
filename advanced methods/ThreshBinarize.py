import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
#thresholding is binary realization of image
#image -> binary image(where pixels are 0/black, 255/white)
#set threshold intensity and set all pixels below that to zero and above to white
img = cv.imread("imgs\human.jpg")
cv.imshow('Human', img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Simple thresholding
threshold, threshs =  cv.threshold(img, 50, 220, cv.THRESH_BINARY)
cv.imshow("ThresholdS", threshs)

#Inverse thresholding
threshold, threshi =  cv.threshold(img, 50, 220, cv.THRESH_BINARY_INV)
cv.imshow("ThresholdI", threshi)

#Adaptive thresholding
thresha =  cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 17, 3)
cv.imshow("ThresholdA", thresha)

cv.waitKey(0)