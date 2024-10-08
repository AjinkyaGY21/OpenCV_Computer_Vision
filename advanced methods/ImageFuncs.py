import cv2 as cv

##converting bgr img to grayscale
img = cv.imread("imgs\group.jpg")
cv.imshow("Crowd", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)
cv.waitKey(0)

# #blur an img
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT) #kernel size odd number(5,5) blur increases with it
cv.imshow("Blurred", blur)
cv.waitKey(0)

# #Edge cascade
canny = cv.Canny(blur,10, 200) #less edges in blur img
cv.imshow("Canny", canny)
cv.waitKey(0)

# #dilate img
dilate = cv.dilate(img,(7,7), iterations = 4) #kernel size odd number(7,7)
cv.imshow("Dialated",dilate)
cv.waitKey(0)

#eroding
erode = cv.erode(img, (7,7), iterations = 11) #kernel size odd number(4,4)
cv.imshow("Eroded",erode)
cv.waitKey(0)

#resize
resize = cv.resize(img, (750,750), interpolation= cv.INTER_CUBIC)
cv.imshow("Resized",resize)
cv.waitKey(0)

#cropping
crop = img[50:150, 100:200]
cv.imshow("Cropped", crop)
cv.waitKey(0)