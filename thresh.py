import cv2 as cv

img = cv.imread('r6.jpg')
cv.imshow('dogs',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


#Simple Thresholding

threshold, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('simple threshold',thresh)

threshold, thresh_inv = cv.threshold(gray,125,255,cv.THRESH_BINARY_INV)
cv.imshow('simple threshold_inv',thresh_inv)



#adaptive thresholing

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
cv.imshow('adaptiveThreshold',adaptive_thresh)


cv.waitKey(0)