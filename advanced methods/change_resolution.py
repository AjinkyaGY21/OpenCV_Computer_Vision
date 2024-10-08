import cv2 as cv

capture = cv.VideoCapture("videos\vid.mp4")
isTrue, frame = capture.read()

def change_resolution(width, height):
    #works only for live videos
    capture.set(3,width)
    capture.set(4,height)