import cv2 as cv
import numpy as np

img = cv.imread("imgs\cats.jpg")
h = img.shape[0] 
w = img.shape[1]
cv.imshow("Cats", img)
blank = np.zeros((h,w), dtype = "uint8")
cv.imshow("Blank",blank)

#canny edge detection algorithm
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
canny = cv.Canny(gray,125,175)
cv.imshow("Canny",canny)

#Laplacian
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Lap",lap)

#SOBEL
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow("Soblex",sobelx)
cv.imshow("Sobley",sobely)
comb_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow("Comb_Sobel",comb_sobel)

cv.waitKey(0)