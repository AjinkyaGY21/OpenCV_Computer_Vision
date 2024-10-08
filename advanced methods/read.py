import cv2 as cv

#READING IMAGES
img = cv.imread("imgs\cat.jpg")
cv.imshow('Cat', img)
cv.waitKey(0) #0 for inf. time

#READING VIDEOS W/O SOUND
capture = cv.VideoCapture("videos/vid.mp4") #arg(instead of path) can be 0:for webcam/1/2
#reading frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(300) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 
#error -215 is raised when video is running out of frames (stops looping)


