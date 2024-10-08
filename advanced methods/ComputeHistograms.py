import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# size of the mask has to be of same dimension as that of the image
#histogram allows you to visualize pixel intensity distribution in image
img = cv.imread("imgs\\fox.jpg")
blank = np.zeros(img.shape[:2], dtype = "uint8")
cv.imshow('Fox', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
h = img.shape[0]
w = img.shape[1]
circle = cv.circle(blank,(120,120),120,255,-1)
cv.imshow('Mask', circle)

masked1 = cv.bitwise_and(img,img,mask = circle)
cv.imshow('Masked1', masked1)

# #grayscale histogram
# masked2 = cv.bitwise_and(gray,gray,mask = circle)
# cv.imshow('Masked2', masked2)
# gray_hist = cv.calcHist([gray],[0], None, [256], [0,256])  # listofimgs indexofchannel mask #bins pixelrange
# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# Pixels")
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()

#RGB histogram
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([masked1],[i],circle,[256],[0,256])
    plt.figure() 
    plt.title(f"{col} histogram")
    plt.xlabel("#bins")
    plt.ylabel("#pixels")
    plt.xlim([0,256])
    plt.plot(hist, color=col)
   
plt.show()  
cv.waitKey(0)