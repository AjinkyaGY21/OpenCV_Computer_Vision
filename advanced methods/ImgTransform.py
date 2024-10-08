import cv2 as cv
import numpy as np

img = cv.imread("imgs\squirrel.jpg")
cv.imshow("Squirrel",img)
cv.waitKey(0)

print(img.shape) #-> (ht,wd,ch)
#frame shape[0]->ht and shape[1]->wd
#translation
def translate(img,x,y):
    # width x height
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dim = (img.shape[1], img.shape[0]) #(width,height)
    return cv.warpAffine(img, trans_mat, dim)

# -x -> left; -y -> up; +x -> right; +y -> down
translated = translate(img,100,100)
cv.imshow("Translated",translated)
cv.waitKey(0)

#rotation
def rotate(img, angle, rot_pt = None):
    (ht,wd) = img.shape[:2]
    if rot_pt is None:
        rot_pt = (wd//2, ht//2)#if no rotation pt => centre
    
    rot_mat = cv.getRotationMatrix2D(rot_pt, angle, scale=1.0)
    dim = (wd,ht)

    return cv.warpAffine(img, rot_mat, dim)

rotated = rotate(img,60)
#-ve angle->CW and =ve angle->ACW
cv.imshow("Rotated", rotated)
cv.waitKey(0)

#Resizing
resized = cv.resize(img,(1000,1000), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)
cv.waitKey(0)

#Flipping
flipped = cv.flip(img, -1) #0/1/-1 -> about vertical/horizontal/both axis
cv.imshow("Flipped",flipped)
cv.waitKey(0)

#Cropping