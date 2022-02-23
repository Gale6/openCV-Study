import cv2 as cv
import numpy as np


img = cv.imread('r6.jpg')
cv.imshow('r6',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('g',gray)

blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

cany = cv.Canny(img,100,200)
cv.imshow('canny',cany)

dilated = cv.dilate(cany,(3,3),iterations = 3)
cv.imshow('dilated',dilated)

eroded  = cv.erode(dilated,(3,3),iterations = 3)
cv.imshow('eroded',eroded)

resized = cv.resize(img,(img.shape[1],img.shape[0]//2),interpolation = cv.INTER_CUBIC)
cv.imshow('resized',resized)

cropped = img[0:100,0:600]
cv.imshow('cropped',cropped)


cv.waitKey(0)
