import cv2 as cv
import numpy as np


img = cv.imread('dogs.jpg')
cv.imshow('dog',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

b,g,r = cv.split(img)

cv.imshow('g',g)
cv.imshow('b',b)
cv.imshow('r',r)


print(img.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('green',green)
cv.imshow('blue',blue)
cv.imshow('red',red)


cv.waitKey(0)