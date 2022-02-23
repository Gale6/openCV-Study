import cv2 as cv
import numpy as np

img = cv.imread('fall.jpg')



resized = cv.resize(img,(img.shape[1]//2,img.shape[0]//2),interpolation = cv.INTER_CUBIC)
cv.imshow('re',resized)

cblank = np.zeros(resized.shape,dtype='uint8')
tblank = np.zeros(resized.shape,dtype='uint8')

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)


#canny
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
canny = cv.Canny(blur,125,175)
cannycontours, cannyhierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(cblank,cannycontours,-1,(0,0,255),1)
cv.imshow('cdrawed',cblank)





#thresh
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
threshContours, threshHierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(tblank,threshContours,-1,(0,0,255),1)
cv.imshow('tdrawed',tblank)


cv.waitKey(0)