import cv2 as cv
import numpy as np  

# #for blank image , dtype for images is uint
blank = np.ones((500,500,3), dtype = np.uint8) #zeros or ones ;args are height, width, no of colors(2:b/w, 3:bgr)
# cv.imshow("Blank", blank)
# cv.waitKey(0)

# #colored box in gui
# blank[400:500, 400:500] = 80,240,160
# cv.imshow("green", blank)
# cv.waitKey(0)

# #drawing rectangle
# cv.rectangle(blank,(0,0),(250,250),(240,80,160),thickness = -1) #arg thickness ->integer for line and -> cv.FILLED or thickness = -1 for color-filled
# cv.imshow("Rectangle", blank)
# cv.waitKey(0)

# #drawing rectangle
# cv.circle(blank,(250,250),200,(120,40,180),thickness = -1)
# cv.imshow("Circle", blank)
# cv.waitKey(0)

# #drawing line
# cv.line(blank, (0,0),(250,250),(120,120,120), thickness = 3)
# cv.imshow("Line", blank)
# cv.waitKey(0)

#writing text on img
cv.putText(blank, "HELLO", (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.3, (200,100,150), 2)
cv.imshow("Text", blank)
cv.waitKey(0)