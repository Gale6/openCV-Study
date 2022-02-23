import cv2 as cv
import numpy as np

img = cv.imread('dogs.jpg')
cv.imshow('dog',img)

average = cv.blur(img,(3,3))
cv.imshow('average',average)

gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('gauss',gauss)

median = cv.medianBlur(img,3)
cv.imshow('median',median)

bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral',bilateral)


cv.waitKey(0)

