import cv2 as cv
import numpy as np

img = cv.imread("imgs\colorballs.jpg")
cv.imshow("Balls", img)

blank = np.zeros(img.shape, dtype = "uint8")
cv.imshow("Blank",blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

canny = cv.Canny(img, 125,75)
cv.imshow("Canny", canny)


#CONTOURS
#hierarchical/external/all contours -> cv.RETR_TREE/cv.RETR_EXTERNAL/cv.RETR_LIST
contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contours found in canny image")

#Blur
blurred = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blurred",blurred)

contours1, hierarchies1 = cv.findContours(blurred, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f"{len(contours1)} contours found in blurred image")

#THRESHOLDING
ret, thresh = cv.threshold(gray,125,250, cv.THRESH_BINARY) #thresh,maxval
cv.imshow("Thresh",thresh)
contours2, hierarchies2 = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(f"{len(contours2)} contours found in blurred image")

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("Blank Contours",blank)

cv.waitKey(0)

