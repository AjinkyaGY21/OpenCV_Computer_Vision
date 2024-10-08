import cv2 as cv
import numpy as np

img = cv.imread("imgs\zebras.jpg")
h = img.shape[0]
w = img.shape[1]
blank = np.zeros((h,w), dtype = "uint8")
# cv.imshow("Zebra", img)
# cv.imshow("Blank", blank)

# circle = cv.circle(blank.copy(), (w//2,h//2), 50, 200, -1)
# cv.imshow("Mask", circle)

# masked1 = cv.bitwise_or(img, img, mask = circle)
# cv.imshow("Masked1", masked1)

rectangle = cv.rectangle(blank.copy(),(50,50),(250,250),255,-1)
cv.imshow("Mask", rectangle)

masked2 = cv.bitwise_and(img,img,mask = rectangle)
cv.imshow("Masked2", masked2)

cv.waitKey(0)