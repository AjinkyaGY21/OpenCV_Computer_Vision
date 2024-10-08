import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#bgr  channels
img = cv.imread("imgs\\butterfly.jpg")
cv.imshow("Butterfly",img)

#default RGB scale 
plt.imshow(img)

#vice-versa conversion are possible but all direct trans are not supported
#converting BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
plt.imshow(rgb)

# #BGR TO GRAYSCALE
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)
# print(img.shape)
# print(gray.shape)

# #BGR TO HSV
# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
# cv.imshow("HSV",hsv)
# print(hsv.shape)

# #BGR TO LAB
# lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
# cv.imshow("LAB",lab)
# print(lab.shape)

cv.waitKey(0)
plt.show()