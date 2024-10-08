import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#no of channels : img-3 r/g/b-1

img = cv.imread("imgs\\butterfly.jpg")
cv.imshow("Butterfly",img)

b,g,r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype = "uint8")
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("BLUE",blue)
cv.imshow("GREEN",green)
cv.imshow("RED",red)

# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# plt.imshow(rgb)
# cv.imshow("RED",r)
# cv.imshow("GREEN",g)
# cv.imshow("BLUE",b)

merged = cv.merge([r,g,b])
cv.imshow("RGB",merged)

cv.waitKey(0)
plt.show()