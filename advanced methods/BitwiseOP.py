import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype = "uint8")
rect = cv.rectangle(blank.copy(), (50,50), (250,250), 255, -1)
circle = cv.circle(blank.copy(), (200,100), 100, 255, -1)

cv.imshow("Circle",circle)
cv.imshow("Rectangle",rect)

bit_and = cv.bitwise_and(rect,circle)
cv.imshow("AND",bit_and)

bit_or = cv.bitwise_or(rect,circle)
cv.imshow("OR",bit_or)

bit_xor = cv.bitwise_xor(rect,circle)
cv.imshow("XOR",bit_xor)

bit_not = cv.bitwise_not(circle)
cv.imshow("Complement",bit_not)

cv.waitKey(0)