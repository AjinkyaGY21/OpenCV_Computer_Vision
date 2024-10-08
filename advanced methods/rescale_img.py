#RESCALING IMAGES and VIDEOS
import cv2 as cv

def rescale_frame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("imgs\cat.jpg")
cv.imshow('Cat', img)

resized_img = rescale_frame(img)
cv.imshow("Cat resized", resized_img)

cv.waitKey(0)